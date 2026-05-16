---
sources:
  - ../../notes/tutorials/07-cultural-fervor.md
wiki:
  - https://vic3.paradoxwikis.com/Pops
generated_at: 2026-05-16
---

# Cultural Fervor

## What it is

Cultural Fervor (added in 1.10) is a **global, per-Culture** score of national spirit. It is not per-country: a single Culture has one Fervor value worldwide, and every country it lives in contributes weighted by that country's share of the Culture's pops. High Fervor slows assimilation, makes conquest of those pops generate more Radicals, raises Liberty Desire for subjects of that Culture, and fuels **Cultural political movements**, which can enter a new high-activism state called **Obstinance**. Fervor is therefore both a tool (for subjects pushing for independence, or for empires destabilising rivals via Support Separatism) and a hazard (for multi-cultural empires whose minorities can snowball into Obstinance and wreck taxes, conscription, and Institutions).

## Mechanics

1. **Fervor is global, not per-country** — A Culture has one Fervor score worldwide; each country's contribution is weighted by that country's share of the Culture's pops. Decision rule: judge Fervor risk from the Culture's *global* pop distribution, not just your own census — losing a war, releasing a subject, or events in foreign countries all shift Fervor at home `[from 07-cultural-fervor]`.
2. **Citizenship Law contribution** — More restrictive Citizenship Laws push your primary Culture's Fervor up (National Supremacy +15, Cultural Exclusion +5); Multiculturalism is *negative* for primary Culture. Only the primary Culture of an *independent* country counts here — subjects do not. Decision rule: peaceful empire → shift toward Multiculturalism; subject seeking independence → stay restrictive `[from 07-cultural-fervor]`.
3. **Education Institution contribution** — Public Schools scales up to +25 Fervor at max level; Religious Schools gives 0. Decision rule: Public Schools is the single strongest lever for raising your primary Culture's Fervor — use it as a subject, avoid maxing it as a stable empire.
4. **War casualties** — Casualties suffered in war add Fervor to the affected Culture. Decision rule: expect a Fervor spike during and after major wars and plan unrest mitigation in states containing that Culture.
5. **Literacy and Academics** — High average literacy and large numbers of Academic pops are among the largest Fervor sources for *any* Culture. Decision rule: industrialised, university-heavy nations drift to high Fervor naturally — and so do their minorities.
6. **Nationalism / Pan-nationalism technologies** — Pops in countries that have researched these techs add Fervor to their Culture.
7. **Acceptance suppresses Fervor (slightly)** — Full Acceptance −4, Second-class −3, Open Prejudice −2, Cultural Erasure −1, Violent Hostility 0. Decision rule: raising Acceptance helps at the margins but does not save you once other sources stack high.
8. **National Awakening at 25** — When a Culture's Fervor crosses 25, it gains a permanent **National Awakening** modifier worth +20 to its target. Because monthly change is proportional to (target − current), this both raises the ceiling and *accelerates* growth. Decision rule: 25 is a hard threshold — once crossed, Fervor snowballs, so act before the trigger, not after.
9. **Cultural movements gain activism from Fervor** — A minority Culture's Fervor directly boosts the activism of its Cultural political movement. Decision rule: any minority Culture with a movement needs continuous Fervor monitoring; suppressing grievances becomes urgent as Fervor climbs.
10. **Obstinance (≥50% activism on Cultural movements only)** — A new movement state between Peaceful and Militant. Penalties hit *every state* containing that Culture (severity scales with pop share): −20% assimilation/conversion, −20% tax collection, −33% conscriptable battalions, and a large negative impact on Institutions. Decision rule: never let a Cultural movement cross 50% activism — the per-state hit is broad and cripples Institutions even where the minority is tiny.
11. **Country-modifier Fervor (events)** — Modifiers like Russia's *Organic Statute of 1832* add Fervor to a target Culture, weighted by that Culture's pop share in the source country. Decision rule: after foreign events touching your minorities (or your primary culture abroad), open the Fervor breakdown tooltip — these contributions are otherwise invisible.
12. **Support Separatism (diplomatic action)** — Unlocked with Nationalism. When your primary Culture has a Cultural minority movement in another country, you can boost its pop attraction and activism. Decision rule: use offensively against rivals with co-cultural minorities; expect symmetric use against you.

## Game numbers & rules of thumb

- Per-country contribution = base value × (Culture's pops in that country / Culture's pops worldwide) `[from 07-cultural-fervor]`.
- Monthly Fervor change ≈ (target − current) × 0.01; growth slows as you approach the target `[from 07-cultural-fervor]`.
- Citizenship Law base contributions: National Supremacy +15, Cultural Exclusion +5; Multiculturalism is negative for primary Culture `[from 07-cultural-fervor]`.
- Public Schools: +5 at level 1, up to +25 at max; Religious Schools: 0 `[from 07-cultural-fervor]`.
- National Awakening trigger: Culture reaches 25 Fervor → permanent +20 to target `[from 07-cultural-fervor]`.
- Obstinance trigger: any Cultural movement at ≥50% activism `[from 07-cultural-fervor]`.
- Obstinance state penalties: −20% tax collection, −20% assimilation/conversion, −33% conscriptable battalions, roughly −40% Institution impact (varies with pop share) `[from 07-cultural-fervor]`.
- Acceptance Fervor reduction: −4 / −3 / −2 / −1 / 0 from Full Acceptance down to Violent Hostility `[from 07-cultural-fervor]`.
- Citizenship-Law Fervor only counts for the primary Culture of an *independent* country — subjects do not contribute through this source `[from 07-cultural-fervor]`.

## Strategy & playbook

**Stable multicultural empire (Austria, Russia, Ottomans).** Your danger is a minority Culture snowballing past 25 Fervor and then its movement crossing 50% activism into Obstinance — which would shred your tax base and Institutions across half your map. Sort the Cultures panel by Fervor monthly and watch the *minorities*, not your primary Culture. Move Citizenship Law toward Cultural Exclusion → Racial Segregation → Multiculturalism as soon as your political situation allows; this lowers your primary Culture's Fervor and improves minority Acceptance. Be careful with Public Schools and Universities: both are huge Fervor sources for *every* Culture they educate, including your minorities. If a minority movement appears, pass a law it likes (or at least is Content with), raise its Acceptance bracket, and lift Standard of Living in its core states by building staple-goods supply.

**Subject going for independence (Brazil under Portugal, Hungary under Austria, any colony).** You want the opposite: maximise your primary Culture's Fervor to drive Liberty Desire. Run National Supremacy, max Public Schools, and build Universities to pump literacy and Academics. National Awakening at 25 is your friend — once you cross, growth accelerates on its own. Time your independence play for after the +20 target kicks in and Liberty Desire has had a few years to compound.

**Aggressive use of Support Separatism.** Once you research Nationalism, every rival with a substantial pop of your primary Culture is a lever. Find a Cultural minority movement abroad, support it, and let the combination of activism boost and pop attraction destabilise the target — ideally pushing it toward Obstinance during a war or right before a diplomatic play.

**Reading the breakdown tooltip is non-optional.** Foreign country modifiers (the Russian *Organic Statute* example), war casualties from someone else's war that involved your Culture, and tech research abroad all show up only in the per-source breakdown. After any major world event — a great power war, a famous decree, a new tech wave — recheck Fervor on every Culture you care about.

## Common pitfalls

- **Ignoring foreign events.** Polish Fervor can spike from a Russian modifier and shatter Prussian Posen; the only place this appears is the breakdown tooltip.
- **Universities everywhere without watching minorities.** Academics are a top Fervor source for *every* Culture they belong to, not just yours.
- **Letting a Cultural movement cross 50% activism.** Obstinance hits tax, conscription, assimilation, and Institutions across every state containing the Culture — even a 1% Polish minority in a German state still triggers the penalty (weakly).
- **Assuming restrictive Citizenship Laws are "safer".** They raise *your* primary Culture's Fervor and worsen minority grievances — the Acceptance level itself adds to protest %.
- **Treating Fervor as country-local.** Releasing a subject, losing pops in a war, or the rise of a diaspora abroad re-weights every contribution to that Culture's Fervor at home.
- **Acting after National Awakening fires.** Once a Culture crosses 25, the +20 target makes the slope steeper — preventive action (Multiculturalism, Acceptance, movement appeasement) is much cheaper before the threshold than after.

## See also

- **In this wiki:**
  - [Passing laws](passing-laws.md)
  - [Citizenship and acceptance](citizenship-and-acceptance.md)
  - [Political movements](political-movements.md)
  - [Standard of living](../pops/standard-of-living.md)
  - [Power blocs](../diplomacy/power-blocs.md)
  - [Small nation play](../diplomacy/small-nation-play.md)
- **Official wiki:**
  - [Political_movements](https://vic3.paradoxwikis.com/Political_movements)
  - [Laws](https://vic3.paradoxwikis.com/Laws)
  - [Pops](https://vic3.paradoxwikis.com/Pops)

## Sources

- `../../notes/tutorials/07-cultural-fervor.md`
