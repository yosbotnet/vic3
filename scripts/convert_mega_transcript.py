# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "yt-dlp>=2024.1.1",
# ]
# ///
"""Split a 'Transcriptomatic Export'-style mega transcript file (multiple
videos concatenated with SOURCE: markers, cleaned VTT body) into our
standard frontmatter markdown layout.

This format has no per-line timestamps — VTT cues were stripped. Output
keeps that limitation: one `[00:00]` marker only, with the full body
as a single block.

Usage:
  uv run scripts/convert_mega_transcript.py <mega_txt> <playlist_slug>
"""

from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_transcripts import (  # noqa: E402
    VideoMeta,
    enumerate_playlist,
    format_transcript_markdown,
    output_filename,
)


SOURCE_RE = re.compile(r"^SOURCE:\s*(\d+)_(.+?)\.en\.vtt\s*$", re.MULTILINE)


def split_mega(text: str) -> list[tuple[int, str, str]]:
    """Return [(index, source_basename, body_text), ...] in order."""
    matches = list(SOURCE_RE.finditer(text))
    out: list[tuple[int, str, str]] = []
    for i, m in enumerate(matches):
        idx = int(m.group(1))
        basename = m.group(2)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        # Strip the leading section separator + trailing separator
        body = re.sub(r"^={5,}", "", body, count=1).strip()
        body = re.sub(r"={5,}$", "", body).strip()
        # Strip the "Kind: captions Language: en" preamble if present
        body = re.sub(r"^Kind:\s*captions\s+Language:\s*\S+\s*", "", body, count=1).strip()
        # Decode HTML entities and collapse &nbsp; runs into single spaces
        body = html.unescape(body)
        body = re.sub(r"\s+", " ", body).strip()
        out.append((idx, basename, body))
    return out


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2

    mega_path = Path(sys.argv[1]).resolve()
    playlist_slug = sys.argv[2]

    repo_root = Path(__file__).resolve().parent.parent
    config = json.loads((repo_root / "scripts" / "playlists.json").read_text())
    pl = next((p for p in config if p["slug"] == playlist_slug), None)
    if pl is None:
        print(f"unknown playlist slug: {playlist_slug}", file=sys.stderr)
        return 2

    print(f"Enumerating playlist {playlist_slug} ...", flush=True)
    metas = enumerate_playlist(pl["url"], playlist_slug)
    metas_by_index = {m.playlist_index: m for m in metas}
    print(f"  {len(metas)} videos in playlist", flush=True)

    print(f"\nParsing mega file: {mega_path} ...", flush=True)
    chunks = split_mega(mega_path.read_text(encoding="utf-8"))
    print(f"  {len(chunks)} SOURCE blocks found", flush=True)

    out_dir = repo_root / "transcripts" / playlist_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    fetched_at = date.today().isoformat()

    ok = 0
    for idx, basename, body in chunks:
        meta = metas_by_index.get(idx)
        if meta is None:
            print(f"  SKIP {idx} ({basename}) — no playlist entry")
            continue
        # Single chunk because we have no per-line timestamps; emit a single
        # entry at start=0 so format_transcript_markdown produces one [00:00] block.
        entries = [{"text": body, "start": 0.0}]
        markdown = format_transcript_markdown(
            meta, entries, source="manual-vtt-cleaned", fetched_at=fetched_at
        )
        out_path = out_dir / output_filename(meta, naming=pl["naming"])
        out_path.write_text(markdown, encoding="utf-8")
        print(f"  [ok] ep{idx:02d} -> {out_path.name} ({len(body)} chars)")
        ok += 1

    print(f"\n{ok}/{len(chunks)} converted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
