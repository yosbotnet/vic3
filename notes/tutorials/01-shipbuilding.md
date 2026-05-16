---
source_transcript: ../../transcripts/tutorials/01-shipbuilding.md
source_video: https://www.youtube.com/watch?v=ct-PUjt6M8c
generated_at: 2026-05-16
---

# Shipbuilding (1.13 Great Wave)

**Source:** [Shipbuilding Tutorial in Victoria 3](https://www.youtube.com/watch?v=ct-PUjt6M8c) (25:54 runtime)

## Summary
The 1.13 Great Wave update consolidates all naval construction into regular Shipyards (no more separate military shipyards), which now output ship construction points used by a shared queue for military ships and supply ships. The Ship Designer (Great Wave DLC) lets you create templates per ship type and retrofit existing fleets to those templates. A new Navy Model law group shapes which ships you specialise in. This system matters from day one because navy upkeep silently consumes a slice of your construction throughput and competes with army/civilian construction for wood, hardwood, and fabric.

## Core mechanics

1. **Shipyards produce ship construction points** — Shipyards now output both Clippers (a tradeable good) and ship construction points; base PM yields 5 points per level [01:01]. If Clipper prices crash and the shipyard loses employment, point output drops. Subsidise the building to keep it fully employed and preserve all points, but if you can keep Clippers profitable you avoid paying wages out of Treasury — unlike Construction Sector wages, which the government always pays [01:30].
2. **Navy maintenance skims construction points off the top** — A portion of weekly ship construction points is consumed maintaining the existing navy before any goes to building [03:00]. Rule: every 133.33 supply ships costs 1 maintenance point [05:02]; every 3,333.33 military construction points worth of built ships costs 1 maintenance point [05:33]. If you expand the fleet without expanding shipyards, maintenance eventually swallows everything and new builds stall [07:31] — expand shipyards in step with the navy.
3. **Allocation slider splits remaining points between military and supply queues** — After maintenance, the slider distributes leftover points; it moves in 25% increments [02:30]. Critically, if the favoured queue has fewer projects than its share, the unused points spill to the other side automatically [02:30] — so setting it fully to military still funds supply when the military queue is empty.
4. **Ship Designer templates (Great Wave DLC)** — For each ship type you create named templates that pick a level (1–3) for Armor, Armament, Propulsion, Supply Capacity, Carrying/Marine Capacity, plus a wild-card slot [09:32]. The running tally on the right shows construction-point cost, weekly upkeep, and the input goods that will be added to your shipyard demand — watch this before committing, because new templates change what your shipyards consume [12:31]. Without the DLC you only get the base template per ship type.
5. **Each design lever has a combat job** — Armor reduces HP loss; Armament raises hull and crew attack (ship sinks at 0 HP, also retreats at low HP; depleting crew also wins the battle) [10:00]. Propulsion sets sea-node movement speed — a fleet moves at the speed of its slowest ship, so don't mix slow ships into fast fleets [10:31]. Supply Capacity is the orange bar consumed when away from home port; once empty, organisation drops and offence/defence fall [10:31]. Carrying/Marine Capacity sets how many battalions/marines per ship — at level 2 a frigate carries only 0.25 battalions (4 frigates per battalion), at level 3 it carries 0.5 [11:30].
6. **Retrofitting upgrades existing ships to a new template** — Open the ship list, edit, multi-select (or Select All), Change Template, pick the target, then Retrofit [14:30]. Affected fleets sail home (must be docked) and the queue subtracts the cost of work already done from the new template's cost, so small tweaks retrofit fast and full redesigns retrofit slow [15:30]. Fleets split automatically so other ships can continue current missions.
7. **Capital vs Cruiser roles in combat** — Capitals (e.g. Ship of the Line) hit hardest and tank with armour but have high Vulnerability, so enemies target them first; Cruisers have higher Screening, soaking attacks to keep capitals firing longer [21:01]. Cruisers also have lower Visibility, letting them slip through hostile sea nodes without triggering battle — making them the right escorts for trade and troop transport [21:30]. Capitals are bad at hitting torpedo boats, torpedo-boat cruisers, submarines, and destroyers, so a capital-only fleet is exposed to torpedo specialists [20:32].
8. **Construction Efficiency = free construction points** — A +25% efficiency modifier means every point spent on that ship counts as 1.25 toward its build cost [16:31]. Read Navy Model laws as efficiency dials: percentages stack additively, so a law granting -10% to all ships and +30% to supply ships nets +20% on supply and -10% on military [17:32].
9. **Navy Model law group** — Pick the law that matches your strategic plan [15:30]:
   - **Merchant Navy**: -10% all ships, +30% supply, +30% troop ships (so +20% net to supply/troop), -10% involvement generation. Use when you don't intend serious naval combat — focus is trade protection and troop transport.
   - **Jeune École**: +25% torpedo craft, +20% specific cruisers, -10% navy goods cost, +10% officer political strength. Use to swarm a larger enemy with cheap specialised hulls.
   - **Capital Fleet**: +25% capital ship efficiency, +20% prestige from navy, +20% officer political strength, +25% naval administration hiring speed. Use to build an intimidating big-gun navy.
   - **Diplomatic Fleet**: +25% to all cruisers, +20% involvement generation, +10% naval administration hiring speed. Use to project power into many strategic regions cheaply (also boosts regional trade advantage).
10. **Naval administrations employ the ships** — Building a hull does not man it; you must build naval administrations alongside [23:00]. Hiring speed matters in war because dead sailors must be replaced before a ship returns to combat. Capital Fleet and Diplomatic Fleet laws speed this up.

## Game numbers & rules of thumb
- Shipyard base PM produces 5 ship construction points per level [01:01].
- Supply-ship maintenance: 1 maintenance point per 133.33 supply ships [05:02].
- Military-ship maintenance: 1 maintenance point per 3,333.33 construction points of built military ships [05:33]; e.g. a 405-point Ship of the Line costs 0.12 maintenance each [06:01].
- Allocation slider moves in 25% steps; unused points spill to the other queue [02:30].
- A frigate at supply/carrying level 2 carries 0.25 battalions and 0.12 marines; at level 3, 0.5 battalions and 0.25 marines [11:30].
- A fleet moves at the speed of its slowest ship [10:31].
- Construction Efficiency adds to construction points multiplicatively: +X% efficiency = each invested point counts as 1+X/100 toward the build [16:31].
- Navy Model law modifiers stack additively with the global ship modifier; e.g. -10% all + 30% supply = +20% net to supply [17:32].
- Capitals have high Vulnerability (targeted first); Cruisers have high Screening and low Visibility [21:01].
- Navy demand at game start is heavy in wood, hardwood, and fabric — competes directly with Construction Sector demand [24:32].

## Common pitfalls
- Expanding the navy without expanding Shipyards — maintenance eventually eats your entire construction throughput and builds crawl [07:31].
- Letting Clipper prices collapse and not subsidising — the shipyard loses employment and ship construction points drop silently [01:30].
- Forgetting to build Naval Administrations alongside new hulls — the ships exist but aren't manned [23:00].
- Designing a new template without checking its input-goods tooltip — your shipyards' demand profile changes the moment you queue it [12:31].
- Mixing a slow ship into a fast fleet — the whole fleet drops to the slowest ship's speed [10:31].
- All-capital fleets versus torpedo specialists — capitals struggle to hit torpedo boats, submarines, and destroyers; bring cruiser screens [20:32].
- Letting fleets operate far from home with too few supply ships — supply bar empties, organisation falls, offence/defence collapse [10:31].

## Cheatsheet
1. Expand Shipyards in lockstep with the navy; check that maintenance is well under half your total construction points before queuing more hulls.
2. Set allocation toward whichever queue you actually need — overflow handles the other side automatically.
3. Pick the Navy Model law that matches your plan: Merchant Navy (trade), Jeune École (asymmetric small), Capital Fleet (big-gun), Diplomatic Fleet (presence + cruisers).
4. Open the Ship Designer, build templates per type, and check the input-goods tooltip before saving — that's your future Shipyard demand.
5. To upgrade a fleet: ship list → edit → Select All → Change Template → Retrofit; ships sail home, queue computes the delta.
6. Build Naval Administrations as you build hulls, especially during wartime so casualties refill.

## See also
- [Naval_warfare](https://vic3.paradoxwikis.com/Naval_warfare) — fleets, sea nodes, supply, screening, vulnerability
- [Laws](https://vic3.paradoxwikis.com/Laws) — Navy Model law group
- [Production_methods](https://vic3.paradoxwikis.com/Production_methods) — Shipyard PMs and ship construction point output
