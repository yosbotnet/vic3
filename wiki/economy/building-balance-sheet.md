---
sources:
  - ../../notes/tutorials/16-building-balance-sheet.md
  - ../../notes/comprehensive-tutorial-2025/01-economics.md
wiki:
  - https://vic3.paradoxwikis.com/Buildings
generated_at: 2026-05-16
---

# Building Balance Sheet

## What it is

The Building balance sheet is the weekly per-Building accounting tooltip that shows where every pound of revenue goes: subtract input costs and Wages, skim a slice into Cash Reserves, then split the rest as total Dividends between owners and the Investment Pool. You read it whenever a Building looks suspicious — profitable but draining reserves, government-owned but not funding your Treasury, or producing less than you expected from a Throughput upgrade. The balance sheet is the only place where ownership type, economic Laws, and Production Method choices visibly collide; understanding it is the difference between optimising the Treasury and silently leaking it.

## Mechanics

1. **Vicky math (UI truncation)** — The game shows truncated decimals, so manually summing lines on the tooltip will miss by 1–2. Decision rule: accept ±1–2 mismatches when checking balance-sheet math; only investigate larger gaps.
2. **Weekly balance order of operations** — Revenue − inputs − Wages = weekly balance. Cash Reserves skim first; the remainder becomes total Dividends, which are then split into owner pay and Investment Pool contribution. Decision rule: read the tooltip strictly top-down, and treat the line labelled "reinvestment" as "total Dividends after reserves," not as the final Pool number.
3. **Cash Reserves as profit buffer and credit base** — Profitable Buildings top up Cash Reserves first; unprofitable ones drain them to keep paying Wages. Your national Credit Limit = base value + sum of all Building Cash Reserves. Decision rule: if you plan to deficit-spend, protect profitable Buildings — their reserves are literally your borrowing capacity.
4. **Throughput multiplies inputs and outputs at the same Wage cost** — A Throughput bonus scales both consumption and production proportionally, but employment is unchanged. Decision rule: when Wages are tight, prioritise Throughput-boosting Production Methods and techs over building new levels — you get more output per worker paid.
5. **Owners get a guaranteed 15% of revenue floor** — If profit cannot pay owners at least 15% of weekly revenue, the Building drains Cash Reserves to fund the gap, even when the balance is positive. Decision rule: if a "profitable" Building is bleeding reserves, check whether weekly balance < 15% of revenue; fix via Production Method swap, cheaper inputs, or higher output prices — not demolition.
6. **Government Dividends Reinvestment split** — Of total Dividends owed to a government owner, a percentage is diverted into the Investment Pool before the remainder is sent to the Treasury (Interventionism +50%, Laissez-faire / Cooperative Ownership +100%). Decision rule: under Laissez-faire or Cooperative Ownership, government-owned Buildings send 100% of Dividends to the Pool — none vanishes, but none reaches your budget either.
7. **Government Dividends Efficiency leak** — Of the Dividends that are *not* diverted to the Pool, only an "efficiency %" actually reaches the Treasury; the rest disappears. Base 25%; Interventionism +25%; Command Economy +40%; −2% per occurrence of debt secured against your own Buildings. Decision rule: never assume government Buildings fund your budget — even at the Command Economy ceiling, roughly 35% of every Dividend pound vanishes.
8. **Investment Pool GDP multiplier** — All Investment Pool contributions are multiplied ×3 at 0 GDP, scaling down linearly to ×1 at 50M GDP. Decision rule: small nations should aggressively route profit into the Pool early — the multiplier collapses as you grow.
9. **Government ownership double-multiplier quirk** — Because a government Building's Dividends route through the Treasury budget, the GDP multiplier hits twice on its Investment Pool slice. Decision rule: this is the *only* upside of government ownership; weigh it against the Efficiency leak before retaining state-owned Buildings.
10. **Local-workforce ownership routes Dividends to worker pops** — Pops doing the work also own the Building, so Dividends top up their pop income on top of Wages, and a fixed % of those Dividends is contributed to the Investment Pool per Profession. Decision rule: expect bigger Pool flows from Buildings staffed by higher Professions (clergy/aristocrats 20% vs. laborers 0%). Slaves never count as owners.
11. **Manor houses and financial districts as ownership Buildings** — Manor houses generally own agricultural Buildings; financial districts generally own urban ones, with Dividends paid to their aristocrats/clergy/capitalists. Decision rule: building manor houses or financial districts replaces local-workforce ownership, concentrating Dividends into upper-strata pops — who pay more tax and contribute to the Pool at 20%.
12. **Efficiency vs. contribution wording** — Positive "efficiency" creates money from nothing; negative "efficiency" deletes it. Decision rule: read every "efficiency" modifier as a money creator/destroyer, not a redirector — Traditionalism's −50% Investment Pool Contribution Efficiency halves Pool contributions into the void.
13. **Untaxable profit is still load-bearing** — Even profit you cannot tax (the Investment Pool slice, owner pockets before dividend taxation unlocks) stays valuable, because it feeds the Pool that the private queue spends to build more buildings — and those buildings pay *taxable* wages. Decision rule: never dismiss a Building as "useless" because its profit lands somewhere you can't tax this decade; judge it by how much it pumps into the Pool that builds your future tax base (2025 comprehensive tutorial, [07:30]).

## Game numbers & rules of thumb

- Credit Limit = base (e.g. ~250K for Congo) + sum of all Building Cash Reserves `[from 16-building-balance-sheet]`.
- Throughput scales inputs and outputs by the same %; employment unchanged `[from 16-building-balance-sheet]`.
- Base Government Dividends Efficiency = 25% `[from 16-building-balance-sheet]`.
- Interventionism: +50% Government Dividends Reinvestment, +25% Government Dividends Efficiency `[from 16-building-balance-sheet]`.
- Traditionalism: 25% of Dividends auto-routed to Investment Pool; universal −50% Investment Pool Contribution Efficiency `[from 16-building-balance-sheet]`.
- Command Economy: +40% Government Dividends Efficiency (the maximum available) `[from 16-building-balance-sheet]`.
- Laissez-faire / Cooperative Ownership: +100% Government Dividends Reinvestment — zero Dividends reach the Treasury `[from 16-building-balance-sheet]`.
- Investment Pool GDP multiplier: ×3 at 0 GDP, linearly down to ×1 at 50M GDP `[from 16-building-balance-sheet]`.
- Investment Pool contribution % from local-workforce Dividends: Laborers 0%, Farmers 10%, Clergy/Aristocrats 20% `[from 16-building-balance-sheet]`.
- Owner Dividend floor = 15% of weekly revenue, paid from Cash Reserves if needed `[from 16-building-balance-sheet]`.
- Government-owned debt penalty: −2% Government Dividends Efficiency per occurrence of debt secured against your own Buildings `[from 16-building-balance-sheet]`.
- **Wage multipliers by profession:** machinists earn ~1.5× laborer wage, shopkeepers ~2×, engineers ~3×. Same ratios apply to dividend distribution when locally owned. `[from beginner-tutorial ep10]`
- **Wage-adjustment thresholds:** a building only raises wages when its profit margin exceeds ~30%, holds steady between 15-30%, and tries to lower wages below 15%. The ceiling it raises toward is each pop's minimum-expected SoL × ~1.33. (verify exact constants on current patch) `[from beginner-tutorial ep10]`

## Strategy & playbook

**Stop treating government Buildings as a Treasury source.** The base 25% Government Dividends Efficiency means three-quarters of every state-owned Dividend pound is *literally deleted*, not redirected. Even Command Economy — the best Efficiency law available — caps the leak at roughly 35%. The implication is decisive: privately owned Buildings are strictly better for long-run revenue, because their Dividends become pop income, which becomes taxable income, with no Efficiency leak. Sell government Buildings to the private sector as soon as the Investment Pool and your Cash Reserves can fund construction without you, and stop expecting nationalised industries to fix a budget shortfall. The two exceptions are (a) you genuinely cannot get private capital to build what you need, or (b) you specifically want the double GDP multiplier on the Pool slice of state Dividends (Mechanic 9) — a niche early-game lever.

**Stack Throughput before levels.** The same Wage bill that produces 100 units of output also produces 120 with a +20% Throughput modifier — and the Wages did not change. That makes Production Method upgrades and Throughput techs the highest-leverage moves when your weekly balance is thin or your labour pool is tapped out. Building new levels demands more Wages, more inputs, and more pops you may not have; Throughput multiplies what is already there. When deciding between "build one more level" and "swap to a better Production Method," default to the PM swap unless you specifically need more employment for SoL or to soak up unemployment.

**Route everything into the Investment Pool while you are small.** The ×3 multiplier at 0 GDP is the single largest growth lever in the game, and it decays linearly to ×1 by 50M GDP. Small nations should therefore tilt every law and ownership choice toward Pool throughput: Interventionism for the +50% Reinvestment, manor houses and financial districts to concentrate Dividends into 20%-contributing pops, and aggressive Throughput upgrades to pump more profit through the pipeline. Once you are mid-sized, the multiplier has already collapsed; further Pool-tilting yields diminishing returns and you should pivot toward Treasury income (Command Economy, private ownership, tax base).

**Diagnose "profitable but draining" Buildings before demolishing.** The 15%-of-revenue owner floor is the most common source of mystery Cash Reserve loss. A Building can show a positive weekly balance and still bleed reserves because the balance is less than 15% of revenue and owners are entitled to that floor. Before touching the build, walk the tooltip top-down: compute revenue × 0.15, compare to weekly balance, and if the floor is biting, fix the *margin* — swap to a cheaper Production Method, change input mix, or push prices up via tariff/trade route changes. Demolishing a structurally fine Building because of this floor is one of the most expensive misreads in the game.

**Match laws to your ownership mix, not the other way round.** Switching to Laissez-faire or Cooperative Ownership *while most of your Buildings are government-owned* sends 100% of those Dividends to the Investment Pool and 0% to your Treasury — a budget catastrophe disguised as a reform. Privatise first, then switch laws. Conversely, switching to Command Economy while the private sector already owns everything wastes the +40% Efficiency bonus on a tiny pool of state Dividends. The general rule: Laws change *how* Dividends move, but ownership type determines *which* Dividends exist to be moved.

## Common pitfalls

- Reading the "reinvestment" tooltip line as the final Pool number — it is total Dividends after Cash Reserves; the actual Pool contribution sits further down.
- Assuming government Buildings fully fund your budget — even under Command Economy ~35% of every Dividend pound vanishes.
- Funding construction with debt while most Buildings are government-owned — you borrow against your own Cash Reserves *and* incur a −2% Efficiency penalty per debt occurrence.
- Switching to Laissez-faire or Cooperative Ownership for Treasury income — those laws divert 100% of government Dividends to the Pool, not your budget.
- Demolishing a profitable Building that is draining Cash Reserves — almost always the 15% owner floor; fix Production Methods or prices instead.
- Forgetting that slaves don't count as owners when computing local-workforce Dividend shares — abolition shifts the ownership math, not just the moral one.
- Treating a negative "efficiency" modifier as a redirect — it deletes money, it does not move it.

## See also

- **In this wiki:** [Treasury and deficit](./treasury-and-deficit.md), [Construction](./construction.md), [Companies](./companies.md), [Foreign investment](./foreign-investment.md), [Standard of living](../pops/standard-of-living.md), [Passing laws](../laws-and-politics/passing-laws.md)
- **Official wiki:** [Buildings](https://vic3.paradoxwikis.com/Buildings), [Treasury](https://vic3.paradoxwikis.com/Treasury), [Production methods](https://vic3.paradoxwikis.com/Production_methods)

## Sources

- `../../notes/tutorials/16-building-balance-sheet.md`
- `../../notes/comprehensive-tutorial-2025/01-economics.md`
