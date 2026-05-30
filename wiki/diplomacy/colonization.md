---
sources:
  - ../../notes/great-wave-japan/ep14.md
  - ../../notes/great-wave-japan/ep16.md
  - ../../notes/great-wave-japan/ep17.md
  - ../../transcripts/beginner-tutorial/ep12.md
  - ../../transcripts/beginner-tutorial/ep13.md
  - ../../transcripts/beginner-tutorial/ep14.md
  - ../../transcripts/beginner-tutorial/ep15.md
  - ../../transcripts/beginner-tutorial/ep16.md
  - ../../notes/comprehensive-tutorial-2025/04-diplomacy.md
  - ../../notes/comprehensive-tutorial-2025/06-belgium-synthesis.md
wiki:
  - https://vic3.paradoxwikis.com/Colonization
generated_at: 2026-05-16
---

# Colonization

## What it is
Colonization is the peaceful claim-and-grow mechanic by which a recognised country with an **Interest** in a Strategic Region can absorb adjacent or maritime Decentralised land — the unclaimed grey provinces of Africa, the Pacific, and Southeast Asia at game start. It is the cheapest path to **goods you can't get at home** (rubber, sugar, dyes, coffee, gold, hardwood, sometimes silk-adjacent crops) and to **minting income via gold mines**, but it is also a **race against every other Great Power** with the same colonisation laws — once a state has an existing claim or an active coloniser, you are locked out (`[ep12]`).

Success looks like: a non-malaria coastal foothold acquired before Britain or France paint it their colour, then a chain of adjacent states added at level-2 or level-3 Colonial Affairs speed, the conquered/colonised states kept **unincorporated** for the +20% Colonial Exploitation throughput, and a port (Anchorage or higher) on each non-contiguous landmass so the new states actually feed into your home Market. Failure looks like staring at a 0% market-access colony, a malaria-severe state crawling at 5% normal speed, or — the Bornean-protectorate scenario — losing a fresh subject because you got tied up in another diplomatic play during the truce window (`[great-wave/ep17]`).

## Mechanics
1. **Decentralised target requirement** — only land owned by Decentralised tags (no central government on the map) is colonisable. Recognised or Unrecognised states must be conquered, not colonised (`[ep12]`). *Decision rule:* if the province has a country colour, it's a war target, not a coloniser target.
2. **Existing-claim lockout** — a state that already has a claim from another country (e.g. Argentine claims in southern South America) cannot be colonised by anyone else, even if it's still grey on the map (`[ep12]`). *Decision rule:* hover the state before declaring Interest; if any claim is listed, skip it.
3. **Declare Interest in a Strategic Region** — prerequisite for any colonisation, war goal, or diplo play in that region. Costs Influence and a Strategic Region "interest slot." Slots scale with country rank; higher Colonial Affairs gives more (`[ep13]`, `[ep15]`). *Decision rule:* declare Interest the same week you finish enacting the Colonisation Law — the colony race starts the moment your institution turns on.
4. **Colonisation Law (one of three)** — the prerequisite law that unlocks the Colonial Affairs institution. **Frontier Colonization** only works on land bordering your existing territory and rewards Migration Attraction in unincorporated states (the US default). **Colonial Resettlement** opens overseas land and also boosts unincorporated Migration Attraction. **Colonial Exploitation** opens overseas land and gives **+20% throughput on Plantations, Mines, Forestries, and Rubber Plantations in unincorporated states**, at the cost of lower starting wages and penalties to manufacturing PMs in those states (`[ep12]`). *Decision rule:* Frontier if you have a land border to colonise into; Exploitation if your colonies will be extractive; Resettlement only if you specifically want pops to relocate.
5. **Colonial Affairs institution levels** — gated by the law and by Bureaucracy. Each level adds Colonisation Speed and Strategic Region interest capacity. Tutorial: level 1 base, level 2 roughly **doubles** colonisation speed, level 3 roughly **triples** vs base (`[ep13]`, `[ep16]`). Each level costs ~30 Bureaucracy (`[ep12]`, `[ep16]`). *Decision rule:* park at level 1 while you have one Interest, push to level 2 when you start a second region, level 3 once you have spare Bureaucracy and active colonisation in 2+ regions.
6. **Colonisation Speed inputs** — speed is driven by **incorporated state population** (pops in your home states do the colonising), Colonial Affairs level, and malaria penalty. Sweden with low pop and level-1 Colonial Affairs takes ~2,000 days for one state with malaria (`[ep13]`). *Decision rule:* colonisation speed scales with how big you already are — small nations should expect slow colonisation and prioritise contiguous, non-malaria targets first.
7. **Malaria tiers** — None / Normal / Severe. Normal malaria gives roughly **−90% Colonisation Speed**; Severe is even worse and is hard-blocked until Quinine in 1.7.6 (`[ep12]`, `[ep15]`). Quinine (Society tech, after Pharmaceuticals) **removes all malaria effects in your colonies and states** and unlocks colonisation of Severe-malaria regions (`[ep12]`, `[ep15]`). *Decision rule:* before Quinine, only colonise No-Malaria provinces (Northern Cape, parts of the Sahel, Pacific islands); queue Pharmaceuticals → Quinine the moment you commit to colonial expansion.
8. **Migration Attraction edicts** — **Greener Grass Campaign** is a state edict that boosts Migration Attraction in the target state, used to coax home-country pops into a fresh colony (`[ep14]`). *Decision rule:* worth toggling on a brand-new colony with strong jobs, but it only helps if home pops have **lower SoL** than the colony — otherwise no one moves.
9. **Conquered colonies need a Reset Production Methods state action** — when you take a colony by war (e.g. Brunei via diplo play), all buildings default to the lowest PM tier and use the wrong inputs. The **Reset Production Methods** state action snaps every building to your nation's best available PM for its inputs (`[ep13]`). *Decision rule:* run Reset PMs the same week you take the colony, before unpause; otherwise mines and plantations drag for years.
10. **Incorporation policy on colonies** — by default colonies are **unincorporated**. Unincorporated states get the **+20% Exploitation throughput** under Colonial Exploitation, do NOT count toward national literacy / Innovation, and do NOT consume your full set of laws. Incorporating drags your national literacy average down and surrenders the Exploitation bonus (`[ep13]`). *Decision rule:* leave colonies unincorporated unless you specifically need them counted for a journal entry or a culture-acceptance trigger.
11. **Non-contiguous market access via port** — a colony separated from your home market by sea has **zero Market Access** until you build at least an **Anchorage (level-1 port)** in a coastal state of the colony. One port can cover an entire contiguous landmass (`[ep16]`). *Decision rule:* queue the Anchorage in the same construction sweep as Reset-PMs and privatisation toggles; without it the colony's goods don't reach your home prices.
12. **Privatisation toggles after conquest** — conquered buildings are not auto-flagged for privatisation. Manually re-tick the privatisation checkbox on each colonial Plantation, Mine, Logging Camp, and Tooling Workshop so the local Aristocrats / Capitalists take the dividends (and the Investment Pool builds upgrades) (`[ep13]`). *Decision rule:* sweep the colony's building list once and toggle privatisation on everything that isn't an Arms Industry or a military building.
13. **Tension / Native uprisings** — Colonial Exploitation accumulates state Tension over time; high enough Tension can trigger native revolts. The Economic outliner's colony view shows current Tension (`[ep15]`). *Decision rule:* keep an eye on Tension on long-held Exploitation colonies; Violent Suppression edict trims it but it's not a permanent fix.
14. **Race blocking** — once a Great Power begins colonising a state, the rest of that state is locked to them; in practice this means a coloniser race spreads outward from each player's foothold. Britain colonising South Cameroon next to Sweden's Cameroon foothold blocks Sweden out of half the region (`[ep16]`). *Decision rule:* plant a flag in every contiguous state you might ever want, even slowly — a level-1 colonisation tick is enough to claim the state and lock everyone else out.
15. **Interest slots by rank, with navy as the lever** — the hard cap on simultaneous Strategic-Region Interests scales with rank: **Major Power = 3 max, Great Power = 6**; technology contributes, but the primary lever to generate more slots is a **bigger navy** (Navy Power Projection grants Interest capacity) (2025 comprehensive tutorial, [54:30]). *Decision rule:* if you're slot-starved for the colony race, the fastest fix is shipbuilding and naval tech, not just pushing rank — and it doubles as the convoy/marine capacity you'll need to reach overseas colonies anyway.
16. **Interest UI and activation delay** — when placing Interests the map colour-codes regions: **blue** = an active Interest you already hold (clickable to remove), **green** = a region you may place an Interest in, **orange** = a permanent/automatic Interest (your home region, where you always have one). A newly-placed Interest **takes time to activate** before it gates anything, and without an active Interest you cannot draft treaties with, colonise, or declare war in that region (2025 comprehensive tutorial, [53:30]). *Decision rule:* place the Interest a few weeks *before* you intend to act — an Interest declared the same week you want to colonise or attack isn't usable yet.
17. **Fresh-conquest turmoil and the violent-treatment decree** — a just-conquered colonial state carries very high turmoil (radicalism) that cripples construction efficiency. The **violent-treatment ("chop hands") decree** trades pop mortality for a reduced turmoil penalty, so construction runs less inefficiently while standard of living slowly recovers via market access (2025 comprehensive tutorial, [1:57:01]). *Decision rule:* on a freshly taken extractive colony you intend to build out fast, the violent-treatment decree buys construction throughput at a demographic cost — a short-term lever, not a permanent setting. See the [Belgium conquer-colonize case study](../case-studies/belgium-conquer-colonize-react.md).
18. **Incorporation cost scales with cultural distance** — incorporating a conquered state costs Bureaucracy and **time** scaled by cultural distance: a same-language state incorporates in roughly **27 months**, but a wrong-culture homeland (sharing no heritage or language) can take **~22 years** — a fifth of the game. You cannot tax an unincorporated state, but its collapsed wages make plantation profit explosive (2025 comprehensive tutorial, [1:46:31], [1:55:00]). *Decision rule:* incorporate close-culture conquests (cheap, fast, taxable); farm distant wrong-culture colonies **unincorporated** — the 22-year incorporation timer is never worth surrendering the collapsed-wage plantation margins. See the [Belgium conquer-colonize case study](../case-studies/belgium-conquer-colonize-react.md).

## Game numbers & rules of thumb
- **Severe malaria penalty:** ~−95% Colonisation Speed without Quinine `[ep13]`, `[ep15]`
- **Normal malaria penalty:** ~−90% Colonisation Speed without Quinine `[ep12]`
- **Colonial Affairs level cost:** ~30 Bureaucracy per level `[ep12]`, `[ep16]`
- **Colonial Affairs level effect:** L2 ≈ 2× speed vs L1, L3 ≈ 3× speed vs L1 `[ep13]`, `[ep16]` (verify — tutorial described as "twice as fast" / "three times as fast")
- **Sweden baseline (small-pop, L1, no malaria edicts):** ~350 day-units of progress per tick on a no-malaria state, ~2,000 day-units on a Normal-malaria state `[ep13]`
- **Colonial Exploitation throughput bonus:** +20% on Plantations, Mines, Forestries, Rubber in unincorporated states `[ep12]`, `[ep13]`
- **Brunei conquest infamy:** 4.5 (Make Subject path was much cheaper than full annexation) `[ep13]`, `[great-wave/ep16]`
- **Greener Grass Campaign edict:** state Migration Attraction +70 in the Sweden tutorial example `[ep14]` (verify — exact value patch-dependent)
- **Quinine prerequisite chain:** Pharmaceuticals → Quinine (Society tier) `[ep12]`, `[ep15]`
- **Gold mine value at colony scale:** Sweden's first Brunei gold mine yielded ~1,500 Minting income at base PM; scaled to ~3,000–4,500 Minting once the mine was upgraded a level under the +20% Exploitation and +30% combined modifier stack `[ep13]`, `[ep14]`
- **Strategic Region interest cost:** declaring Interest in a new region uses an Interest slot; slot count rises with Colonial Affairs level and country rank `[ep15]`
- **Interest slot caps by rank:** Major Power = **3 max**, Great Power = **6**; Navy Power Projection is the primary lever to raise the cap, with technology contributing (2025 comprehensive tutorial, [54:30])
- **Incorporation time by cultural distance:** same-language state ≈ **27 months**; wrong-culture homeland ≈ **22 years** (no shared heritage/language). Unincorporated states can't be taxed but pay collapsed plantation wages (2025 comprehensive tutorial, [1:46:31], [1:55:00])
- **Co-locating Interest with Power Bloc Leverage:** an active Interest in a Strategic Region grants +100 Leverage Factor toward countries in that region (see `power-blocs.md`) — colonial Interests do double duty `[ep15]`

## Strategy & playbook
**Early game — pick the law that matches your geography, then race.** If you have a land border into Decentralised land (USA into the Plains, Russia into Central Asia, a colonial-power-with-existing-toehold like Sweden's Zululand), **Frontier Colonization** is the cheapest opening because it only requires bordering, and the institution costs the same Bureaucracy as the others. If your colonies will be entirely overseas, take **Colonial Resettlement** first (it's easier to pass than Exploitation in most cabinets, since the Industrialists and Intelligentsia usually back it). The instant the institution turns on, declare Interest in the nearest non-malaria Strategic Region and start the first colony. The first 1–2 game years of the colonial race are decisive: every state you've already started colonising is one Britain, France, and the Netherlands can't take.

**Mid game — switch to Colonial Exploitation when your colonies are extractive, and unlock malaria.** Once you have your foothold and you know you want **gold, sugar, coffee, dyes, rubber, hardwood**, swap to Colonial Exploitation. The +20% throughput on Plantations, Mines, Forestries, and Rubber in unincorporated states is the single largest production modifier you'll stack on those buildings, and it stacks with state mining edicts for a combined ~50% in tutorial Sweden's Brunei (`[ep13]`). Cabinet composition matters: getting Industrialists + Intelligentsia + Armed Forces in support takes the enactment chance from ~24% to ~40%, often via Land-Reform → Tenant Farmers shuffle (`[ep12]`). Research **Pharmaceuticals → Quinine** in parallel; until Quinine lands, you simply cannot meaningfully colonise the malaria belt (`[ep12]`, `[ep15]`).

**Late game — keep colonies unincorporated, sweep the secondary regions, and consider protectorate-first.** The temptation is to incorporate fat colonies to "tidy up the map" — don't. Incorporation surrenders the Exploitation throughput bonus AND drags your national literacy average down, which can drop your Innovation cap and choke your research (`[ep13]` discussion of low-literacy Borneo). The right pattern is to keep adding contiguous unincorporated states, build one Anchorage per landmass, and reset PMs after any conquest. For weak coastal targets you don't want to colonise slowly, the **protectorate-first** pattern (`great-wave/ep16`, Brunei → Sulu → Lanfang) is faster than colonising and lower infamy than annexing: declare a Make-Subject diplo play, get the protectorate, demote to puppet later, optionally annex when Liberty Desire drops. Note the **truce-window trap** (`great-wave/ep17`, Bulongan): if you're tied up in a second diplo play during the protection truce, the subject can "fail to protect" and break free — sequence subject wars so you have free diplomatic bandwidth.

**Conquered-colony first-week checklist (the Brunei pattern).** When you take an existing colony by war (not by colonisation): (1) Reset Production Methods via state action — every building is on the worst PM by default; (2) leave the state **unincorporated**; (3) queue an Anchorage in a coastal state if it's non-contiguous; (4) tick **privatise** on every Plantation, Mine, Forestry, Logging Camp, Tooling Workshop (not Arms Industries); (5) cancel any half-built building that duplicates a home-state queue (e.g. a fertilizer plant you're already building at home); (6) toggle the best mining edict on Gold/Silver/Iron states for the +10% throughput stack. Sweden's Brunei went from a freshly-conquered drag into the run's largest Minting source inside ~12 in-game months following this sequence (`[ep13]`, `[ep14]`).

**Migration to colonies: lower their SoL ceiling than yours, then push.** Pops migrate **up** the SoL gradient, not down. Sweden's Brunei stalled because Swedish home pops had higher SoL than colonial Borneo even after Cultural Exclusion accepted Europeans, so no one moved — Greener Grass Campaign added Attraction but couldn't overcome the gradient (`[ep14]`). For migration to actually work, the colony needs **good wages from a profitable extractive building** (the gold mine job market eventually pulled some Chinese laborers from neighbouring states), and your home pops need a SoL squeeze (overcrowding, slum churn). If migration is critical, run **Multiculturalism** (or at minimum Cultural Exclusion to accept the home culture group) on top of Greener Grass.

## Common pitfalls
- **Incorporating a low-literacy colony.** It drags your national literacy average down and can drop your Innovation cap. Keep colonies unincorporated unless you have a specific reason `[ep13]`.
- **Subsidising a colony's Urban Centers / Services early.** The pops aren't there yet — you're paying wages for empty buildings. Let the gold mine and plantations hire first; Services come later organically `[ep13]`.
- **Colonising Severe-malaria provinces before Quinine.** ~95% speed penalty makes the attempt a Bureaucracy and Authority sink. Either Quinine first or stick to no-malaria coastal foothold states `[ep12]`, `[ep15]`.
- **Picking Colonial Exploitation in states where you're building Industry.** The law specifically penalises manufacturing PMs in unincorporated states; if you plan Textile / Steel / Tooling in a colony, Exploitation is the wrong law `[ep12]`.
- **Conquering a colony and forgetting Reset Production Methods.** Every building runs on the lowest PM with the worst input mix until you click the state action — months of lost throughput `[ep13]`.
- **Skipping the Anchorage on a non-contiguous colony.** Zero Market Access; the colony's gold and plantation goods do not enter your national Market and the prices stay garbage `[ep16]`.
- **Forgetting to re-tick privatisation on conquered buildings.** They sit state-owned, the Investment Pool doesn't upgrade them, and dividends don't flow to Aristocrats/Capitalists `[ep13]`.
- **Inviting a new colony into a war-truce-blocked subject relationship.** "Failed to protect" auto-independence wipes the subject if you're already in another diplo play during the truce window `[great-wave/ep17]`.
- **Race-blocking yourself.** Sitting on a slow colonisation tick in one state while Britain paints the rest of the region. Plant a flag in every contiguous state you might want, even at L1 Colonial Affairs speed `[ep16]`.
- **Losing Interest mid-colonisation.** If your Interest in a region lapses (slot reassigned, dropped manually), in-progress colonisation **freezes**. Visible in the tutorial as "no progress in one of our colonies" after Interest was reassigned `[ep16]`.

## Cheatsheet
1. **Pass the Colonisation Law that matches your geography** (Frontier if you have a land border, Exploitation if extractive, Resettlement if you specifically want pops to relocate). Get Industrialists + Intelligentsia + Armed Forces in cabinet for the ~40% enactment chance `[ep12]`.
2. **Declare Interest in the nearest no-malaria Strategic Region** the same week the institution turns on, then start the first colony.
3. **Queue Pharmaceuticals → Quinine** in Society research before you commit to malaria-belt expansion `[ep12]`, `[ep15]`.
4. **Push Colonial Affairs to L2 (≈30 Bureaucracy)** once you start a second region — speed roughly doubles. L3 (≈60 Bureaucracy total) when you have spare and active colonisation in 2+ regions `[ep13]`, `[ep16]`.
5. **On any conquered colony, in this order:** Reset PMs → leave unincorporated → build an Anchorage if non-contiguous → tick privatise on all non-military buildings → enable mining edicts on extractive states `[ep13]`, `[ep14]`, `[ep16]`.
6. **Keep colonies unincorporated** for the +20% Exploitation throughput and to keep low-literacy colonial pops out of your national average; only incorporate for a specific journal-entry or acceptance trigger `[ep13]`.

## See also
- **In this wiki:**
  - [Standard of Living](../pops/standard-of-living.md) — pops migrate up the SoL gradient; the colony has to beat home wages or the Greener Grass Campaign does nothing.
  - [Treasury and Deficit](../economy/treasury-and-deficit.md) — Colonial Affairs is paid in Bureaucracy, but colony construction (ports, mines, replacement PMs) is a real treasury drain.
  - [Construction](../economy/construction.md) — Anchorage ports and PM upgrades on conquered colonies need construction sector throughput.
  - [Companies](../economy/companies.md) — colonial extractives (rubber, sugar, coffee, gold) often unlock company prerequisites.
  - [Trade](../economy/trade.md) — non-contiguous colonies need port-based market access before their goods enter your national prices.
  - [Building Balance Sheet](../economy/building-balance-sheet.md) — colonial mines and plantations are read with the same per-building lens as home industries.
  - [Foreign Investment](../economy/foreign-investment.md) — investment rights interact with Colonial Affairs in late game.
  - [Passing Laws](../laws-and-politics/passing-laws.md) — the Colonisation Law and Migration Controls Laws are passed through the normal enactment path.
  - [Citizenship and Acceptance](../laws-and-politics/citizenship-and-acceptance.md) — accepted cultures can migrate to your colonies; discriminated cultures cannot.
  - [Technology](../laws-and-politics/technology.md) — Quinine sits in the Society tree; Pharmaceuticals is its prerequisite.
  - [Power Blocs](power-blocs.md) — colonial Interests double as +100 Leverage Factor in the Strategic Region.
  - [Small Nation Play](small-nation-play.md) — flip side: surviving great-power colonial Interests in your own region.
  - [War and Naval Invasions](../military/war-and-naval-invasions.md) — many colonies arrive via Make-Subject diplo play + marine naval invasion, not via slow colonisation.
  - [Japan: Phase 5 Expansion](../case-studies/japan-great-wave/phase-5-expansion.md) — the Bornean protectorate chain (Brunei, Sulu, Lanfang, Bulongan) and the "failed to protect" truce-window loss.
  - [Belgium: conquer, colonize, react](../case-studies/belgium-conquer-colonize-react.md) — the Congo left unincorporated for collapsed-wage plantation profit, the violent-treatment decree on a fresh conquest, and malaria-prevention tech gating equatorial colonisation.
- **Official wiki:**
  - [Colonization](https://vic3.paradoxwikis.com/Colonization)
  - [Decentralized power](https://vic3.paradoxwikis.com/Decentralized_power)
  - [Institutions](https://vic3.paradoxwikis.com/Institutions)
  - [Strategic regions](https://vic3.paradoxwikis.com/Strategic_regions)

## Sources
- `../../transcripts/beginner-tutorial/ep12.md`
- `../../transcripts/beginner-tutorial/ep13.md`
- `../../transcripts/beginner-tutorial/ep14.md`
- `../../transcripts/beginner-tutorial/ep15.md`
- `../../transcripts/beginner-tutorial/ep16.md`
- `../../notes/great-wave-japan/ep14.md`
- `../../notes/great-wave-japan/ep16.md`
- `../../notes/great-wave-japan/ep17.md`
- `../../notes/comprehensive-tutorial-2025/04-diplomacy.md` — "The Comprehensive Victoria 3 Tutorial (2025) | Iberian Twilight" by Tarkusarkusar, 2025-12-16, ch. 4 Diplomacy (Interest slots, colour coding, activation delay).
- `../../notes/comprehensive-tutorial-2025/06-belgium-synthesis.md` — same video, Belgium synthesis (incorporation cost by cultural distance, violent-treatment decree).
