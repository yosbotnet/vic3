---
source_transcript: ../../transcripts/tutorials/18-military-navy.md
source_video: https://www.youtube.com/watch?v=q7Xb2gC7ktE
generated_at: 2026-05-16
---

# Navy (2025)
**Source:** [Victoria 3 Military Tutorial Part Two - Navy in 2025](https://www.youtube.com/watch?v=q7Xb2gC7ktE) (26:41 runtime)

## Summary
The Navy's primary job in Victoria 3 is logistics: keeping your country and overseas armies supplied via Convoys, and disrupting the enemy's supply by Convoy Raiding. Navies are built as Flotillas in Naval Bases, supplied by Military Shipyards, and led by Admirals/Commodores with bigger command caps than Generals. Beyond combat, naval power projection is a major Prestige source, which lowers your interest rate.

## Core mechanics
1. **Flotilla** — The basic Naval unit (analogous to a battalion). Manpower is the most decisive number — two Navies of equal Flotilla count but unequal Manpower will be wildly mismatched. DECISION RULE: rebuild casualties before re-engaging; don't field "paper" Flotillas at low Manpower. `[02:00]` `[03:30]`
2. **Naval Commander ranks** — Commodore organizes 20 Flotillas at base; promote up to Grand Admiral for up to 100. Exceeding command cap drops Organization. DECISION RULE: size each Navy to the Commander's cap; promote before adding more Flotillas. `[02:00]` `[02:31]` `[04:31]`
3. **Ship type ratio** — Three types: Light Ships, Capital Ships, Support Vessels (Support unlocked with Submarines). Capital + Support combined cannot exceed Light Ships, or Organization drops. DECISION RULE: at base tech keep Light Ships >= Capital Ships (e.g. 10 Frigates + 10 Man-o-Wars per 20-Flotilla Navy), and bias toward more Light Ships if the Capital input good is scarce. `[05:00]` `[06:01]`
4. **Military Shipyard supplies the Navy** — One building type produces the goods for all ship Production Methods, but each Shipyard can only run ONE PM (e.g. Man-o-Wars OR Ironclads, not both). DECISION RULE: don't upgrade Capital Ships to Ironclads until you have Monitors tech, OR import the missing good, OR build a second Shipyard on a different PM. `[07:01]` `[08:31]` `[09:32]`
5. **Upgrades require HQ stationing** — Hitting upgrade does nothing if the Navy is in a Sea Node. DECISION RULE: pull Navies back to an HQ before upgrading. `[11:01]`
6. **Naval Base hiring uses primary culture** — Officers require very high cultural acceptance, so without Multiculturalism they must come from the primary culture. DECISION RULE: build Naval Bases in primary-culture states until Multiculturalism is passed. `[12:02]` `[12:32]`
7. **State traits for naval industry** — Coastal "dockland"-style state modifiers give +15% Military Shipyard throughput and +15 Flotilla cap. DECISION RULE: always concentrate Shipyards and Naval Bases in these states first. `[13:01]`
8. **Naval Orders** — Interception / Coordinated Interception start naval battles in a Sea Node; Escort Convoys / Organize Merchant Convoys protect your trade; Convoy Raiding disrupts enemy routes. DECISION RULE: pick the order to match the Sea Node's role in the war (your supply route -> Escort; enemy supply -> Raid; enemy fleet present -> Interception). `[14:01]` `[14:30]`
9. **Convoy Raiding wins wars** — Cutting an enemy supply route slashes their armies' morale recovery, so they retreat from battles faster. DECISION RULE: prioritize raiding key import nodes (Small Arms, Artillery, etc.) over fleet-to-fleet battles when possible. `[16:31]` `[17:33]`
10. **Overseas supply needs Convoys** — Armies in an HQ or on a contiguous land front don't consume Convoys; armies sent overseas do, scaled by battalion count and number of Sea Nodes traversed. DECISION RULE: route armies via allied territory to minimize Sea Nodes used, and check Convoy availability before committing a large army overseas. `[18:01]` `[19:32]` `[20:01]`
11. **Convoy cost formula** — Base = battalions x 10. Multiplier = 1 + 0.1 per Sea Node beyond the first. Commander supply-efficiency traits multiply the total down (displayed value is truncated). DECISION RULE: a 90-battalion army across 8 Sea Nodes is ~1,500 raw Convoys — only commit if your Convoy pool can cover it plus existing trade. `[21:31]` `[22:04]` `[23:31]`
12. **Navy Power Projection -> Prestige -> cheaper debt** — Navy contributes more Prestige per Flotilla than Army per battalion in general. Higher Prestige -> higher Rank -> lower interest rate. DECISION RULE: treat Navy spending partly as a debt-cost reduction, not pure military spend. `[25:02]` `[25:33]`

## Game numbers & rules of thumb
- Commodore (lowest Naval rank) organizes 20 Flotillas; Grand Admiral (highest) organizes 100. `[02:00]` `[02:31]`
- No naval conscripts — Navy Manpower comes only from Naval Base employment. `[05:00]`
- A Frigate consumes 1 Man-o-War good; a Man-o-War ship consumes 3 Man-o-Wars goods (good name = next-tier ship name). `[07:01]`
- Ironclad Capital Ships need 3 Ironclads goods; Monitor Light Ships need 1 Ironclads good. `[07:32]` `[08:00]`
- One Military Shipyard runs one Production Method at a time — Man-o-Wars OR Ironclads, never both. `[08:31]`
- Man-o-Wars goods are generally more available on the world Market than Ironclads. `[10:02]`
- Dockland-style state modifiers: +15% Military Shipyard throughput, +15 max Flotillas in that state. `[13:01]`
- Convoy supply cost: battalions x 10 x (1 + 0.1 x (sea_nodes - 1)), then x commander efficiency multiplier. `[21:31]` `[22:04]`
- Pathing picks the route with the fewest Sea Nodes — allied territory can dramatically shorten supply lines. `[20:31]`

## Common pitfalls
- Upgrading Capital Ships to Ironclads before researching Monitors — your single Shipyard PM can't supply both goods at once, and your fleet starves of inputs.
- Hitting "Upgrade" while the Navy is parked in a Sea Node — nothing happens until you move it to an HQ.
- Building Naval Bases in low-acceptance states pre-Multiculturalism — Officer slots stay empty due to "qualifications" issues.
- Letting Capital + Support exceed Light Ship count — silent Organization penalty.
- Trying to garrison every Sea Node on a long trade route (e.g. opium to East Asia) — impossible; instead keep a mobile Navy and react to enemy Raids.
- Sending a big army overseas without checking Convoy headroom — they'll arrive but never recover morale and rout on first contact.
- Ignoring the truncated display on commander Supply efficiency (shown 0.6, actually ~0.67) when doing manual Convoy math.

## Cheatsheet
1. Build Military Shipyards and Naval Bases first in primary-culture coastal states with dockland-style modifiers.
2. Keep each Navy at its Commander's cap (20 at Commodore, up to 100 at Grand Admiral) with Light Ships >= Capital Ships.
3. Don't upgrade Capital Ships to Ironclads until Monitors is researched, OR import the missing good, OR run a second Shipyard on the other PM. Pull fleets to HQ to apply upgrades.
4. In war: assign Escort Convoys on your critical import Sea Nodes, Convoy Raiding on the enemy's, Interception only where you can win the fleet battle.
5. Before sending an army overseas, check the Sea Node breakdown: battalions x 10 x (1 + 0.1 x extra nodes) ~= raw Convoys needed; route through allies to cut nodes.
6. Maintain a sizeable Navy for Power Projection Prestige — it pays for itself through lower interest on Treasury debt.

## See also
- [Naval_warfare](https://vic3.paradoxwikis.com/Naval_warfare)
- [Warfare](https://vic3.paradoxwikis.com/Warfare)
- [Commanders](https://vic3.paradoxwikis.com/Commanders)
