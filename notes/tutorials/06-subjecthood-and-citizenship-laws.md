---
source_transcript: ../../transcripts/tutorials/06-subjecthood-and-citizenship-laws.md
source_video: https://www.youtube.com/watch?v=_Zh8iP8yHaQ
generated_at: 2026-05-16
---

# Subjecthood and Citizenship Laws (1.10+)
**Source:** [Subjecthood and Citizenship Laws Tutorial in Victoria 3's 1.10 Update](https://www.youtube.com/watch?v=_Zh8iP8yHaQ) (22:46 runtime)

## Summary
Patch 1.10 added the new Subjecthood Citizenship Law and reworked how every other Citizenship Law grants Acceptance. Acceptance is now layered through heritage traits, language traits, trait groups, and tradition traits — each Law weighs these differently. Choice of Citizenship Law now determines whether your country pursues nationalism, pacification of minorities, or a watered-down multiculturalism, and directly affects Cultural Fervor, separatism, and tax loss from Obstinence.

## Core mechanics
1. **Subjecthood (new in 1.10)** — Defines Pops as subjects of a sovereign rather than promoting a national identity. Gives +100 Authority, −50% Support Separatism Strength/Resistance, −25% Assimilation, +100 Acceptance for primary culture, and uniquely **+30 Acceptance for Pops living in their homeland** `[03:30]`. DECISION RULE: use when your primary culture is a small minority of your country (e.g. settler/colonial states) or when you need to defuse Cultural Minority Movements before they hit Obstinence; pair with non-State-Religion Law to maximize benefit `[19:32]`.
2. **Ethnostate** — +200 Authority, +50% Support Separatism Strength, −50% resistance, +20 Primary Culture Fervor from Laws, heavy heritage-trait weighting, **−10 Acceptance for cultures sharing no language traits** `[10:30]`. DECISION RULE: use when you want maximum Cultural Fervor and your primary culture already dominates the country; expect serious Obstinence/separatism if you have large foreign minorities.
3. **National Supremacy** — "Diet Ethnostate": +150 Authority, +15 Primary Culture Fervor, gives slightly more Acceptance than Ethnostate to cultures that share traits with the primary one (+40 heritage trait, +20 trait group), still penalizes cultures with no shared traits `[11:30]`. DECISION RULE: use as a softer nationalist path when you have minorities that resemble your primary culture and you want to keep them workable while still buffing Fervor.
4. **Racial Segregation** — +100 Authority, +10 Primary Culture Fervor, very high acceptance for culturally-similar Pops (+60 heritage, +50 heritage trait group) but −20 Acceptance for cultures sharing no heritage traits `[13:31]`. DECISION RULE: pick when most of your population shares a heritage trait group with your primary culture; avoid if you rule large culturally-foreign populations.
5. **Cultural Exclusion** — +50 Authority, −25% Support Separatism Strength, +25% resistance, +5 Primary Culture Fervor, +60 heritage/+50 trait group, and **+10 Acceptance for cultures sharing no heritage or language traits** `[15:00]`. DECISION RULE: choose when you want a defensive posture (resist outside separatist agitation) and need to keep wholly foreign minorities at least minimally accepted.
6. **Multiculturalism (nerfed in 1.10)** — −50% Support Separatism Strength, +50% resistance, **−10 Primary Culture Fervor**, −25% Assimilation, +60 heritage/+50 trait group, and +20 Acceptance for no shared heritage / no shared language traits `[16:30]`. DECISION RULE: still the best Law for accepting fully foreign cultures, but they now cap at Level 3 (Open Prejudice) from laws alone — stack with Total Separation and same-religion Pops to push higher `[17:31]`.
7. **Heritage / language / tradition traits** — Each culture has one heritage trait and one language trait, each in a trait group; some cultures also share a tradition trait. Each Citizenship Law grants Acceptance for sharing the specific trait, the trait group, and the tradition trait — at different magnitudes `[06:30]`. DECISION RULE: before changing Law, inspect your largest minority cultures' trait groups and traditions to predict their final Acceptance tier.
8. **Support Separatism diplomatic action** — Unlocked by the Nationalism tech; raises Pop attraction and activism in a foreign country's minority movement matching your primary culture `[02:01]`. DECISION RULE: use offensively against rivals with your primary-culture minorities; expect retaliation if your own Citizenship Law has poor Separatism Resistance.
9. **Obstinence from Cultural Minority Movements** — When a minority movement's activism hits 50%, every state with that culture's Pops enters Obstinence, costing tax revenue and reducing Institution, Conscription, and Assimilation effects `[02:30]`. DECISION RULE: track movement activism via the Politics screen; if a movement is climbing, raise Acceptance (often by switching Citizenship Law) before it crosses 50%.
10. **Cultural Fervor from Laws is fractional, not absolute** — The Fervor bonus from your Citizenship Law is multiplied by the share of your primary culture's worldwide Pops living in your country, and only applies if you're independent `[20:32]`. DECISION RULE: don't expect the full Law value if your primary culture is split across many countries — check the worldwide vs. domestic Pop counts before banking on a Fervor boost.

## Game numbers & rules of thumb
- Subjecthood: +30 Acceptance for Pops in homeland (only Citizenship Law that does this) `[03:30]`.
- The No Colonial Affairs Law adds an extra +10 Acceptance for living in homeland in 1.10 `[05:01]`.
- Ethnostate / National Supremacy / Racial Segregation give negative Acceptance to cultures with no shared heritage (or, for Ethnostate, no shared language) traits `[10:30]`.
- Cultural Exclusion and Multiculturalism are the only Citizenship Laws giving positive Acceptance to cultures with no shared traits `[15:00]`.
- Multiculturalism ceiling from Laws alone for a fully foreign culture: ~Level 3 Open Prejudice (40 culture + up to 15 religion = 55 Acceptance) `[18:00]`.
- Support Separatism action adds roughly +15% activism to the targeted minority movement on cast `[02:30]`.
- Obstinence directly reduces state tax collection (example shown: 7.8% Obstinence → −19.6% taxes) `[06:01]`.
- Subjecthood still permits Assimilation of Pops in Acceptance tiers 2–5 (just at −25% speed); combine with the Promote National Values decree to assimilate minorities in their homelands `[20:32]`.
- Cultural Fervor scaling: bonus = (your country's primary-culture Pops ÷ worldwide primary-culture Pops) × Law value; requires independence `[21:01]`.

## Common pitfalls
- Assuming Multiculturalism still gives every culture +75 Acceptance — it no longer does; foreign cultures bottom out at Open Prejudice from Laws alone `[17:01]`.
- Stacking nationalist Laws (Ethnostate / National Supremacy / Racial Segregation) over large foreign minorities and triggering nationwide Obstinence through cascading minority movements.
- Forgetting that Support Separatism cuts both ways: nationalist Laws boost your offensive strength but slash your resistance, leaving you vulnerable to rivals targeting your minorities `[01:30]`.
- Picking Ethnostate expecting the full +20 Fervor when most of your primary culture lives abroad — you'll only get a fraction `[21:32]`.
- Running Subjecthood while keeping State Religion: minority Acceptance gains are wiped out by religious penalties; switch to Freedom of Conscience or Total Separation to actually realize the homeland bonus `[19:32]`.

## Cheatsheet
1. Open the Population screen and identify your primary culture's share of country Pops and worldwide Pops.
2. List your largest minority cultures and check their heritage trait, language trait, trait group, and tradition trait against your primary culture.
3. If primary culture is a small minority and many Pops live in their own homeland → pick **Subjecthood**, drop State Religion.
4. If minorities share heritage/language traits with primary culture → pick **National Supremacy** or **Racial Segregation** for higher Acceptance plus Fervor.
5. If you must rule large fully-foreign minorities and need stability over Fervor → pick **Cultural Exclusion** (defensive) or **Multiculturalism** (max Acceptance).
6. Watch Cultural Minority Movement activism; if any approaches 50%, switch toward a more accepting Law before Obstinence hits.

## See also
- [Laws](https://vic3.paradoxwikis.com/Laws)
- [Pops](https://vic3.paradoxwikis.com/Pops)
- [Political_movements](https://vic3.paradoxwikis.com/Political_movements)
