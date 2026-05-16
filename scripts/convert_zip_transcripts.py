# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "yt-dlp>=2024.1.1",
# ]
# ///
"""Convert pre-downloaded MM:SS-prefixed transcripts (.txt) into our standard
frontmatter+timestamp markdown. Designed for content that can't be fetched
directly (e.g., when the captions endpoint is IP-blocked but the user can
download the transcripts via the YouTube UI or a third-party tool).

Usage:
  uv run scripts/convert_zip_transcripts.py <src_dir> <playlist_slug>

Playlist slug must match an entry in scripts/playlists.json — we use that to
look up the playlist URL and naming policy, then enumerate the playlist via
yt-dlp to get authoritative per-video metadata (title, video_id, duration).

Episode matching: filename must contain `ep<NN>` (1-based).
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_transcripts import (  # noqa: E402
    enumerate_playlist,
    format_transcript_markdown,
    output_filename,
)


LINE_RE = re.compile(r"^(\d+):(\d+)\s+(.*)$")
EP_RE = re.compile(r"ep(\d+)", re.IGNORECASE)


def parse_txt(path: Path) -> list[dict]:
    entries: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = LINE_RE.match(line.strip())
        if not m:
            continue
        mins, secs, text = m.groups()
        start = int(mins) * 60 + int(secs)
        text = text.strip()
        if text:
            entries.append({"text": text, "start": float(start)})
    return entries


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2

    src_dir = Path(sys.argv[1]).resolve()
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

    out_dir = repo_root / "transcripts" / playlist_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    fetched_at = date.today().isoformat()

    txt_files = sorted(src_dir.glob("*.txt"))
    print(f"\nConverting {len(txt_files)} files from {src_dir} ...", flush=True)

    ok = 0
    skipped: list[str] = []
    for txt in txt_files:
        m = EP_RE.search(txt.stem)
        if not m:
            skipped.append(f"{txt.name}: no episode number in filename")
            continue
        ep_num = int(m.group(1))
        meta = metas_by_index.get(ep_num)
        if meta is None:
            skipped.append(f"{txt.name}: no playlist entry for ep{ep_num}")
            continue
        entries = parse_txt(txt)
        if not entries:
            skipped.append(f"{txt.name}: no parseable transcript lines")
            continue
        body = format_transcript_markdown(
            meta, entries, source="manual-zip", fetched_at=fetched_at
        )
        out_path = out_dir / output_filename(meta, naming=pl["naming"])
        out_path.write_text(body, encoding="utf-8")
        print(f"  [ok] {txt.name} -> {out_path.name} ({len(entries)} segments)")
        ok += 1

    print(f"\n{ok} converted, {len(skipped)} skipped")
    for s in skipped:
        print(f"  SKIP {s}")
    return 0 if not skipped else 1


if __name__ == "__main__":
    raise SystemExit(main())
