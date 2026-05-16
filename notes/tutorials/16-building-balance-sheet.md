---
source_transcript: ../../transcripts/tutorials/16-building-balance-sheet.md
source_video: https://www.youtube.com/watch?v=xoKAX0X_GIw
generated_at: 2026-05-16
---

# Building balance sheets and why government ownership leaks money
**Source:** [Building Balance Sheet Tutorial in Victoria 3](https://www.youtube.com/watch?v=xoKAX0X_GIw) (24:17 runtime)

## Summary
A weekly Building balance sheet flows in a fixed order: revenue minus inputs and Wages gives the weekly balance, a slice is skimmed into Cash Reserves, and the rest becomes total Dividends split between owners and the Investment Pool. Ownership type (government, local workforce, manor houses / financial districts) determines who receives those Dividends and how much actually reaches your Treasury. Government-owned Buildings always leak income through "government dividends efficiency," which caps at well below 100% — so privately owned Buildings are strictly better for long-run revenue.

## Core mechanics
1. **Vicky math (UI truncation)** — The game shows truncated decimals, so manual sums miss by 1–2. DECISION RULE: when checking balance-sheet math, accept any error within ±1–2; only investigate larger gaps. `[01:30]`
2. **Cash Reserves as profit buffer and credit base** — Profitable Buildings top up Cash Reserves first; unprofitable Buildings drain them to stay open. DECISION RULE: your national Credit Limit = base value + sum of all Building Cash Reserves, so protect profitable Buildings if you plan to deficit-spend. `[03:05]` `[03:30]`
3. **Throughput multiplies inputs and outputs at the same Wage cost** — A Throughput bonus scales both consumption and production but not employment. DECISION RULE: prioritize Throughput-boosting Production Methods and techs over expansion when Wages are tight, since you get more output per worker paid. `[04:31]` `[05:00]`
4. **Weekly balance order of operations** — Revenue − inputs − Wages = weekly balance; then Cash Reserves skim first, then the remainder becomes total Dividends. DECISION RULE: when reading the tooltip, treat the "reinvestment" line as "total Dividends after reserves" — the split into owner pay vs. Investment Pool happens further down. `[06:01]` `[07:00]`
5. **Government Dividends Reinvestment split** — Of total Dividends owed to a government owner, a % is diverted into the Investment Pool (Interventionism = +50%, Lzaire/Cooperative Ownership = +100%). DECISION RULE: under Lzaire/Cooperative, government-owned Buildings send 100% of Dividends to the Pool — none vanishes, but none reaches your budget either. `[07:31]` `[19:32]`
6. **Government Dividends Efficiency leak** — Only the "efficiency %" of government Dividends actually reaches the Treasury; the rest literally disappears. Base is 25%; Interventionism +25%, Command Economy +40%, debt secured against your own Buildings −2% per occurrence. DECISION RULE: never assume government-owned Buildings fund your budget — at best Command Economy still loses ~35% of its Dividends to the void. `[12:00]` `[13:00]` `[20:03]`
7. **Investment Pool GDP multiplier** — All Investment Pool contributions are multiplied ×3 at 0 GDP, scaling down linearly to ×1 at 50M GDP. DECISION RULE: small-nation Investment Pools punch far above weight — exploit this early by routing as much profit as possible into the Pool. `[09:31]` `[10:32]`
8. **Government ownership double-multiplier quirk** — Because a government Building's Dividends route through the Treasury budget, the GDP multiplier hits twice on its Investment Pool slice. DECISION RULE: this is the one upside of government ownership; private Buildings get the multiplier only once. `[10:32]` `[11:00]`
9. **Local-workforce ownership routes Dividends to worker pops** — The pops doing the work also own the Building, so Dividends top up their pop income on top of Wages, and a fixed % of those Dividends is contributed to the Investment Pool per Profession. DECISION RULE: laborers contribute 0% to the Pool; farmers 10%; clergy/aristocrats 20% (see wiki Treasury table). Expect bigger Investment Pool flows from Buildings staffed by higher Professions. `[14:31]` `[16:01]` `[16:30]`
10. **Manor houses and financial districts as ownership Buildings** — Manor houses generally own agricultural Buildings; financial districts generally own urban ones, with Dividends paid to their aristocrats/clergy/capitalists. DECISION RULE: building manor houses / financial districts replaces local-workforce ownership and concentrates Dividends into upper-strata pops (whose taxes you collect and who feed the Pool at 20%). `[17:01]`
11. **Owners get a guaranteed 15% of revenue floor** — If a Building can't pay owners 15% of weekly revenue from profit, it drains Cash Reserves to make up the gap, even when "profitable." DECISION RULE: if you see profitable Buildings with shrinking reserves, check whether revenue × 15% exceeds the weekly balance — fix by swapping Production Methods, lowering input prices, or raising output prices. `[21:00]` `[21:30]` `[23:01]`
12. **Efficiency vs. contribution wording** — Positive "efficiency" creates money from nothing; negative "efficiency" deletes it. Negative "investment pool contribution efficiency" (e.g., universal −50% under Traditionalism) means Pool contributions are halved into the void. DECISION RULE: read every "efficiency" modifier as a money creator/destroyer, not a redirector. `[20:31]` `[21:00]`

## Game numbers & rules of thumb
- Credit Limit = base (e.g. 250K for Congo) + sum of all Building Cash Reserves. `[03:30]`
- Throughput scales both inputs and outputs by the same %, employment unchanged. `[04:31]`
- Base Government Dividends Efficiency = 25%. `[12:30]`
- Interventionism: +50% Government Dividends Reinvestment, +25% Government Dividends Efficiency. `[07:31]`
- Traditionalism: 25% of Dividends auto-routed to Investment Pool; everyone gets −50% Investment Pool Contribution Efficiency. `[18:00]` `[20:31]`
- Command Economy: +40% Government Dividends Efficiency (the maximum available). `[19:32]`
- Lzaire / Cooperative Ownership: +100% Government Dividends Reinvestment (no Dividends reach the budget). `[19:32]`
- Investment Pool GDP multiplier: ×3 at 0 GDP linearly down to ×1 at 50M GDP. `[10:02]`
- Investment Pool contribution % from Dividends by Profession: Laborers 0%, Farmers 10%, Clergy/Aristocrats 20% (see wiki Treasury page). `[16:01]` `[16:30]`
- Owners receive at least 15% of weekly revenue as Dividends if Cash Reserves can cover the shortfall. `[21:30]`
- Government-owned debt penalty: −2% Government Dividends Efficiency while in debt against your own Buildings. `[13:00]`

## Common pitfalls
- Reading the "reinvestment" tooltip line as final reinvestment — it's actually total Dividends after Cash Reserves; the real Pool number is further down. `[07:00]`
- Assuming government Buildings fully fund your budget — even under Command Economy at least ~35% of every Dividend pound vanishes. `[20:03]`
- Funding construction with debt while most Buildings are government-owned — you borrow against your own Cash Reserves and eat a Government Dividends Efficiency penalty on top. `[13:00]`
- Switching to Lzaire/Cooperative expecting more Treasury income — those laws send 100% of government Dividends to the Investment Pool, not your budget. `[19:32]`
- Panicking when a profitable Building drains Cash Reserves — likely the 15%-of-revenue owner floor; fix Production Methods or prices instead of demolishing. `[21:30]`
- Forgetting that slaves don't count as owners when computing local-workforce Dividend shares. `[15:31]`

## Cheatsheet
1. Read every Building's balance top-down: revenue − inputs − Wages → balance → Cash Reserves skim → total Dividends → split into owner pay + Investment Pool.
2. Sell government-owned Buildings to the private sector as soon as Cash Reserves can fund construction without you — long-run Treasury income is higher.
3. Stack Throughput before levels: same Wage bill, more output, healthier weekly balance.
4. Early game, route as much as possible into the Investment Pool — the ×3 multiplier collapses to ×1 by 50M GDP.
5. If switching laws for Treasury revenue, prefer Command Economy (+40% Efficiency) over Lzaire/Cooperative (100% diverted to Pool, 0% to budget).
6. When a profitable Building drains Cash Reserves, check whether weekly balance < 15% of revenue; fix via Production Method swap or price changes.

## See also
- [Treasury](https://vic3.paradoxwikis.com/Treasury) — contains the Profession-to-Investment-Pool contribution table referenced in the video.
- [Buildings](https://vic3.paradoxwikis.com/Buildings) — ownership types, Cash Reserves, and dividend mechanics.
- [Laws](https://vic3.paradoxwikis.com/Laws) — economic system modifiers (Traditionalism, Interventionism, Command Economy, Lzaire, Cooperative Ownership).
