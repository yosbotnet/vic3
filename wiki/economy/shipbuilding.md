---
sources:
  - ../../notes/tutorials/01-shipbuilding.md
wiki:
  - https://vic3.paradoxwikis.com/Naval_warfare
generated_at: 2026-05-16
---

# Shipbuilding (1.13+)

## What it is

The shipbuilding system rewritten in update 1.13 (Great Wave). All naval construction now flows through regular **Shipyards** — there is no separate military shipyard. Shipyards produce **ship construction points** that feed a shared queue split between **military ships** and **supply ships**, while **navy maintenance** silently skims points off the top before any new hull is built. The optional **Ship Designer** (Great Wave DLC) turns each ship class into an editable template that drives both combat performance and the input goods your shipyards demand. A new **Navy Model** law group is the strategic dial that says *which* kinds of ships your industry is good at producing.

The system matters from day one: navy demand is heavy in wood, hardwood, and fabric, so it competes directly with your Construction Sector for the same goods — shipbuilding decisions are construction decisions.

## Mechanics

1. **Shipyards produce ship construction points** — The same building outputs Clippers (a tradeable good) *and* ship construction points; the base production method yields 5 points per level `[from 01-shipbuilding]`. Decision rule: if Clippers stay profitable, leave the shipyard unsubsidised and let the market pay wages; if Clipper prices collapse and employment drops, **subsidise immediately** — otherwise point output silently falls and your queue stalls without any explicit warning.
2. **Navy maintenance skims points off the top** — A portion of weekly points is consumed maintaining the existing fleet *before* any goes to building. Decision rule: keep maintenance well under half your total point output. Whenever you queue more hulls, expand Shipyards in the same breath — a fleet that has outgrown its shipyards stops growing.
3. **Allocation slider splits the leftover between military and supply queues** — Moves in 25% increments. Critically, **unused points spill** to the other queue automatically: if you set the slider fully to military but the military queue is empty, supply still gets built. Decision rule: aim the slider at the queue you actively want to grow; do not micromanage it for balance, the spill handles that.
4. **Ship Designer templates (Great Wave DLC)** — For each ship type you create named templates choosing a level (1–3) for **Armor**, **Armament**, **Propulsion**, **Supply Capacity**, **Carrying/Marine Capacity**, plus a wild-card slot. The right-hand tally shows construction-point cost, weekly upkeep, and — most importantly — the **input goods** the shipyard will start demanding. Decision rule: **read the input-goods tooltip before saving**, because the moment a template is queued, your shipyard's demand profile changes. Without the DLC, you only get the base template per type.
5. **Each design lever has a distinct combat job** —
   - **Armor** reduces HP loss; ships sink at 0 HP and may retreat at low HP. Crew depletion can also lose the battle.
   - **Armament** raises hull and crew attack.
   - **Propulsion** sets sea-node movement speed. A fleet moves at the speed of its **slowest ship** — do not mix slow hulls into fast fleets.
   - **Supply Capacity** is the orange bar consumed away from home port. Empty supply drops organisation and collapses offence/defence.
   - **Carrying/Marine Capacity** sets battalions and marines per ship. At Lv2 a frigate carries only 0.25 battalions (so 4 frigates per battalion); Lv3 carries 0.5.
6. **Retrofitting upgrades existing ships to a new template** — Ship list → edit → multi-select (or Select All) → Change Template → Retrofit. Fleets sail home (must be docked) and the queue **subtracts the cost of work already done** from the new template's cost. Decision rule: small tweaks retrofit quickly, full redesigns retrofit slowly — bias edits toward additive upgrades rather than wholesale rewrites if you need the fleet back fast. Fleets split automatically so unaffected ships continue current missions.
7. **Capital vs Cruiser roles** — **Capitals** (e.g. Ship of the Line) hit hardest and tank with armour but have high **Vulnerability**, so enemies target them first. **Cruisers** have high **Screening** (soak attacks to keep capitals firing) and low **Visibility** (slip through hostile sea nodes without triggering battle). Decision rule: never field a capital-only fleet — capitals are bad at hitting torpedo boats, torpedo-boat cruisers, submarines, and destroyers, so torpedo specialists shred them. Cruisers are also the correct escort for trade and troop transport because of their low Visibility.
8. **Construction Efficiency = free construction points** — A +25% efficiency modifier means every invested point counts as 1.25 toward that ship's cost. Decision rule: read Navy Model law modifiers as efficiency dials and **stack them additively** with global modifiers (–10% all + +30% supply = +20% net on supply, –10% on military).
9. **Navy Model law group** — Pick the law matching your strategic plan:
   - **Merchant Navy** — net buff to supply and troop ships, debuff elsewhere. Use when you don't intend serious naval combat: trade protection and troop transport only.
   - **Jeune École** — buffs torpedo craft and specific cruisers, cheaper navy goods, +officer political strength. Use to swarm a larger enemy with cheap specialised hulls.
   - **Capital Fleet** — buffs capital ships, +prestige from navy, faster naval administration hiring. Use to build an intimidating big-gun navy.
   - **Diplomatic Fleet** — buffs all cruisers, +involvement generation, +regional trade advantage, faster admin hiring. Use to project presence into many strategic regions cheaply.
10. **Naval administrations man the ships** — Building a hull does not crew it; **Naval Administration** buildings provide the sailors. Decision rule: queue administrations *alongside* hulls, not after — and especially in wartime, where dead sailors must be re-hired before a damaged ship returns to combat. Capital Fleet and Diplomatic Fleet laws speed this hiring.

## Game numbers & rules of thumb

- Shipyard base PM produces **5 ship construction points per level** `[from 01-shipbuilding]`.
- Supply-ship maintenance: **1 maintenance point per 133.33 supply ships** `[from 01-shipbuilding]`.
- Military-ship maintenance: **1 maintenance point per 3,333.33 construction points of built military ships** `[from 01-shipbuilding]`. A 405-point Ship of the Line therefore costs ~0.12 maintenance each.
- Allocation slider moves in **25% steps**; unused points spill to the other queue.
- A frigate at Lv2 supply/carrying carries **0.25 battalions and 0.12 marines**; at Lv3, **0.5 battalions and 0.25 marines** `[from 01-shipbuilding]`.
- A fleet moves at the **speed of its slowest ship**.
- Construction Efficiency: **+X% efficiency → each invested point counts as 1+X/100** toward the build.
- Navy Model modifiers stack **additively** with the global ship modifier.
- **Capitals: high Vulnerability** (targeted first). **Cruisers: high Screening, low Visibility.**
- Navy demand at game start leans heavy on **wood, hardwood, and fabric** — the same goods Construction Sectors want.

## Strategy & playbook

**Treat shipyards as a second construction queue.** The same building that ships Clippers to the world market is now the bottleneck on every hull in your navy. Before you queue a war or a colonial push, look at the maintenance ticker: if maintenance is already eating most of your point output, no amount of slider-fiddling will fix it — you need more Shipyard levels. The cheap heuristic is to keep maintenance under half of total output, and to add a Shipyard level every time you commit to a meaningful new fleet. Because Shipyards also produce Clippers, this expansion is rarely a pure loss; in a peacetime economy the Clipper revenue partially funds itself, and a healthy market price keeps wages off the Treasury entirely.

**Pick the Navy Model law before you design the fleet, not after.** The four laws are not flavour — they are construction-efficiency multipliers, and they decide which hulls are cheap to spam. If your plan is to protect trade and ferry armies, **Merchant Navy** turns supply and troop ships into bargains while paying a small tax on combat hulls you weren't going to build anyway. If you are a small power trying to bleed a great power's navy, **Jeune École** lets you swarm with torpedo boats and specialised cruisers. If you want a prestige navy that headlines diplomatic plays, **Capital Fleet** stacks +25% on the big-gun line and accelerates admin hiring so casualties refill quickly. If you are a colonial power who needs presence in many sea regions cheaply, **Diplomatic Fleet** turns cruisers into your default hull and pays you in involvement and regional trade.

**Design templates around input goods, not just stats.** When you open the Ship Designer, the right-hand panel tells you what your shipyards will start demanding the moment you queue this template. A new template that adds Steel and Oil is a *new industrial commitment* — make sure you have or are building those supply chains first, or your hulls will stall on missing inputs while you scramble to build steelworks. Conversely, picking a slightly weaker armament tier might keep your shipyards on cheaper inputs and let you actually build the navy you've designed. This is the lever non-DLC players cannot pull, which is part of why Great Wave is so impactful for naval majors.

**Build composite fleets, not monocultures.** Capitals are obvious — big guns, big armour, big prestige — but they are also targeted first and they cannot reliably hit torpedo craft. A real combat fleet wants Cruisers screening Capitals, plus enough Supply Capacity to operate away from home. A real trade-protection or invasion fleet wants Cruisers up front (low Visibility, they slip through enemy nodes) plus enough Supply Ships that the orange bar never empties. Match Propulsion across the fleet, because the slowest ship sets fleet speed — a single Lv1-Propulsion supply ship will drag your battle line into being out-manoeuvred.

**Retrofit instead of rebuilding.** When tech or laws make a new template available, do not scrap and rebuild — open the ship list, select all of the obsolete type, Change Template, Retrofit. The queue subtracts work already done, so an additive upgrade is fast. This is the cheap way to keep a navy current across decades; reserve fresh builds for net expansion.

## Common pitfalls

- **Expanding the navy without expanding Shipyards** — maintenance silently eats your entire construction throughput and the queue crawls.
- **Letting Clipper prices collapse without subsidising** — the shipyard loses employment, point output drops, and you don't get a popup.
- **Forgetting Naval Administrations** — hulls exist but aren't manned, especially painful when wartime casualties cannot be replaced.
- **Saving a Ship Designer template without checking its input-goods tooltip** — your shipyards' demand profile (and therefore your import bill or supply-chain plan) changes the moment it enters the queue.
- **Mixing a slow ship into a fast fleet** — the whole fleet drops to the slowest ship's speed.
- **All-capital fleets** — capitals struggle against torpedo boats, torpedo-boat cruisers, submarines, and destroyers; without cruiser screens they get carved up.
- **Operating far from home with too few supply ships** — supply bar empties, organisation falls, offence/defence collapse mid-engagement.
- **Treating the allocation slider as a balance** — it spills automatically; the slider is a *priority*, not a *ratio*.

## See also

- **In this wiki:**
  - [military/navy.md](../military/navy.md) — fleet roles, sea nodes, naval engagements
  - [military/war-and-naval-invasions.md](../military/war-and-naval-invasions.md) — convoys, transport fleets, invasion mechanics
  - [economy/construction.md](./construction.md) — competing demand on wood, hardwood, fabric
  - [economy/building-balance-sheet.md](./building-balance-sheet.md) — reading Shipyard profitability and Clipper prices
  - [case-studies/japan-great-wave.md](../case-studies/japan-great-wave.md) — a 1.13 playthrough using the new system
- **Official wiki:**
  - [Naval_warfare](https://vic3.paradoxwikis.com/Naval_warfare)
  - [Laws](https://vic3.paradoxwikis.com/Laws)
  - [Production_methods](https://vic3.paradoxwikis.com/Production_methods)

## Sources

- `../../notes/tutorials/01-shipbuilding.md` — *Shipbuilding Tutorial in Victoria 3* (1.13 Great Wave), transcribed mechanics, numbers, and law modifiers.
