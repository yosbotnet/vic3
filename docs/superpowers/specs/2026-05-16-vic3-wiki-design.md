# Victoria 3 Knowledge Base — Design

Date: 2026-05-16
Status: Approved by user (pending spec review)

## Goal

Build a personal Victoria 3 knowledge base from YouTube content in three phases:

1. **Raw transcripts** of two playlists (38 videos, ~14 hours).
2. **Per-video study notes** distilled by Claude from the transcripts.
3. **Topic-organized wiki / course** synthesized from the notes, with the
   campaign playthrough used as case-study material.

Each phase ends in a hard checkpoint: the user reviews output before the next
phase begins.

## Source playlists

| Slug                | URL                                                                          | Videos | Style                  |
| ------------------- | ---------------------------------------------------------------------------- | -----: | ---------------------- |
| `tutorials`         | https://www.youtube.com/playlist?list=PL1QPWs6KwuOCu0dfHoKgsySV3xE_eQ9Z8     |     21 | Topic tutorials        |
| `great-wave-japan`  | https://www.youtube.com/playlist?list=PLsT4scrqjQbTSBvfQQBpMnGQzcwkteRvp     |     17 | Campaign playthrough   |

Source of truth: `scripts/playlists.json`. New playlists are added there and
re-running the fetch picks them up.

## Repo layout

```
/Users/ybc/code/vic3/
├── transcripts/
│   ├── tutorials/
│   │   ├── 01-shipbuilding.md
│   │   └── ...
│   └── great-wave-japan/
│       ├── ep01.md
│       └── ...
├── notes/                     # phase 2
│   ├── tutorials/
│   └── great-wave-japan/
├── wiki/                      # phase 3
│   ├── README.md              # index / course path
│   ├── economy/
│   ├── politics/
│   ├── diplomacy/
│   ├── military/
│   └── case-studies/
├── scripts/
│   ├── fetch_transcripts.py
│   └── playlists.json
└── docs/superpowers/
    ├── specs/   # this file
    └── plans/   # implementation plan(s)
```

## Phase 1 — Raw transcripts

### Tooling

- **Primary:** `youtube-transcript-api` (Python). Direct caption fetch, no
  audio download, structured output (text + start timestamps).
- **Fallback:** `yt-dlp --write-auto-sub --sub-lang en --skip-download` for
  videos where the API errors out (private captions, regional blocks, etc.).
- **Playlist enumeration:** `yt-dlp --flat-playlist` (already proven working).

### Output format

One markdown file per video:

```
---
title: "Shipbuilding Tutorial in Victoria 3"
video_id: ct-PUjt6M8c
url: https://www.youtube.com/watch?v=ct-PUjt6M8c
duration_seconds: 1554
playlist: tutorials
playlist_index: 1
fetched_at: 2026-05-16
caption_source: youtube-transcript-api   # or yt-dlp-auto
language: en
---

[00:00] full transcript text with timestamp markers every ~30 seconds so a
note that references a specific moment can be looked up quickly...

[00:32] next chunk...
```

### Filenames

- `tutorials/`: `NN-<slug>.md` where `NN` is the zero-padded `playlist_index`
  and `<slug>` is derived from the title (lowercased, non-alnum → `-`, "in
  victoria 3" / "tutorial" / version tags stripped).
- `great-wave-japan/`: `ep01.md` … `ep17.md` (titles only differ by episode
  number, so the slug carries no extra information).

### Script behavior

- Reads `scripts/playlists.json`, processes each playlist.
- Idempotent: skips files that already exist unless `--force` is passed.
- Logs per-video status (`ok` / `skipped` / `fallback` / `failed`).
- Exits non-zero if any video ends in `failed` so partial runs are visible.
- No retry loops with sleeps; one attempt per source, fallback to the next.

### What "done" means for phase 1

- 38 transcript files exist with correct frontmatter.
- Any `failed` videos are listed in chat so the user can decide how to handle
  them (manual caption upload, skip, etc.) before phase 2.

## Phase 2 — Per-video study notes

One markdown file per source transcript, in `notes/<playlist>/<same-name>.md`.

### Tutorial notes structure

```
# <Topic>

**Source:** [<title>](<url>) (NN:NN)

## Summary
2-4 sentences on what the video covers and when it matters in a campaign.

## Core mechanics
Numbered list of the actual game mechanics explained. Use in-game terms
(e.g., "Construction Sector", "Standard of Living", "GDP"). Each item is
1-3 sentences.

## Numbers & formulas
Bulleted list of any concrete numbers, multipliers, thresholds, or formulas
the video states. Tag each with the timestamp `[mm:ss]` for verification.

## Common pitfalls
Bulleted list of mistakes the video warns about.

## Cheatsheet
A 3-6 line "do this, then this" recipe a player could keep open while
playing.
```

### Campaign notes structure

```
# Episode N — <short descriptor>

**Source:** [<title>](<url>)

## What happened
2-4 sentence narrative of the episode.

## Decisions made
Bulleted list of strategic decisions. For each: what was chosen, the
alternatives, and the reasoning given on stream.

## Outcomes
What worked, what backfired. Tie outcomes back to the decisions above.

## Reusable lessons
Bulleted list of takeaways generalized away from the Japan campaign
specifically (e.g., "early subsidization of basic-goods buildings beats
direct construction when literacy is low because…").
```

### Generation approach

- One subagent per video, dispatched in parallel batches (use
  `superpowers:dispatching-parallel-agents` skill). Batch size kept moderate
  to stay within rate limits — exact number tuned during execution.
- Each subagent is given: the transcript file path, the note template for
  that playlist, the output path. It returns only success/failure.
- Faithfulness rule baked into the prompt: every number/formula must be
  traceable to a `[mm:ss]` timestamp in the transcript. If a claim cannot be
  sourced, omit it.

### What "done" means for phase 2

- 38 note files exist.
- User has spot-checked at least 2 tutorial notes and 1 campaign note and
  confirmed the style is what they want before phase 3 begins.

## Phase 3 — Topic-organized wiki / course

### Structure

- `wiki/README.md` — index + suggested learning order for a new player.
- `wiki/economy/` — construction, companies, trade, market, balance sheet,
  foreign investment, standard of living.
- `wiki/politics/` — laws and law passing, political movements, citizenship,
  cultural fervor, acceptance/assimilation/conversion.
- `wiki/diplomacy/` — power blocs, treaty ports, small-nation play.
- `wiki/military/` — army, navy, war.
- `wiki/case-studies/japan-great-wave.md` — single synthesized writeup of
  the campaign, broken into themed sections (industrial takeoff, political
  reform, military buildup) with links into the topic pages above.

Exact topic-to-video mapping is built during execution by reading the
tutorial notes. The list above is the starting hypothesis; if a tutorial
turns out to belong elsewhere it gets placed there.

### Per-page contents

- Lead paragraph: what the system is, when it matters.
- Mechanics section: definitive explanation, drawing from one or more
  tutorial notes (cited as `[Source: 02-deficit-spending]`).
- Strategy section: how to use it in practice. May draw on campaign notes.
- "See also" links to related wiki pages.

### What "done" means for phase 3

- Wiki is internally navigable from `README.md` (every page reachable, no
  dead links).
- Every claim is traceable back to a source note (and through it to a
  transcript timestamp).

## Git workflow

- Repo initialized at start of phase 1.
- Commit at the end of each phase, with messages like:
  - `phase 1: raw transcripts for tutorials + great-wave-japan playlists`
  - `phase 2: per-video study notes`
  - `phase 3: topic-organized wiki`
- Intermediate commits within a phase only if there's a clear logical chunk
  (e.g., "phase 1 script + tutorials playlist", "phase 1 great-wave-japan").

## Out of scope (YAGNI)

- Static site generator. Plain markdown only.
- Video / audio download. Captions only.
- Translation. English transcripts only.
- Automated tests for the wiki content. Spot-checking is the QA mechanism.
- LLM-graded "is this note faithful" check. Faithfulness rule in the prompt
  + user spot-check at the phase 2 gate is the QA mechanism.
- Re-fetching transcripts on every run. Idempotent skip is the default.

## Open risks

- **Auto-generated captions only.** Most of these videos likely don't have
  human captions, so transcripts will contain occasional misheard words
  (especially in-game proper nouns). The note prompt should be told to treat
  obvious caption errors as such and infer the intended in-game term.
- **Caption rate limiting.** `youtube-transcript-api` has historically been
  hit by YouTube blocks. If we get blocked, the `yt-dlp` fallback should
  pick up the slack.
- **Notes may diverge in style.** Parallel subagents working independently
  can produce stylistically inconsistent notes. Mitigation: a fixed template
  in the prompt + user review at the phase 2 gate before phase 3 commits to
  the style.
