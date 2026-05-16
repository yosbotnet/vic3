---
source_transcript: ../../transcripts/tutorials/04-standard-of-living-wages-and-wealth.md
source_video: https://www.youtube.com/watch?v=fvHnfklJCvY
generated_at: 2026-05-16
---

# Standard of Living, Wages & Wealth

**Source:** [Standard of Living, Wages, and Wealth Tutorial in Victoria 3](https://www.youtube.com/watch?v=fvHnfklJCvY) (48:58 runtime)

## Summary
Standard of Living (SoL) is a per-Pop measure derived primarily from a Pop's Wealth level, with small modifiers from health, pollution, and Power Bloc principles. Wealth itself is driven mainly by Wages, which determine what categories of goods a Pop can afford in their basket of needs. Raising SoL grows the customer base for expensive goods, which in turn raises GDP — so SoL is both a moral and an economic lever, balanced against the fact that higher wages mean lower building profitability.

## Core mechanics

1. **GDP counts everything except building inputs** — Of the five consumption sinks (building inputs, Pop needs, trade centers, goods transfers, unused goods), only building inputs are subtracted from GDP. Pop needs are the most stable demand sink because they don't need brokering. DECISION RULE: when judging "real" demand for a good, prefer Pop-needs consumption over trade routes; design your economy so wealthy Pops can absorb your luxury output. `[02:31]` `[03:31]`

2. **Wealth → basket of needs** — A Pop's Wealth level unlocks goods categories (basic food, luxury food, clothing, household items, services, free movement, etc.). Higher Wealth = more categories AND more expensive goods within each category. Luxury items require Wealth >= 15. DECISION RULE: to make textile mills, furniture, glassworks etc. profitable, you must push lower-strata Wealth above 15 — otherwise their customer base is tiny. `[05:31]` `[07:30]`

3. **Wealth equilibrium loop** — Each week the game checks if a Pop's net income (income − needs expenses − taxes) can sustain the next Wealth level's basket. If yes, they climb; if negative at current level, they fall. The most volatile term is needs expense because market prices change weekly. DECISION RULE: to bump Pops up a Wealth tier, make goods in the NEXT tier's basket cheaper, not just the current one. `[22:31]` `[23:31]`

4. **Base wage vs. normal wage** — Base wage is set per building, per state, and represents the lowest-paid worker's pay; it rises ~10% every 2 weeks if a building can't fill jobs and the building is still profitable. Normal wage is the average of all base wages across incorporated, non-government buildings; it sets the base wage of all government buildings and the threshold for welfare. DECISION RULE: to read your current normal wage, hover wages on any government building (e.g. barracks). Don't confuse it with "average annual government wage" which includes multipliers. `[10:32]` `[15:00]`

5. **Profession wage multipliers** — Laborers (multiplier ×1) are the base; farmers ×2, machinists ×1.5, bureaucrats ×4, etc. A building can only raise the BASE wage — every profession scales off it. DECISION RULE: to lift a particular Pop group's Wealth, change the building's Production Method to convert Laborers into a higher-multiplier Profession (e.g. Laborers → Machinists). `[13:31]` `[27:31]`

6. **Wage modifiers from laws** — Citizenship and church/state laws apply % modifiers to individual Pop wages: National Supremacy gives +20% to tier-5 acceptance (and big penalties below); Ethnostate gives up to +25%; State Religion gives +10% to the state faith, −10% to others. DECISION RULE: if your country is overwhelmingly primary-culture, Ethnostate/National Supremacy max wages; if diverse, Multiculturalism avoids the penalty but gives no bonus. Assimilation/conversion are wage tools. `[14:00]` `[26:00]`

7. **Workforce ratio matters more than wage rates** — Wealth is shared between workers and dependents in a Pop group. Only ~25% of a Pop works by default; Women's Suffrage adds +15%. Child Labor laws raise dependent income (e.g. +30% to dependent income under "child labor allowed"). DECISION RULE: enacting Women's Suffrage is often a bigger SoL boost than fiddling with PMs because it nearly doubles wage-earners per Pop group. Avoid Old Age Pension if you can't spare the 1% workforce hit. `[17:30]` `[42:31]`

8. **Direct SoL modifiers (not Wealth)** — Public Health Insurance: +0.5 SoL per institution level to all Pops AND reduces pollution penalty (level 4 = −60% pollution effect). Private Health Insurance: +0.5 per level but only upper strata. Pollution: −0.5 SoL per state at certain pollution thresholds. Food Standardization (Power Bloc principle, level 3): +1 SoL to all Pops. DECISION RULE: SoL values are always rounded down to whole numbers per Pop — averages show decimals, individual Pops do not. `[29:31]` `[31:01]`

9. **Welfare payment threshold** — The Social Security institution sets a % of normal wage. Any Pop earning less than (threshold% × normal wage) receives a payment equal to the gap, paid weekly. Unemployed Pops have wage = 0, so they receive the full threshold amount. DECISION RULE: payments shown this week are for last week's gap. To predict next payment: ((threshold × normal_wage) − pop_wage) / 52 × workforce. `[32:00]` `[35:30]`

10. **Choosing a welfare law** — Poor Laws: cheapest politically permissible but inflicts −15% political strength per institution level on recipients (up to −75%), so they don't translate Wealth into clout. Wage Subsidies: same welfare schedule, no political penalty, plus +10% building wage target per level (effective minimum wage). Old Age Pension: starts at 30% welfare and scales to 150% at max, gives bigger food security and minimum wage, BUT −1% workforce per level and you can bankrupt yourself paying unemployed Pops massive subsidies. DECISION RULE: Wage Subsidies is the political sweet spot. Old Age Pension is bureaucracy-efficient (60% welfare at level 2 vs. level 3 of Poor Laws) but only safe with low unemployment. `[41:02]` `[46:01]`

11. **Job-switching friction blocks reemployment** — A Pop only switches jobs if the new wage is ≥10% higher than current effective income. When welfare overpays unemployed Pops, no realistic building wage can lure them back, creating persistent unemployment. DECISION RULE: if you set welfare above ~100% of normal wage, expect chronic unemployment; lower the institution level before raising it speculatively. `[44:30]` `[45:01]`

12. **SoL feedback into politics and migration** — Each strata has a minimum expected SoL that rises with literacy (e.g. Socialism gives +1). Below expected SoL → Radicals; above → Loyalists. Raising/lowering Social Security swings both. SoL also drives migration attraction — higher SoL than neighbors pulls in Pops. DECISION RULE: don't slash welfare laws abruptly — the SoL drop produces a wave of Radicals. Use the SoL heat-map (hover the headline SoL number) to gauge migration pull. `[47:33]` `[48:01]`

## Game numbers & rules of thumb

- Luxury goods unlock at Wealth level 15. `[07:30]`
- Building base wage rises ~10% every 2 weeks when understaffed and still profitable. `[12:30]`
- Profession wage multipliers: Laborers ×1, Machinists ×1.5, Farmers ×2, Bureaucrats ×4. `[13:31]` `[15:30]`
- Dependent income ratio for Laborers: 0.5 × workforce income. `[18:00]`
- Child Labor Allowed: +30% dependent income. `[18:32]`
- Women's Suffrage: +15% workforce ratio. `[17:30]`
- National Supremacy: +20% wages at tier-5 acceptance. `[14:00]`
- Ethnostate: up to +25% wages, largest non-tier-5 penalty. `[26:00]`
- State Religion: ±10% wages; Freedom of Conscience: ±5%. `[26:32]`
- Public Health Insurance: +0.5 SoL/level (all Pops); reduces pollution effect by 60% at level 4. `[29:31]` `[31:01]`
- Private Health Insurance: +0.5 SoL/level (upper strata only). `[31:01]`
- Food Standardization Power Bloc principle level 3: +1 SoL to all Pops. `[31:32]`
- Social Security welfare thresholds: level 1 = 20% of normal wage, +20%/level, level 5 = 100%. `[40:00]`
- Old Age Pension: starts at 30%, scales to 150% at level 5. `[43:30]`
- Old Age Pension: +3% food security/level; −1% workforce/level; +20% dependent income. `[42:30]`
- Poor Laws political-strength penalty to welfare recipients: −15%/level (max −75%). `[41:02]`
- Wage Subsidies building wage target: +10%/level (functions as minimum wage). `[42:02]`
- Bureaucracy cost per Social Security level (illustrative): ~329 under Old Age Pension vs ~989/level 3 under Poor Laws — Old Age Pension reaches 90% welfare at level 3, saving 2 institution levels vs others. `[46:01]` `[46:32]`
- Pop-to-Pop job switch threshold: ≥10% higher wage than current. `[44:30]`
- SoL/Wealth display rule: individual Pops are always whole numbers; only averages show decimals. `[30:00]`

## Common pitfalls

- **Reading "average annual government wage" as the normal wage.** It includes multipliers; check the wage tooltip's "base wage" field on a government building instead. `[15:30]`
- **Cranking Old Age Pension to maximum.** 150% welfare to unemployed Pops can pay them more than any building can offer, freezing them out of the workforce and bankrupting the treasury. `[43:30]` `[44:00]`
- **Slashing welfare to save money.** Falling SoL generates Radicals from every affected strata; ratchet down gradually. `[48:01]`
- **Pushing wages without checking building profitability.** Higher wages strangle building expansion; the private sector won't build new levels and GDP growth stalls. `[25:00]`
- **Picking Old Age Pension purely for bureaucracy savings.** The −1% workforce per level is a permanent drag on production. `[42:31]`
- **Ignoring per-state pricing.** SoL is computed per state because prices differ; the same Pop type can have different SoL in different states, which drives internal migration. `[24:30]`

## Cheatsheet

1. Get every lower-strata Pop to Wealth 15+ so they consume luxury goods — that's what makes textile/furniture/glassworks profitable.
2. Lift wages via Production Methods that convert Laborers into higher-multiplier Professions (Machinists, etc.), not by brute law changes.
3. Pass Women's Suffrage early — nearly doubling wage-earners per Pop group beats most wage tweaks.
4. Stack SoL modifiers: Public Health Insurance (+0.5/level + pollution mitigation), Food Standardization principle (+1).
5. For welfare, default to Wage Subsidies (no political penalty, free minimum wage). Use Poor Laws only when politics forces it; touch Old Age Pension only with low unemployment and ample treasury.
6. Calibrate Social Security level so welfare ≤ ~100% of normal wage — above that, unemployment becomes structural.

## See also

- [Standard_of_living](https://vic3.paradoxwikis.com/Standard_of_living)
- [Pops](https://vic3.paradoxwikis.com/Pops)
- [Laws](https://vic3.paradoxwikis.com/Laws)
