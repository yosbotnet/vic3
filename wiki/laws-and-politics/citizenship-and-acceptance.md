---
sources:
  - ../../notes/tutorials/06-subjecthood-and-citizenship-laws.md
  - ../../notes/tutorials/10-acceptance-assimilation-and-conversion.md
  - ../../notes/comprehensive-tutorial-2025/02-pops.md
wiki:
  - https://vic3.paradoxwikis.com/Laws
generated_at: 2026-05-16
---

# Citizenship & Acceptance

## What it is
Every Pop has an **Acceptance score** (Culture score + Religion score) that drops it into one of five statuses — violent hostility, cultural eraser, open prejudice, second-class citizen, full acceptance — and that status gates hiring, qualifications, wages, and political strength `[from 10-acceptance-assimilation-and-conversion]`. Two laws decide the formula: the **Citizenship Law** sets the culture half, the **Church-and-State Law** sets the religion half. Picking the wrong pair leaves whole states unhireable for Barracks or Government Admin, bleeds tax through Obstinence, and feeds Cultural Minority Movements that rivals can weaponize via Support Separatism `[from 06-subjecthood-and-citizenship-laws]`.

Patch 1.10 reshaped this layer: Acceptance is now computed from heritage traits, language traits, trait groups, and tradition traits — each Citizenship Law weighs them differently — Multiculturalism was nerfed, and a brand-new Subjecthood law was added for settler/colonial states `[from 06-subjecthood-and-citizenship-laws]`.

## Mechanics
1. **Acceptance status bands** — 0–19 violent hostility, 20–39 cultural eraser, 40–59 open prejudice, 60–79 second-class citizen, 80–100 full acceptance. Decision rule: before unpause, open Society → Statuses and plan industry and recruitment around the map this paints `[from 10-acceptance-assimilation-and-conversion]`.
2. **Citizenship Law sets the Culture score formula** — Each law assigns Acceptance for sharing the primary culture's heritage trait, language trait, trait group, and tradition trait, at different magnitudes `[from 06-subjecthood-and-citizenship-laws]`. Worked example under Racial Segregation: primary +100; both Cultural and Heritage traits +70; Heritage only +50; Cultural only +30; any other culture +10 `[from 10-acceptance-assimilation-and-conversion]`. Decision rule: before enacting, read the tooltip and check how your largest minorities' traits map to the law's brackets.
3. **Church-and-State Law sets the Religion score formula** — State Religion: +25 same / −25 different. Freedom of Conscience: +20 state religion, +15 shared religious trait (e.g. Christian, Muslim), no outsider penalty. Total Separation: an extra +15 over State Religion baseline. Decision rule: if religion alone pushes a state to status 1, weigh switching laws against forcing Conversion `[from 10-acceptance-assimilation-and-conversion]`.
4. **Homeland bonus** — Pops in a state that is their culture's homeland get +10 Acceptance. Subjecthood uniquely stacks **another +30** on top, and the No Colonial Affairs law adds a further +10 `[from 06-subjecthood-and-citizenship-laws]`. Decision rule: expect homeland Pops to sit roughly one tier higher than the same Pops elsewhere `[from 10-acceptance-assimilation-and-conversion]`.
5. **Subjecthood (new in 1.10)** — +100 Authority, −50% Support Separatism Strength/Resistance, −25% Assimilation, +100 Acceptance for primary culture, +30 Acceptance for Pops in their homeland. Decision rule: use when your primary culture is a small minority of your country (settler/colonial states) or to defuse a Cultural Minority Movement before it crosses 50% activism; pair with non-State-Religion or the homeland bonus is wiped out by religious penalties `[from 06-subjecthood-and-citizenship-laws]`.
6. **The nationalist ladder — Ethnostate, National Supremacy, Racial Segregation** — All three give Authority, Primary Culture Fervor, and high Acceptance to culturally-similar Pops, but **penalize** cultures with no shared heritage (or, for Ethnostate, no shared language) by −10 to −20 Acceptance. Decision rule: pick only when most of your population shares a heritage trait group with your primary culture; otherwise expect Obstinence and separatism `[from 06-subjecthood-and-citizenship-laws]`.
7. **Cultural Exclusion** — +50 Authority, −25% Support Separatism Strength, +25% Resistance, +5 Primary Culture Fervor, and **+10 Acceptance even to cultures with no shared heritage or language traits**. Highest Citizenship Law obtainable pre-tech (provided you have no slavery) and the defensive pick that keeps wholly foreign minorities at least minimally hireable `[from 06-subjecthood-and-citizenship-laws]` `[from 10-acceptance-assimilation-and-conversion]`.
8. **Multiculturalism (nerfed in 1.10)** — Requires tier-3 Human Rights tech. −50% Support Separatism Strength, +50% Resistance, **−10 Primary Culture Fervor**, −25% Assimilation, +20 Acceptance to fully foreign cultures. Decision rule: still the best for accepting fully foreign cultures, but from laws alone they now cap at ~Level 3 Open Prejudice — stack with Total Separation and same-religion Pops to push higher `[from 06-subjecthood-and-citizenship-laws]`.
9. **Status effects gate hiring** — Status 1 Pops cannot work military or Government Admin buildings, at −50% qualifications, −30% wages, −30% political strength. Status 2 can work military but not government, still −30% qualifications. Status 3 still loses −10% qualifications and wages. Decision rule: never build Barracks, Government Admin, or qualification-hungry PMs in a state dominated by status 1–2 Pops `[from 10-acceptance-assimilation-and-conversion]`.
10. **Assimilation needs status ≥2 AND non-homeland** — Pops in their own homeland never assimilate, ever, regardless of law `[from 10-acceptance-assimilation-and-conversion]`. Subjecthood still permits Assimilation in tiers 2–5 (just at −25% speed); the **Promote National Values** decree lets you push through even in homelands `[from 06-subjecthood-and-citizenship-laws]`.
11. **Conversion is the stepping stone** — Pops only convert when their religion sits at low acceptance versus the state religion, and it runs 90% slower in unincorporated states. Once converted, the +25 state-religion bonus often lifts them two tiers and unlocks Assimilation. Decision rule: don't reflexively drop State Religion — sometimes keeping it is what makes the jump happen `[from 10-acceptance-assimilation-and-conversion]`.
12. **Tools that accelerate it** — **Promote National Values** decree boosts both assimilation and conversion in a state, but only unlocks once at least one Pop is already shifting. **Religious Schools** institution gives +20% conversion per level, at the cost of boosting the religious Interest Group's political strength `[from 10-acceptance-assimilation-and-conversion]`.
13. **Obstinence from Cultural Minority Movements** — When a minority movement's activism reaches 50%, every state with that culture's Pops enters Obstinence, slashing tax revenue and reducing Institution, Conscription, and Assimilation effects. Decision rule: watch movement activism on the Politics screen; raise Acceptance (often by switching Citizenship Law) before it crosses the threshold `[from 06-subjecthood-and-citizenship-laws]`.
14. **Support Separatism cuts both ways** — Unlocked by Nationalism tech, it raises activism in a rival's minority movement matching your primary culture. Nationalist Citizenship Laws boost your offensive strength but slash your Resistance, leaving your own minorities exposed `[from 06-subjecthood-and-citizenship-laws]`.
15. **Cultural Fervor from laws is fractional** — The Fervor bonus is multiplied by the share of your primary culture's worldwide Pops living in your country, and only applies if you're independent. Decision rule: check domestic vs. worldwide Pop counts before banking on the full +20 from Ethnostate `[from 06-subjecthood-and-citizenship-laws]`.
16. **Spot the icons** — A small icon next to a Pop's religion (converting) or culture (assimilating) means the process is active; hover for monthly flow. Use it to verify acceptance changes are actually moving Pops `[from 10-acceptance-assimilation-and-conversion]`.
17. **Acceptance gates immigration, not just hiring** — Acceptance is also the bouncer on inbound migration. Migration has three gates: (a) a **cultural community** of the migrant's culture must already exist somewhere in your **market** (a community is ≥1 Pop of that culture, and they spawn into your states completely randomly if your culture is present in the market), (b) the migrant must already be **in your market**, and (c) **mass** migration additionally requires the destination give that culture **Acceptance ≥ 30**. Decision rule: a restrictive nationalist Citizenship Law that drops a foreign culture below 30 Acceptance doesn't just hurt hiring — it switches off mass migration of that culture entirely (a European nation under National Supremacy will never receive Chinese mass migrations), so weigh immigration goals against your Citizenship Law choice (2025 comprehensive tutorial, [30:31] / [33:00]).
18. **Immigration attraction is mostly unused arable land** — Mass-migration attraction is driven heavily by available jobs, dominated by **unused arable land** (room for new farms/plantations); this is why the USA is typically the #1 migration target. The **Greener Grass Campaign** decree raises immigration attraction — but decrees cost Authority, which your laws generate, so it competes with every other decree. Decision rule: if you want to *win* the migration tug-of-war (not just clear the Acceptance ≥ 30 gate), you need both job-room and attraction — pairing open arable land with the Greener Grass Campaign decree, while keeping the target cultures above 30 Acceptance (2025 comprehensive tutorial, [32:00] / [34:30]).

## Game numbers & rules of thumb
- Acceptance bands: 0–19 / 20–39 / 40–59 / 60–79 / 80–100 `[from 10-acceptance-assimilation-and-conversion]`.
- Homeland bonus: +10 baseline; Subjecthood adds +30; No Colonial Affairs adds +10 `[from 06-subjecthood-and-citizenship-laws]` `[from 10-acceptance-assimilation-and-conversion]`.
- Religion: State Religion ±25; Freedom of Conscience +20 state / +15 shared trait, no penalty; Total Separation +15 over State Religion `[from 10-acceptance-assimilation-and-conversion]`.
- Status 1 penalties: −50% qualifications, −30% wages, −30% political strength, blocked from military and government admin `[from 10-acceptance-assimilation-and-conversion]`.
- Status 2: −30% qualifications, −20% wages, blocked from government admin `[from 10-acceptance-assimilation-and-conversion]`.
- Status 3: −10% qualifications, −10% wages `[from 10-acceptance-assimilation-and-conversion]`.
- Ethnostate / National Supremacy / Racial Segregation give negative Acceptance to cultures with no shared heritage (or language) traits — only Subjecthood, Cultural Exclusion, and Multiculturalism give positive Acceptance to fully foreign cultures `[from 06-subjecthood-and-citizenship-laws]`.
- Multiculturalism ceiling from laws alone for a fully foreign culture: ~Level 3 Open Prejudice (≈40 culture + up to 15 religion = 55 Acceptance) `[from 06-subjecthood-and-citizenship-laws]`.
- Obstinence is tax-multiplicative: 7.8% Obstinence shown to cause a −19.6% tax penalty in a state `[from 06-subjecthood-and-citizenship-laws]`.
- Conversion is 90% slower in unincorporated states `[from 10-acceptance-assimilation-and-conversion]`.
- Religious Schools institution: +20% conversion per level `[from 10-acceptance-assimilation-and-conversion]`.
- Cultural Fervor scaling: Law value × (your domestic primary-culture Pops ÷ worldwide primary-culture Pops); independence required `[from 06-subjecthood-and-citizenship-laws]`.
- Multiculturalism requires tier-3 Human Rights tech; Cultural Exclusion is the highest law obtainable without tech (no slavery) `[from 10-acceptance-assimilation-and-conversion]`.
- Mass-migration Acceptance gate: a culture needs **Acceptance ≥ 30** at the destination to send mass migrations there (2025 comprehensive tutorial, [33:00]).
- Migration also requires a cultural community (≥1 Pop of the culture, spawns randomly) in your market and the migrant already being in your market (2025 comprehensive tutorial, [30:31]).
- Greener Grass Campaign decree raises immigration attraction (costs Authority, which laws generate) (2025 comprehensive tutorial, [34:30]).

## Strategy & playbook

**Read the map before you legislate.** Open Society → Statuses, Cultures, and Religions on day 1. List your primary culture's share of country Pops, its share of worldwide Pops, and your largest minority cultures with their heritage/language/trait-group/tradition traits versus your primary `[from 06-subjecthood-and-citizenship-laws]`. The same Citizenship Law that turns a homogeneous Prussia into a Fervor engine will detonate Obstinence in a multi-ethnic Austria. The acceptance map is also a hiring map: states dominated by status 1–2 Pops cannot fill Barracks or Government Admin, and qualification-hungry production methods will starve there `[from 10-acceptance-assimilation-and-conversion]`.

**Pick the right Citizenship Law for your demographic shape.** If your primary culture is a small minority of your country (settler/colonial states, conquered empires), Subjecthood is the 1.10 answer — drop State Religion at the same time, or the +30 homeland bonus is cancelled by religious penalties `[from 06-subjecthood-and-citizenship-laws]`. If minorities share heritage or language traits with your primary culture, National Supremacy or Racial Segregation give Fervor without crashing Acceptance. If you must rule large fully-foreign minorities and need stability over Fervor, take Cultural Exclusion as the defensive pre-tech pick (it gives +10 even to no-shared-trait cultures and is the highest non-tech law without slavery) or push to Multiculturalism after Human Rights `[from 06-subjecthood-and-citizenship-laws]` `[from 10-acceptance-assimilation-and-conversion]`.

**Use Religion as the cheap lever.** Religious tier-jumps are often larger than cultural ones for the cost. Before switching Citizenship Laws, check whether the blocker is the religion column: if minority Pops are one State-Religion conversion away from a two-tier jump, **keep** State Religion so Conversion fires, rather than reflexively switching to Freedom of Conscience `[from 10-acceptance-assimilation-and-conversion]`. Once Pops convert, the +25 bonus typically opens Assimilation too, since Assimilation requires status ≥2 in a non-homeland state.

**Run the assimilation pipeline deliberately.** After the first unpause, apply the **Promote National Values** decree in every state showing the convert/assimilate icon — it doesn't unlock on day 1 because no Pop is yet shifting `[from 10-acceptance-assimilation-and-conversion]`. Pair Subjecthood with this decree to push assimilation through homelands, where it normally never happens `[from 06-subjecthood-and-citizenship-laws]`. Add Religious Schools only when you can stomach a stronger Church Interest Group — it's +20% conversion per institution level but it permanently boosts religious political weight on top of State Religion's +30% `[from 10-acceptance-assimilation-and-conversion]`.

**Specialise states to acceptance.** Route low-qualification industry (plantations, mines, basic agriculture) into your low-acceptance states; reserve Barracks, Government Admin, and high-PM industry for states where Pops sit at status 3 or above `[from 10-acceptance-assimilation-and-conversion]`. Track Cultural Minority Movement activism on the Politics screen — if any climbs toward 50%, switch to a more accepting law before Obstinence drains tax revenue across every state holding that culture `[from 06-subjecthood-and-citizenship-laws]`.

## Common pitfalls
- Assuming Multiculturalism still gives every culture +75 Acceptance — post-1.10 foreign cultures bottom out at Open Prejudice from laws alone `[from 06-subjecthood-and-citizenship-laws]`.
- Stacking Ethnostate / National Supremacy / Racial Segregation over large foreign minorities and triggering cascading Cultural Minority Movements and nationwide Obstinence `[from 06-subjecthood-and-citizenship-laws]`.
- Running Subjecthood while keeping State Religion — religious penalties cancel the +30 homeland Acceptance bonus you switched laws to get `[from 06-subjecthood-and-citizenship-laws]`.
- Picking Ethnostate expecting the full +20 Fervor when most of your primary culture lives abroad — you only get the fraction that's home `[from 06-subjecthood-and-citizenship-laws]`.
- Building Barracks or Government Admin in a state dominated by status 1 Pops — hiring stalls and battalions never fill `[from 10-acceptance-assimilation-and-conversion]`.
- Upgrading a PM that requires qualified professions (e.g. Machinists) in a low-acceptance state — Pops fail to qualify; multiple levels at a lower PM beat fewer levels stuck on a higher one `[from 10-acceptance-assimilation-and-conversion]`.
- Treating low-acceptance wage penalties as a profit win — those Pops then under-consume in your market `[from 10-acceptance-assimilation-and-conversion]`.
- Dropping State Religion reflexively when Conversion would have delivered the +25 two-tier jump `[from 10-acceptance-assimilation-and-conversion]`.
- Forgetting homeland Pops never assimilate — switching Citizenship Laws will not move them culturally, only religiously (unless Subjecthood + Promote National Values is active) `[from 10-acceptance-assimilation-and-conversion]` `[from 06-subjecthood-and-citizenship-laws]`.
- Forgetting Support Separatism cuts both ways: nationalist laws boost your offensive strength but slash your Resistance, leaving your own minorities exposed `[from 06-subjecthood-and-citizenship-laws]`.
- Treating Religious Schools as free conversion speed — it inflates the religious Interest Group's political weight `[from 10-acceptance-assimilation-and-conversion]`.

## See also
- **In this wiki:**
  - [Passing laws](passing-laws.md)
  - [Cultural fervor](cultural-fervor.md)
  - [Political movements](political-movements.md)
  - [Slavery abolition](slavery-abolition.md)
  - [Standard of living](../pops/standard-of-living.md)
- **Official wiki:**
  - [Laws](https://vic3.paradoxwikis.com/Laws)
  - [Pops](https://vic3.paradoxwikis.com/Pops)
  - [Political_movements](https://vic3.paradoxwikis.com/Political_movements)

## Sources
- `notes/tutorials/06-subjecthood-and-citizenship-laws.md` — Subjecthood and Citizenship Laws (1.10+)
- `notes/tutorials/10-acceptance-assimilation-and-conversion.md` — Acceptance, Assimilation, and Conversion
- `notes/comprehensive-tutorial-2025/02-pops.md` — chapter "2. Pops" of "The Comprehensive Victoria 3 Tutorial (2025) | Iberian Twilight" (Tarkusarkusar, 2025-12-16); migration gates and the Acceptance ≥ 30 mass-migration threshold.
