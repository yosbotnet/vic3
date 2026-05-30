---
sources:
  - ../../notes/great-wave-japan/ep01.md
  - ../../notes/great-wave-japan/ep02.md
  - ../../notes/great-wave-japan/ep05.md
  - ../../notes/great-wave-japan/ep06.md
  - ../../notes/great-wave-japan/ep08.md
  - ../../notes/great-wave-japan/ep10.md
  - ../../notes/great-wave-japan/ep11.md
  - ../../notes/great-wave-japan/ep12.md
  - ../../notes/great-wave-japan/ep13.md
  - ../../notes/great-wave-japan/ep14.md
  - ../../notes/great-wave-japan/ep16.md
  - ../../notes/tutorials/21-how-to-play-as-a-small-nation.md
  - ../../notes/comprehensive-tutorial-2025/06-belgium-synthesis.md
  - ../../notes/comprehensive-tutorial-2025/03-domestic-politics.md
wiki:
  - https://vic3.paradoxwikis.com/Technology
generated_at: 2026-05-16
---

# Technology & Research

## What it is

Technology is the long-term lever for everything that compounds in Victoria 3 — building output, military strength, political reform options, late-game buildings. Unlike laws or construction, you don't *spend* on tech directly; you generate Innovation (mostly via Universities and Art Academies) which advances active research, while passive Technology Spread brings you techs your neighbours already have. The right tech path varies by starting position, but the rules for *how* to spend research time and bonuses are general.

## Mechanics

1. **Active research vs Technology Spread** — Active research advances one tech per tree at a rate set by Innovation. Spread runs in parallel and grants techs that neighbours already have, one per tree branch, with no choice over what spreads. Decision rule: before queuing a tech, open the Technology Spread panel — if a tech is already coming via spread, queue something else instead. Researching a spreading tech wastes weeks of Innovation [from [21-how-to-play-as-a-small-nation](https://github.com/yosbotnet/vic3/blob/main/notes/tutorials/21-how-to-play-as-a-small-nation.md)].

2. **Innovation cap is set by your building base, not your literacy** — High literacy without Universities still caps Innovation low. [ep02](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep02.md) shows Japan at 77% literacy (rank 1 globally) capturing only 50 of 165 possible Innovation because no Universities were built. Decision rule: get Universities online as a priority *before* declaring your literacy strategy a success.

3. **Literacy affects tech SPREAD speed, not active research speed** — Losing literacy from annexed-pop dilution is acceptable; it only slows what spreads to you, not what you research [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)]. Patch 1.13.1 added a twist: literacy now decays toward education access. If literacy is sliding for no obvious reason, raise education access via Promote Social Mobility, schooling laws, or religious-academia institutions — the old "literacy is sticky" intuition is obsolete [[ep13](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep13.md)].

4. **Permanent unlocks beat temporary modifiers, always** — When a journal entry, event, or mission offers a choice between an institution unlock (e.g., Public Schools) and a flat +X% research speed for N years, take the institution. Institutions compound; flat modifiers expire. This rule held across the Japan run: Mission Report → Public Schools over +6% research [[ep08](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep08.md)], "Modernizing the Arsenal" journal pin for 10y arms/artillery research bonus over temporary alternatives [[ep16](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep16.md)], "Smoke Streams" event chosen for university bonus when few universities existed (relative scaling > absolute number) [[ep12](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep12.md)].

5. **Time-limited research bonuses go on path-shorteners, not raw-biggest numbers** — A 5-year +X% research bonus is worth more on whatever shortens the path to a *pivotal* tech (railways, atmospheric engine, banking) than on a tech with the largest absolute research value. Permanent picks taken later still apply [[ep06](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep06.md)].

6. **Schedule high-value techs into bonus windows** — When you can see an upcoming temporary research malus followed by a bonus window (common with national-spirit cycles or 1.13 patch events), queue cheap prerequisites during the malus and stack high-value techs to land inside the bonus [[ep13](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep13.md)].

7. **Innovation building upgrades compound — never skip them** — When a research unlock opens a new Innovation-building PM (Dialectics → Universities pathway is the canonical one), adopt it as soon as the inputs are affordable. Passive science output is the cheapest source of long-run tech tempo; skipping it is a permanent self-tax [[ep05](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep05.md)].

8. **Tech prerequisites gate laws and buildings; pre-check them** — Some laws and buildings are locked behind specific techs (Warrior Caste repeal needs General Training; iron-frame buildings need Atmospheric Engine; viable engine ships need the propulsion tier). Read the prerequisite chain *before* queuing the law/building; reordering reactively wastes journal-entry time windows [[ep01](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep01.md), [ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md), [ep11](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep11.md)].

9. **Universities are government-only — research costs government wages** — The two halves of research speed are literacy (it raises how much Innovation/research you can *hold*, the cap) and Universities (they *generate* the actual research). There are **no privatised Universities** — the building is always government-run, so every level of research output is paid for out of government wages, not private investment. Decision rule: budget Universities as a *government expense*, not a self-financing private building; in a tight treasury, rushing a slow high-tier tech via mass Universities (e.g. malaria prevention for a Congo colony plan) means accepting a real, ongoing wage bill — there is no privatise-it escape hatch (2025 comprehensive tutorial, [2:02:30]).

10. **Institutions & bureaucracy: the maintenance loop** — Certain laws *create* an institution in your nation (e.g. an education institution from a schooling law). In the institutions tab you then spend **bureaucracy** to raise an institution's **size** for stronger country-wide buffs — and you must keep paying that bureaucracy to *maintain* the size; it is an ongoing upkeep, not a one-off purchase. Bureaucracy itself comes from the **Government Administration** building, which is always government-run and can get expensive as you scale. Decision rule: an institution's buffs are usually worthwhile, but each notch of size is a permanent bureaucracy bill — before raising an education or healthcare institution, confirm you can sustain the Government Administration (and keep paper cheap, since it feeds the admin cost) without forcing a bureaucracy deficit (2025 comprehensive tutorial, [43:00]).

## Game numbers & rules of thumb

- **University:** 400 construction, +20 urbanization per level, plus Innovation. The canonical research building [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md), [ep11](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep11.md)].
- **Art Academy:** 400 construction, +20 urbanization per level (equivalent footprint to University) [[ep11](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep11.md)].
- **Government Administration:** 250 construction, +20 urbanization, builds extremely fast, downgradable. *Not* a research building — but the cheapest urbanization-per-construction-point, so it's the urbanization-speedrun building for journal-entry urbanization tier requirements [[ep11](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep11.md)]. Compare urbanization-per-construction-point, not per-level [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md), [ep11](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep11.md)].
- **Technology Spread:** one tech per tree branch from neighbours, passive [from [21-how-to-play-as-a-small-nation](https://github.com/yosbotnet/vic3/blob/main/notes/tutorials/21-how-to-play-as-a-small-nation.md)].
- **Literacy:** affects tech-spread speed only, not active research speed [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)].
- **Literacy decay (1.13.1+):** decays toward your education-access level — maintain education-access laws to hold literacy [[ep13](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep13.md)].
- **Universities are always government-run** — no privatised version exists, so research output is funded from government wages (2025 comprehensive tutorial, [2:02:30]).

## Strategy & playbook

### Opening tech pivot by country position

The right *first* tech depends on what your country is:

- **Multi-state regional power** → **Stock Exchange first** (+10% Market Access — huge for split economies) [from [21-how-to-play-as-a-small-nation](https://github.com/yosbotnet/vic3/blob/main/notes/tutorials/21-how-to-play-as-a-small-nation.md), see also [small-nation-play](../diplomacy/small-nation-play.md)].
- **Single-state minor** → **Skip Stock Exchange** (Market Access doesn't matter with one state); go straight to Academia and Universities.
- **Threatened or contested** → **Rush military tree to General Staff** (unlocks General Training, materially raises battalion quality) before anything else.
- **Backward great power (Japan-type)** → **Cotton Gin → Lathe → Atmospheric Engine, then jump to next propulsion tier** [[ep01](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep01.md)]. Production/construction techs still beat shiny DLC techs for an early backward economy; Atmospheric Engine is the gate to iron-frame buildings and to viable engine-equipped ships.

In every case, after the opening pivot **head for Academia and start building Universities one at a time** (one per state, staggered, to manage cash) — each level adds Innovation, which directly compresses research weeks but consumes paper and wages [[ep16](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep16.md)].

### Mid-game tech path (economic stabilisation)

Once the opening pivot is done, the Japan run's mid-game path is a strong template for any country with treasury pain: **Currency Standards → Banking → Central Archives → Dialectics, then military** [[ep06](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep06.md)]. Reasoning:

- **Central Archives** multiplies tax capacity and government-admin output — fixes bureaucracy deficits at their source.
- **Banking** lowers loan interest, the most common active pain point during reform.
- **Dialectics** feeds future Universities (PM upgrade).
- **Military deferred** until the economic base is solid; military techs are useful but rarely save your run.

Other high-leverage mid-game picks observed: a Gentry-dividend tech that broadened the private investment pool (aristocrats, farmers, clergymen contribute) [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)]; Chemical Bleaching to crush paper prices for bureaucracy [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)]; a Company tech that grants Industrialist clout before naval upgrades [[ep16](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep16.md)].

### Build paper, then universities, then qualifications

Universities run on paper. Building Universities before bringing the paper price down means each level is hugely expensive and may turn unprofitable [[ep02](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep02.md)]. The build order that worked for Japan:

1. **Paper Mill** (or import paper) to lower the market price.
2. **Tools and Steel** to handle the construction-good cost spike.
3. **Universities staggered one per state** — cheap qualification booster (+20 urbanization at 400 construction) and Innovation engine.
4. **Upgrade Universities' PM** when Dialectics lands.

Bottleneck rule: queue Tools and Steel buildings *before* mass-queuing Universities and upgraded buildings, and use queue reordering to push input-good buildings to the front [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)].

### Reading journal and event tech rewards

Journal and event rewards routinely offer "permanent unlock vs temporary research-speed bonus" choices. The default rule **permanent wins**:

- Mission Report → Public Schools (institution) over +6% research speed [[ep08](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep08.md)].
- "Modernizing the Arsenal" journal pin → 10y arms/artillery research bonus *because* it's permanent within the journal slot, beating temporary alternatives [[ep16](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep16.md)].
- Industrialized Japan completion → military research speed reward [[ep12](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep12.md)].
- "Smoke Streams" event → university bonus (high relative scaling because few universities built yet) [[ep12](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep12.md)].

For *temporary* bonuses you can't refuse, spend them on path-shorteners to a pivotal tech (e.g., railways), not on whatever has the biggest raw number [[ep06](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep06.md)].

### When to take "Always pick a research that is always happening"

The Japan run encountered an event offering a tech that "always happens" — a Gentry-dividend tech that broadens private investment. Decision rule [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)]: take it. A tech granting a structural always-on improvement (private investment from a new IG class, dividend efficiency, etc.) beats an incremental research pick because the effect runs every tick from then on.

## Common pitfalls

- **High literacy without Universities** — you cap Innovation low regardless of literacy. Build Universities before claiming your literacy strategy works [[ep02](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep02.md)].
- **Ignoring Technology Spread** — actively researching a tech that's already spreading to you wastes weeks of Innovation. Check the Spread panel before queuing [from [21-how-to-play-as-a-small-nation](https://github.com/yosbotnet/vic3/blob/main/notes/tutorials/21-how-to-play-as-a-small-nation.md)].
- **Universities before paper mills** — uni run cost is dominated by paper; high paper prices make them unprofitable. Bring the paper price down first [[ep02](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep02.md)].
- **Mass-queuing Universities before Tools and Steel** — construction-good price spikes stall the run. Queue input-good buildings first [[ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)].
- **Skipping Innovation PM upgrades** — Dialectics-style upgrades compound. Skipping them is a permanent tax on your research speed [[ep05](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep05.md)].
- **Taking temporary +% research over permanent unlocks** — the temporary number looks bigger but is gone in 5–10 years. Institutions and unlocks compound forever [[ep08](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep08.md), [ep16](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep16.md)].
- **Spending temporary bonuses on big-number techs** instead of path-shorteners to a pivotal tech [[ep06](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep06.md)].
- **Reactive prerequisite-chasing** — discovering a law needs a tech you haven't researched, mid-enactment. Pre-check law-prerequisite chains [[ep09](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep09.md), [ep10](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep10.md)].
- **Letting literacy slide without checking education access (1.13.1+)** — literacy decays toward education access; if it falls without obvious cause, the fix is education access laws, not waiting [[ep13](https://github.com/yosbotnet/vic3/blob/main/notes/great-wave-japan/ep13.md)].

## Cheatsheet

1. **Open** with the country-position-appropriate first tech (Stock Exchange / military / Cotton Gin) — see Strategy section.
2. **Build Paper Mill** before Universities; **Universities one per state, staggered**.
3. **Open the Technology Spread panel** before every research queue. Don't actively research what's already spreading.
4. **Mid-game economic backbone tech path:** Currency Standards → Banking → Central Archives → Dialectics, then military.
5. **For every choice:** permanent unlock > temporary modifier. Spend temporaries on path-shorteners to pivotal techs.
6. **Pre-check law prerequisites** when queuing reform — don't discover the missing tech mid-enactment.

## Journal entries

Most unpinned journal entries (Path to Liberalism, Urbanize, Patronize Romanticism, colonial branching-out entries) trigger from normal play; completion typically grants a temporary research-speed bonus or building throughput bonus. When given a choice, take research-speed. Pinned entries with explicit tasks (build a level-5 University, etc.) are usually cheap to chase given other tech-tree priorities. (verify specific entries against current patch — entry names shift) `[from beginner-tutorial ep04]`

## See also

- **In this wiki:**
  - [Passing Laws](passing-laws.md) — laws are gated by techs; tech path drives reform sequencing.
  - [Construction](../economy/construction.md) — University/Art Academy/GA construction costs and queue ordering.
  - [Companies](../economy/companies.md) — some techs unlock company prerequisites.
  - [Standard of Living](../pops/standard-of-living.md) — literacy and education-access mechanics.
  - [Small-Nation Play](../diplomacy/small-nation-play.md) — opening tech pivot is the most differentiated decision for small countries.
  - [Japan case-study: Phase 2 — The Honorable Restoration scramble](../case-studies/japan-great-wave/phase-2-restoration.md) — the mid-game tech-path decisions in context.

- **Official wiki:**
  - [Technology](https://vic3.paradoxwikis.com/Technology) — full tech tree, per-tech effects.
  - [Institutions](https://vic3.paradoxwikis.com/Institutions) — Public Schools and other unlock-permanent rewards.

## Sources

- `notes/comprehensive-tutorial-2025/03-domestic-politics.md` (chapter "3. Domestic Politics" of "The Comprehensive Victoria 3 Tutorial (2025) | Iberian Twilight", Tarkusarkusar, 2025-12-16) — institutions & bureaucracy maintenance loop.
