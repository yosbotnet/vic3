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
