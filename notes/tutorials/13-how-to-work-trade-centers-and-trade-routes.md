---
source_transcript: ../../transcripts/tutorials/13-how-to-work-trade-centers-and-trade-routes.md
source_video: https://www.youtube.com/watch?v=FAghv7otHAE
generated_at: 2026-05-16
---

# Trade Centers and Trade Routes

**Source:** [How to Work Trade Centers and Trade Routes in Victoria 3](https://www.youtube.com/watch?v=FAghv7otHAE) (31:43 runtime)

## Summary
Trade Centers are state-level buildings that handle imports and exports, with their throughput governed by Trade Capacity and their profitability by Relative Trade Advantage. To dominate an export, concentrate Trade Center levels in a strong state (ideally one with Natural Harbors), declare Interests in the main importing markets, sign Trade Privileges agreements, and assign a Company with a Trade Rights charter so its Trade Centers gain extra advantage on the goods it produces.

## Core mechanics

1. **Trade Center placement (concentrate vs. spread)** — Trade Centers can both import (selling at local price in their state) and export. Throughput bonuses (e.g., from state traits) only stack within one state. DECISION RULE: put most of your levels in your single best Trade Center state (high trade capacity + good state traits), and keep 1–2 levels in other states only when you need them as local sources of specific imported goods. `[02:00]`
2. **Trade Capacity gates trade volume** — Every Trade Center has a Trade Capacity that caps how many units it can trade per week. If you are at cap, new export/import directions will not start. DECISION RULE: when an enabled route is not flowing, check Trade Capacity first; build another level (or boost throughput) before doing anything else. `[02:31]` `[11:00]`
3. **Natural Harbors state trait** — Gives +15% Trade Capacity per level, +5% Market Access Price Impact, plus port/shipyard throughput and extra Naval Base levels. DECISION RULE: prefer a Natural Harbors state as your main Trade Center hub. `[03:30]`
4. **Subventions to start an export, tariffs to block an import** — Trade Centers will not export a good unless it is profitable enough. DECISION RULE: on a good you have a surplus of, set a low export Subvention to kickstart exports and a max import Tariff so you never accidentally import it; remove the Subvention once Relative Trade Advantage is high enough to be profitable on its own. `[05:01]` `[16:00]`
5. **Declared Interests in importing markets** — You lose Trade Advantage points for every relevant market (largest importers/exporters of the good) where you have no Interest. DECISION RULE: spend your Interest slots on the regions of the biggest importers of the good you want to dominate; if a region has no Goods Potential for that good, those small countries will always import, making the Interest doubly valuable. `[05:32]` `[06:32]`
6. **Relative Trade Advantage formula** — Relative Trade Advantage = (your % of global advantage / % of global trade volume) − 100%. Positive means you out-compete the volume share, negative means you under-compete. DECISION RULE: only push exports where your % of global advantage exceeds your % of global trade volume; otherwise raise advantage (Interests, Privileges, Mercantilism, Company) before scaling. `[09:31]` `[10:30]`
7. **Trade Privileges treaties** — Trade Privileges with another country grant a large Trade Advantage bonus for trade in both directions for the agreement's duration (default 25 years). DECISION RULE: sign Trade Privileges with the biggest importers of your target export; be willing to trade smaller concessions (no tariff on a specific good, defensive pact, an obligation) to land it. `[14:01]` `[14:31]`
8. **Companies and the Trade Rights charter** — A Company with the Trade Rights charter can build its own Trade Centers, and any Trade Center it owns gets extra Trade Advantage on the goods the Company produces. DECISION RULE: hold off on expanding Trade Centers right before founding a relevant Company so it builds them itself; always give an export-focused Company Trade Rights plus monopoly rights on its core building. `[13:31]` `[20:01]` `[20:31]`
9. **Company Prosperity** — Prosperity rises toward a Prosperity Target derived from staffed building levels and how each owned building's productivity compares to global productivity for that building type. Once Prosperity hits 100, the Company can drop to 75 and stay Prosperous. DECISION RULE: fix the lowest-productivity buildings the Company owns (cheaper inputs, better Production Methods, more Infrastructure) until you hit 100 once, then defend the floor. `[22:02]` `[22:30]` `[30:01]`
10. **Charters cost authority and shape strategy** — Free charter slots are limited; extra ones cost Authority (e.g., 100 for Colonization Rights). You must already have a Declared Interest in a colonizable region to grant Colonization Rights. DECISION RULE: plan your Interest map before you found the Company so the charters you want (Trade Rights, monopoly, Colonization Rights for a future resource like rubber) are all legal at founding time. `[20:31]` `[21:30]`
11. **Trade Advantage stacks** — Sources include Trade Privileges treaties, Mercantilism (+25%), Trade Capacity (small per-level bonus), Company-owned Trade Centers, and Interest coverage. DECISION RULE: when chasing dominance in one good, layer all of these simultaneously rather than relying on any single source. `[11:30]` `[12:30]` `[27:33]`
12. **Use imports sparingly — they cost capacity** — Trade Center capacity used to import a missing good is capacity not earning export revenue. DECISION RULE: domesticate inputs (e.g., research Intensive Agriculture, set domestic Production Methods) so Trade Capacity stays free for high-margin exports. `[18:02]`

## Game numbers & rules of thumb

- Natural Harbors state trait: +15% Trade Capacity, +5% Market Access Price Impact per level. `[03:30]`
- 100% Market Access Price Impact means a good sells at the originating state's local price everywhere — closer to 100% = cheaper imported goods. `[04:00]`
- Mercantilism economic law gives +25% Trade Advantage. `[12:30]`
- Trade Capacity itself adds a small Trade Advantage bonus (~+2% at 46 capacity in the example), so bigger Trade Centers compound their own advantage. `[12:30]`
- Trade Privileges treaties run 25 years by default and provide tens of points of Trade Advantage per partner. `[14:31]` `[15:31]`
- An ambitious executive can add ~+5% throughput to every building the Company owns; combined with state traits and Company bonuses this can push throughput well above +50%. `[19:31]`
- Company Prosperity floor is 75 once you have ever hit 100 — drop below 75 and you lose Prosperous status. `[30:31]`
- Colonization Rights charter costs 100 Authority and needs a Declared Interest in a colonizable region. `[21:30]`
- Relative Trade Advantage directly modifies export price (example: +49% advantage → +12% export price). `[15:31]`

## Common pitfalls

- Building one Trade Center level in every state — you lose the throughput stacking and end up with low capacity everywhere. `[02:00]`
- Adding new export directions while already at Trade Capacity — nothing happens; the new route will not start until capacity is freed. `[11:00]`
- Forgetting to set a max import Tariff on a good you want to export — your own Trade Centers can start importing it and tank your surplus. `[05:32]`
- Leaving export Subventions on a good that is now highly profitable on its own — you keep paying for incentives you no longer need. `[16:00]`
- Spending Interests randomly instead of on the biggest importers/exporters of your target good — you eat permanent Trade Advantage penalties from "lacking interests in relevant markets". `[12:30]`
- Expanding the Trade Center yourself right before founding the Company — those levels won't be Company-owned and miss the Company's Trade Advantage bonus. `[13:31]`
- Building the Company's monopoly good (e.g., Logging Camps) in other states yourself — you want the Company to build them to get the bonuses; build the *input* goods (Iron, Tooling inputs) instead. `[28:30]`
- Ignoring underperforming buildings in distant states the Company owns (e.g., a Trade Center bleeding from expensive Merchant Marines or poor Infrastructure) — they drag the Company's Prosperity below target. `[29:32]`
- Accepting "free goods" diplomatic offers that lock you into non-colonization or investment rights you don't want. `[17:30]`

## Cheatsheet

1. Pick a hub state with Natural Harbors (or best Trade Capacity trait) and pin all your Trade Centers to the outliner.
2. For your target export: set max Tariff on imports + small Subvention on exports; for needed imports: Subvention on import + max Tariff on export.
3. Declare Interests in the regions of the largest importers of that good (and any small-country region with no domestic Goods Potential for it).
4. Research Corporate Charters, found the matching Company, and give it Trade Rights + monopoly on its core building + (later) Colonization Rights for any resource expansions.
5. Negotiate Trade Privileges (25-year) with the top importing markets; trade defensive pacts, obligations, or single-good no-tariff clauses to get acceptance.
6. Watch Relative Trade Advantage and Company Prosperity — fix low-productivity Company buildings with cheaper inputs and more Infrastructure until Prosperity hits 100, then defend the 75 floor.

## See also

- [Markets](https://vic3.paradoxwikis.com/Markets)
- [Companies](https://vic3.paradoxwikis.com/Companies)
- [Diplomacy](https://vic3.paradoxwikis.com/Diplomacy)
