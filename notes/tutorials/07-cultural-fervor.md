---
source_transcript: ../../transcripts/tutorials/07-cultural-fervor.md
source_video: https://www.youtube.com/watch?v=i-If6oNqoc0
generated_at: 2026-05-16
---

# Cultural Fervor

**Source:** [Cultural Fervor Tutorial in Victoria 3](https://www.youtube.com/watch?v=i-If6oNqoc0) (21:36 runtime)

## Summary
Cultural Fervor (added in 1.10) is a worldwide measure of a Culture's national spirit. High Fervor slows assimilation, generates more radicals on conquest, raises Liberty Desire, and fuels Cultural political movements that can enter a new high-activism state called Obstinance. Crucially, a Culture's Fervor is global — what happens to that Culture in any country influences its Fervor everywhere.

## Core mechanics
1. **Fervor is global, not per-country** — A Culture has one Fervor score worldwide. Each country's contribution is weighted by the share of that Culture's pops living there. DECISION RULE: when judging Fervor risks, look at the Culture's global pop distribution, not just your own census `[03:30]`.
2. **Citizenship Law contribution** — More restrictive Citizenship Laws give more Fervor to your primary Culture (e.g. National Supremacy +15, Cultural Exclusion +5). Multiculturalism *reduces* primary-Culture Fervor. DECISION RULE: if you want to keep primary-Culture Fervor low (peaceful empire), move toward Multiculturalism; if you want high Fervor for Liberty Desire as a subject, stay restrictive `[04:30]` `[10:31]`.
3. **Education Institution contribution** — Public Schools grants up to +25 Fervor at top level; Religious Schools grants 0. DECISION RULE: Public Schools is the strongest lever for raising your primary Culture's Fervor `[08:32]` `[09:30]`.
4. **War casualties** — Casualties suffered in war add Fervor to the affected Culture. DECISION RULE: expect a Fervor spike during/after major wars; plan unrest mitigation in states with that Culture `[10:00]`.
5. **Literacy and Academics** — High average literacy and large numbers of Academic pops of a Culture are among the largest Fervor sources. DECISION RULE: industrialised, university-heavy nations naturally drift to high Fervor — be ready to manage it `[10:31]`.
6. **Research nationalism / Pan-nationalism techs** — Pops in countries that have researched these techs add Fervor to their Culture `[10:31]`.
7. **High Acceptance suppresses Fervor (slightly)** — Full Acceptance −4, Second-class −3, Open Prejudice −2, Cultural Erasure −1, Violent Hostility 0. Effects are small at high Fervor totals `[11:00]`.
8. **National Awakening at 25** — Once a Culture reaches 25 Fervor, it gains a National Awakening adding +20 to its target. This both raises the ceiling and *accelerates* progress (rate = target − current). DECISION RULE: 25 is a critical threshold — crossing it kicks off snowballing Fervor growth `[11:31]` `[12:31]`.
9. **Cultural movements gain activism from Fervor** — A minority Culture's Fervor directly boosts activism of its Cultural political movement. DECISION RULE: monitor Fervor of any minority Culture that has a movement; suppressing the movement's grievances becomes urgent as Fervor climbs `[13:30]`.
10. **Obstinance (≥50% activism, Cultural movements only)** — A new state between Peaceful and Militant. Causes −20% assimilation/conversion, −20% tax collection, −33% conscriptable battalions, and large negative impact on Institutions in every state containing that Culture (severity scaled by pop share). DECISION RULE: never let a Cultural movement cross 50% activism — the per-state hit is severe and broad `[14:00]` `[14:31]` `[15:33]`.
11. **Country-modifier Fervor (events)** — Modifiers like Russia's Organic Statute of 1832 add Fervor to the affected Culture, weighted by the share of that Culture in the source country. DECISION RULE: foreign events affecting your minorities (or your primary culture abroad) can suddenly push Fervor up — watch the breakdown tooltip `[17:30]` `[19:00]`.
12. **Support Separatism (diplomatic action)** — Unlocked with Nationalism. When your primary Culture has a Cultural minority movement in another country, you can boost its pop attraction and activism. DECISION RULE: use offensively against rivals with co-cultural minorities; expect rivals to do the same to you `[20:31]`.

## Game numbers & rules of thumb
- Fervor target per country contribution = base value × (Culture's pops in that country / Culture's pops worldwide) `[05:00]`.
- Monthly Fervor change = (target − current) × 0.01 (approximately); growth slows as you approach the target `[11:31]`.
- Citizenship Law base contributions: National Supremacy +15, Cultural Exclusion +5; Multiculturalism is negative for primary Culture `[04:30]` `[10:31]`.
- Public Schools Education Institution: +5 at level 1 up to +25 at max level; Religious Schools gives 0 `[09:00]` `[09:30]`.
- National Awakening trigger: Culture reaches 25 Fervor → +20 to target, permanent `[11:31]`.
- Obstinance trigger: any Cultural movement at ≥50% activism `[14:00]`.
- Obstinance state penalties: −20% tax collection, −20% assimilation/conversion, −33% conscriptable battalions, and roughly −40% Institution impact (varies) `[14:31]` `[15:00]`.
- Acceptance Fervor reduction: −4 / −3 / −2 / −1 / 0 from Full Acceptance down to Violent Hostility `[11:00]`.
- Only the primary Culture of an *independent* country receives Citizenship-Law Fervor; subjects don't count toward that source `[08:03]`.

## Common pitfalls
- **Ignoring foreign events.** Polish Fervor can spike from a Russian modifier and break Prussia's Posen — the breakdown tooltip is the only place you'll see this `[17:30]`.
- **Building Universities everywhere without watching minority Fervor.** Academics are a top Fervor source for *every* Culture they belong to, including minorities that may have movements `[10:31]`.
- **Letting a Cultural movement cross 50% activism.** Obstinance hits tax, conscription, assimilation, and Institutions across every state containing the Culture, even tiny minority shares (e.g. 1% Polish pops still triggers it weakly) `[15:33]`.
- **Assuming restrictive Citizenship Laws are "safer".** They raise *your* primary Culture's Fervor and worsen minority-movement grievances (acceptance level adds to protest %) `[17:01]`.
- **Treating Fervor as country-local.** Releasing a subject or losing pops abroad changes the weighting on every Fervor source for that Culture `[03:30]`.

## Cheatsheet
1. Open Society → Cultures regularly; sort by Fervor and check the trend arrow.
2. For each Culture above ~25 (National Awakening), check if it has an active Cultural movement.
3. If a Cultural minority movement exists: pass a law it likes (or at least is Content with), raise its Acceptance, build staple goods in its states to lift Standard of Living, and reduce radicals.
4. If your primary Culture's Fervor is too high (peaceful empire), shift toward Multiculturalism and avoid maxing Public Schools.
5. If you're a subject seeking independence, do the opposite: National Supremacy + Public Schools + Universities to drive Fervor and Liberty Desire.
6. After any major war or foreign event, recheck the Fervor breakdown tooltip for new sources.

## See also
- [Political_movements](https://vic3.paradoxwikis.com/Political_movements)
- [Laws](https://vic3.paradoxwikis.com/Laws)
- [Pops](https://vic3.paradoxwikis.com/Pops)
