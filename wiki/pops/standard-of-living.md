---
sources:
  - ../../notes/tutorials/04-standard-of-living-wages-and-wealth.md
  - ../../notes/comprehensive-tutorial-2025/01-economics.md
  - ../../notes/comprehensive-tutorial-2025/02-pops.md
wiki:
  - https://vic3.paradoxwikis.com/Standard_of_living
generated_at: 2026-05-16
---

# Standard of Living, Wages, and Wealth

## What it is

Standard of Living (SoL) is a per-Pop score derived almost entirely from a Pop's Wealth level, nudged up or down by health, pollution, and a handful of Power Bloc principles. Wealth in turn is driven by Wages, and Wages decide which categories of goods a Pop can buy in their weekly basket of needs. That basket — not trade routes, not building inputs — is the most reliable demand sink in the game, which is why SoL is simultaneously the morality dial AND the GDP dial.

You should care from the first decade. Until your lower strata cross the Wealth threshold that unlocks luxury goods, you have no customers for textiles, furniture, or glass; until you have customers, those building chains stay unprofitable and the private sector won't expand them. Conversely, every wage you raise eats into building profitability, so the system asks you to balance "rich enough to consume" against "cheap enough to keep building." Welfare, suffrage, citizenship, and Production Method choices are all really SoL levers in disguise.

## Mechanics

1. **GDP-counted demand vs. real demand** — Of the five consumption sinks (building inputs, Pop needs, trade centers, goods transfers, unused goods) only building inputs are subtracted from GDP. Pop needs are the stable, no-brokering sink that compounds with your population. Build your economy so wealthy Pops absorb your luxury output — that revenue is sticky in a way trade-route revenue is not.

2. **Wealth unlocks the basket of needs** — A Pop's Wealth level controls both how many categories of goods they buy (basic food, luxury food, clothing, household items, services, free movement, etc.) AND how expensive the picks within each category are. Until the lower strata cross the luxury threshold, factories making luxury goods have no domestic market; pushing their Wealth past it is the unlock event for the second half of your industrial chain.

3. **Wealth equilibrium loop** — Each week the game tests whether a Pop's net income (income − needs cost − taxes) can sustain the basket of the NEXT Wealth level; if yes they climb, if their current basket is unaffordable they fall. The volatile term is the needs cost because market prices move weekly. To promote a Pop tier, you must cheapen the goods in the tier ABOVE them, not the tier they already buy.

4. **Base wage vs. normal wage** — Base wage is set per building per state and represents the lowest-paid worker's pay; understaffed, still-profitable buildings raise it automatically. Normal wage is the average of base wages across all incorporated, non-government buildings and sets both government wages and the welfare threshold. Read the current normal wage by hovering the wages field on a government building (e.g. a barracks) — the "average annual government wage" headline includes profession multipliers and is the wrong number.

5. **Profession wage multipliers** — Every profession scales off the building's base wage by a fixed multiplier (Laborers ×1, Machinists ×1.5, Farmers ×2, Bureaucrats ×4, etc.). The building can only move the base — but you can change which professions live inside it. To lift a particular Pop group's Wealth, swap to a Production Method that converts Laborers into a higher-multiplier profession instead of raising wages by law.

6. **Wage modifiers from laws** — Citizenship and religion laws apply percentage modifiers to individual Pop wages. National Supremacy rewards tier-5 acceptance and punishes everything below; Ethnostate gives the biggest top-end bonus and the biggest penalty to outsiders; State Religion is ±10% by faith. In a homogeneous country, Ethnostate or National Supremacy maxes wages; in a diverse one, Multiculturalism merely avoids the penalty. Assimilation and conversion are therefore wage tools, not just identity policy.

7. **Workforce ratio beats wage rates** — Wealth is split between workers and dependents in a Pop group, and only ~25% of a Pop works by default. Women's Suffrage adds +15% workforce ratio, nearly doubling earners; Child Labor laws boost dependent income. Passing Women's Suffrage is usually a bigger SoL boost than any PM tweak. Avoid Old Age Pension if you can't spare the −1% workforce per level.

8. **Direct SoL modifiers (not Wealth)** — A few sources add SoL outside the Wealth loop: Public Health Insurance gives +0.5 SoL/level to everyone and shaves the pollution penalty; Private Health Insurance gives the same +0.5/level but only to upper strata; the Food Standardization Power Bloc principle gives +1 SoL flat. Per-Pop SoL is always rounded DOWN to a whole number — only the strata averages show decimals — so a half-point modifier sometimes does nothing and sometimes everything.

9. **Welfare payment threshold** — Social Security sets a percentage of normal wage; any Pop earning below (threshold × normal wage) receives the gap, paid weekly. Unemployed Pops have wage = 0 and so collect the full threshold amount. Predict next week's bill with ((threshold × normal_wage) − pop_wage) / 52 × workforce; the figure displayed this week is for last week's gap.

10. **Choosing a welfare law** — Poor Laws are the cheapest to pass but inflict −15% political strength per institution level on recipients (max −75%), neutering the clout you just paid for. Wage Subsidies have the same welfare schedule, no political penalty, AND +10% building wage target per level (a stealth minimum wage). Old Age Pension scales 30%→150% and gives bigger food security, but costs −1% workforce per level and can pay unemployed Pops more than any factory will. Default to Wage Subsidies; reach for Old Age Pension only with low unemployment and a fat treasury.

11. **Job-switching friction blocks reemployment** — A Pop only switches jobs when the new wage is at least 10% above current effective income. If welfare overpays unemployed Pops, no realistic building wage can lure them back, and the unemployment becomes structural. Calibrate welfare so it stays roughly below normal wage; never raise the Social Security level speculatively.

12. **SoL feedback into politics and migration** — Each strata has a minimum expected SoL that rises with literacy and with ideologies like Socialism. Below expected → Radicals; above → Loyalists. SoL also drives migration attraction: states with higher SoL than their neighbors pull Pops in. Slashing welfare is therefore a double cost — a wave of Radicals AND a reversed migration current.

13. **SoL is the beating heart of the economy, not just a morality score** — Each SoL level, a Pop buys that level's goods and then spends any leftover money trying to climb to the next (each level consumes more goods). Richer Pops therefore buy more, which directly raises the profits of the buildings selling to them — the demand side of the loop that lets the private sector expand. Decision rule: treat raising SoL as an *economic* lever (it grows building profits and the Investment Pool), not only a way to suppress Radicals; the two levers that lift it are cheaper consumed goods and better-paying jobs (2025 comprehensive tutorial, [24:31]). Of the two, **better jobs is the stronger lever** — the game weights job income as more important — so a PM swap that converts Laborers into higher-multiplier professions usually beats chasing cheaper inputs (2025 comprehensive tutorial, [25:00]).

14. **Peasants drag down state SoL and wages** — Peasants live off subsistence, pay little tax, buy few goods, and supply few goods to the market; worse, their low SoL drags down a state's *average* SoL, which in turn depresses the wages every building in that state pays. The fix is to build jobs that pull them off the land — peasants happily take better-paying factory/farm work as soon as it exists, and while peasants remain you will never struggle to staff new buildings. Decision rule: read a state full of peasants as fuel, not as a problem; an economy that *stalls because it ran out of peasants to employ* is a sign you did it right — at that point grow via trade, not more domestic buildings (2025 comprehensive tutorial, [10:32]).

15. **Slaves — 2× workforce but a long-term trap** — Importing slaves makes their dependents work too, so you get roughly twice the workers of a free Pop, and they pay no taxes: the wage they'd have earned becomes excess profit for the building's owners instead. But the model degrades over time — slaves have low SoL that drags state wages and breeds Radicals, and they cannot fill the advanced jobs (Machinists, Engineers) that better Production Methods demand. Decision rule: slavery is a short-term profit cheat that caps your industrial ceiling; plan to abolish it before your PM ladder needs qualified labour the slaves can't supply (2025 comprehensive tutorial, [22:01]).

16. **Subsistence output is the peasants' "fake money"** — The mechanical reason peasants (mechanic 14) barely touch the real economy: no one actually pays them. The game grants them money from *subsistence output* — money that isn't produced by any building or paid out of any budget — purely so they have something to spend, and they then spend it on a tiny basket of goods that aren't genuinely produced or sold either. Tarkus's example: ~600,000 peasants in a state consume only 6 of the 516 grain on the market. This is why "converting" peasants means building real jobs — only a wage-paying job plugs them into the priced market as both earners and consumers (2025 comprehensive tutorial, [09:30]).

17. **Literacy and qualifications — three effects, one decision rule** — Qualifications are generated for every Pop weekly, and the rate scales with the Pop's literacy: more literate Pops accrue more qualifications, which is what lets them fill the advanced jobs (Machinists, Engineers) that better Production Methods demand (2025 comprehensive tutorial, [28:00]). Literacy itself does three distinct things to a Pop: (a) it generates those qualifications, (b) it RAISES the Pop's minimum required SoL (so a literate Pop is harder to keep out of Radicalism — cf. mechanic 12), and (c) it LOWERS the Pop's birth rate (2025 comprehensive tutorial, [28:30]). Decision rule: above roughly 40% average literacy you can essentially ignore qualifications entirely — there are only three job tiers, and everyone can fill even the most advanced of them, so the mechanic stops mattering. Only worry about qualifications in genuinely low-literacy situations (e.g. playing as China); most nations a new player picks already sit above 40% (2025 comprehensive tutorial, [29:02]). Literacy is still worth raising regardless, because national average literacy is what drives your technology research speed — accept the higher SoL demand and fewer kids as the price.

## Game numbers & rules of thumb

- Luxury goods unlock at Wealth level 15. `[from 04-standard-of-living-wages-and-wealth]`
- Building base wage rises ~10% every 2 weeks when understaffed and still profitable. `[from 04-standard-of-living-wages-and-wealth]`
- Profession wage multipliers: Laborers ×1, Machinists ×1.5, Farmers ×2, Bureaucrats ×4. `[from 04-standard-of-living-wages-and-wealth]`
- Laborer dependent income = 0.5 × workforce income; Child Labor Allowed adds +30% dependent income. `[from 04-standard-of-living-wages-and-wealth]`
- Women's Suffrage: +15% workforce ratio (default base ~25%). `[from 04-standard-of-living-wages-and-wealth]`
- National Supremacy: +20% wages at tier-5 acceptance. `[from 04-standard-of-living-wages-and-wealth]`
- Ethnostate: up to +25% wages; largest non-tier-5 penalty in the law tree. `[from 04-standard-of-living-wages-and-wealth]`
- State Religion: ±10% wages; Freedom of Conscience: ±5%. `[from 04-standard-of-living-wages-and-wealth]`
- Public Health Insurance: +0.5 SoL/level for all Pops; pollution penalty −60% at level 4. `[from 04-standard-of-living-wages-and-wealth]`
- Private Health Insurance: +0.5 SoL/level, upper strata only. `[from 04-standard-of-living-wages-and-wealth]`
- Food Standardization Power Bloc principle (level 3): +1 SoL to all Pops. `[from 04-standard-of-living-wages-and-wealth]`
- Social Security welfare schedule: level 1 = 20% of normal wage, +20%/level, level 5 = 100%. `[from 04-standard-of-living-wages-and-wealth]`
- Old Age Pension: 30% at level 1, 150% at level 5; +3% food security/level; −1% workforce/level; +20% dependent income. `[from 04-standard-of-living-wages-and-wealth]`
- Poor Laws: −15% political strength per institution level to recipients (max −75%). `[from 04-standard-of-living-wages-and-wealth]`
- Wage Subsidies: +10% building wage target per level (effective minimum wage). `[from 04-standard-of-living-wages-and-wealth]`
- Old Age Pension reaches 90% welfare at institution level 3 vs. level 5 elsewhere — saves ~2 institution levels of bureaucracy. `[from 04-standard-of-living-wages-and-wealth]`
- Pop-to-Pop job switch threshold: new wage must be ≥10% above current. `[from 04-standard-of-living-wages-and-wealth]`
- Per-Pop SoL and Wealth are always rounded to whole numbers; only averages show decimals. `[from 04-standard-of-living-wages-and-wealth]`

## Strategy & playbook

The opening priority is to drag every lower-strata Pop across Wealth 15. Until that line is crossed, your textile mills, furniture workshops, and glassworks have no domestic customer base and the private sector won't fund their next levels. The fastest tools for this are NOT wage edicts — they are Production Method swaps that convert Laborers into Machinists or higher-multiplier professions, plus Women's Suffrage to nearly double the share of Pops earning a wage. A single suffrage law usually moves more SoL than a year of fiddling with individual PMs.

Treat citizenship and religion laws as wage policy. If your country is overwhelmingly primary-culture and primary-faith, Ethnostate plus State Religion is a free +20–25% wage stack with no construction cost. If you're diverse, Multiculturalism only neutralises the penalty — the real bonus comes from assimilating and converting Pops into the favoured groups. Plan citizenship reform around your demographics, not around ideology.

Once the lower strata are buying luxuries, layer the direct SoL modifiers. Public Health Insurance scales cleanly (+0.5 per level to everyone, plus pollution mitigation), and the Food Standardization Power Bloc principle is a free +1 SoL if your bloc can afford to slot it. Because per-Pop SoL is rounded down, these half-points matter most when they push a Pop across an integer threshold; check the SoL heat-map after each change to see which states actually moved.

Welfare is where most campaigns either bleed money or generate Radicals. Default to Wage Subsidies: same payment schedule as Poor Laws, no political-strength penalty on recipients, and a built-in +10%/level minimum wage that lifts SoL automatically. Use Poor Laws only when the political situation forbids passing anything else. Reach for Old Age Pension only with low unemployment AND treasury headroom — at high levels it pays unemployed Pops more than factories can offer, and the 10% job-switch threshold means those Pops never come back. Keep welfare below roughly 100% of normal wage as a hard rule.

Finally, remember that SoL is a politics and migration engine, not just a number. Above-expected SoL generates Loyalists and pulls migrants in; below-expected generates Radicals and pushes them out. That means SoL changes have multi-year tails — never slash welfare in one step, and never raise it speculatively without checking the next-payment formula first.

**Diagnostic workflow for radicalizing pops:** open Population → click the radicalizing pop → Economy tab. Read net income (income − expenses), then check spend breakdown to find the most-expensive need. To raise SoL, either (a) remove consumption tax on a good they buy heavily, (b) build local production of an overpriced need, or (c) upgrade the employing building's PM to convert Laborers into higher-wage professions. `[from beginner-tutorial ep03]`

**Migration Attraction mapmode** shows per-state attraction (SoL, available arable land, Frontier Colonization, etc.). High-attraction states draw internal migration and trigger Mass Migration events. Reading this map tells you where labor will arrive and where the AI's settler nations are about to consume pops you wanted. `[from beginner-tutorial ep15]`

## Common pitfalls

- Reading the "average annual government wage" headline as the normal wage — it bakes in profession multipliers. Hover the base wage field on a barracks instead.
- Cranking Old Age Pension to maximum: 150% welfare to unemployed Pops can exceed any building's offer, freezing them out of work and draining the treasury.
- Slashing welfare in a single step to save money — the SoL drop spawns Radicals across every affected strata.
- Pushing wages without watching building profitability; the private sector stops expanding and GDP growth stalls.
- Picking Old Age Pension purely for its bureaucracy efficiency — the −1% workforce per level is a permanent production drag.
- Ignoring per-state pricing: SoL is computed per state, so the same Pop type can sit at different SoL across your country and quietly drive internal migration.
- Forgetting that per-Pop SoL is rounded down — a +0.5 modifier sometimes shows nothing and sometimes flips an entire strata.

## See also

- **In this wiki:**
  - [laws-and-politics/citizenship-and-acceptance.md](../laws-and-politics/citizenship-and-acceptance.md)
  - [laws-and-politics/passing-laws.md](../laws-and-politics/passing-laws.md)
  - [laws-and-politics/political-movements.md](../laws-and-politics/political-movements.md)
  - [economy/building-balance-sheet.md](../economy/building-balance-sheet.md)
  - [economy/companies.md](../economy/companies.md)
  - [diplomacy/power-blocs.md](../diplomacy/power-blocs.md)
- **Official wiki:**
  - [Standard_of_living](https://vic3.paradoxwikis.com/Standard_of_living)
  - [Pops](https://vic3.paradoxwikis.com/Pops)
  - [Laws](https://vic3.paradoxwikis.com/Laws)

## Sources

- `notes/tutorials/04-standard-of-living-wages-and-wealth.md` — [Standard of Living, Wages, and Wealth Tutorial in Victoria 3](https://www.youtube.com/watch?v=fvHnfklJCvY)
- `../../notes/comprehensive-tutorial-2025/01-economics.md` — The Comprehensive Victoria 3 Tutorial (2025), Tarkusarkusar
- `../../notes/comprehensive-tutorial-2025/02-pops.md` — The Comprehensive Victoria 3 Tutorial (2025), Tarkusarkusar
