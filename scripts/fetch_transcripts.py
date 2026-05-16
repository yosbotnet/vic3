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
