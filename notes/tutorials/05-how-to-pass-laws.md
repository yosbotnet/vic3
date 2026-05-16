---
source_transcript: ../../transcripts/tutorials/05-how-to-pass-laws.md
source_video: https://www.youtube.com/watch?v=4BvR96vzXfc
generated_at: 2026-05-16
---

# Passing Laws (1.12+)
**Source:** [How to Pass Laws in Update 1.12 - Victoria 3](https://www.youtube.com/watch?v=4BvR96vzXfc) (39:05 runtime)

## Summary
Law enactment in 1.12 has four ways to start, a three-phase checkpoint process driven by Success/Advance/Debate/Stall percentages, and a new Negotiation/Amendability system that lets you bargain with Interest Groups for clout and Amendments. Mastering it requires managing Government composition, Interest Group Approval, Legitimacy, Political Movements, and enactment speed so revolutions don't outrun you.

## Core mechanics

1. **Ways to start an enactment** — You can begin only if one of these holds: (a) a supporting Interest Group is in Government, (b) your country leader's ideology endorses the law, (c) a supporting Political Movement has at least 25% activism, or (d) a Law Commitment treaty article from a higher-ranked country pushes Success above 0. DECISION RULE: if none apply, change Government, swap leaders, build movement activism, or sign a commitment treaty before clicking enact `[01:01]` `[02:30]`.

2. **Legitimacy gate** — An illegitimate Government (below 25 Legitimacy) cannot start an enactment at all, except via a supporting Movement at 25%+ activism. DECISION RULE: if Legitimacy is borderline, do not add neutral Interest Groups to Government just to negotiate — the Legitimacy drop can lock you out `[06:02]` `[28:02]`.

3. **The three phases & four percentages** — Every enactment runs Introduction → Consideration → Adoption with checkpoint dates. At each checkpoint one of four outcomes fires: Success (advance/pass), Advance (helpful event or flat bonus), Debate (neutral event with a choice), Stall (harmful event or flat penalty). DECISION RULE: watch Stall; a Stall that drops you to 0% Success = a Setback, and 3 Setbacks (4 with the Creative Legislature power-bloc principle lvl 3) cancels the law `[06:31]` `[07:30]`.

4. **Success chance composition** — Sum of: political clout of supporting IGs in Government + leader bonus (+5% per level between current and proposed law within oppose→neutral→endorse) + supporting Movement support if its activism is 25%+. DECISION RULE: before starting, swap in the highest-clout supporting IG, and consider waiting for a supporting Movement to cross 25% activism `[08:00]` `[09:02]`.

5. **Stall chance composition** — Every opposing IG (in or out of Government) adds its clout, modified by Approval: Angry IGs get x1.5, Unhappy x1.0, Neutral x0.5, Happy/Loyal x0 (won't add). Marginalised IGs add 0. Opposing Movement at 25%+ activism adds its support. DECISION RULE: raise opposing IG Approval first — pass a law they like, then immediately enact the unpopular one before the happiness drifts back `[10:30]` `[20:30]`.

6. **Enactment time & checkpoint cadence** — Default 100 days between checkpoints; Government Principles = 200 days; Distribution of Power, Economic System, and Slavery = 150 days. Excess Authority gives -25% enactment time at 100% excess. DECISION RULE: keep excess Authority high during big enactments to outrun Movement radicalisation; speed matters more than success% if a revolution is brewing `[15:31]` `[16:00]`.

7. **Revolution race** — Movement activism drifts toward target; at 75% target the Movement starts a revolution and progress ticks toward current activism. Active opposing laws reduce target activism. DECISION RULE: identify what laws the Movement endorses and pass cheap ones first to bleed off activism before going for the contested law `[16:31]` `[19:31]`.

8. **Happiness change from enactment** — IGs gain/lose 5 Approval per level of distance (current→proposed), cap +/-10. Exceptions: Land Reform x1.5 cap +/-15; Government Principles & Slavery x2 cap +/-20. Happiness is locked during the enactment and drifts back to baseline over 60 months after passing. DECISION RULE: chain enactments — pass a law an IG loves, then enact a law they hate while they're still Happy so they add 0 to Stall `[13:31]` `[20:01]` `[20:31]`.

9. **Agitators & IG leaders** — Invite agitators (requirements on the invite tooltip) and install them as IG leaders to change the IG's ideology, which can break up Political Parties whose IGs no longer mesh. Requires the IG to be pressured by the agitator's Movement AND be in Government. Female agitators need Women's Suffrage to lead. DECISION RULE: use agitators to fracture inconvenient Parties or push an IG toward supporting a target law `[22:00]` `[23:30]`.

10. **Negotiation: shift IG stance** — Negotiate with a Neutral IG (must be in Government) to flip Support → adds their clout to Success. Negotiate with an Opposing IG (need NOT be in Government) to flip Neutral → removes their clout from Stall. DECISION RULE: the order of negotiations matters because each completed negotiation changes percentages and adds outstanding promises that lower other IGs' Amenability `[24:01]` `[26:01]`.

11. **Amenability bands** — 0–24: refuses. 25–49: negotiates but costs/effects doubled. 50–74: normal cost. 75–100: cost halved. DECISION RULE: chase 75+ before committing to expensive Amendments; if stuck at 25–49 and the demand is steep, negotiate someone else first `[25:31]` `[26:01]`.

12. **Negotiation outcomes** — Each negotiation gives 3 commitment choices plus a back-out. Option types include Amendments (permanent passive effects bolted onto the law for as long as active — very strong) or Journal-Entry promises (build X levels of Y in 10 years, etc.). Backing out costs Amenability and Approval immediately. DECISION RULE: prefer Amendments when offered — they're permanent. For Journal promises, only accept if the build target is already on your roadmap `[36:31]` `[37:00]`.

13. **Failing a negotiation promise** — All IGs lose 5 Amenability and you lose 5 Legitimacy for 5 years, you gain +20% radicals from that IG, and the specific IG hits you with -10 Amenability for 15 years plus -5 Approval. You may Delay once (+3 years, -1 Approval); after that, Abandon = full penalty. DECISION RULE: don't accept promises you can't deliver — the 15-year Amenability scar shuts you out of future negotiations with that IG `[37:31]` `[38:00]`.

## Game numbers & rules of thumb

- Leader/IG level support: +5% Success chance per oppose→neutral→endorse level of distance `[08:31]`.
- Movement must be at 25%+ activism to affect Success or Stall, or to enable a start without an in-Government supporter `[02:01]`.
- Law Commitment treaty: +5% Success per rank the partner is above you (Major < Unrecognised Major < Great < Super); useless from equal or lower rank `[04:30]` `[05:30]`.
- Default checkpoint cadence: 100 days; Government Principles 200; Distribution of Power / Economic System / Slavery 150 `[15:31]`.
- Setbacks to fail: 3 (4 with Creative Legislature lvl 3) `[07:30]`.
- 100% excess Authority → -25% enactment time `[16:00]`.
- Approval multipliers on Stall: Angry x1.5, Unhappy x1.0, Neutral x0.5, Happy/Loyal x0 `[10:30]` `[13:31]`.
- Happiness change per level of law distance: +/-5, cap +/-10; Land Reform x1.5 cap 15; Government Principles & Slavery x2 cap 20 `[13:31]` `[14:31]`.
- Post-enactment Approval changes drift back to baseline over 60 months `[20:31]`.
- Movement turns into revolution at 75% activism; revolution progress drifts toward current activism `[17:30]`.
- Marginalised IG threshold: drops below 4% clout, stays marginalised until 5% (or 2.5% if in a Party); marginalised IGs add 0 to Success and Stall `[10:30]` `[29:01]`.
- End-of-debate factor: if Success + Advance + Stall > 100, the excess is scaled down proportionally `[12:01]`.
- Amenability bands: 0–24 refuse; 25–49 cost x2; 50–74 normal; 75–100 cost x0.5 `[25:31]`.
- Amenability base: 50, then add the modifiers below `[27:02]`.
- Legitimacy contribution to Amenability = Legitimacy x 0.35 + 5 (range 13.75 at 25 Legit to 40 at 100 Legit) `[27:31]`.
- Clout contribution to Amenability = (Clout - 8) x -1 x 4; only IGs under 8% clout get a positive value, max +12 at 5% clout `[28:30]` `[29:30]`.
- Approval contribution to Amenability = Approval x 2.5 `[30:00]`.
- Supporting Movement pressure contribution = pressure% x 60, capped at 35 (cap reached around 58% pressure); opposing Movement pressure subtracts the same way `[30:31]`.
- "Opposes but Approval still neutral" bonus = |Clout - 8| x 4 x 0.5 (i.e., half of the normal clout penalty) `[31:31]`.
- "Law likely to pass anyway" Amenability: +5 if Success > Stall+2, +10 if Success > Stall+8, +25 if Success > Stall+15 `[32:31]` `[33:01]`.
- "Law will fail anyway" Amenability: +5 if Success < Stall - Clout - 5, +10 if -10, +20 if -15 `[33:32]` `[34:01]`.
- "Could turn the tide" penalty: -5 to Amenability if Success > Stall - Clout - 5 `[34:31]`.
- "Already letting through due to high Approval": -500 (effectively unnegotiable) if an opposing IG stays Happy after start `[35:01]`.

## Common pitfalls

- Adding a neutral IG to Government to negotiate but tanking Legitimacy below 25, locking you out of enactments entirely `[27:02]`.
- Trying a Law Commitment treaty with an equal or lower-ranked country expecting Success-chance help — it gives none, only treaty acceptance value `[04:30]`.
- Letting enactment drag while a Political Movement radicalises; slow checkpoints can mean a revolution finishes before your law does `[18:31]`.
- Stacking too many outstanding negotiation promises — each one drags every IG's Amenability down, ruining later negotiations `[26:01]`.
- Accepting a Journal-Entry build commitment you can't realistically finish in 10 years; the failure penalty is steep and lasts 15 years on the IG `[38:00]`.
- Enacting an unpopular law first instead of warming the IG up with one they like — you pay full Angry x1.5 Stall instead of x0 `[20:31]`.

## Cheatsheet

1. Engineer a start: get a supporting IG into Government, or use leader ideology, or wait for a supporting Movement to hit 25% activism, or sign a Law Commitment with a higher-ranked partner.
2. Check Legitimacy >= 25 and pad excess Authority to 100% for the -25% enactment-time bonus.
3. Pre-warm: pass a small law opposing IGs like first, so they're Happy/Loyal (x0 Stall multiplier) when you start the real law within the 60-month drift window.
4. Open Negotiation — sort by Amenability, hit 75+ targets first for half-price Amendments, then chain to others (their Amenability rises as Stall falls).
5. Prefer Amendment outcomes over Journal-Entry promises; only accept build commitments aligned with your existing plans.
6. If a Movement is radicalising fast, pass a different law that Movement endorses to drain its activism before retrying the contested one.

## See also

- [Laws](https://vic3.paradoxwikis.com/Laws)
- [Interest Groups](https://vic3.paradoxwikis.com/Interest_groups)
- [Political Movements](https://vic3.paradoxwikis.com/Political_movements)
