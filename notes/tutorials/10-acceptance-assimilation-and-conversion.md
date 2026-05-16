---
source_transcript: ../../transcripts/tutorials/10-acceptance-assimilation-and-conversion.md
source_video: https://www.youtube.com/watch?v=ojTYyYRsNUk
generated_at: 2026-05-16
---

# Acceptance, Assimilation, and Conversion

**Source:** [Acceptance Assimilation and Conversion Tutorial in Victoria 3](https://www.youtube.com/watch?v=ojTYyYRsNUk) (24:02 runtime)

## Summary
Every Pop has an Acceptance score (Culture score + Religion score) that places them in one of five statuses, from violent hostility to full acceptance. Status drives hiring eligibility, qualifications, wages, and political strength, so low-acceptance Pops cripple production in states where they dominate. Assimilation (Culture change) and Conversion (Religion change) are the long-game tools — alongside Citizenship and Church-and-State Laws — for moving Pops up the ladder before you can reach Multiculturalism.

## Core mechanics
1. **Acceptance score = Culture score + Religion score** — Both contributions are added, then mapped to one of five statuses: 0–19 violent hostility, 20–39 cultural eraser, 40–59 open prejudice, 60–79 second-class citizen, 80–100 full acceptance. DECISION RULE: before unpause, open Society → Statuses, see which Pops fall where, and plan production/laws around it. `[01:30]` `[02:03]`
2. **Citizenship Law sets the Culture score formula** — Under Racial Segregation: Primary culture +100; shares both Cultural and Heritage traits +70; Heritage only +50; Cultural only +30; any other culture +10. DECISION RULE: read each candidate Citizenship Law's tooltip to see exactly how it will redistribute your Pops across statuses before enacting. `[02:30]` `[05:02]`
3. **Church-and-State Law sets the Religion score formula** — State Religion: +25 if state religion, −25 if not. Freedom of Conscience: +20 state religion, +15 if shares a religious trait (e.g. Muslim, Christian), no penalty for outsiders. Total Separation: gives an extra +15 vs. State Religion. DECISION RULE: if a state's penalty pushes Pops to status 1, evaluate switching laws OR forcing Conversion. `[06:01]` `[15:31]` `[18:00]`
4. **Homeland bonus** — Pops living in a state that is a homeland for their culture get +10 acceptance. DECISION RULE: expect Pops in their own homelands to sit one tier higher than the same Pops elsewhere — plan industry there accordingly. `[06:31]` `[07:01]`
5. **Status effects gate hiring and productivity** — Violent hostility: cannot work military or government admin buildings, −50% qualifications, −30% wages, −30% political strength. Cultural eraser: can work military but not government, still −30% qualifications. DECISION RULE: never build Barracks, Government Admin, or high-PM industry in a state dominated by status-1 Pops. `[08:33]` `[09:00]` `[11:01]`
6. **Assimilation requires status 2+ AND non-homeland** — Pops in their own homeland never assimilate, regardless of status. Elsewhere, they need at least cultural eraser. DECISION RULE: to assimilate a minority, first raise their acceptance to ≥20 in states that are not their homeland. `[12:00]` `[12:31]` `[19:31]`
7. **Conversion requires low religious acceptance** — Pops only convert if their current religion sits at low acceptance vs. the state religion; conversion is 90% slower in unincorporated states. DECISION RULE: use Conversion as a stepping stone — once converted, the +25 state-religion bonus often lifts Pops two tiers and unlocks Assimilation. `[13:00]` `[15:00]` `[19:31]`
8. **Promote National Values decree** — Boosts assimilation and conversion in a state, but only selectable in states where Pops are already assimilating/converting (so usually unavailable on day 1). DECISION RULE: after the first unpause, apply it in every state that has the conversion/assimilation icon. `[13:31]` `[17:01]`
9. **Religious Schools institution** — +20% conversion, scaled by institution level. Cost: empowers the religious Interest Group (+10% political strength on top of State Religion's +30%). DECISION RULE: enact only when you accept giving the Church real political weight; otherwise rely on decree + law switches. `[13:00]` `[20:01]`
10. **Spot conversion/assimilation in progress** — A small icon next to a Pop group's religion (converting) or culture (assimilating) means the process is active; hover to see monthly flow. DECISION RULE: use this to verify your acceptance changes are actually producing movement before committing further. `[13:31]` `[14:00]`

## Game numbers & rules of thumb
- Acceptance status bands: 0–19 / 20–39 / 40–59 / 60–79 / 80–100. `[02:03]`
- Racial Segregation Culture bonuses: primary +100, both traits +70, heritage only +50, cultural only +30, any culture +10. `[05:02]`
- State Religion: ±25; Freedom of Conscience: +20 state / +15 shared trait, no penalty; Total Separation: +15 over State Religion baseline. `[06:01]` `[18:00]`
- Homeland bonus: +10. `[06:31]`
- Status 1 (violent hostility): −50% qualifications, −30% wages, −30% political strength, blocked from military and government admin buildings. `[08:33]` `[10:00]`
- Status 2 (cultural eraser): −30% qualifications, −20% wages; can work military but not government. `[11:01]` `[19:01]`
- Status 3 (open prejudice): −10% qualifications, −10% wages. `[19:01]`
- Status 4 vs 5 under Racial Segregation: wages +5% vs +15%. `[11:31]`
- Conversion is 90% slower in unincorporated states. `[13:00]`
- Religious Schools: +20% conversion, scales with institution level. `[13:00]`
- Multiculturalism requires the tier-3 Human Rights technology; it accepts almost everyone. `[22:01]`
- Cultural Exclusion is the highest Citizenship Law obtainable without tech (provided you have no slavery); under it, status-1 Pops become hireable in Barracks. `[22:31]`

## Common pitfalls
- Building Barracks or Government Admin in a state where the majority sits at status 1 — hiring stalls and battalions/admin can never fill. `[08:33]` `[09:00]`
- Upgrading Production Methods that require qualified professions (e.g. Machinists) in a low-acceptance state — Pops fail to qualify and the PM cannot hire. Multiple levels on a lower PM beat fewer levels stuck on a higher one. `[09:30]` `[21:30]`
- Treating low wages from low acceptance as a profit boost — those Pops then spend less in your economy. `[10:00]`
- Dropping State Religion reflexively: sometimes keeping it lets minority Pops convert and gain +25, jumping two tiers; switching laws may move them only within the same tier. `[17:30]` `[18:30]`
- Forgetting that homeland Pops never assimilate — switching laws will not move them culturally, only religiously. `[12:31]`
- Treating Religious Schools as free conversion speed — it inflates the religious Interest Group's political weight. `[20:01]`

## Cheatsheet
1. Before unpause: open Society → Statuses, Cultures, Religions; identify which states are dominated by status 1–2 Pops.
2. Read your current Citizenship Law tooltip and check the per-status modifiers; aim for Cultural Exclusion pre-tech, Multiculturalism after Human Rights.
3. If a state's minority is blocked only by religion, prefer keeping State Religion so Conversion delivers +25 (often a two-tier jump); only switch to Freedom of Conscience / Total Separation if Conversion is impossible or undesired.
4. After first unpause, apply Promote National Values in every state showing the convert/assimilate icon.
5. Specialise states: route agriculture (low-qualification) to low-acceptance states; reserve industry and military builds for states where Pops sit at status 3+.
6. Use Religious Schools only when you can tolerate a stronger religious Interest Group.

## See also
- [Pops](https://vic3.paradoxwikis.com/Pops)
- [Laws](https://vic3.paradoxwikis.com/Laws)
- [Decrees](https://vic3.paradoxwikis.com/Decrees)
