# Phase 1: Raw Transcripts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fetch English captions for every video in two YouTube playlists (21 tutorials + 17 campaign episodes = 38 videos) and write them to disk as markdown files with frontmatter and per-30-second timestamp markers.

**Architecture:** A single Python script driven by a JSON config of playlists. Enumeration uses `yt-dlp --flat-playlist` to get the video list. Each video's captions are fetched via `youtube-transcript-api` (primary) with a `yt-dlp --write-auto-sub` fallback for videos the API can't reach. Script is idempotent (skips existing files unless `--force`).

**Tech Stack:** Python 3, `uv` for dependency management via PEP 723 inline script metadata, `youtube-transcript-api`, `yt-dlp` (already invoked via `uvx`), `pytest` for tests.

---

## File Structure

| Path | Purpose |
| --- | --- |
| `.gitignore` | Ignore `__pycache__`, `.pytest_cache`, `*.vtt` temp files |
| `scripts/playlists.json` | Source of truth: list of `{slug, url, naming}` |
| `scripts/fetch_transcripts.py` | The whole fetcher (single file — small enough to stay focused) |
| `scripts/test_fetch_transcripts.py` | pytest tests for the pure functions in the fetcher |
| `transcripts/tutorials/*.md` | Output (21 files) |
| `transcripts/great-wave-japan/*.md` | Output (17 files) |

The fetcher is one file because everything in it serves a single workflow (enumerate → fetch → format → write). Splitting by "technical layer" would obscure the flow. The pure formatting helpers are at the top; the I/O at the bottom; the CLI entrypoint at the very end.

---

### Task 1: Project skeleton (config + gitignore + dirs)

**Files:**
- Create: `/Users/ybc/code/vic3/.gitignore`
- Create: `/Users/ybc/code/vic3/scripts/playlists.json`
- Create: `/Users/ybc/code/vic3/transcripts/tutorials/.gitkeep`
- Create: `/Users/ybc/code/vic3/transcripts/great-wave-japan/.gitkeep`

- [ ] **Step 1: Write `.gitignore`**

```gitignore
__pycache__/
*.pyc
.pytest_cache/
.venv/
*.vtt
*.srt
.DS_Store
```

- [ ] **Step 2: Write `scripts/playlists.json`**

```json
[
  {
    "slug": "tutorials",
    "url": "https://www.youtube.com/playlist?list=PL1QPWs6KwuOCu0dfHoKgsySV3xE_eQ9Z8",
    "naming": "slug"
  },
  {
    "slug": "great-wave-japan",
    "url": "https://www.youtube.com/playlist?list=PLsT4scrqjQbTSBvfQQBpMnGQzcwkteRvp",
    "naming": "episode"
  }
]
```

Note: `naming: "slug"` produces `NN-<title-slug>.md`. `naming: "episode"` produces `epNN.md` (episodes only differ by number).

- [ ] **Step 3: Create output directories with placeholders**

```bash
mkdir -p /Users/ybc/code/vic3/transcripts/tutorials /Users/ybc/code/vic3/transcripts/great-wave-japan
touch /Users/ybc/code/vic3/transcripts/tutorials/.gitkeep /Users/ybc/code/vic3/transcripts/great-wave-japan/.gitkeep
```

- [ ] **Step 4: Verify structure**

Run: `ls -la /Users/ybc/code/vic3/ /Users/ybc/code/vic3/scripts /Users/ybc/code/vic3/transcripts`
Expected: `.gitignore`, `scripts/playlists.json`, two empty transcript dirs with `.gitkeep`

- [ ] **Step 5: Commit skeleton**

```bash
cd /Users/ybc/code/vic3
git add .gitignore scripts/playlists.json transcripts/
git -c commit.gpgsign=false commit -m "phase 1: project skeleton (gitignore, playlists config, output dirs)"
```

---

### Task 2: Failing test for `slugify_title`

**Files:**
- Create: `/Users/ybc/code/vic3/scripts/test_fetch_transcripts.py`

- [ ] **Step 1: Write the failing test**

Create `scripts/test_fetch_transcripts.py`:

```python
from fetch_transcripts import slugify_title


def test_slugify_strips_in_victoria_3_suffix():
    assert slugify_title("Shipbuilding Tutorial in Victoria 3") == "shipbuilding"


def test_slugify_strips_tutorial_word():
    assert slugify_title("Deficit Spending Tutorial in Victoria 3") == "deficit-spending"


def test_slugify_strips_version_tags():
    assert (
        slugify_title("How to Pass Laws in Update 1.12 - Victoria 3")
        == "how-to-pass-laws"
    )
    assert (
        slugify_title("Subjecthood and Citizenship Laws Tutorial in Victoria 3's 1.10 Update")
        == "subjecthood-and-citizenship-laws"
    )


def test_slugify_collapses_non_alnum():
    assert slugify_title("World Market & Trade Center!") == "world-market-trade-center"


def test_slugify_lowercases():
    assert slugify_title("FOO Bar") == "foo-bar"


def test_slugify_handles_apostrophes():
    assert slugify_title("Victoria 3's Power Blocs") == "power-blocs"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest pytest test_fetch_transcripts.py -v
```

Expected: `ModuleNotFoundError: No module named 'fetch_transcripts'` (file doesn't exist yet).

---

### Task 3: Implement `slugify_title`

**Files:**
- Create: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Create the script with PEP 723 metadata and slugify_title**

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "youtube-transcript-api>=0.6.2",
#     "yt-dlp>=2024.1.1",
# ]
# ///
"""Fetch YouTube captions for playlists listed in scripts/playlists.json."""

from __future__ import annotations

import re

_STRIP_PATTERNS = [
    re.compile(r"\bin\s+update\s+\d+(\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\bupdate\s+\d+(\.\d+)*\b", re.IGNORECASE),
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
```

- [ ] **Step 2: Run tests to verify they pass**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest pytest test_fetch_transcripts.py -v
```

Expected: all 6 slugify tests pass.

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py scripts/test_fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: slugify_title with tests"
```

---

### Task 4: Failing test for `format_transcript_markdown`

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/test_fetch_transcripts.py`

- [ ] **Step 1: Append the failing test**

Append to `scripts/test_fetch_transcripts.py`:

```python
from fetch_transcripts import VideoMeta, format_transcript_markdown


def _meta() -> VideoMeta:
    return VideoMeta(
        title="Shipbuilding Tutorial in Victoria 3",
        video_id="ct-PUjt6M8c",
        url="https://www.youtube.com/watch?v=ct-PUjt6M8c",
        duration_seconds=1554,
        playlist="tutorials",
        playlist_index=1,
    )


def test_format_includes_frontmatter():
    transcript = [
        {"text": "Hello world", "start": 0.0},
        {"text": "and welcome", "start": 5.2},
    ]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert out.startswith("---\n")
    assert 'title: "Shipbuilding Tutorial in Victoria 3"' in out
    assert "video_id: ct-PUjt6M8c" in out
    assert "playlist: tutorials" in out
    assert "playlist_index: 1" in out
    assert "caption_source: youtube-transcript-api" in out
    assert "fetched_at: 2026-05-16" in out


def test_format_emits_timestamp_marker_at_start():
    transcript = [{"text": "Hello world", "start": 0.0}]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert "[00:00] Hello world" in out


def test_format_emits_timestamp_every_30_seconds():
    transcript = [
        {"text": "first", "start": 0.0},
        {"text": "still in first chunk", "start": 15.0},
        {"text": "second chunk", "start": 32.0},
        {"text": "still second", "start": 45.0},
        {"text": "third chunk", "start": 65.0},
    ]
    out = format_transcript_markdown(_meta(), transcript, source="youtube-transcript-api", fetched_at="2026-05-16")
    assert "[00:00]" in out
    assert "[00:32]" in out
    assert "[01:05]" in out
    assert "[00:15]" not in out  # no marker mid-chunk
    assert "[00:45]" not in out


def test_format_quotes_title_with_special_chars():
    meta = VideoMeta(
        title='Victoria 3\'s "Best" Tutorial',
        video_id="x",
        url="https://example",
        duration_seconds=10,
        playlist="tutorials",
        playlist_index=1,
    )
    out = format_transcript_markdown(meta, [{"text": "hi", "start": 0.0}], source="youtube-transcript-api", fetched_at="2026-05-16")
    # YAML-safe: the title line must round-trip through a YAML parser
    import yaml
    front = out.split("---\n", 2)[1]
    parsed = yaml.safe_load(front)
    assert parsed["title"] == 'Victoria 3\'s "Best" Tutorial'
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest --with pyyaml pytest test_fetch_transcripts.py -v
```

Expected: 4 new tests fail with `ImportError: cannot import name 'VideoMeta'` (or `format_transcript_markdown`).

---

### Task 5: Implement `VideoMeta` and `format_transcript_markdown`

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Add VideoMeta dataclass and formatter**

Insert after the `slugify_title` function:

```python
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
    # Frontmatter: use json.dumps for the title to guarantee YAML-safe quoting.
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
            # Advance to the next marker boundary at or after this start.
            while next_marker_at <= start:
                next_marker_at += marker_interval_seconds
        else:
            current_chunk.append(text)
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    body = "\n\n".join(chunks) + "\n"
    return frontmatter + body
```

- [ ] **Step 2: Run tests to verify they pass**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest --with pyyaml pytest test_fetch_transcripts.py -v
```

Expected: all 10 tests pass.

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py scripts/test_fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: VideoMeta + format_transcript_markdown with tests"
```

---

### Task 6: Failing test for `output_filename`

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/test_fetch_transcripts.py`

- [ ] **Step 1: Append the failing test**

```python
from fetch_transcripts import output_filename


def test_output_filename_slug_naming():
    meta = VideoMeta(
        title="Shipbuilding Tutorial in Victoria 3",
        video_id="x", url="u", duration_seconds=0,
        playlist="tutorials", playlist_index=1,
    )
    assert output_filename(meta, naming="slug") == "01-shipbuilding.md"


def test_output_filename_pads_to_two_digits():
    meta = VideoMeta(
        title="Foo", video_id="x", url="u", duration_seconds=0,
        playlist="tutorials", playlist_index=7,
    )
    assert output_filename(meta, naming="slug") == "07-foo.md"


def test_output_filename_episode_naming():
    meta = VideoMeta(
        title="Victoria 3: Japan Becomes a Superpower! | The Great Wave - ep1",
        video_id="x", url="u", duration_seconds=0,
        playlist="great-wave-japan", playlist_index=1,
    )
    assert output_filename(meta, naming="episode") == "ep01.md"


def test_output_filename_episode_naming_two_digit():
    meta = VideoMeta(
        title="...ep17", video_id="x", url="u", duration_seconds=0,
        playlist="great-wave-japan", playlist_index=17,
    )
    assert output_filename(meta, naming="episode") == "ep17.md"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest --with pyyaml pytest test_fetch_transcripts.py -v
```

Expected: 4 new tests fail with `ImportError: cannot import name 'output_filename'`.

---

### Task 7: Implement `output_filename`

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Add output_filename**

Append after `format_transcript_markdown`:

```python
def output_filename(meta: VideoMeta, *, naming: str) -> str:
    """Stable per-video filename driven by playlist naming policy."""
    index = f"{meta.playlist_index:02d}"
    if naming == "episode":
        return f"ep{index}.md"
    if naming == "slug":
        slug = slugify_title(meta.title) or f"video-{meta.video_id}"
        return f"{index}-{slug}.md"
    raise ValueError(f"unknown naming policy: {naming!r}")
```

- [ ] **Step 2: Run tests to verify they pass**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest --with pyyaml pytest test_fetch_transcripts.py -v
```

Expected: all 14 tests pass.

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py scripts/test_fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: output_filename with tests"
```

---

### Task 8: Playlist enumeration via yt-dlp subprocess

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

No new test — this is a thin wrapper over a subprocess. Verification is "does it return the right list of `VideoMeta` for the real tutorials playlist", which we do at the integration step.

- [ ] **Step 1: Add enumeration function**

Append after `output_filename`:

```python
import subprocess


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
        # Duration can be 'NA' for live/upcoming; treat as 0.
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
```

Why tab-delimited: titles can contain `|`, `,`, and other punctuation, but yt-dlp's `--print` output never inserts tabs.

- [ ] **Step 2: Smoke test it against the real tutorials playlist**

```bash
cd /Users/ybc/code/vic3
uv run scripts/fetch_transcripts.py --debug-enumerate tutorials
```

This subcommand doesn't exist yet — that's fine, we'll wire it in Task 11. For now just verify the function in a one-off:

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with youtube-transcript-api --with yt-dlp python -c "from fetch_transcripts import enumerate_playlist; metas = enumerate_playlist('https://www.youtube.com/playlist?list=PL1QPWs6KwuOCu0dfHoKgsySV3xE_eQ9Z8', 'tutorials'); print(len(metas), metas[0])"
```

Expected: `21 VideoMeta(title='Shipbuilding Tutorial in Victoria 3', ...)`

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: enumerate_playlist via yt-dlp subprocess"
```

---

### Task 9: Caption fetch via youtube-transcript-api (primary path)

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Add fetch function**

Append:

```python
def fetch_captions_api(video_id: str) -> list[dict]:
    """Fetch English captions via youtube-transcript-api.

    Returns a list of {"text": str, "start": float} dicts. Raises on failure
    so the caller can fall back to yt-dlp.
    """
    from youtube_transcript_api import YouTubeTranscriptApi

    # Prefer manually-created English captions, then auto-generated English.
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    try:
        transcript = transcript_list.find_manually_created_transcript(["en", "en-US", "en-GB"])
    except Exception:
        transcript = transcript_list.find_generated_transcript(["en", "en-US", "en-GB"])
    return [{"text": e["text"], "start": e["start"]} for e in transcript.fetch()]
```

- [ ] **Step 2: Smoke test against a known-captioned video**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with youtube-transcript-api python -c "from fetch_transcripts import fetch_captions_api; entries = fetch_captions_api('ct-PUjt6M8c'); print(len(entries), entries[0])"
```

Expected: A number > 100 and a dict like `{'text': '...', 'start': 0.0}`. If this errors with `TranscriptsDisabled` or `NoTranscriptFound`, that's still a success — it proves the error path works and the fallback in the next task will pick up.

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: fetch_captions_api primary path"
```

---

### Task 10: Caption fetch via yt-dlp (fallback path)

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Add fallback function**

Append:

```python
import json as _json
import tempfile
from pathlib import Path


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
        data = _json.loads(candidates[0].read_text())

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
```

- [ ] **Step 2: Smoke test fallback path**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with yt-dlp python -c "from fetch_transcripts import fetch_captions_ytdlp; entries = fetch_captions_ytdlp('ct-PUjt6M8c'); print(len(entries), entries[0])"
```

Expected: A count > 100 and an entry dict. Should match the API output reasonably closely.

- [ ] **Step 3: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: fetch_captions_ytdlp fallback path"
```

---

### Task 11: Wire it all together (main + CLI)

**Files:**
- Modify: `/Users/ybc/code/vic3/scripts/fetch_transcripts.py`

- [ ] **Step 1: Add the writer, runner, and CLI**

Append:

```python
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
    playlists = _json.loads(CONFIG_PATH.read_text())
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
```

- [ ] **Step 2: Verify the CLI parses**

```bash
cd /Users/ybc/code/vic3
uv run scripts/fetch_transcripts.py --help
```

Expected: argparse help with `--only` and `--force`.

- [ ] **Step 3: Re-run unit tests to make sure nothing regressed**

```bash
cd /Users/ybc/code/vic3/scripts
uv run --with pytest --with pyyaml pytest test_fetch_transcripts.py -v
```

Expected: 14 tests pass.

- [ ] **Step 4: Commit**

```bash
cd /Users/ybc/code/vic3
git add scripts/fetch_transcripts.py
git -c commit.gpgsign=false commit -m "phase 1: wire runner, writer, and CLI"
```

---

### Task 12: Run against the tutorials playlist

**Files:**
- Creates: `/Users/ybc/code/vic3/transcripts/tutorials/*.md` (21 files)

- [ ] **Step 1: Execute**

```bash
cd /Users/ybc/code/vic3
uv run scripts/fetch_transcripts.py --only tutorials
```

Expected: Per-video status lines `[ok      ]` or `[fallback]` for all 21 videos. Exit code 0.

- [ ] **Step 2: Verify file count and inspect one**

```bash
cd /Users/ybc/code/vic3
ls transcripts/tutorials/ | grep -c '\.md$'
head -20 transcripts/tutorials/01-shipbuilding.md
```

Expected: count is `21`. Head shows frontmatter then `[00:00]` marker.

- [ ] **Step 3: Verify idempotency (rerun should skip all)**

```bash
cd /Users/ybc/code/vic3
uv run scripts/fetch_transcripts.py --only tutorials
```

Expected: All 21 lines say `[skipped ]`.

- [ ] **Step 4: Commit tutorial transcripts**

```bash
cd /Users/ybc/code/vic3
git add transcripts/tutorials/
git -c commit.gpgsign=false commit -m "phase 1: raw transcripts for tutorials playlist (21 videos)"
```

---

### Task 13: Run against the great-wave-japan playlist

**Files:**
- Creates: `/Users/ybc/code/vic3/transcripts/great-wave-japan/*.md` (17 files)

- [ ] **Step 1: Execute**

```bash
cd /Users/ybc/code/vic3
uv run scripts/fetch_transcripts.py --only great-wave-japan
```

Expected: 17 status lines, exit 0.

- [ ] **Step 2: Verify**

```bash
cd /Users/ybc/code/vic3
ls transcripts/great-wave-japan/ | grep -c '\.md$'
head -20 transcripts/great-wave-japan/ep01.md
```

Expected: count is `17`. Head shows frontmatter with `playlist: great-wave-japan`.

- [ ] **Step 3: Commit campaign transcripts**

```bash
cd /Users/ybc/code/vic3
git add transcripts/great-wave-japan/
git -c commit.gpgsign=false commit -m "phase 1: raw transcripts for great-wave-japan playlist (17 episodes)"
```

---

### Task 14: Phase 1 gate — report to user

- [ ] **Step 1: Generate phase 1 summary**

```bash
cd /Users/ybc/code/vic3
echo "=== File counts ==="
ls transcripts/tutorials/ | grep '\.md$' | wc -l
ls transcripts/great-wave-japan/ | grep '\.md$' | wc -l
echo
echo "=== Caption sources used ==="
grep -h '^caption_source:' transcripts/tutorials/*.md transcripts/great-wave-japan/*.md | sort | uniq -c
echo
echo "=== Total transcript size ==="
du -sh transcripts/
```

Expected: 21 + 17 = 38, source breakdown by `youtube-transcript-api` vs `yt-dlp-auto`, total size.

- [ ] **Step 2: Report to user**

Surface to user:
- Total files produced
- Any videos that failed (from prior task output)
- The caption-source breakdown (tells us whether the fallback ever kicked in)
- Path to spot-check (e.g., `transcripts/tutorials/01-shipbuilding.md`)
- Ask: "Phase 1 done. Proceed to phase 2 (per-video notes)?"

Do not start phase 2 until the user confirms.
