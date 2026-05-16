---
sources:
  - ../../transcripts/beginner-tutorial/ep04.md
  - ../../transcripts/beginner-tutorial/ep13.md
  - ../../transcripts/beginner-tutorial/ep17.md
  - ../../notes/great-wave-japan/ep08.md
wiki:
  - https://vic3.paradoxwikis.com/Unifications
generated_at: 2026-05-16
---

# Nation Formation

## What it is
Nation Formation is the act of replacing your current country tag with a larger, pre-defined tag (Scandinavia, Germany, Italy, Empire of Japan, North German Confederation, Iberia, etc.) once you control — or coerce — a defined set of constituent states. It is mechanically distinct from simply expanding via conquest: formation triggers a one-shot transition that swaps your flag, name, capital region, and automatically accepts the relevant cultures, often unlocking new Homelands and Journal Entries. It matters because it is the cleanest mid-game lever for jumping a tier in Rank and culture-acceptance simultaneously, and because some Journal Entries (e.g. the Komei Restoration line that leads to the Empire of Japan) effectively *require* it as their payoff.

There are two paths to every formable tag: a **peaceful path** that requires you to already control (directly or through low-autonomy subjects) the listed states, and a **Major Unification Play** that uses a special Diplomatic Play, gated by the Pan-Nationalism tech, to declare a region-wide war for unification against every independent holder of an in-region state.

## Mechanics
1. **Two formation paths** — Every formable tag is reachable either by (a) **direct control** of the per-formation state list, or (b) launching a **Major Unification Play** that adds every independent in-region state holder as a defender simultaneously. The culture screen shows both buttons — checkmarks indicate which constituent states you currently satisfy. *Decision rule:* prefer the peaceful path; only pull the Unification Play when one or two stubborn holdouts make peaceful state-count math impossible.
2. **The state-count requirement** — Each formation lists the constituent state regions and a minimum threshold (not always all of them). Scandinavia, for example, lists 16 region states and requires 11 of them. *Decision rule:* read the tooltip on the formation button — the checkmarks tell you exactly which states still need to flip.
3. **Pan-Nationalism gates the war path** — The Major Unification Play button is greyed out until you research **Pan-Nationalism**. Without it, your only option is the peaceful state-count path. *Decision rule:* if your formation is contested by a Great Power, treat Pan-Nationalism as a critical-path tech and slot it ahead of late-tier industry.
4. **Subject autonomy gating** — A subject's states only count toward formation if the subject is at **Dominion or lower autonomy** (Dominion, Puppet, Vassal, Personal Union, integrated). **Protectorates do NOT count.** This is the single most common formation blocker. *Decision rule:* the moment a country is on your formation list, plan to reduce them at least one tier below Protectorate.
5. **Reduce Autonomy diplomatic action** — Decrease Autonomy is the chain that walks subjects up the integration ladder (Protectorate → Dominion → Puppet → annexed). It is only clickable when the subject's **Liberty Desire is below the threshold** (low — see numbers below). The button is on the Diplomacy → Subjects screen. *Decision rule:* if Liberty Desire is climbing, freeze the action queue and switch to relations + economic dependence until it drops.
6. **Personal Union is dynastic, not contractual** — A PU (the relationship Sweden starts with Norway) requires **Nationalism** to integrate directly, and can break from dynastic events without warning. PU itself contributes 0% of subject income but does pass 50% of convoys. *Decision rule:* don't bank a multi-decade formation plan on a PU staying intact — convert it to a Puppet (or integrate via Nationalism) once the option is available, even at the relations cost.
7. **PU → Puppet → annex chain** — Decreasing a PU to Puppet takes 30% of subject income, 50% of convoys, and adds +50 Liberty Desire as a one-shot. From Puppet you can integrate via the standard flow. *Decision rule:* schedule the demote during a period of high relations and low Liberty Desire — the +50 LD hit on demotion can otherwise lock you out of the next step for years.
8. **Formation accepts cultures automatically** — Pressing the formation button accepts the relevant constituent cultures (Norwegian, Danish, Finnish for Scandinavia; the Japanese-archipelago cultures for Empire of Japan). This shifts your political balance overnight — newly-accepted cultures become voters and pop-up new IGs. *Decision rule:* model the political shift before forming. Forming Scandinavia mid-law-enactment can derail a contested law as the electorate changes underneath you.
9. **Major Unification Play returns out-of-region war goals** — The Play auto-targets in-region states only; out-of-region holdings of the same target country are offered as **give-back / return** war goals to keep infamy manageable. *Decision rule:* take only the in-region war goals; let the Play give back out-of-region land rather than swallow the infamy.
10. **Minor vs Major formation** — There are minor formations (e.g. North German Confederation as a stepping-stone) and major formations (Germany, Scandinavia, Italy, Empire of Japan). They share the same Play mechanic but differ in scope and prerequisites. *Decision rule:* check whether your target is reachable via a minor formation first — it's often cheaper than the major Play.
11. **Formation can fire via Journal Entry** — Some formations are tied to a Journal Entry (e.g. the Komei Restoration triggers Empire of Japan formation rather than going through the standard culture-screen button). *Decision rule:* if a Journal Entry is open for your target, treat the JE clock as the formation timer — that's the path the game expects you to use.

## Game numbers & rules of thumb
- Scandinavia: 16 constituent state regions listed, **11 required** for peaceful formation (Sweden starts with check marks on its own 5 states plus the 3 Norwegian states via PU; the rest are Danish + Finnish + Icelandic).
- Pan-Nationalism is the tech that unlocks the **Launch Unification Play** button for Major formations.
- Personal Union income share: **0%** taxation, **50%** convoy share. Puppet: **30%** taxation, **50%** convoy share, applied at conversion with **+50 Liberty Desire** one-shot.
- Reduce Autonomy / improvements baseline cap: **+50 relations** from Improve Relations alone — to climb above 50 you need a **Trade Agreement, Defensive Pact, or Alliance** (verify exact +pp).
- Subject-autonomy formation gate: **Dominion or lower** counts; **Protectorate does NOT count** (this is the explicit gating shown when forming Scandinavia in the tutorial).
- Forming the nation accepts the listed cultures automatically and may rename your capital region.
- Major Unification Play targets every independent in-region state holder *simultaneously* — verify the join list (allies of holders can be dragged in) before pressing.
- A subject of a Great Power inside the formation region drags that Great Power into the Play. Sweden's tutorial attempt pulled in Great Britain and France because of their relations and ties (verify exact trigger).
- Empire of Japan example: formation happens as the Komei Restoration Journal Entry completes; daimyo convert to Kazoku, capital relocates, three Restoration JEs open on a 12-year clock.

## Strategy & playbook
**Peaceful path.** Pick this whenever your formation list is dominated by minors and small powers you can wear down individually. The work is sequencing: identify every in-region state, mark the holders, and triage by accessibility. Holders that are already your subjects need Reduce Autonomy chains to reach Dominion or lower (a Protectorate held for "stability" is dead weight — it gives you nothing toward the state count). Holders that are independent need either conquest or diplomatic absorption (Puppet via Diplomatic Play, then annex). Holders that are subjects of a Great Power (Russia held Finland in the Sweden tutorial; Britain held everything in the Danish western Atlantic) are the hard cases — either accept that those states won't contribute to your count, or wait for a Pan-Nationalism Major Play that lets you contest them under one big war.

**War path (Major Unification Play).** Use this when the peaceful state count cannot reach the threshold without fighting a Great Power, or when a single subject of a Great Power is the last missing state. Pre-conditions: Pan-Nationalism researched, infamy at or near zero (the Play is expensive), and an Army roughly twice the size of any single independent holder in the region (the Play declares against *all* of them at once). Time it for when you have at least one strong ally — the Sweden tutorial run failed twice when France and the UK joined the Danish side, and only succeeded on a reload when both stayed neutral. Always inspect the Opening Moves screen before locking the Play: see who Joins and who Backs Away. If a Great Power's flag is on the defender list, abort, fix relations or sway, and re-try. Use the give-back war goals on out-of-region territories — taking them only pumps infamy without helping the formation.

**Subject management is the formation engine.** Every prospective member subject needs to be at **Dominion or lower** at formation time. The order of operations is: build economic dependence in their states (Foreign Investment, factories that they need), keep relations climbing toward the +50 cap and beyond via Trade Agreement / Defensive Pact / Alliance, and only then press Decrease Autonomy. Liberty Desire is the gate — if it's climbing because of recent tax extraction or a war, pause and bleed it down before reducing. For a PU specifically, expect a +50 LD spike at the moment of demotion to Puppet; queue the action only when current LD is comfortably below threshold so the spike doesn't overshoot.

**Timing formation around Journal Entries.** Some formations *are* the payoff of a Journal Entry chain rather than a separate decision. The Empire of Japan formation fires as part of the Komei Restoration in the Japan campaign — the JE's 12-year clock is effectively your formation deadline, and the JE rewards (Restoration laws, daimyo → Kazoku, capital move) come bundled. For tag-formed nations without a JE wrapper (Scandinavia, Italy, North German Confederation), pick the formation moment for a *political* reason — formation accepts new cultures and shifts your electorate, so press it when you want that shift (e.g. to add liberal Norwegian voters to push through Right of Assembly), not in the middle of a contested vote you'd otherwise win.

**Handle Great Power neighbours preemptively.** If your formation region borders a Great Power that owns or subjects part of it, the Major Play will pull them in. The Sweden tutorial fought this exact problem with Russia (holding Finland), Great Britain (defending Denmark), and France (random siding). The reliable answer is the relations stack: Trade Agreement to lift the +50 cap, Defensive Pact / Alliance to push higher, Investment Rights / foreign-investment buildings to lock in economic dependence. If even that fails, a Major Play often turns into a save-scum re-roll for a quiet diplomatic window when the neighbour doesn't decide to join.

## Common pitfalls
- **Leaving prospective-member subjects at Protectorate autonomy.** Protectorates contribute zero to the formation state count even if you own them outright — they must be Dominion or lower to count.
- **Launching the Major Unification Play without inspecting the defender list.** A single in-region state held by a subject of a Great Power drags that Great Power into the Play; the tutorial got France *and* Britain dragged into a Scandinavian Play that looked clean on paper.
- **Banking on a Personal Union to last.** PUs can break on dynastic events without warning. Convert to Puppet (and onward to annexation) once Nationalism is researched, even at the relations cost.
- **Forgetting the cultural-acceptance side effect.** Formation auto-accepts the listed cultures, which immediately changes your voter base and IG strengths. Forming during a contested law vote can flip outcomes — model the new electorate first.
- **Stacking infamy via Major Play returns.** The Play offers in-region annexation as the primary war goal and out-of-region states as give-back. Adding the out-of-region states as extra war goals doubles your infamy without advancing formation.
- **Improving relations and stalling at 50.** The Improve Relations action caps at +50. To get past that — required for high-trust subject demotion and for swaying allies into the Play — you need a Trade Agreement, Defensive Pact, or Alliance.
- **Ignoring Liberty Desire spikes.** Every demotion step (e.g. PU → Puppet) carries a +50 Liberty Desire one-shot. Pressing it while LD is already mid-range can lock you out of the next step for years.

## Cheatsheet
1. **Read the formation tooltip** in the Culture screen: list the constituent states, count the checkmarks, identify each missing state's holder.
2. **Triage holders into three buckets:** (a) my subjects above Dominion → schedule Decrease Autonomy chain; (b) independent minors → set as Rival, fight or Puppet via Diplomatic Play; (c) subjects of Great Powers → either accept loss or plan a Major Unification Play.
3. **Research Pan-Nationalism** if any bucket-(c) state is critical to your count, and **research Nationalism** to integrate a Personal Union.
4. **Build economic dependence in target subjects** via Foreign Investment and factories in their states; **upgrade relations past 50** with a Trade Agreement, Defensive Pact, or Alliance; **wait for Liberty Desire to drop** below threshold (~25% region, verify) before clicking Decrease Autonomy.
5. **Before launching a Major Unification Play:** confirm zero or near-zero infamy, an Army that outweighs the largest single in-region holder, at least one swayed ally, and a defender preview that does NOT include any unintended Great Power. Save manually as insurance.
6. **At formation time:** confirm every required state has a checkmark, expect new cultures to enter your electorate, and look for bundled Journal Entries (Empire of Japan-style) that may unlock the next phase of the campaign.

## See also
- **In this wiki:**
  - [Standard of Living](../pops/standard-of-living.md)
  - [Treasury and Deficit](../economy/treasury-and-deficit.md)
  - [Construction](../economy/construction.md)
  - [Companies](../economy/companies.md)
  - [Trade](../economy/trade.md)
  - [Foreign Investment](../economy/foreign-investment.md)
  - [Passing Laws](../laws-and-politics/passing-laws.md)
  - [Citizenship and Acceptance](../laws-and-politics/citizenship-and-acceptance.md)
  - [Cultural Fervor](../laws-and-politics/cultural-fervor.md)
  - [Technology](../laws-and-politics/technology.md)
  - [Power Blocs](../diplomacy/power-blocs.md)
  - [Small Nation Play](../diplomacy/small-nation-play.md)
  - [Colonization](../diplomacy/colonization.md)
  - [Army](../military/army.md)
  - [Navy](../military/navy.md)
  - [War and Naval Invasions](../military/war-and-naval-invasions.md)
  - [Japan Great Wave — Phase 2: Restoration](../case-studies/japan-great-wave/phase-2-restoration.md) (Empire of Japan formation example)
- **Official wiki:**
  - [Unifications](https://vic3.paradoxwikis.com/Unifications)
  - [Subjects](https://vic3.paradoxwikis.com/Subjects)
  - [Diplomatic_plays](https://vic3.paradoxwikis.com/Diplomatic_plays)
