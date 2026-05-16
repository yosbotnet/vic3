---
source_transcript: ../../transcripts/tutorials/11-construction.md
source_video: https://www.youtube.com/watch?v=w4WNFRnZsFs
generated_at: 2026-05-16
---

# Construction

**Source:** [Construction Tutorial in Victoria 3](https://www.youtube.com/watch?v=w4WNFRnZsFs) (47:00 runtime)

## Summary
Walks through the construction loop in Victoria 3 from the perspective of a small nation (Dai Nam) at game start: how to bootstrap your first Construction Sectors without going bankrupt, how to use a Trade Center to import scarce construction goods, how to feed the Investment Pool by selling urban buildings to the private sector, and how to scale up production methods as tech unlocks. The advice applies primarily to the opening 10–20 years of a campaign and to any moment in a run where you ask "what should I build next?"

## Core mechanics
1. **Construction loop** — Construction Sectors cost money (input goods + wages), but more buildings raise GDP, GDP raises Minting, Minting raises budget, and a higher budget funds more Construction Sectors. It is exponential: slow at the start, faster as the loop compounds.
2. **Minting** — A flat per-week amount plus a GDP-derived share added to your weekly income. Boosted by certain laws/techs and by Gold Fields and Gold Mines, both of which directly output minting.
3. **Construction points** — Each Construction Sector contributes points to a weekly construction budget. Points are split between the government queue and the private queue based on your Economic System law.
4. **Economic System split** — Under Traditionalism the private sector only gets 25% of construction points, so the government carries almost everything. Interventionism/Agrarianism give the private sector 50%, which is when the loop really accelerates.
5. **Investment Pool & private queue** — The private queue is funded from the Investment Pool, fed by Manor Houses, Financial Districts and Companies. Whoever contributes most to the pool gets priority; manor houses dominate at game start, which is why the private queue defaults to agricultural builds.
6. **Selling buildings to the private sector** — Selling urban buildings (especially profitable ones) hands them to Financial Districts, which then contribute more to the Investment Pool, empower Industrialists, and shift the private queue toward urban/industrial builds.
7. **Trade Centers for construction inputs** — Since the 1.9 update a Trade Center lets you import construction goods at local prices, so you can build Construction Sectors before all your input-good buildings are finished. They prioritize the most profitable trades, so you must steer them with tariffs.
8. **Construction efficiency** — State traits, decrees (Road Maintenance), and excess Bureaucracy modify how many construction points actually land on a building each week. Negative efficiency stretches build times; positive efficiency shortens them.
9. **Production-method scaling for sectors** — Wooden Frame Buildings use fabric + wood; Urban Planning unlocks Iron Frame Buildings, which need iron + tools but more than double per-sector output and also add state construction efficiency.
10. **Loan interest is rank-based** — Small nations face huge interest rates and cannot sustain debt; large nations get rank discounts and can safely borrow to expand construction.

## Numbers & formulas
- Base minting: 500 pounds per week flat. [02:30]
- Minting from GDP: 1 pound per 1,000 pounds of GDP (example: 1.7M GDP -> 1,700 minting). [03:00]
- USA example: +10% minting from Banking, Central Banking, and Mutual Funds laws/techs. [03:00]
- Starting construction points with zero Construction Sectors: 10 (no material/wage cost, private queue inactive). [02:30]
- Small-nation example loan interest rate modifier: -75% from rank, but effective rate still ~34% making debt unsustainable. [06:00] [12:01]
- Traditionalism gives the private sector 25% of construction points. [07:01]
- One Construction Sector on Wooden Frame Buildings needs 25 fabric and 75 wood. [08:01]
- Each Construction Sector adds 2 construction points on Wooden Frame Buildings. [09:31]
- Math for two sectors under Traditionalism: 10 base + 2*2 = 14 total; 14 * 0.75 = 10.5 government points. [09:31]
- One sector instead: 12 * 0.75 = 9 government points (worse than starting). [10:00]
- Two sectors need 50 fabric and 150 wood total. [10:00]
- One Cotton Plantation provides 40 fabric. [10:00]
- One Logging Camp: 30 wood base; 60 wood on Sawmills production method (requires tools). [10:00]
- Trade Center example build cost: 100 construction points. [16:31]
- Indo-Chinese Forests state trait: +10% Logging Camp throughput but -10% state construction efficiency. [16:31]
- -10% construction efficiency turns 10 weekly points into 9 effective points; 100/9 ≈ 11.1 weeks (game rounds to 12). [17:00]
- Road Maintenance decree: +10% state construction efficiency. [17:31]
- Excess Bureaucracy example (Chile +207): +10% state construction efficiency. [18:30]
- Cost of one Government Administration on the third production method (paper-using): ~2.54K per week. [19:30]
- Iron Frame Buildings: each Construction Sector outputs 5 construction points (vs 2) plus a small state construction efficiency bonus. [27:30]
- One Construction Sector on Iron Frame Buildings needs 50 iron and 20 tools per level. [28:02]
- One Iron Mine level outputs 20 iron; need 5 levels to cover two Iron Frame Construction Sectors. [28:02]
- One Tooling Workshop level outputs 30 tools. [29:00]
- Promote Social Mobility decree: +25% qualifications (also raises education access/literacy). [31:32]
- One University level: +10% qualifications in the state. [32:01]
- Dai Nam starting military: 55 battalions costing 4.57K/week in wages; cut to 20 brings wages to ~1.66K/week. [21:02] [22:01]
- Irregular Infantry: only +10 offense / +10 defense. [21:30]
- Investment Pool contribution example: Manor Houses 442/week vs Financial Districts 14.44/week. [26:01]
- Switch off Traditionalism (Interventionism/Agrarianism) for 50% private share of construction. [46:02]
- Rough "second phase" threshold: ~30 construction points before pivoting to building export industries. [46:30]

## Common pitfalls
- Building one Construction Sector first under Traditionalism — you end up with fewer effective government points than before.
- Stockpiling cash. If your weekly balance is more than +1K green, you can afford another Construction Sector; sitting on reserves wastes the loop.
- Spamming a long government construction queue. The private queue checks what is already on the government list and will skip it; keep the government list to essentials so the private sector picks up the rest.
- Going into debt as a small nation. With rank-based interest near 34%, even a short stint in the red spirals out of control.
- Building Construction Sectors without a way to supply their input goods. Substinence farms' "free" wood/fabric output drops as peasants leave, so those numbers are unreliable.
- Letting Trade Centers import luxury goods first. They go for the most profitable trades, so without tariffs they will not focus on your construction inputs.
- Over-spamming battalions. Each battalion costs wages (and often goods); 55 Irregular Infantry is mostly useless and drains the budget you need for construction.
- Staying on High Taxes long-term. It cuts standard of living and pop spending, throttling the very GDP loop you are trying to grow.
- Sitting at a higher production method when qualifications cannot fill it. Sometimes downgrading (e.g. Sawmills -> Simple Forestry) yields more total output until you can build a University.

## Cheatsheet
1. Research order: Urban Planning, Stock Exchange, then Academia and Romanticism so you can shift off Traditionalism and unlock Iron Frame Buildings + Universities.
2. First build queue (small nation, 1.9+): Trade Center first, then two Construction Sectors, then the input-goods chain (Cotton Plantation, Logging Camp, Tooling Workshop, more Logging Camps). Tariff luxury imports and tariff wood/fabric exports so the Trade Center prioritizes your construction goods; subsidize the Trade Center.
3. Keep all Construction Sectors and their input goods in one state to get local-price discounts; add the Road Maintenance decree if the state has negative construction efficiency.
4. Once Construction Sectors are up, sell profitable urban buildings (Tooling Workshops, Textile Mills) to the private sector to feed Financial Districts and the Investment Pool — only sell when reserves are running low.
5. After Urban Planning, switch sectors to Iron Frame Buildings (build 5 Iron Mines and a Tooling Workshop first; subsidize iron/tools imports through the Trade Center during the transition).
6. Add a Construction Sector whenever weekly budget sits above +1K; use consumption taxes on services, transportation, luxury clothes, luxury furniture (not on staples) to fund expansion, and only use High Taxes briefly while waiting for a sale.
