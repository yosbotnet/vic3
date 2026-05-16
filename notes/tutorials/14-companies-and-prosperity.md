---
source_transcript: ../../transcripts/tutorials/14-companies-and-prosperity.md
source_video: https://www.youtube.com/watch?v=tguDlYhyIqU
generated_at: 2026-05-16
---

# Companies and Prosperity (1.9+)
**Source:** [Companies and Prosperity Tutorial in Victoria 3 Post 1.9 Update](https://www.youtube.com/watch?v=tguDlYhyIqU) (26:40 runtime)

## Summary
The 1.9 update plus the Charters of Commerce DLC overhauled Companies into a central pillar of every run. Companies now have Executives (a new character type), can spawn Regional Headquarters in foreign states, and unlock Prestige Goods once Prosperous. Prosperity is no longer a simple bar but a target-and-rate system driven by building productivity vs. global average and the share of fully-staffed building levels. Charters (trade, investment, colonization, industry, monopoly) let you steer where and how a Company expands.

## Core mechanics
1. **Executive character** — Every Company has an Executive who belongs to an Interest Group (adding political power to it, like a general) and carries traits granting bonuses to all Company buildings (e.g., Basic Entrepreneur = +5% Throughput). You cannot interact with them directly; they appear in random yearly character events. DECISION RULE: when picking between otherwise-equal Company candidates, prefer the one whose Executive trait fits your strategy (Throughput, construction, popularity). `[02:01]`
2. **Prosperity target vs. current** — Current Prosperity climbs (or falls) each week toward a Target value that is recalculated continuously. You become Prosperous at 100 and stop being Prosperous if you drop below 75. DECISION RULE: do not expect Prosperity quickly — push the *target* up first (productivity, staffed levels) and current will follow. `[07:31]`
3. **Productivity component (capped ±50)** — Base 50, modified by the percentage your Company's weighted-average building productivity is above/below the global average for that building type. DECISION RULE: keep your Company's buildings on high-output Production Methods and avoid letting input shortages drag productivity below the world average. `[09:31]`
4. **Staffed building levels component (capped +50)** — You get +1 to target per fully-staffed building level, scaled by employment ratio (e.g., 97.14% employed on 17 levels = +16.54). Built but unstaffed levels give nothing. DECISION RULE: only build Company buildings when there is real demand to fill the jobs; an empty level hurts more than it helps. `[11:30]`
5. **Executive popularity modifier** — Every 5 points of Executive popularity = ±1 to the Prosperity target. DECISION RULE: a wildly unpopular Executive is a real drag — factor this in when an event offers a swap. `[14:02]`
6. **Rate of change** — If productivity > global average, base rate is +0.2/week plus 4% of fully-staffed levels; if below, base flips to −1/week plus only 2% of fully-staffed levels. DECISION RULE: small Companies with sub-average productivity bleed Prosperity fast — fix productivity before adding levels. `[14:32]`
7. **Charters (DLC) — free slots vs. authority** — Each country has a number of free active charters (from tech/laws); beyond that, each charter costs 100 Authority. Without the DLC only Trade Rights is available. DECISION RULE: spend free charter slots first on the highest-leverage charter type for that Company; only pay 100 Authority when the bonus is clearly worth it. `[18:31]`
8. **Investment Rights charter** — Lets a Company build a Regional HQ in a foreign state (after it owns 5 building levels there) and build using *that country's* Investment Pool, but reinvestment flows back to your home Investment Pool. DECISION RULE: use on rich foreign markets to siphon their capital into your own Investment Pool. `[19:32]`
9. **Trade Rights charter (free, no DLC)** — Lets a Company build Trade Centers; those Trade Centers receive the Company Throughput bonus and get trade advantage on Company goods. DECISION RULE: hand this to Companies whose goods you want to dominate on the world market. `[21:00]`
10. **Colonization Rights charter** — Company colonizes a chosen state; once fully colonized it becomes a chartered Company Subject under you, inheriting the Company's construction-efficiency bonus. DECISION RULE: for resource-extraction colonies, pair the target state with a Company that specializes in the local resource. `[21:32]`
11. **Industry Rights charter** — Adds one additional building type the Company can construct, drawn from related industries (e.g., Fish input → Food Industries). A Company can have only one Industry Rights charter at a time. DECISION RULE: pick the downstream building that consumes your Company's output, to lock in vertical integration. `[22:32]`
12. **Monopoly Rights charter** — Only that Company (and the government) can build the named building type; private builders cannot. DECISION RULE: monopolize building types you want built fast and with the Company's Throughput/construction bonuses — but only if government + Company can keep up with demand. `[23:01]`
13. **Prestige Goods unlock** — Becoming Prosperous opens a Journal Entry to produce the Company's Prestige Good; completion typically requires staying Prosperous and in the top-3 global producers of the relevant good for 36 (non-consecutive) months. DECISION RULE: once Prosperous, protect your top-3 ranking on that good — expand production or sabotage rivals' output as needed. `[06:32]`
14. **Foreign buildings — no PM control** — When a Company owns a building in another country, you cannot set its Production Methods, which can tank productivity and Prosperity. DECISION RULE: be cautious giving Investment Rights into volatile markets, especially for goods with spiky input prices. `[24:01]`

## Game numbers & rules of thumb
- Prosperity becomes active at 100; falls off below 75. `[07:31]`
- Productivity component to target: base 50, ±(% deviation from global avg) of that 50; hard cap ±50. `[09:31]`
- Staffed-levels component: +1 per fully-staffed level, scaled by employment ratio; hard cap +50. `[11:30]`
- Executive popularity: ±1 to target per 5 points of popularity. `[14:02]`
- Rate base = +0.2/week if productivity ≥ global avg, else −1/week. `[14:32]`
- Rate bonus per fully-staffed level: 4% if above global avg, 2% if below. `[15:01]`
- Productivity is a weighted average across all Company buildings, weighted by building levels. `[08:30]`
- Foreign Regional HQ becomes possible after the Company owns 5 building levels in that country. `[19:32]`
- Each charter beyond free slots costs 100 Authority. `[18:31]`
- Investment Pool reinvestment from a foreign Regional HQ flows back to the *owner's* Investment Pool, not the host's. `[20:30]`
- Up to 9 Companies total currently possible: 5 from the Society tech line (Corporate Charters → Joint-Stock Companies → Investment Banks → Corporate Governance → Macroeconomics), +1 from Corporate State + Companies principle (tier 3) in a Power Bloc, +2 free slots from the two canal Companies. `[25:32]`

## Common pitfalls
- Spamming Company buildings to "boost" Prosperity — empty levels add nothing to the staffed-levels component and can drag the average productivity down. `[11:30]`
- Forgetting the productivity cap is ±50: more above-average productivity past a point gives no extra Prosperity. `[13:32]`
- Adding a Production Method that needs more workers right before checking Prosperity — employment ratio drops instantly and your target/rate both fall. `[12:30]`
- Giving Investment Rights into a country with bad input prices: the foreign building runs an inefficient PM you cannot change, dragging the whole Company's productivity. `[24:01]`
- Burning Authority on a charter when you still have free slots elsewhere — hover the charter to see your free-charter count first. `[19:00]`
- Confusing "Company-owned subject" with "Company-owned by Great Britain" — chartered Company subjects are still your subject, so you can impose law changes on them. `[05:00]`
- Assuming small/tall Companies can reach Prosperity — the staffed-levels component effectively requires scale. `[17:30]`

## Cheatsheet
1. Rush the Society tech line (Corporate Charters first) to unlock Company slots early, and pick Companies whose buildings you already plan to spam.
2. For each Company: keep its buildings on the best PM available and ensure full employment before adding more levels — productivity and staffed levels are the two big Prosperity inputs.
3. Spend free charter slots first: Trade Rights on export-oriented Companies, Monopoly Rights on buildings you want privately built, Industry Rights to vertically integrate.
4. Use Investment Rights on wealthy neighbors to bleed their Investment Pool into yours; use Colonization Rights with a resource-matched Company for extraction colonies.
5. Once Prosperous, defend the top-3 production ranking on the Company's Prestige Good for 36 cumulative months to lock in the prestige good.
6. Watch Executive popularity and traits — swap or accept events that improve them when offered.

## See also
- [Companies](https://vic3.paradoxwikis.com/Companies)
- [Buildings](https://vic3.paradoxwikis.com/Buildings)
- [Production_methods](https://vic3.paradoxwikis.com/Production_methods)
