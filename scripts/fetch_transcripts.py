# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "youtube-transcript-api>=0.6.2,<2.0",
#     "yt-dlp>=2024.1.1",
# ]
# ///
"""Fetch YouTube captions for playlists listed in scripts/playlists.json."""

from __future__ import annotations

import re

_STRIP_PATTERNS = [
    re.compile(r"\bin\s+update\s+\d+(\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\bupdate\s+\d+(\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\b\d+\.\d+(\.\d+)*\s+update\b", re.IGNORECASE),
    re.compile(r"\bin\s+victoria\s*3(?:'s)?\b", re.IGNORECASE),
    re.compile(r"\bvictoria\s*3(?:'s)?\b", re.IGNORECASE),
    re.compile(r"\btutorial\b", re.IGNORECASE),
    re.compile(r"\bpart\s+(one|two|three|\d+)\b", re.IGNORECASE),
    re.compile(r"\bin\s+\d{4}\b"),
    re.compile(r"\bpost\b", re.IGNORECASE),
]


def slugify_title(title: str) -> str:
    """Turn a YouTube video title into a stable filename slug."""
    s = title
    for pat in _STRIP_PATTERNS:
        s = pat.sub(" ", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


import json
from dataclasses import dataclass
from typing import Iterable, Mapping


@dataclass(frozen=True)
class VideoMeta:
    title: str
    video_id: str
    url: str
    duration_seconds: int
    playlist: str
    playlist_index: int


def _format_timestamp(seconds: float) -> str:
    total = int(seconds)
    minutes, secs = divmod(total, 60)
    return f"[{minutes:02d}:{secs:02d}]"


def format_transcript_markdown(
    meta: VideoMeta,
    transcript: Iterable[Mapping],
    *,
    source: str,
    fetched_at: str,
    language: str = "en",
    marker_interval_seconds: int = 30,
) -> str:
    """Render frontmatter + transcript body with timestamp markers."""
    title_yaml = json.dumps(meta.title, ensure_ascii=False)
    frontmatter = (
        "---\n"
        f"title: {title_yaml}\n"
        f"video_id: {meta.video_id}\n"
        f"url: {meta.url}\n"
        f"duration_seconds: {meta.duration_seconds}\n"
        f"playlist: {meta.playlist}\n"
        f"playlist_index: {meta.playlist_index}\n"
        f"fetched_at: {fetched_at}\n"
        f"caption_source: {source}\n"
        f"language: {language}\n"
        "---\n\n"
    )

    chunks: list[str] = []
    current_chunk: list[str] = []
    next_marker_at = 0.0
    for entry in transcript:
        start = float(entry["start"])
        text = str(entry["text"]).strip()
        if not text:
            continue
        if start >= next_marker_at:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
            current_chunk.append(f"{_format_timestamp(start)} {text}")
            while next_marker_at <= start:
                next_marker_at += marker_interval_seconds
        else:
            current_chunk.append(text)
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    body = "\n\n".join(chunks) + "\n"
    return frontmatter + body


def output_filename(meta: VideoMeta, *, naming: str) -> str:
    """Stable per-video filename driven by playlist naming policy."""
    index = f"{meta.playlist_index:02d}"
    if naming == "episode":
        return f"ep{index}.md"
    if naming == "slug":
        slug = slugify_title(meta.title) or f"video-{meta.video_id}"
        return f"{index}-{slug}.md"
    raise ValueError(f"unknown naming policy: {naming!r}")


import subprocess
import tempfile
from pathlib import Path


def enumerate_playlist(playlist_url: str, playlist_slug: str) -> list[VideoMeta]:
    """Return ordered VideoMeta for each video in the playlist using yt-dlp."""
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--print",
        "%(playlist_index)s\t%(title)s\t%(duration)s\t%(id)s",
        playlist_url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    metas: list[VideoMeta] = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        index_str, title, duration_str, video_id = line.split("\t", 3)
        try:
            duration = int(float(duration_str))
        except (ValueError, TypeError):
            duration = 0
        metas.append(
            VideoMeta(
                title=title,
                video_id=video_id,
                url=f"https://www.youtube.com/watch?v={video_id}",
                duration_seconds=duration,
                playlist=playlist_slug,
                playlist_index=int(index_str),
            )
        )
    return metas


def fetch_captions_api(video_id: str) -> list[dict]:
    """Fetch English captions via youtube-transcript-api.

    Returns a list of {"text": str, "start": float} dicts. Raises on failure
    so the caller can fall back to yt-dlp.
    """
    from youtube_transcript_api import YouTubeTranscriptApi

    # Handle both 0.6.x (static methods) and 1.x (instance methods) APIs.
    if hasattr(YouTubeTranscriptApi, "list_transcripts"):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_manually_created_transcript(
                ["en", "en-US", "en-GB"]
            )
        except Exception:
            transcript = transcript_list.find_generated_transcript(
                ["en", "en-US", "en-GB"]
            )
        raw = transcript.fetch()
    else:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        try:
            transcript = transcript_list.find_manually_created_transcript(
                ["en", "en-US", "en-GB"]
            )
        except Exception:
            transcript = transcript_list.find_generated_transcript(
                ["en", "en-US", "en-GB"]
            )
        raw = transcript.fetch()

    # In 1.x, fetch() returns FetchedTranscriptSnippet objects with .text/.start.
    # In 0.6.x, it returns plain dicts.
    out: list[dict] = []
    for entry in raw:
        if isinstance(entry, dict):
            out.append({"text": entry["text"], "start": entry["start"]})
        else:
            out.append({"text": entry.text, "start": entry.start})
    return out


def fetch_captions_ytdlp(video_id: str) -> list[dict]:
    """Fetch English auto captions via yt-dlp as JSON3.

    Returns the same list-of-dict shape as fetch_captions_api so the writer
    doesn't care which path produced the captions. Raises on failure.
    """
    url = f"https://www.youtube.com/watch?v={video_id}"
    with tempfile.TemporaryDirectory() as tmp:
        out_template = str(Path(tmp) / "%(id)s.%(ext)s")
        cmd = [
            "yt-dlp",
            "--skip-download",
            "--write-auto-sub",
            "--write-sub",
            "--sub-lang", "en,en-US,en-GB",
            "--sub-format", "json3",
            "-o", out_template,
            url,
        ]
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        candidates = sorted(Path(tmp).glob(f"{video_id}*.json3"))
        if not candidates:
            raise RuntimeError(f"yt-dlp produced no captions for {video_id}")
        data = json.loads(candidates[0].read_text())

    entries: list[dict] = []
    for event in data.get("events", []):
        if "segs" not in event:
            continue
        start_ms = event.get("tStartMs", 0)
        text = "".join(seg.get("utf8", "") for seg in event["segs"]).strip()
        if not text or text == "\n":
            continue
        entries.append({"text": text, "start": start_ms / 1000.0})
    if not entries:
        raise RuntimeError(f"yt-dlp captions for {video_id} were empty after parsing")
    return entries


import argparse
import sys
from datetime import date


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "playlists.json"
TRANSCRIPTS_DIR = REPO_ROOT / "transcripts"


def fetch_and_write(meta: VideoMeta, naming: str, force: bool, fetched_at: str) -> str:
    """Fetch one video's captions and write the markdown file.

    Returns one of: 'ok', 'skipped', 'fallback', 'failed:<reason>'.
    """
    out_dir = TRANSCRIPTS_DIR / meta.playlist
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / output_filename(meta, naming=naming)

    if out_path.exists() and not force:
        return "skipped"

    source = "youtube-transcript-api"
    try:
        transcript = fetch_captions_api(meta.video_id)
    except Exception as api_err:
        try:
            transcript = fetch_captions_ytdlp(meta.video_id)
            source = "yt-dlp-auto"
        except Exception as ytdlp_err:
            return f"failed:api={type(api_err).__name__} ytdlp={type(ytdlp_err).__name__}"

    body = format_transcript_markdown(meta, transcript, source=source, fetched_at=fetched_at)
    out_path.write_text(body, encoding="utf-8")
    return "ok" if source == "youtube-transcript-api" else "fallback"


def run(only: list[str] | None, force: bool) -> int:
    playlists = json.loads(CONFIG_PATH.read_text())
    fetched_at = date.today().isoformat()
    overall_failed: list[str] = []

    for pl in playlists:
        if only and pl["slug"] not in only:
            continue
        print(f"\n=== playlist: {pl['slug']} ===", flush=True)
        metas = enumerate_playlist(pl["url"], pl["slug"])
        print(f"  {len(metas)} videos", flush=True)
        for meta in metas:
            status = fetch_and_write(meta, naming=pl["naming"], force=force, fetched_at=fetched_at)
            tag = status.split(":", 1)[0]
            print(f"  [{tag:8s}] {meta.playlist_index:02d} {meta.title}", flush=True)
            if status.startswith("failed"):
                overall_failed.append(f"{pl['slug']}/{meta.playlist_index:02d} {meta.title}: {status}")

    if overall_failed:
        print("\nFAILED VIDEOS:", file=sys.stderr)
        for line in overall_failed:
            print(f"  {line}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        action="append",
        help="Only process this playlist slug (repeatable). Default: all from playlists.json",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing transcript files",
    )
    args = parser.parse_args(argv)
    return run(only=args.only, force=args.force)


if __name__ == "__main__":
    raise SystemExit(main())
