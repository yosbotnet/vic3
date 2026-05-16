---
source_transcript: ../../transcripts/tutorials/01-shipbuilding.md
source_video: https://www.youtube.com/watch?v=ct-PUjt6M8c
generated_at: 2026-05-16
---

# Shipbuilding in Victoria 3 (1.13 Great Wave)

**Source:** [Shipbuilding Tutorial in Victoria 3](https://www.youtube.com/watch?v=ct-PUjt6M8c) (25:54 runtime)

## Summary
Covers the 1.13 Great Wave shipbuilding overhaul: the unified Shipyards building, the ship construction point economy, allocation between supply and military queues, the Ship Designer (Great Wave DLC), retrofitting existing fleets, and the new Navy Model law category. Useful from game start onward — especially when laying out an initial construction queue, expanding a navy, picking a navy model law, or planning fleet upgrades mid-campaign.

## Core mechanics
1. **Unified Shipyards** — Military shipyards are gone; all ships are built from regular Shipyards, which now output Ship Construction Points alongside Clippers. Keeping Clippers profitable lets the building stay employed without subsidies; if it loses employment it produces fewer construction points.
2. **Ship construction points & maintenance** — Each existing ship draws a small ongoing maintenance cost from your total construction points before any new building happens. As your navy grows, maintenance eats more of your shipyard output, so you must expand Shipyards in step with the fleet.
3. **Construction allocation slider** — A slider in the ship construction panel splits available points between the supply ship queue and the military queue in 25% steps. Even when set fully to military, any unused military-side points spill over to supply ship construction.
4. **Ship Designer (Great Wave DLC)** — Lets you make templates per ship type by tuning Armor, Armament, Propulsion, Supply Capacity, Carrying Capacity / Marine Capacity, plus wildcard mods. Each upgrade raises construction cost and changes input goods consumed by Shipyards.
5. **Supply ships & organization** — Fleets away from home port deplete their orange supply bar; supply ships out in the world refill it. When the bar empties, the fleet loses organization and therefore offense/defense.
6. **Retrofitting** — You can change the template of existing ships via Edit → Select All → Change Template → Retrofit. Affected fleets return to port, then the queue adds "retrofit" entries that cost only the difference between old and new template construction costs.
7. **Capital vs Cruiser roles** — Capital ships have heavy armor and damage but high vulnerability and poor targeting vs torpedo boats, torpedo boat cruisers, submarines, and destroyers. Cruisers have higher screening (soaking attacks for capitals) and lower visibility (better for escorting trade and battalions through hostile sea nodes).
8. **Navy Model law group** — A new law category (Merchant Navy, Jeune École, Capital Fleet, Diplomatic Fleet) that grants construction efficiency bonuses to specific ship classes and shapes the navy's strategic role.
9. **Ship construction efficiency** — A percentage modifier from laws (and other sources) that effectively gives free construction points: the displayed per-week points get multiplied up before being applied to a ship's total cost.
10. **Naval administrations** — Ships are not crewed by being built; you must also build Naval Administrations to hire sailors. Capital Fleet speeds this up by 25%, Diplomatic Fleet by 10%, which matters both at peace and for replacing combat losses.

## Numbers & formulas
- Base Shipyards (first PM) produce 5 ship construction points per level [01:01].
- Example: 2 levels with +12% throughput → 11 points [01:30].
- Allocation slider moves in 25% increments [03:00].
- Example: 11 points total, 3 used for navy maintenance, leaves 8 for new construction [03:00].
- Example late game: 40 points generated, 7 to maintenance, 50/50 split of the remaining 33 → 16.35 to each side (actual maintenance ≈ 7.3) [04:00] [04:32] [05:02].
- Supply ship maintenance: 1.1 maintenance points per 133.4 supply ships (e.g., 414 ships → ~3.1) [05:02].
- Military ship maintenance: 1 point per 3,333.3 construction points worth of ships [05:33] [06:01].
- Ship of the line cost: 405 construction points → 0.12 maintenance each (405 / 3,333.3) [06:01] [06:30].
- Mod 1837 ship cost: 773 construction points [07:01].
- "Transport ship" cost: 574 construction points [07:01].
- Base cruiser template cost: 162 construction points [07:31].
- Example fleet totals: 10 ship of the line + 1 mod 1837 + 16 transport ships = 9,184; +10 base cruisers = 15,627 → 15,627 / 3,333.3 = 4.69 military maintenance [07:01] [07:31].
- Designer example: frigate fully upgraded with wildcard ≈ 403 construction points → 0.12 maintenance each [12:01].
- Capital Fleet bonus: +25% capital ship construction efficiency [16:00].
- Example: 8.18 generated × 1.25 = 10.225 (UI shows 10.22) applied toward the 405-point ship of the line [16:31] [17:02].
- Merchant Navy: −10% all ship construction efficiency, +30% supply ships → net +20% on supply ships [17:32] [18:01].
- Merchant Navy: +30% troop ship construction efficiency → net +20% after the −10% [18:01] [18:30].
- Merchant Navy: −10% ship involvement generation [18:30].
- Example involvement pool: Armada Nationale 310 involvement points [19:00].
- Jeune École: +25% torpedo craft, +20% cruiser construction efficiency, −10% navy goods cost, +10% officer political strength [20:01] [22:00].
- Capital Fleet: +25% capital ship construction efficiency, +20% navy prestige, +20% officer political strength, +25% naval administration hiring speed [22:31] [23:00].
- Diplomatic Fleet: +25% cruiser construction efficiency (all cruisers), +20% ship involvement generation, +10% naval administration hiring speed [23:31] [24:01].

## Common pitfalls
- Letting shipyards lose employment (unprofitable Clippers) silently reduces your construction points — subsidize if needed.
- Forgetting that navy maintenance is paid out of your construction points before anything new is built; an oversized navy with too few shipyards grinds new builds to a halt [08:01].
- Building ships without building Naval Administrations — the hulls exist but are not crewed [23:00].
- Assuming the slider being "all military" sends 100% to military: it only redirects unused supply allocation; military queue still draws spillover [02:30].
- Designing maxed-out templates without watching the input-goods breakdown — those goods become new Shipyard inputs and can spike prices [12:31].
- 1.13 dramatically increases early demand for wood, hardwood, and fabric; ignoring this when also needing artillery (e.g., starting as Sweden with no foundry) makes the opening construction queue painful [24:32] [25:01].

## Cheatsheet
1. At game start, build/expand Shipyards before expanding the navy and check Clipper price so Shipyards stay employed.
2. Set the allocation slider based on need: full-left if you mainly want supply spillover from the military queue, step right toward supply when fleets are losing org abroad.
3. Pick a Navy Model law to match your plan — Merchant Navy for trade/transport, Jeune École for cheap cruisers/torpedo craft, Capital Fleet for big battle fleets, Diplomatic Fleet for cruiser spam + strategic interests.
4. With Great Wave, open the Ship Designer, create templates per type, and watch the construction-point total (it drives maintenance at 1 per 3,333.3 points).
5. To upgrade a fleet: capital ship list → Edit → Select All → Change Template → pick new template → Retrofit; fleets auto-return to port and only the cost difference is built.
6. As the navy grows, queue more Shipyards and Naval Administrations together so points and crews scale with hulls.
