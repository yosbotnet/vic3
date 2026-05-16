---
sources:
  - ../../notes/tutorials/08-foreign-investment-rights.md
wiki:
  - https://vic3.paradoxwikis.com/Companies
generated_at: 2026-05-16
---

# Foreign Investment

## What it is

Foreign Investment is the system that lets one country's private sector — its Financial Districts, Manor Houses, and Company main HQs — construct and own buildings inside another country. Rights flow in one direction: a grant from A to B lets B build in A, not the other way around. Once a Company hits a threshold of foreign building levels, a Regional HQ spawns in the host country and starts re-routing reinvestment money back to the owner's Investment Pool.

Granting rights accelerates GDP growth on both sides (host pops own the buildings and pay tax to their own state), but it bleeds your Investment Pool if you don't get rights back, and it locks in foreign owners who can only be removed by nationalization or war. The intended endgame, per the source, is that granted rights are a temporary growth boost that always concludes with nationalizing the foreign-owned levels.

## Mechanics

1. **Treaty article (Investment Rights)** — A one-directional Treaty clause. Each article grants rights in one direction only — you may take "they get rights in me," "I get rights in them," or both as two separate articles. Decision rule: never grant without taking. A one-way grant gives your Investment Pool no counter-income, only a drain when their Regional HQs spawn.
2. **Foreign Investment 3 (Power Bloc mandate)** — A bloc mandate that gives the holder Foreign Investment rights in every bloc member of lower Rank than the holder. Decision rule: as a Great Power leading a bloc, take this mandate — it converts every junior member into a free build target with no treaty negotiation.
3. **Private-sector foreign building (no Charter)** — With rights in hand, your Financial Districts, Manor Houses, and Company main HQs can directly build levels abroad. Those levels are owned by the main HQ at home, so dividends flow to your own pops. No Regional HQ is created.
4. **Investment Rights Charter (Company)** — A Company charter that lets that Company establish Regional Headquarters abroad. Without it, the Company can still build via its main HQ, but never creates a Regional HQ. Decision rule: grant the Charter to Companies you want extracting wealth from foreign markets long-term; withhold it from Companies you only want building at home.
5. **Regional HQ spawn condition** — Triggers automatically once a Chartered Company's main HQ owns 5+ building levels in a single foreign country. You cannot place one manually; you reach the threshold and one appears.
6. **Regional HQ economics (you own one abroad)** — Buildings under the Regional HQ are owned by host-country pops, who get dividends and pay tax to the host. But reinvestment from those buildings flows back to your Investment Pool, and new levels are built using the host's private construction queue and Investment Pool. Decision rule: target large, populous, resource-rich hosts (USA, Qing, France, Germany) — small or under-developed hosts have neither the construction capacity nor the Investment Pool to grow your foothold.
7. **Regional HQ damage (foreigners own one in you)** — Reinvestment from those buildings leaves your country and feeds the foreign owner's Investment Pool instead of yours. Decision rule: track the weekly Investment Pool change number; if it stays red, the bleed is structural — start nationalizing.
8. **Nationalization** — Open the affected building, click Nationalize, and select only the levels owned by the foreign Regional HQ (the game appears to remove Regional HQ levels first when partially nationalizing). The Regional HQ disappears once it owns zero levels. Decision rule: Laissez-Faire forbids nationalization entirely — change economic laws first, or take the buildings as war reparations.
9. **Free nationalization** — Command Economy plus Cooperative Ownership lets you nationalize at no cost. Decision rule: if you need to expel many Regional HQs at once, swap to these laws before starting — paying for mass nationalization deepens any debt problem you were trying to solve.
10. **Debt spiral chain** — Negative Investment Pool change → pool drains → private construction queue stops → government covers 100% of construction cost → budget collapses. Decision rule: treat a sustained-negative Investment Pool as a fire. If you cannot nationalize yet, lower construction cost by cheapening inputs (more domestic production of construction goods).
11. **GDP and minting** — Goods produced inside a host country count toward the host's GDP and minting, even when owned by your Company. The host genuinely benefits; granted rights are a real diplomatic carrot, not pure sacrifice.
12. **Prestige goods abroad** — A Company's foreign-built buildings can produce the Company's prestige good directly into the host's market, transferring goods access without trade routes.

## Game numbers & rules of thumb

- Regional HQ spawn threshold: **5+ building levels** owned by the same Company main HQ in one foreign country `[from 08-foreign-investment-rights]`.
- Foreign Investment 3 mandate applies only to bloc members of **lower Rank** than the holder `[from 08-foreign-investment-rights]`.
- Laissez-Faire: private sector covers **75%** of construction points and cost; if the private queue halts, the government inherits 100% of the bill `[from 08-foreign-investment-rights]`.
- Laissez-Faire **forbids nationalization** of any kind `[from 08-foreign-investment-rights]`.
- Command Economy + Cooperative Ownership = **free** nationalization `[from 08-foreign-investment-rights]`.
- Investment Pool weekly change is the operative metric — brief dips into red are tolerable, sustained red is the action trigger `[from 08-foreign-investment-rights]`.
- A persistently large idle Investment Pool is wasted money; it should be spent or absorbed, not hoarded `[from 08-foreign-investment-rights]`.
- Possible bug (as of 1.9): reinvestment from foreign Regional HQs into your pool may be inflated several times above the sum of individual contributions; if patched, owning foreign Regional HQs becomes substantially less lucrative `[from 08-foreign-investment-rights]`.

## Strategy & playbook

**As the investor (Great Power, bloc leader).** Lead a Power Bloc, take the Foreign Investment 3 mandate, and you immediately have build rights in every lower-ranked member. Pick one or two strong Companies and grant them the Investment Rights Charter. Steer those Companies into the largest, most populous hosts you can reach — the USA, Qing, France, Germany are the named-good targets because their domestic Investment Pools and construction capacity can actually grow your levels past 5 and keep adding more. Small hosts give you a Regional HQ that never gets to do anything; you spent a Charter slot for nothing. Re-check the Investment Pool weekly change every few years to confirm the income is real (especially given the 1.9 reinvestment bug — plan for the post-patch number, not the current one).

**As the recipient (mid-rank or small nation).** Receiving rights is generally good: foreign Financial Districts and Companies build levels for you at zero treasury cost, and the resulting buildings count toward your GDP and minting. The catch is that any Regional HQ in your borders re-routes reinvestment outward. The treatment plan is staged: take the rights now for the growth, but commit in advance to nationalizing the foreign-owned levels later. Don't sign Laissez-Faire when foreign Regional HQs are accumulating — you'll lock yourself out of the only peaceful exit. Interventionism or further-left economic laws keep nationalization on the table; Command Economy + Cooperative Ownership makes it free.

**Reciprocity discipline at the treaty table.** The single most consequential decision rule in this system is: never grant one-way. A reciprocal article costs no extra slot to negotiate but gives your Investment Pool a counter-income stream when their Regional HQs eventually spawn. A one-way grant guarantees outbound drain with nothing coming back.

**Watching the Investment Pool.** The weekly change number is the early-warning indicator. Brief red is fine — a new foreign Regional HQ just spawned, things will normalize. Sustained red across multiple years is the trigger to act: nationalize foreign-owned levels (one building at a time, selecting only the Regional HQ's levels), or if you can't nationalize yet, attack the underlying construction cost so domestic private builders stay solvent.

**Removal playbook.** To expel a foreign Regional HQ peacefully: (1) confirm your economic law allows nationalization (not Laissez-Faire); ideally move to Command Economy + Cooperative Ownership for free expropriation. (2) Open each building the Regional HQ owns and Nationalize only its levels, leaving the main-HQ-owned levels alone. (3) Once the Regional HQ holds zero levels it dissolves. To expel by force: win a war and take the buildings as part of the peace settlement.

## Common pitfalls

- **One-way grants.** Giving rights without taking rights back guarantees Investment Pool drain with no counter-income. Always pair the articles.
- **Laissez-Faire trap.** Being locked into Laissez-Faire when a foreign Regional HQ starts bleeding your Investment Pool — you cannot nationalize at all until you change laws or win a war. Change the law preemptively if you're hosting any foreign rights.
- **Ignoring the weekly change number.** Waiting until the Investment Pool is nearly empty before reacting means the debt spiral has already started and the nationalization cost itself deepens the hole.
- **Granting rights to weak hosts.** Low-pop, low-infrastructure hosts can't build much for you, so the upside is small — but if they reciprocated, their Regional HQs in your country still drain your pool just as hard as a Great Power's would.
- **Treating granted rights as permanent.** The intended endgame is nationalization. Investors who plan to hold foreign Regional HQs forever lose them anyway, either to host nationalization or to war; recipients who never plan to nationalize cede a permanent reinvestment leak.

## See also

- **In this wiki:**
  - [Companies](companies.md)
  - [Construction](construction.md)
  - [Treasury & Deficit](treasury-and-deficit.md)
  - [Building Balance Sheet](building-balance-sheet.md)
  - [Trade](trade.md)
  - [Power Blocs](../diplomacy/power-blocs.md)
  - [Small Nation Play](../diplomacy/small-nation-play.md)
  - [Passing Laws](../laws-and-politics/passing-laws.md)
  - [Japan: Great Wave](../case-studies/japan-great-wave.md)
- **Official wiki:**
  - [Companies](https://vic3.paradoxwikis.com/Companies)
  - [Power_blocs](https://vic3.paradoxwikis.com/Power_blocs)
  - [Diplomacy](https://vic3.paradoxwikis.com/Diplomacy)

## Sources

- `../../notes/tutorials/08-foreign-investment-rights.md`
