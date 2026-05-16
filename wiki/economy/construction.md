---
sources:
  - ../../notes/tutorials/11-construction.md
wiki:
  - https://vic3.paradoxwikis.com/Construction
generated_at: 2026-05-16
---

# Construction

## What it is
Construction is the only way buildings get built in Victoria 3, and the rate at which you build is the rate at which your country grows. Construction Sectors burn Goods and wages each week to produce Construction points, which are then spent on every other building — including more Construction Sectors. Run correctly, this becomes a compounding loop where each new Sector funds the next. Run wrong — wrong order, wrong state, wrong Production Method — and a small nation drowns in interest on debt before the loop ever spins up.

The strategic question is never "should I build more Sectors?" (the answer is yes) but "in what order do I build the Sector + its inputs + its Trade Center so I don't bankrupt myself before the goods arrive?"

## Mechanics

1. **The Construction Loop** — Sectors cost Goods + wages but produce Buildings that grow GDP, which raises Minting, which funds more Sectors. DECISION RULE: whenever your weekly surplus exceeds ~1k, queue another Sector plus one level of each of its input goods; never let the loop stall.
2. **Minting from GDP** — Treasury income is a flat base plus 1 pound per 1,000 pounds of GDP (with law/tech multipliers), and Gold Fields / Gold Mines add to it directly. DECISION RULE: when gold is discovered, fully employ the Gold Field — subsidize it if you have to — and prioritize building the Gold Mine. It is straight cash injected into Minting.
3. **Rank gates interest rates** — Loan interest scales inversely with rank/prestige; unrecognized minors pay ~30%+ and cannot service debt, great powers pay single digits and can. DECISION RULE: as a small nation never let reserves hit zero; as a great power, debt is an acceptable accelerant for the loop.
4. **Trade Centers unlock cheap inputs** — A Trade Center in your capital state lets Sectors buy imported Goods at local prices instead of waiting for domestic supply. DECISION RULE: as a non-Isolationist small nation, build 1 Trade Center BEFORE your first Sectors. Isolationism blocks Trade Centers — under that law, build all input goods domestically first.
5. **Private Construction Queue split** — Under Traditionalism the Private sector takes 25% of all Construction points; Interventionism raises this to 50%. DECISION RULE: always build at least 2 Sectors at once under Traditionalism — 1 Sector yields fewer government points than the free baseline (see numbers below).
6. **Local-price siting** — Inputs cost less if produced in the same state as the Sector consuming them. DECISION RULE: pick ONE industrial state (ideally one with iron) and concentrate Sectors plus their input chains there; do not scatter Sectors across the map.
7. **Production Method ladder for Sectors** — Wooden Frame Buildings → Iron Frame Buildings (Urban Planning tech) — each tier multiplies points per level but demands new inputs (Iron + Tools). DECISION RULE: upgrade the moment you have the tech AND domestic iron + tools; use Trade Center subventions on iron to bridge the gap.
8. **State construction efficiency** — A modifier applied to points spent in a state, from terrain (negative in Andes/Indo-Chinese Forests), the Road Maintenance decree (+10%), and excess Bureaucracy (~+10% per 200 excess). DECISION RULE: enable Road Maintenance in any heavy-build state with negative terrain efficiency; only chase excess Bureaucracy if your Government Admin upkeep can carry it.
9. **Queue discipline** — The Private Construction Queue skips anything already in the government queue. DECISION RULE: queue ONLY essentials (Sectors, their inputs, urgent urban). Everything else stays out so the Private sector pays for it.
10. **Privatization to refill reserves** — Selling existing urban buildings (Tooling Workshops, Textile Mills) channels cash into Financial Districts and raises Industrialist clout, since Financial Districts build urban while Manor Houses build agricultural. DECISION RULE: when reserves drain toward zero, privatize one profitable urban Building, then toggle privatization OFF so the replacement does not auto-sell.
11. **Qualifications gate PM upgrades** — Higher Production Methods need higher-tier workers (Machinists, Engineers); a half-staffed upgraded PM can output LESS than a fully-staffed lower one. DECISION RULE: do the arithmetic before switching PMs; if qualifications are short, enable Promote Social Mobility (+25%) and/or build Universities (+10% per level) first.
12. **Target a small weekly deficit while building** — Cash sitting in the treasury is wasted production. DECISION RULE: tune taxes and wages so weekly budget runs slightly negative (~−400) while reserves are healthy; surplus >1k means you should have added a Sector already.
13. **Tariff-steering Trade Centers** — Trade Centers chase the most profitable trades, which default to luxuries you do not need. DECISION RULE: during the initial build phase, max import tariffs on luxuries and max export tariffs on Wood/Fabric/Iron so the Trade Center brings in construction inputs. Revert when domestic inputs are online.
14. **Import subventions as bridges** — A subvention forces the Trade Center to import a specific Good even if unprofitable. DECISION RULE: subvent any critical input (tools, iron, paper) while its domestic Building is under construction; drop the subvention the week the Building completes.
15. **Consumption taxes by consumer class** — Pop spending breaks down by strata, and SoL hits scale with the share each strata buys. DECISION RULE: tax Services, Transportation, Luxury Clothes, Luxury Furniture (upper-strata heavy); avoid taxing Clothes and Grain (universal — drops SoL across all classes).
16. **High Taxes is emergency-only** — The High Taxes law extracts more revenue but drains pop spending money, which shrinks the very economy you are taxing. DECISION RULE: use only briefly while waiting for a privatization sale to land; drop to Medium the moment reserves recover.

## Game numbers & rules of thumb

All from `[from 11-construction]`:

- Baseline with no Sectors: 10 free Construction points/week, no Goods cost, Private queue inactive.
- Minting: flat base (~500) + 1 per 1,000 GDP + law/tech % bonuses + Gold output.
- Traditionalism Private split: 25%. Interventionism: 50%.
- Wooden Frame Sector: 2 points/level.
- Iron Frame Sector (Urban Planning): 5 points/level + state construction efficiency; requires Iron + Tools.
- Sector math under Traditionalism: 1 Sector = (10 base + 2) × 0.75 = 9 gov points (LESS than the 10 free baseline). 2 Sectors = 14 × 0.75 = 10.5. Hence "never build just one."
- Road Maintenance decree: +10% state construction efficiency.
- Excess Bureaucracy: ~+10% per ~200 excess.
- Promote Social Mobility: +25% state qualifications (and education access → literacy).
- University: +10% qualifications per level (needs Academia tech + Paper input).
- Healthy weekly deficit while building: around −400. Surplus >1k means add a Sector.
- Reserve floor is hard — sell a Building before you hit zero.
- ~30 Construction points is the threshold to pivot toward "main export" focus and trade-advantage treaties.

## Strategy & playbook

**Phase 1 — Pre-loop setup (small nation, 1.9+).** Research Urban Planning first so the Iron Frame upgrade is waiting when you need it. Pick one capital-adjacent industrial state — ideally with iron in the ground — as your build hub. Queue, in this exact order: 1 Trade Center, 2 Construction Sectors, 1 Cotton Plantation, 1 Logging Camp, 1 Tooling Workshop, then 2 more Logging Camps. The Trade Center comes first because it lets the Sectors actually pay local prices on imported Wood and Fabric while your domestic supply is being built. Two Sectors, not one, because under Traditionalism a single Sector leaves you net-down on government points. If you are running Isolationism you cannot build Trade Centers — in that case domestic Wood and Fabric must come first and the Sectors come third.

**Phase 2 — Steering inputs with tariffs and subventions.** Max-tariff luxury imports and Wood/Fabric/Iron exports so the Trade Center prioritizes construction goods over selling perfume. Apply import subventions on whichever input you do not yet produce — usually Tools and Iron during the early game. Trim battalions hard: Irregular Infantry costs wages for very little combat value, so keep the army minimal until you can field Line Infantry. Tune taxes so the weekly budget sits at roughly −400 — stockpiled cash is wasted growth.

**Phase 3 — Iron Frame transition.** Once Urban Planning is in and your Iron Mines + Tooling Workshop can cover 50 Iron + 20 Tools per Sector level, switch the Sectors to Iron Frame Buildings. This is the single biggest single-decision speed-up in the early game — 2 points/level becomes 5 plus state efficiency. Keep the iron-import subvention running until the switch is complete and your domestic supply absorbs the new demand.

**Phase 4 — Compounding and crisis management.** Whenever surplus crosses 1k, add a Sector plus matching input levels. Whenever reserves trend toward zero, privatize one profitable urban Building (Tooling Workshop or Textile Mill), pocket the cash, and immediately toggle privatization OFF on the building type so the replacement does not auto-sell. This double-bonuses you: cash now, and money flows into Financial Districts which build the urban buildings that mostly otherwise will not get built (the gamestart Investment Pool is Manor-House-dominated, so Private builds default to farms). Add Road Maintenance to any building state with negative terrain efficiency. Only chase excess Bureaucracy if you can afford the Government Admin upkeep — efficient states are cheaper than overbuilt ones.

**Phase 5 — Export pivot at ~30 points.** Around 30 Construction points you have outgrown the bootstrap. Shift to a "main export" focus, sign trade-advantage treaties, and let the loop spin on its own momentum while you start funding the things construction enables — armies, navies, the political reforms that lift the Private split from 25% to 50%.

## Common pitfalls

- **Building only ONE Construction Sector under Traditionalism.** The math gives you 9 gov points instead of the free 10 — you went backwards. Always two.
- **Trusting subsistence-farm Wood/Fabric supply.** Those numbers shrink as pops leave subsistence for your new jobs. Today's "+5 market surplus" is tomorrow's shortage.
- **Spamming a huge government queue.** The Private queue skips duplicates, so you end up paying for everything yourself.
- **Building too many battalions before Line Infantry.** Irregulars give negligible combat power and burn wages you need for Sectors.
- **Upgrading a PM without checking qualifications.** A 60%-staffed higher PM can output less than a 100%-staffed lower one.
- **Leaving privatization toggled ON after a sale.** The next Tooling Workshop auto-sells the moment it completes, even with healthy reserves.
- **Sitting on High Taxes.** SoL collapses, pops stop spending, and the economy contracts under you.
- **Going into debt as a small nation.** ~30%+ interest makes it unrecoverable — rank up first, borrow later.

## See also

- **In this wiki:**
  - [economy/treasury-and-deficit.md](./treasury-and-deficit.md)
  - [economy/building-balance-sheet.md](./building-balance-sheet.md)
  - [economy/companies.md](./companies.md)
  - [economy/trade.md](./trade.md)
  - [economy/foreign-investment.md](./foreign-investment.md)
  - [economy/shipbuilding.md](./shipbuilding.md)
  - [pops/standard-of-living.md](../pops/standard-of-living.md)
  - [case-studies/japan-great-wave/index.md](../case-studies/japan-great-wave/index.md)
- **Official wiki:**
  - https://vic3.paradoxwikis.com/Buildings
  - https://vic3.paradoxwikis.com/Production_methods
  - https://vic3.paradoxwikis.com/Treasury

## Sources

- `notes/tutorials/11-construction.md`
