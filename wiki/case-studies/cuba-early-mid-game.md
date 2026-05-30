---
sources:
  - ../../../notes/cuba-trading-in-sin-live/01-early-mid-game.md
generated_at: 2026-05-30
---

# Cuba — Step-by-Step Playthrough

**Source:** [Trading in Sin as CUBA LIVE! | Victoria 3 GIGACHAD Live](https://www.youtube.com/watch?v=cn0RBR3aUfw) by Tarkusarkusar, 2025-12-10 (Great Wave DLC, early-access build). Notes: [01-early-mid-game](https://github.com/yosbotnet/vic3/blob/main/notes/cuba-trading-in-sin-live/01-early-mid-game.md).

This is the **click-by-click companion** to the [Cuba case study](cuba-spanish-restoration.md). That page is the strategic highlight reel; this is the slow version — a follow-along playbook covering the **whole run, 1836 → 1921**. It's deliberate (only ~1860 by the 2-hour mark, ~1883 by 3½ hours), so the phases map to **early game (≈ first 2h), mid game (≈ 2–3½h), and the late-game endgame (≈ 3½h–end)**. The early game has a single near-correct opening worth copying exactly; the mid and late game branch, so treat Phases 6–7 as principles rather than a script and **make them your own**.

!!! note "Patch context"
    From a December 2025 Great Wave DLC early-access stream, so some specifics (the four Cuban prestige companies, the governor-request feature, a couple of production methods, one or two bugs called out below) are DLC/patch-dependent — the *sequence and reasoning* transfer even if a number has moved. Timestamps like `[0:13:30]` point into the source VOD.

## Phase 1 — The opening: infrastructure before plantations (1836 → ~1841)

The single most important opening idea: **you are playing a plantation economy, but you do not open with plantations.** Build the construction backbone first or everything stalls on infrastructure.

1. **Before unpausing,** look at Cuba's new prestige-goods companies — **sugar**, **cigars**, **liquor**. The sugar one gives *migration attraction* and feeds the investment pool; these are what make a plantation-led economy work now `[0:12:31]`.
2. **Queue two Construction Sectors** — set one to *agriculture industries* and one to *resource industries* `[0:13:30]`. See [Construction](../economy/construction.md).
3. **Build the backbone, not plantations:** lumber camp → iron-tools workshop → iron mine. Skip hardwood. "Despite wanting a plantation economy, it's best to do lumber and tools first because we want our construction going" `[0:14:31]`.
4. **Swap tools to *steel tools* one week before the iron mine finishes** — it creates steel demand and makes tools far more profitable. (Cuba's steel maths line up: one steel building outputs ~65, tools wants 30 + another 40 — "perfectly balanced") `[0:27:32]` `[0:29:30]`.
5. **Railways are the binding constraint.** The moment you run out of infrastructure the investment pool stops building and the whole construction bill lands on the government. Finish the iron→steel→motors→railway chain before scaling sectors; drop the **Road Maintenance** decree as a stopgap `[0:19:01]` `[0:25:31]`.
6. **Decree: Greener Grass Campaigns immediately** for migration attraction `[0:15:00]`. See [Citizenship & Acceptance](../laws-and-politics/citizenship-and-acceptance.md).
7. **Research:** Stock Exchange first (a "no-brainer"), then Egalitarianism (Proportional Taxation + universities), then Joint-Stock Companies for company charters `[0:15:00]` `[0:33:30]`.
8. **Request a governor and pick the Influential Planter** (plantation throughput). **Reject the Experienced Extractor** despite the bonus — its 1% mortality is a hard no `[0:20:01]` `[0:21:00]`.
9. **Politics:** your Landowners are strong but happen to be **Reformers** — good. **Do not try to ban slavery yet** (landowner clout is too high to negotiate). Pass **Census Suffrage** while the planters are happy `[0:15:31]` `[0:32:00]`. See [Passing Laws](../laws-and-politics/passing-laws.md).
10. **Public Healthcare** via the church-in-government institution, mainly for migration attraction (level 2's +1 migration score is gated behind Quinine) `[0:32:30]`.
11. **Diplomacy:** keep Spain friendly; declare interests toward **America** (trade) and **England**. **Do not join Spain's market** — there's no steel in it `[0:18:02]` `[0:28:30]`.
12. **Bureaucracy:** when it goes negative, queue a bureaucracy building (filing-cabinets PM) — it pays for itself — but don't over-build before you hit the tax-capacity cap `[0:30:00]`.

!!! tip "Early-access bug to expect"
    On this build, unprofitable buildings sometimes get stuck flipping between employing and unemploying workers. **Subsidise** new mines/tools when they come online to force them to staff up `[0:24:00]`.

## Phase 2 — The sin economy: cigars + sugar (~1841 → 1849)

Once railways lift the infra cap, switch to iron construction, spam iron, then go heavy on plantations — but watch for overbuild (he queued ~9 iron mines and cut back to ~5) `[0:35:36]` `[0:37:33]`.

1. **Found your prestige companies *before* foreigners buy the buildings.** Build tobacco plantations to **level 5 in at least two states**, found the **cigar company**, and grant it a **tobacco monopoly on investment rights** the instant it exists — otherwise foreign investors snap up your tobacco `[0:42:00]` `[0:45:30]`. See [Companies](../economy/companies.md).
2. Use the **Exploited Rollers** PM on cigars — more jobs means more migration attraction, worth more than the cheaper PM here `[0:42:31]`.
3. **Found the sugar company next** for its migration-attraction bonus; grant it a sugar monopoly (and don't accidentally hand it logging rights) `[0:47:00]`.
4. **Pump migration:** low taxes + Greener Grass + healthcare draw mass-migration waves — ~71k French in a single event, later Mexicans. Don't stop them. A cultural community must already exist in a state before pops migrate there freely, so ports + the decree + a little RNG seed new states `[0:38:30]` `[0:40:31]`.
5. **Trade:** build out trade centres (~44) to export cigars and sugar, and **stay in the Spanish market** for the European migrant flow. Once you have a navy, drop a **naval interest in North Germany** — Prussia is the biggest cigar buyer `[0:58:00]` `[1:06:01]`. See [Trade](../economy/trade.md).
6. **Reclaim your industry:** nationalise the French regional HQ (~£450k of investments, then ~£1M of coal mines) to stop dividends leaking abroad `[0:59:32]`.

## Phase 3 — Dominion without a war (~1849)

You want diplomatic freedom but not the cost of an early war, and you want to keep the Spanish market. **Dominion** gives you both — for free:

- **The conscript bluff:** add conscripts but **never raise them**. The inflated army strength is enough that Spain grants **Dominion** for just an obligation. Dominion pays 25% tax vs a Colony's 30%, lets you run your own diplomacy, and keeps you in the Spanish market `[0:49:01]` `[0:52:00]`. See [Small-Nation Play](../diplomacy/small-nation-play.md).

## Phase 4 — The war of independence (~1850s)

1. **Build a navy** (basic + military shipyard) — you need it to project interest and to land in Haiti/Puerto Rico `[0:54:00]`.
2. **Pass the political package:** Universal Suffrage (negotiate Church support with political concessions, ~42% pass), then Proportional Taxation, then remove Migration Controls `[1:02:00]` `[1:08:01]`.
3. **Conquer Haiti under Nationalism** — Cuba's arable land runs out, and Haiti adds land, sugar, and dyes `[1:14:00]` `[1:21:00]`.
4. **Don't go Laissez-Faire while still a subject** — foreigners would buy out your industry. Wait until after independence `[1:20:03]`.
5. **Force the war:** expel Spanish diplomats to tank relations (so Spain won't grant independence peacefully), then declare with **Puerto Rico** added as a war goal `[1:23:02]`.
6. **Win it:** raise military wages; **conscript early** (his single biggest self-named mistake was conscripting too *late*); **drop artillery** (bad this early); assign groceries as army supply; pause construction to dodge war debt; and **defend Havana before you launch the Puerto Rico landing** — Spain will take your capital if your army is away (he reloaded ~2 months after exactly this). Then cash in on Spain's **Carlist uprising** to land and capitulate them `[1:28:00]` `[1:29:00]` `[1:26:30]` `[1:35:02]`. See [War & Naval Invasions](../military/war-and-naval-invasions.md).
7. **Payoff:** independence brings **immediate Great Power** status; the independence journal lets you **ban slavery**, unlocking Afro-Caribbean culture. Take **Parliamentary** government `[1:38:03]`.

## Phase 5 — Your first expansion (~1860)

1. **Form the Caribbean Union power bloc** with the **Cultural Commonwealth** doctrine — it lets you grant Afro-Caribbean culture to Romance-speaking subjects so they incorporate fast (and later auto-annex into a confederation) `[1:38:32]` `[1:41:31]`. See [Power Blocs](../diplomacy/power-blocs.md).
2. **Cheap protectorate wars** — New Granada, then Venezuela, then Bolivia — timed around great-power distraction (wait for Brazil to leave its current war; declare on Bolivia before it finishes its war with Chile to dodge extra infamy). Coastal capitals are easy naval-landing wins `[1:50:31]` `[2:06:01]`.
3. **Set up the law swap:** rig elections for the Liberals and install a market-liberal agitator in the Petite Bourgeoisie so it won't oppose Laissez-Faire `[1:58:12]` `[1:59:32]`.
4. **Nationalise all foreign buildings (~£16M of a £31M credit limit), *then* pass Laissez-Faire** — never the other way, so foreign owners can't benefit (the company-HQ monopolies stay foreign; you end ~95% Cuban-owned) `[2:10:02]` `[2:11:00]`.
5. **Stack trade centres in Havana** (higher trade-capacity bonus than Guantánamo) `[2:05:00]`.

## Phase 6 — Into the mid game (~1860 → 1883)

From here the run branches — these are **principles, not a script** (and several beats are reactive to RNG). Copy the economic habits; improvise the conquests.

1. **Drop taxes after Laissez-Faire.** Once private industry carries you, taxes cost more in lost migration and pop consumption than they raise — lower them and let the consumer economy spin up `[2:33:31]`.
2. **The consumer loop is near-infinitely scalable.** Groceries (and later liquor) become "insane profits": build more → prices drop → pops buy more → build more. It only peters out around ~20 buildings per state, so keep scaling it `[3:05:00]` `[3:07:04]`.
3. **Add the Bacardi rum leg.** Found the liquor prestige company — it needs **food industries in Eastern Cuba** first; convert food industries to liquor, build glass for the chain, and **subsidise** until liquor demand catches up `[2:49:31]` `[2:53:31]`.
4. **Switch plantations to automatic irrigation (pump-jacks PM)** — a short-term loss for a long-run output gain (and it consumes engines, feeding your own industry) `[3:18:08]`.
5. **Save-scum IG-leader rolls.** The ideology roll is day-seeded, so advance one in-game day and reload to re-roll for the modernizer/leader you need `[2:16:30]`.
6. **Take the External Trade mandate** when your trade volume is huge — it restores trade-centre profitability after you've over-traded a good `[2:39:02]`.
7. **Use labour-saving PMs when you're population-constrained** (he caught himself running exploitative PMs during a worker shortage — "playing terribly"). Build universities to keep tech moving `[2:44:00]` `[2:21:01]`.
8. **Colonise for inputs, not vanity:** Cuba imports almost all its grain, so he takes **Siam** (rice/cotton, future opium) and **colonises the Congo** (cotton/dyes, unopposed). Leave distant colonies unincorporated if incorporation would take ~13+ years `[3:10:03]` `[3:15:05]`.
9. **Forming a confederation needs *puppets*, not protectorates** — convert subjects to puppets first (build army to intimidate them into accepting), then form `[3:27:03]`.
10. **Don't route strategic inputs through a subject you might lose** — his lead supply ran through subject Peru-Bolivia and was cut the moment Brazil occupied it `[3:33:30]`.

!!! warning "Two patch traps he calls out"
    - The **"short-term tax cut" event is actually *permanent*** on this build — take "temporary embarrassment" instead `[2:32:32]`.
    - **Electricity micromanagement is miserable** — set it to auto-expand + subsidise and forget it `[2:56:01]`.

By now you have a migration-fed, sin-goods + consumer economy, independence, Great Power status, a power bloc, and colonies feeding your inputs. The opening through Phase 5 is the bit worth copying exactly; from here on, copy the *habits* below — not the conquests.

## Phase 7 — The late game & how it ends (~1883 → 1921)

Pure principles now: the wars and timings are RNG, but the economic habits transfer.

1. **You do not have to go communist — this run wins on Laissez-Faire.** When the Trade-Union/Communist IG gets powerful, *appease* it with social laws (Workers' Protections → Graduated Taxation → Right to Associate, plus Women's Suffrage) and even seat it in government, but **keep your economic system on Laissez-Faire**. He flirts with the command-economy path the whole game and never takes it — "communism kind of just makes your economy die" `[3:48:30]` `[5:26:01]`.
2. **Women's Suffrage is a labour-supply lever** — it pulls ~30% more workers into the market. Wages dip hard short-term (≈3.3 → 1.48) but capitalist profits surge `[4:02:31]` `[4:15:30]`.
3. **Pass Free Trade under a left coalition by swapping one market-liberal industrialist into government** — the protectionist Industrialist IG is what blocks it `[4:12:36]`.
4. **Two habits that save you from false panics:** never run labour-saving PMs while pops are unemployed (he had ~150k idle), and after any big PM/institution/welfare change **wait a month or two for the market to re-settle before diagnosing a profit "crash"** `[4:08:33]` `[4:10:01]`.
5. **Don't sit on the investment pool** — he left £56M, then £275M, idle; keep construction running (steel-frame buildings, more sectors) `[4:08:01]` `[5:19:00]`.
6. **Cars are the breakout late-game earner** (Automobiles + Steel Motors) — they need rubber, which is the real reason the Congo colony matters `[4:33:30]`.
7. **Release low-SoL colonies as colonial nations** so their numbers stop dragging your average SoL (Congo sat at ~7); released countries inherit your laws `[4:37:30]` `[5:01:00]`.
8. **Late wars (Brazil, then a regime-change war on communist Spain):** split your army to **defend Havana before any offensive landing**, use the **teleport-army trick** (dismiss commanders, disband and rebuild the army at a home front) to relocate troops, and accept a white peace when a transatlantic landing just won't land `[4:48:08]` `[4:53:00]` `[5:24:00]`.

**How it ends (1921):** Cuba finishes **#1 Great Power**, ~**£450M GDP** after forming the **Antillian Confederation** (puppets first), Havana at ~30 standard of living — and still on **Laissez-Faire**. The sin economy plus cars carries it: roughly, per week, cigars £188k, sugar £238k, Bacardi/groceries £500k, cars £1.15M. Two honest closing notes from him: the Cuba DLC "feels a little OP," and incorporating the confederation's subjects was *probably worse* than leaving them autonomous tax-payers — so don't treat that last step as obviously correct `[5:25:31]` `[5:26:01]`.

## Pitfalls checklist

- [ ] Built the construction backbone (lumber/tools/iron/rail) *before* plantations `[0:13:30]`
- [ ] Took the Influential Planter governor, not the Experienced Extractor `[0:21:00]`
- [ ] Did **not** join Spain's market `[0:28:30]`
- [ ] Founded the cigar/sugar companies *before* foreigners bought the buildings `[0:44:31]`
- [ ] **Conscripted early** — the run's biggest self-named mistake was conscripting too late `[1:29:31]`
- [ ] Defended Havana before launching naval invasions `[1:26:30]`
- [ ] Nationalised *before* Laissez-Faire, and never went Laissez-Faire while a subject `[2:10:02]`
- [ ] Refused the (permanent) "short-term tax cut" event `[2:32:32]`
- [ ] Converted protectorates to puppets *before* trying to form the confederation `[3:27:03]`
- [ ] Kept strategic inputs (grain, lead) off war-vulnerable subjects `[3:33:30]`
- [ ] Kept the economy on Laissez-Faire — appeased the trade unions without flipping to a command economy `[5:26:01]`
- [ ] Didn't run labour-saving PMs while pops were unemployed, and didn't leave the investment pool idle `[4:08:33]`
- [ ] Defended Havana before offensive landings in the late wars too `[4:48:08]`

## See also

- [Restoring the Spanish Empire (Cuba)](cuba-spanish-restoration.md) — the strategic case study this guide accompanies (the full-run highlight reel).
- [Construction](../economy/construction.md) · [Companies](../economy/companies.md) · [Trade](../economy/trade.md) · [Citizenship & Acceptance](../laws-and-politics/citizenship-and-acceptance.md) · [Small-Nation Play](../diplomacy/small-nation-play.md) · [War & Naval Invasions](../military/war-and-naval-invasions.md) · [Power Blocs](../diplomacy/power-blocs.md)
- **Source notes:** [01-early-mid-game](https://github.com/yosbotnet/vic3/blob/main/notes/cuba-trading-in-sin-live/01-early-mid-game.md)
