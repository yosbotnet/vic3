---
sources:
  - ../../notes/tutorials/05-how-to-pass-laws.md
wiki:
  - https://vic3.paradoxwikis.com/Laws
generated_at: 2026-05-16
---

# Passing Laws (1.12+)

## What it is

Law enactment is the engine that converts your political position into structural change — production methods you can build, taxes you can collect, armies you can raise, pops you can recruit. In 1.12 it is no longer a single percentage roll: it is a four-start-condition, three-phase, four-outcome checkpoint process with a Negotiation layer that lets you trade Amenability and promises for permanent Amendments. The strategic problem is not "what does this button do" but "in what order do I touch Government, Interest Groups, Movements, Legitimacy, and Authority so the law lands before a revolution does?"

## Mechanics

1. **Start condition** — You can begin an enactment only if at least one holds: (a) a supporting IG is in Government, (b) the country leader's ideology endorses the law, (c) a supporting Political Movement is at >=25% activism, or (d) a Law Commitment treaty article from a higher-ranked country pushes Success above 0. DECISION RULE: if none apply, the cheapest fix is usually swapping a Government IG; leader replacement is second; growing movement activism is slow; treaty-based starts only work if a higher-ranked partner will sign.

2. **Legitimacy gate** — A Government below 25 Legitimacy cannot start any enactment, except via a >=25% supporting Movement. DECISION RULE: do not bolt a neutral IG into Government purely to negotiate if it will drop you below 25 Legitimacy — you will lock yourself out of all enactments.

3. **Three phases, four outcomes** — Every enactment passes through Introduction, Consideration, and Adoption checkpoints. Each checkpoint rolls one of: Success (advance/pass), Advance (helpful event/bonus), Debate (neutral choice event), Stall (harmful event/penalty). A Stall that reduces Success to 0% is a Setback; 3 Setbacks fail the law (4 with Creative Legislature lvl 3). DECISION RULE: the failure mode you actually manage is Setbacks, not Success percentage — keep Success buffered well above 0 so a single bad event can't zero you.

4. **Success chance** — Sum of clout from supporting IGs in Government + leader endorsement bonus (+5% per oppose->neutral->endorse step) + supporting Movement support if activism >=25%. DECISION RULE: before clicking enact, swap the highest-clout supporting IG into Government; a small leader bonus is worth less than a clout-heavy supporter.

5. **Stall chance** — Sum of clout from every opposing IG (in or out of Government), modified by Approval: Angry x1.5, Unhappy x1.0, Neutral x0.5, Happy/Loyal x0. Marginalised IGs contribute 0. Opposing Movement at >=25% activism adds its support. DECISION RULE: lowering opposing IG clout is hard; raising their Approval to Happy/Loyal (x0) is the lever you actually control.

6. **Enactment speed** — Default 100 days between checkpoints. Government Principles = 200 days; Distribution of Power, Economic System, Slavery = 150 days. 100% excess Authority gives -25% enactment time. DECISION RULE: speed beats elegance when a Movement is radicalising — pad excess Authority before starting any law that touches an active Movement's grievance.

7. **Revolution race** — Movement activism drifts toward a target; at 75% the Movement starts a revolution that progresses toward current activism. Passing laws the Movement endorses lowers the target. DECISION RULE: identify the Movement's endorsed laws and pass the cheapest ones first to bleed activism before attempting the contested one.

8. **Happiness change from enactment** — IGs gain or lose 5 Approval per step of law-distance, capped at +/-10. Land Reform uses x1.5 cap 15; Government Principles and Slavery use x2 cap 20. Approval shifts are locked during enactment and drift back to baseline over 60 months. DECISION RULE: chain enactments inside the 60-month drift window — pass a law an opposing IG loves, then immediately enact the law they hate while they're still Happy (x0 Stall multiplier).

9. **Agitators & IG leaders** — Invited agitators can be installed as IG leaders, rewriting that IG's ideology and potentially breaking inconvenient Political Parties. Requires the IG to be both pressured by the agitator's Movement and in Government. Female agitators need Women's Suffrage. DECISION RULE: use agitators surgically to fracture a Party that locks two IGs into the same vote, or to flip an IG's stance on your target law.

10. **Negotiation — stance shift** — Negotiate with a Neutral in-Government IG to flip them Supporting (their clout adds to Success). Negotiate with an Opposing IG (need not be in Government) to flip them Neutral (their clout no longer adds to Stall). DECISION RULE: negotiation order matters — each completed deal shifts percentages and stacks outstanding promises that lower other IGs' Amenability, so do the cheapest/highest-leverage swaps first.

11. **Amenability bands** — 0–24 refuses entirely; 25–49 costs and effects doubled; 50–74 normal; 75–100 halved. DECISION RULE: target 75+ before committing to expensive Amendments; if an IG is stuck in 25–49 and the demand is steep, negotiate someone else first or skip them.

12. **Negotiation outcomes** — Each negotiation offers 3 commitment options plus a back-out. Amendments are permanent passive effects on the law for as long as it's active. Journal-Entry promises are time-bound build/policy commitments (e.g., build X levels of Y in 10 years). Backing out costs Amenability and Approval. DECISION RULE: take Amendments whenever offered — they're permanent. Only accept Journal promises that match what you were going to build anyway.

13. **Failing a promise** — All IGs lose 5 Amenability and you lose 5 Legitimacy for 5 years; +20% radicals from the failing IG; that IG specifically takes -10 Amenability for 15 years and -5 Approval. Delay (+3 years, -1 Approval) is available once. DECISION RULE: a missed promise scars the IG for 15 years — never accept a build commitment unless construction queue and resources already cover it.

## Game numbers & rules of thumb

- Leader endorsement: +5% Success per oppose->neutral->endorse step `[from 05-how-to-pass-laws]`.
- Movement threshold to affect Success/Stall or enable a no-supporter start: 25% activism `[from 05-how-to-pass-laws]`.
- Law Commitment treaty Success bonus: +5% per rank gap, and only if the partner outranks you `[from 05-how-to-pass-laws]`.
- Checkpoint cadence: 100 days default; 200 for Government Principles; 150 for Distribution of Power, Economic System, Slavery `[from 05-how-to-pass-laws]`.
- Setbacks-to-fail: 3 (4 with Creative Legislature lvl 3) `[from 05-how-to-pass-laws]`.
- Excess Authority bonus: -25% enactment time at 100% excess `[from 05-how-to-pass-laws]`.
- Stall Approval multipliers: Angry x1.5, Unhappy x1.0, Neutral x0.5, Happy/Loyal x0 `[from 05-how-to-pass-laws]`.
- Approval shift cap: +/-10 standard, +/-15 Land Reform, +/-20 Government Principles & Slavery; drift back over 60 months `[from 05-how-to-pass-laws]`.
- Revolution trigger: Movement at 75% activism `[from 05-how-to-pass-laws]`.
- Marginalised IG: drops at <4% clout, recovers at 5% (2.5% in a Party); marginalised IGs add 0 everywhere `[from 05-how-to-pass-laws]`.
- End-of-debate scaling: if Success + Advance + Stall > 100, excess scales down proportionally `[from 05-how-to-pass-laws]`.
- Amenability base: 50, plus modifiers. Legitimacy contribution ≈ Legit x 0.35 + 5 (≈14 at 25 Legit, 40 at 100). Clout contribution favours small IGs (max +12 at 5% clout). Approval contribution = Approval x 2.5. Movement pressure contribution caps at +/-35 (cap ≈ 58% pressure). "Likely to pass" gives +5/+10/+25 at Success leads of 2/8/15; "will fail" gives +5/+10/+20 at Stall leads of 5/10/15 over (Success + that IG's clout). A "could turn the tide" opposer gets -5. An Opposing IG that's still Happy at start becomes effectively unnegotiable (-500) `[from 05-how-to-pass-laws]`.

## Strategy & playbook

**Engineer the start before opening the screen.** The single biggest mistake is clicking enact with the wrong Government. Walk the checklist in order: is a supporting IG already in Government? If not, can you swap one in without dropping Legitimacy below 25? If not, can your country leader endorse? If not, is there a supporting Movement near 25% activism you can nudge? Only fall back on a Law Commitment treaty if a higher-ranked partner will actually sign — equal or lower rank gives zero Success help. The start condition is free leverage; spending in-game weeks setting it up beats fighting a 5% Success enactment for years.

**Pre-warm opposing IGs, then chain.** The Stall formula treats Happy/Loyal IGs as x0 — they vanish from opposition for the duration of the enactment. The post-enactment Approval shift lasts 60 months before drifting back. The play is to pass a small popular-with-the-opposition law first (a production-method unlock they like, a tariff change, anything cheap they endorse), then immediately enact the law they would normally fight. While they're still Happy from the warm-up, their entire clout pool contributes 0 to Stall. This is why "what order do I pass these in" is the real game.

**Race the revolution with Authority, not Success.** When a Political Movement is climbing toward 75% activism, optimising Success percentage is the wrong axis — you need to compress total enactment time. Pad excess Authority to 100% for the -25% bonus; pick smaller laws over Government Principles / Slavery / Economic System / Distribution of Power when possible (those take 150–200 days per checkpoint instead of 100). If the contested law has a Movement endorsing a different law, pass that other law first — every passed endorsement bleeds the Movement's target activism, often more efficiently than trying to outrun it.

**Negotiate in dependency order.** Each completed negotiation moves Success and Stall and stacks outstanding promises that drag every IG's Amenability down. Sort the IG list by Amenability before starting and hit 75+ targets first for half-cost Amendments. Prefer Amendments over Journal-Entry promises — Amendments are permanent passive effects bolted to the law, Journal promises are 10-year timebombs that cost 5 Legitimacy for 5 years and -10 IG Amenability for 15 years if you miss them. Only sign a build promise that matches construction you were going to do anyway.

**Use agitators as a structural lever, not a tactic.** Inviting an agitator and installing them as an IG leader rewrites that IG's ideology, which can shatter a Political Party that was locking two IGs into voting together. This is the move when negotiation can't break a deadlock — you change who the IG is, not what they want today. Requires the IG to be in Government and pressured by the agitator's Movement; female agitators require Women's Suffrage.

## Common pitfalls

- Adding a neutral IG to Government to negotiate, but the Legitimacy hit drops you below 25 and locks all future starts `[from 05-how-to-pass-laws]`.
- Signing a Law Commitment with an equal- or lower-ranked partner expecting Success help — it gives none, only treaty acceptance weight `[from 05-how-to-pass-laws]`.
- Letting an enactment drag past a Movement's 75% threshold; slow checkpoints mean the revolution finishes before the law does `[from 05-how-to-pass-laws]`.
- Stacking multiple outstanding negotiation promises — each one drags every IG's Amenability down, ruining later deals `[from 05-how-to-pass-laws]`.
- Accepting a Journal-Entry build commitment you can't deliver in 10 years; -10 Amenability for 15 years effectively bans you from negotiating with that IG `[from 05-how-to-pass-laws]`.
- Enacting an unpopular law before warming up the opposition — you pay full Angry x1.5 Stall instead of Happy x0 `[from 05-how-to-pass-laws]`.
- Optimising for Success when Setbacks are the real fail condition — three checkpoint Stalls to 0% end the law regardless of your peak Success number `[from 05-how-to-pass-laws]`.

## See also

- **In this wiki:**
  - [Political Movements](political-movements.md)
  - [Citizenship and Acceptance](citizenship-and-acceptance.md)
  - [Cultural Fervor](cultural-fervor.md)
  - [Slavery Abolition](slavery-abolition.md)
  - [Japan: The Great Wave](../case-studies/japan-great-wave/index.md)
- **Official wiki:**
  - [Laws](https://vic3.paradoxwikis.com/Laws)
  - [Interest_groups](https://vic3.paradoxwikis.com/Interest_groups)
  - [Political_movements](https://vic3.paradoxwikis.com/Political_movements)

## Sources

- `notes/tutorials/05-how-to-pass-laws.md` (transcript of "How to Pass Laws in Update 1.12 - Victoria 3", 39:05).
