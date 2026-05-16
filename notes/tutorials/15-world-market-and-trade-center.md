---
source_transcript: ../../transcripts/tutorials/15-world-market-and-trade-center.md
source_video: https://www.youtube.com/watch?v=E6fTjF9wb_I
generated_at: 2026-05-16
---

# World Market & Trade Centers (1.9)

**Source:** [World Market and Trade Center Tutorial in Victoria 3](https://www.youtube.com/watch?v=E6fTjF9wb_I) (21:53 runtime)

## Summary
The 1.9 / Charters of Commerce update replaces manual trade routes with a World Market where imports/exports flow through Trade Centers. A state needs a coast, a Port, and a Trade Center to access the World Market (landlocked nations need transit rights). Price you actually pay/earn depends on your Relative Advantage versus other traders, and you steer the auto-trading private sector with Tariffs, Subventions, Trade Privileges, and the Trade Policy law.

## Core mechanics
1. **World Market access** — Conceptual global pool of imports/exports with an Inherent Demand per good. To trade you need a coastal state, a Port, and a Trade Center; landlocked countries need a Transit Rights agreement. DECISION RULE: if a state is coastal and lacks one, build Port + Trade Center before anything else when local goods are missing. `[01:02]` `[01:30]`
2. **Trade Center building** — The sole building that interacts with the World Market. Has levels, can be subsidised/privatised/nationalised, and switches Production Methods. DECISION RULE: in 1.9 prioritise building a Trade Center even before your first Construction Sector when starting goods (e.g. wood) are missing locally. `[03:33]` `[19:03]`
3. **Trade Capacity** — Works like Infrastructure: each level of Trade Center provides capacity (base 50/level), and each good consumes capacity per unit traded. DECISION RULE: when capacity is maxed and you still need more of a good, expand the Trade Center another level. `[04:31]` `[05:00]`
4. **Merchant Marines input** — Trade Centers consume Merchant Marines, produced by Ports from Clippers. DECISION RULE: if you have no Clippers, either switch the Trade Center PM to import Merchant Marines, or have it import Clippers so the Port can make them locally. `[06:02]` `[06:30]`
5. **Trade Advantage (per good, per direction)** — Base 100, modified by Trade Privileges with exporters/importers, having an Interest in their region, your Trade Policy law, and your spare Trade Capacity (up to +20%). DECISION RULE: to cheapen a critical import, sign Trade Privileges and declare an Interest in regions of the top exporters. `[08:01]` `[08:30]` `[09:32]`
6. **Relative Advantage drives price** — Your share of global Trade Advantage for a good minus your share of global trade volume. Positive => discount on imports / premium on exports; negative => penalty. DECISION RULE: raise advantage AND/OR cut volume to swing relative advantage positive. `[10:30]` `[12:01]`
7. **Tariffs & Subventions** — Tariffs charge the Trade Center per unit (discouraging that trade); Subventions pay it per unit (encouraging it, even on unprofitable routes). DECISION RULE: use Subventions to force imports you strategically need (e.g. Artillery when you have no foundries); use Tariffs to throttle leaks of strategic exports or unwanted imports. `[13:30]` `[20:32]`
8. **Trade Center revenue formula** — Per trade capacity used on a good: (local price − import price + subvention − tariff) × traded quantity per capacity, then × capacities used. DECISION RULE: a route stays auto-profitable while local minus world price exceeds tariff; if it stops, only Subventions will keep it running. `[13:00]` `[14:00]`
9. **Production Method scaling** — Higher PMs add only 1 Merchant Marine per level but massively raise traded quantity per capacity; Smallscale Trading halves traded quantity (and revenue). DECISION RULE: upgrade PMs as soon as you can pay the Merchant Marines — the throughput gain dominates the input cost. `[15:30]` `[16:02]`
10. **Trade Policy laws** — Mercantilism: +25% export advantage, −25% import advantage, stronger tariffs/subventions (export-focused nations). Protectionism: neutral advantage, normal tariffs, +25% leverage resistance (best general-purpose). Free Trade: +25% advantage but cannot tariff, only subventise; −25% leverage resistance. Isolationism: cannot build Trade Centers at all, only diplomatic goods exchange; heavy authority/leverage but trade-crippling. DECISION RULE: default Protectionism unless you are a dedicated exporter (Mercantilism) or a strong economy that needs no protection (Free Trade). `[16:32]` `[17:30]` `[18:01]`

## Game numbers & rules of thumb
- Trade Center base capacity: 50 per level. `[04:31]`
- Capacity used per good = traded units / traded-quantity-per-capacity (varies per good; see wiki Goods table). `[05:00]` `[14:32]`
- Spare Trade Capacity gives up to +20% Trade Advantage. `[10:01]`
- Natural Harbors state trait: +15% Trade Capacity. `[05:32]`
- Smallscale Trading PM: −1 Merchant Marine input, −50% traded quantity per capacity. `[15:30]`
- Mercantilism: +25% export / −25% import Trade Advantage; stronger tariff & subvention rates. `[16:32]`
- Protectionism: 0% advantage shift, +25% leverage resistance. `[17:30]`
- Free Trade: +25% Trade Advantage on everything; tariffs disabled; −25% leverage resistance. `[17:30]`
- Isolationism: no Trade Centers; +50% authority, large leverage resistance, reduced tech spread/interests. `[18:31]`
- Inherent Demand exists on every good so world prices never collapse to zero. `[02:01]`

## Common pitfalls
- Building a Trade Center in a landlocked state with no transit rights — it cannot access the World Market. `[01:30]`
- Forgetting the Port: without one (and Merchant Marines flowing), the Trade Center produces nothing. `[06:30]`
- Picking Free Trade then wondering why a runaway import keeps draining you — you cannot tariff under Free Trade, only subventise. `[18:01]`
- Assuming Mercantilism is "best for trade" — its −25% import advantage hurts any nation that depends on imports. `[16:32]`
- Reading Trade Advantage as the price modifier — only Relative Advantage moves price; raw advantage only matters via your share of the global pool. `[08:01]` `[10:30]`
- Letting Subventions stay on a route after you no longer need that good — the Trade Center will keep importing at a loss on your dime. `[20:32]`

## Cheatsheet
1. In any state missing key local goods, build Port -> Trade Center before Construction Sectors.
2. Set Trade Policy to Protectionism by default; Mercantilism only if you are export-driven.
3. For critical imports, sign Trade Privileges and declare an Interest in the top exporters' region to boost Trade Advantage.
4. Upgrade Trade Center PM past Regular Trading as soon as Merchant Marines are affordable — throughput scales hard.
5. Use Subventions to force-import strategic goods you cannot produce (artillery, wood, etc.); use Tariffs to choke unwanted flows.
6. Expand Trade Center levels when capacity is full OR to push spare capacity toward the +20% Trade Advantage cap.

## See also
- [Markets](https://vic3.paradoxwikis.com/Markets)
- [Goods](https://vic3.paradoxwikis.com/Goods)
- [Laws](https://vic3.paradoxwikis.com/Laws)
