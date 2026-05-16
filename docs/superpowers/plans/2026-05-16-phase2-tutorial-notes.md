# Phase 2: Per-Video Tutorial Notes Implementation Plan

> **For agentic workers:** Implement task-by-task. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Produce one markdown study-notes file per tutorial transcript in `notes/tutorials/`, following the structure defined in the design spec (summary → core mechanics → numbers & formulas → common pitfalls → cheatsheet).

**Scope note:** Campaign episodes (`great-wave-japan`) were deferred from phase 1 due to YouTube rate limits. Phase 2 covers only the 21 tutorial transcripts. Campaign notes get written when the backfill (task #6) completes — that's a small follow-up plan, not part of this one.

**Architecture:** A single subagent per video, dispatched in parallel batches via the Agent tool. Each subagent reads one transcript file, follows a fixed prompt template, and writes one output file. The orchestrator (this Claude session) dispatches batches, checks for failures, and re-dispatches as needed.

**Tech Stack:** Markdown files only. No code beyond the orchestration done by Claude. No new dependencies.

---

## File Structure

| Path | Purpose |
| --- | --- |
| `notes/tutorials/` | One `.md` per tutorial video, same basename as the transcript (e.g., transcript `01-shipbuilding.md` → note `01-shipbuilding.md`) |
| `notes/tutorials/_template.md` | The note template (committed for visibility — also embedded in the subagent prompt) |

Notes filenames mirror transcript filenames so a reader can pair `transcripts/tutorials/05-how-to-pass-laws.md` with `notes/tutorials/05-how-to-pass-laws.md`.

---

### Task 1: Write the note template

**Files:**
- Create: `/Users/ybc/code/vic3/notes/tutorials/_template.md`

- [ ] **Step 1: Write template**

Content:

````markdown
---
source_transcript: <relative path from notes/tutorials/, e.g. ../../transcripts/tutorials/01-shipbuilding.md>
source_video: <youtube url>
generated_at: 2026-05-16
---

# <Topic name — e.g., "Shipbuilding">

**Source:** [<video title>](<url>) (NN:NN runtime)

## Summary

2–4 sentences on what the video covers and when in a campaign this knowledge applies.

## Core mechanics

1. **<Mechanic name>** — 1–3 sentences using in-game terms (Construction Sector, Standard of Living, GDP, etc.).
2. **<Next mechanic>** — …
3. …

## Numbers & formulas

- **<What>:** <value or formula> `[mm:ss]`
- **<What>:** <value or formula> `[mm:ss]`
- …

(Every number/formula must be sourced from a `[mm:ss]` timestamp in the transcript. If the video doesn't state explicit numbers, this section may be short or omitted.)

## Common pitfalls

- <Mistake the video warns about>
- …

## Cheatsheet

3–6 line "do this, then this" recipe a player could keep open while playing.

1. <Step>
2. <Step>
3. …
````

- [ ] **Step 2: Commit**

```bash
git -C /Users/ybc/code/vic3 add notes/tutorials/_template.md
git -C /Users/ybc/code/vic3 -c commit.gpgsign=false commit -m "phase 2: note template for tutorial videos"
```

---

### Task 2: Define the subagent prompt

This isn't a code task — it's the prompt to use when dispatching each per-video subagent. Captured here so re-runs are reproducible.

**Subagent type:** `general-purpose` (no specialized agent needed; the subagent just reads + writes a file).

**Prompt template** (substitute `<TRANSCRIPT_PATH>` and `<NOTE_PATH>` per video):

```
You are writing a single study-notes markdown file from a YouTube
Victoria 3 tutorial transcript.

Read this transcript:
  <TRANSCRIPT_PATH>

Write the output to:
  <NOTE_PATH>

The transcript has YAML frontmatter (title, url, duration_seconds) and
a body of timestamped text where each `[mm:ss]` marks roughly 30
seconds of speech.

Follow this exact note structure (h2 headings in this order):

  # <Topic name — concise, no "Tutorial" suffix>

  **Source:** [<title from frontmatter>](<url from frontmatter>) (NN:NN runtime, where NN:NN is mm:ss from duration_seconds)

  ## Summary
  2–4 sentences on what the video covers and when in a campaign this
  knowledge applies.

  ## Core mechanics
  Numbered list. Each item: **bold mechanic name** — 1–3 sentences in
  in-game terms (Construction Sector, Standard of Living, GDP, etc.).

  ## Numbers & formulas
  Bulleted list. EVERY number/formula MUST end with the `[mm:ss]`
  timestamp it appears at in the transcript. If a value is not stated
  in the video, omit it — do not invent numbers. If the video states no
  numbers at all, this section may be omitted entirely.

  ## Common pitfalls
  Bulleted list of mistakes the video warns about. Omit if the video
  doesn't discuss pitfalls.

  ## Cheatsheet
  3–6 line numbered "do this, then this" recipe a player could keep
  open while playing.

YAML frontmatter to put at the very top of the note:

  ---
  source_transcript: <relative path from notes/tutorials/ to the transcript>
  source_video: <url from transcript frontmatter>
  generated_at: 2026-05-16
  ---

Rules:
- Be faithful to the video. Do not add knowledge from outside the transcript.
- Treat obvious caption errors (misheard proper nouns, garbled in-game terms)
  as such — infer the intended term where it's clear (e.g., "construction"
  not "constraction"). When uncertain, mirror the transcript's wording.
- Use Victoria 3's actual terminology. If you spot a term the captions
  mangled but you recognize as in-game terminology, use the correct form.
- Output ONLY the markdown file. Do not preface with explanation, do not
  output a summary of what you did. The Write tool call is the entire
  deliverable.

Report back: just "done" plus the output file size in bytes.
```

- [ ] **Step 1: Save the prompt template inline (already in this plan); no commit needed.**

---

### Task 3: Dispatch first batch (3 tutorials) for quality check

Rationale: rather than dispatching all 21 in parallel and discovering the prompt produces something the user doesn't like, run 3 first, get user approval on the style, then run the remaining 18.

**Files affected (created by subagents):**
- `/Users/ybc/code/vic3/notes/tutorials/01-shipbuilding.md`
- `/Users/ybc/code/vic3/notes/tutorials/02-deficit-spending.md`
- `/Users/ybc/code/vic3/notes/tutorials/11-construction.md`

Choice rationale: video 01 is the most recently produced (post 1.13), 02 is a classic economic mechanic, 11 is mechanics-heavy with many concrete numbers. Together they exercise the template's full structure.

- [ ] **Step 1: Dispatch three subagents in parallel**

Use the Agent tool, `subagent_type: "general-purpose"`, three calls in a single message. Each prompt is the template from Task 2 with paths substituted.

- [ ] **Step 2: Verify all three files exist and have the expected structure**

```bash
ls -la /Users/ybc/code/vic3/notes/tutorials/
head -40 /Users/ybc/code/vic3/notes/tutorials/01-shipbuilding.md
head -40 /Users/ybc/code/vic3/notes/tutorials/11-construction.md
```

Each should have YAML frontmatter, an H1, and the H2 sections (Summary, Core mechanics, etc.).

- [ ] **Step 3: Commit the sample batch**

```bash
git -C /Users/ybc/code/vic3 add notes/tutorials/
git -C /Users/ybc/code/vic3 -c commit.gpgsign=false commit -m "phase 2: sample notes for 3 tutorials (style check)"
```

- [ ] **Step 4: Show output to user and ask for go/no-go**

Surface to user: the 3 files plus a brief observation on what each looks like. Ask: "Style look right? Any structural changes before I run the remaining 18?"

Do not proceed to Task 4 until the user approves.

---

### Task 4: Dispatch remaining 18 tutorials

**Files affected:**
- All 21 transcripts have a corresponding note except the 3 from Task 3.

Run them in two parallel batches of 9 (so a failure in one batch doesn't tie up the whole set, and dispatching too many subagents at once gets unwieldy).

- [ ] **Step 1: Dispatch batch of 9**

Videos 03, 04, 05, 06, 07, 08, 09, 10, 12. All 9 Agent calls in a single message.

- [ ] **Step 2: Verify batch produced 9 new files**

```bash
ls /Users/ybc/code/vic3/notes/tutorials/ | grep -c '\.md$'
```

Expected: 12 (3 from Task 3 + 9 from this batch + 1 for `_template.md`)... actually 13 including template. So `grep -v _template | grep -c '\.md$'` should give 12.

- [ ] **Step 3: Dispatch second batch of 9**

Videos 13, 14, 15, 16, 17, 18, 19, 20, 21. All 9 Agent calls in a single message.

- [ ] **Step 4: Verify all 21 notes exist**

```bash
ls /Users/ybc/code/vic3/notes/tutorials/ | grep -v _template | grep -c '\.md$'
```

Expected: 21.

- [ ] **Step 5: Spot-check 3 randomly picked notes for prompt adherence**

```bash
for f in 05-how-to-pass-laws 14-companies-and-prosperity 19-military-army; do
  echo "=== $f ==="
  head -3 /Users/ybc/code/vic3/notes/tutorials/$f.md
  grep -E '^## ' /Users/ybc/code/vic3/notes/tutorials/$f.md
  echo
done
```

Each should show: frontmatter, then `## Summary`, `## Core mechanics`, `## Numbers & formulas` (or omitted), `## Common pitfalls` (or omitted), `## Cheatsheet`.

- [ ] **Step 6: Commit**

```bash
git -C /Users/ybc/code/vic3 add notes/tutorials/
git -C /Users/ybc/code/vic3 -c commit.gpgsign=false commit -m "phase 2: notes for remaining 18 tutorial videos"
```

---

### Task 5: Phase 2 gate — report to user

- [ ] **Step 1: Generate summary**

```bash
cd /Users/ybc/code/vic3
echo "=== Notes produced ==="
ls notes/tutorials/ | grep -v _template | wc -l
echo
echo "=== Size totals ==="
wc -l notes/tutorials/*.md | tail -1
du -sh notes/
echo
echo "=== Section presence (count of notes with each section) ==="
for h in '## Summary' '## Core mechanics' '## Numbers & formulas' '## Common pitfalls' '## Cheatsheet'; do
  printf "%-25s %d\n" "$h:" "$(grep -l "$h" notes/tutorials/*.md | grep -v _template | wc -l)"
done
```

- [ ] **Step 2: Surface to user**

- Total notes produced (should be 21)
- Per-section presence counts (helps spot if subagents skipped a section)
- Path to spot-check
- Status of campaign backfill (still pending — say "want me to retry now?")
- Ask: "Phase 2 done. Proceed to phase 3 (synthesize topic-organized wiki)?"

Do not start phase 3 until the user confirms.
