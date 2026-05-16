---
sources:
  - ../../notes/tutorials/12-treaty-port-and-market-price.md
  - ../../notes/tutorials/13-how-to-work-trade-centers-and-trade-routes.md
  - ../../notes/tutorials/15-world-market-and-trade-center.md
wiki:
  - https://vic3.paradoxwikis.com/Markets
generated_at: 2026-05-16
---

# Trade

## What it is

Trade in Victoria 3 (post-1.9 / Charters of Commerce) is how your nation exchanges goods with the World Market — a global pool of imports and exports with an inherent demand floor that keeps prices from collapsing to zero [from 15-world-market-and-trade-center]. The system has three interlocking layers: (1) **Trade Centers**, the state-level building that actually moves goods in and out [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes]; (2) **Market Price formation**, where Buy-vs-Sell Order ratios push local prices up or down within a ±75% band of base price [from 12-treaty-port-and-market-price]; and (3) **Treaty Ports**, a special case where you own a state that sits inside a foreign Market and lets you double-dip on cross-Market trade [from 12-treaty-port-and-market-price]. The strategic value of trade is steering an auto-trading private sector — via Tariffs, Subventions, Trade Privileges, Interests, the Trade Policy law, and Companies — so that your imports come cheap, your exports earn a premium, and your goods balance underwrites construction, military, and standard of living.

## Mechanics

1. **World Market access** — Conceptual global pool with an Inherent Demand per good; to trade, a state needs a coast, a Port, and a Trade Center. Landlocked nations need Transit Rights [from 15-world-market-and-trade-center]. **Decision rule:** if a coastal state is missing a key local good, build Port + Trade Center before your first Construction Sector there [from 15-world-market-and-trade-center].

2. **Trade Center building** — The sole building that interacts with the World Market; has levels, can be subsidised/privatised/nationalised, and switches Production Methods. It consumes **Merchant Marines** (produced by Ports from Clippers) [from 15-world-market-and-trade-center]. **Decision rule:** if you have no Clippers, either switch the Trade Center PM to import Merchant Marines, or import Clippers so the Port can make them locally [from 15-world-market-and-trade-center].

3. **Trade Capacity gates volume** — Each Trade Center level provides capacity (base 50/level); each good consumes capacity per unit traded. When capacity caps, new export/import directions will not start [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** when an enabled route isn't flowing, check capacity first — expand a level or boost throughput before anything else [from 13-how-to-work-trade-centers-and-trade-routes].

4. **Trade Center placement — concentrate, don't spread** — Throughput bonuses (state traits, Company bonuses) only stack within one state [from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** pin most levels in your single best hub state (ideally Natural Harbors) and keep 1–2 outlier levels only where you need a local source of a specific imported good [from 13-how-to-work-trade-centers-and-trade-routes].

5. **Trade Advantage (per good, per direction)** — Base 100, modified by Trade Privileges with the partner, having a Declared Interest in their region, your Trade Policy law, spare Trade Capacity (up to +20%), Mercantilism, and Company-owned Trade Centers [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** when chasing dominance in one good, layer all sources simultaneously — no single source wins it alone [from 13-how-to-work-trade-centers-and-trade-routes].

6. **Relative Trade Advantage drives price** — `Relative Advantage = (your % of global advantage / your % of global trade volume) − 100%`. Positive means cheap imports / premium exports; negative means a price penalty [from 13-how-to-work-trade-centers-and-trade-routes][from 15-world-market-and-trade-center]. **Decision rule:** only push exports where your % of global advantage exceeds your % of global volume; otherwise raise advantage (Interests, Privileges, Mercantilism, Company) before scaling volume [from 13-how-to-work-trade-centers-and-trade-routes].

7. **Tariffs & Subventions** — Tariffs charge the Trade Center per unit (discouraging that direction); Subventions pay it per unit (forcing trade even on unprofitable routes) [from 15-world-market-and-trade-center]. The route stays auto-profitable while `local price − world price > tariff`; once it stops, only a Subvention will keep it running [from 15-world-market-and-trade-center]. **Decision rule:** on a good you want to export, set a small export Subvention to kickstart it and a max import Tariff so you never accidentally import it; remove the Subvention once Relative Trade Advantage carries it [from 13-how-to-work-trade-centers-and-trade-routes][from 15-world-market-and-trade-center].

8. **Declared Interests in importing markets** — You lose Trade Advantage points for every relevant market (top importer/exporter of the good) where you have no Interest [from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** spend Interest slots on the regions of the biggest importers of your target export; small countries in a region with no Goods Potential for that good will always import, making the Interest doubly valuable [from 13-how-to-work-trade-centers-and-trade-routes].

9. **Trade Privileges treaties** — Grant a large Trade Advantage bonus in both directions for the agreement's duration (default 25 years) [from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** sign Trade Privileges with the biggest importers of your target export; be willing to throw in a defensive pact, an obligation, or a single-good no-tariff to land it [from 13-how-to-work-trade-centers-and-trade-routes].

10. **Companies with the Trade Rights charter** — A Company with Trade Rights can build its own Trade Centers, and any Trade Center it owns gets extra Trade Advantage on the Company's goods [from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** hold off on expanding Trade Centers right before founding a relevant Company so it builds them itself; for an export-focused Company always grant Trade Rights + monopoly rights on its core building [from 13-how-to-work-trade-centers-and-trade-routes].

11. **Trade Policy law** — Mercantilism: +25% export / −25% import Trade Advantage, stronger tariffs/subventions. Protectionism: neutral advantage, normal tariffs, +25% leverage resistance. Free Trade: +25% advantage on everything but cannot tariff (only subventise); −25% leverage resistance. Isolationism: cannot build Trade Centers at all (only diplomatic goods exchange) [from 15-world-market-and-trade-center]. **Decision rule:** default Protectionism; switch to Mercantilism only if you are a dedicated exporter, Free Trade only if your economy is so dominant it needs no protection [from 15-world-market-and-trade-center].

12. **Market Price formula (surplus)** — When Sell Orders > Buy Orders, price = `(surplus / Buy Orders) × −75%`, floored at −75% [from 12-treaty-port-and-market-price]. **Decision rule:** to raise the price of a good you produce, suppress oversupply — cut production methods, export it, or stop subsidising [from 12-treaty-port-and-market-price].

13. **Market Price formula (deficit)** — When Buy Orders > Sell Orders, price = `(deficit / Sell Orders) × +75%`, capped at +75% [from 12-treaty-port-and-market-price]. **Decision rule:** to lower a scarcity price, add Sell Orders (build more producers or open imports) — adding Buy Orders barely moves it because Sell Orders is the denominator [from 12-treaty-port-and-market-price].

14. **Treaty Port belongs to the cedant's Market** — The state is yours, but it sits in the other country's Market; trade in its Trade Center moves their goods, not yours [from 12-treaty-port-and-market-price]. Treaty Port Trade Centers are exempt from all tariffs, subventions, and embargos in both directions [from 12-treaty-port-and-market-price]. **Decision rule:** target Treaty Ports at countries whose Market you otherwise can't reach (isolationists, Canton-System variants), and don't expect tariff income from them — value them for access [from 12-treaty-port-and-market-price].

15. **Treaty Port Trade Advantage and profit flow** — You get Trade Advantage on any good the cedant exports that you import, scaled by the cedant Market's share of world exports of that good [from 12-treaty-port-and-market-price]. Trade Centers in your Treaty Port are owned by your Financial Districts; dividends and reinvestment flow to your pops and Investment Pool [from 12-treaty-port-and-market-price]. **Decision rule:** prefer Treaty Ports in big exporting Markets, and route goods from the port back home — you book profit on the export leg (in their Market) AND the import leg (in yours) [from 12-treaty-port-and-market-price].

16. **Imports cost capacity too** — Capacity used to import a missing good is capacity not earning export revenue [from 13-how-to-work-trade-centers-and-trade-routes]. **Decision rule:** domesticate inputs (e.g., research Intensive Agriculture, switch domestic PMs) so Trade Capacity stays free for high-margin exports [from 13-how-to-work-trade-centers-and-trade-routes].

17. **Conquered/colony market access requires a port.** A non-contiguous conquered state has 0% market access until you build a port. An Anchorage is sufficient — you don't need a Cargo Port for market access. `[from beginner-tutorial ep07]`

## Game numbers & rules of thumb

- Market Price is bounded by **±75%** of base price [from 12-treaty-port-and-market-price].
- Surplus price = `(Sell − Buy) / Buy × −0.75`; deficit price = `(Buy − Sell) / Sell × +0.75` [from 12-treaty-port-and-market-price].
- Trade Center base capacity: **50 per level** [from 15-world-market-and-trade-center].
- **Natural Harbors** state trait: +15% Trade Capacity (and +5% Market Access Price Impact per level in the export hub case) [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes].
- Spare Trade Capacity gives **up to +20%** Trade Advantage [from 15-world-market-and-trade-center].
- **Mercantilism**: +25% export / −25% import Trade Advantage, stronger tariffs/subventions [from 15-world-market-and-trade-center].
- **Protectionism**: 0% advantage shift, +25% leverage resistance (best general-purpose) [from 15-world-market-and-trade-center].
- **Free Trade**: +25% Trade Advantage on everything; tariffs disabled, only subventions; −25% leverage resistance [from 15-world-market-and-trade-center].
- **Isolationism**: no Trade Centers possible; +50% authority, large leverage resistance [from 15-world-market-and-trade-center].
- Trade Privileges treaties run **25 years** by default and provide tens of points of Trade Advantage per partner [from 13-how-to-work-trade-centers-and-trade-routes].
- Relative Trade Advantage moves price roughly proportionally (example: +49% advantage → +12% export price) [from 13-how-to-work-trade-centers-and-trade-routes].
- Trade Advantage from a Treaty Port scales with the cedant Market's share of world exports (e.g. 6% of world small-arms exports → ~12 Trade Advantage in the importing Trade Center) [from 12-treaty-port-and-market-price].
- **Smallscale Trading** PM: −1 Merchant Marine input, −50% traded quantity per capacity — upgrade past it as soon as Merchant Marines are affordable [from 15-world-market-and-trade-center].
- Higher Trade Center PMs add only +1 Merchant Marine per level but massively raise traded quantity per capacity [from 15-world-market-and-trade-center].
- Colonization Rights charter: 100 Authority, requires an existing Declared Interest in a colonizable region [from 13-how-to-work-trade-centers-and-trade-routes].
- Company Prosperity has a **100 ceiling / 75 floor** once you've ever hit 100 [from 13-how-to-work-trade-centers-and-trade-routes].
- Peaceful Treaty Port subsidies cap around **£34.4k/week** in negotiation — if AI score is still deeply negative at the cap, escalate to war [from 12-treaty-port-and-market-price].
- **Unincorporated states:** flat −10% Market Access Price Modifier baseline (caps price arbitrage from colonies). `[from beginner-tutorial ep07]`

## Strategy & playbook

**Pick a hub, then build outward.** Audit your states for the Natural Harbors trait (or the best Trade Capacity modifier you have) and crown one state as your trade hub [from 13-how-to-work-trade-centers-and-trade-routes]. Pin its Trade Center to the outliner, set it to Regular Trading the moment Merchant Marines are affordable, and resist the temptation to drop one Trade Center level in every coastal state — throughput bonuses don't stack across states, so spreading thin gives you low capacity everywhere [from 13-how-to-work-trade-centers-and-trade-routes]. Outlier Trade Centers only earn their keep when a state genuinely needs a local source of a specific imported good (e.g. wood for early construction) [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes].

**Choose Trade Policy to match your economy.** Protectionism is the default for almost every nation: zero advantage shift but +25% leverage resistance and normal tariffs give you maximum flexibility [from 15-world-market-and-trade-center]. Switch to Mercantilism only when you have a genuine export-dominant economy and don't depend on imports — its −25% import advantage will hurt anyone who needs foreign goods [from 15-world-market-and-trade-center]. Free Trade is for late-game industrial juggernauts who can outcompete on raw advantage and don't need tariffs as a tool [from 15-world-market-and-trade-center]. Isolationism is a trade-cripple: you give up Trade Centers entirely for authority and leverage resistance, and even your own Treaty Ports become the only window your trade partners have into you [from 15-world-market-and-trade-center][from 12-treaty-port-and-market-price].

**To dominate an export, stack every Trade Advantage source you have.** Price only moves on **Relative** Advantage — your share of the global advantage pool minus your share of global volume — so raw points only matter relative to competitors [from 13-how-to-work-trade-centers-and-trade-routes][from 15-world-market-and-trade-center]. The reliable playbook: max-tariff imports of the good so you don't leak surplus, small Subvention on exports to kickstart it, Declared Interests in the regions of the top importers (and any tiny country in a no-Goods-Potential region), Trade Privileges with those top importers, Mercantilism if your portfolio supports it, and a Company with Trade Rights + monopoly on the producing building — that Company will then build its own Trade Centers and stack a further advantage bonus on that good [from 13-how-to-work-trade-centers-and-trade-routes]. Watch Relative Advantage in the goods overview: when it goes positive, drop the export Subvention before you keep paying for incentives you no longer need [from 13-how-to-work-trade-centers-and-trade-routes][from 15-world-market-and-trade-center].

**Read Market Prices as Buy/Sell ratios, not absolute numbers.** Prices are bounded ±75% of base and are entirely driven by the ratio of Buy to Sell Orders [from 12-treaty-port-and-market-price]. If a good you produce is hitting the −75% floor, the cure is to suppress oversupply (cut production methods, export it, stop subsidising) — adding buyers barely moves it. If a critical input is sitting at +75%, the only real fix is more sellers (more producers, opened imports) — and again, more buyers will not lower the price because Sell Orders is the denominator [from 12-treaty-port-and-market-price]. This is also why Subventions on a forced import work: they don't change Market Price, they just let your Trade Center keep importing at a loss until you can rebalance supply [from 15-world-market-and-trade-center].

**Use Treaty Ports as paid access to closed Markets.** A Treaty Port is the single best lever against isolationist or law-variant-locked nations (Canton System and similar) [from 12-treaty-port-and-market-price]. The state is yours but sits in their Market, so a Trade Center there trades their goods to their Market; route those goods home and you collect profit on the export leg (in their Market) and the import leg (in yours), with Trade Advantage scaled by the cedant Market's share of world exports for each good [from 12-treaty-port-and-market-price]. Trade Centers in the port are owned by your Financial Districts, so dividends and reinvestment flow to your pops and Investment Pool — treat it as a domestic investment site, not foreign aid [from 12-treaty-port-and-market-price]. Try Draft Treaty → Treaty Port article first with money offers; if AI acceptance is hopelessly negative even at max subsidy, escalate via Force Diplomatic Play with the "take a Treaty Port" demand and the "enforce Treaty Port" war goal [from 12-treaty-port-and-market-price].

**Force-pricing exports to fix a stuck price-floor producer.** If a building (e.g., Livestock Ranch) is unprofitable because the good has hit the −75% floor, set an export route on that good. Draining Sell Orders lifts the price. The export route IS the lever for the "suppress oversupply" rule. `[from beginner-tutorial ep04]`

## Common pitfalls

- Building a Trade Center level in every coastal state — you lose throughput stacking and end up with low capacity everywhere [from 13-how-to-work-trade-centers-and-trade-routes].
- Building a Trade Center in a landlocked state with no Transit Rights — it cannot reach the World Market [from 15-world-market-and-trade-center].
- Forgetting the Port (or Merchant Marines flow) — the Trade Center produces nothing without them [from 15-world-market-and-trade-center].
- Adding new export directions while already at Trade Capacity — nothing happens until capacity is freed or expanded [from 13-how-to-work-trade-centers-and-trade-routes].
- Forgetting a max import Tariff on a good you want to export — your own Trade Centers can start importing it and tank your surplus [from 13-how-to-work-trade-centers-and-trade-routes].
- Leaving export Subventions on a good that's now profitable on its own, or import Subventions on a good you no longer need — Trade Centers happily keep trading at a loss on your dime [from 13-how-to-work-trade-centers-and-trade-routes][from 15-world-market-and-trade-center].
- Spending Interests randomly instead of on the top importers/exporters of your target good — you eat permanent "lacking interests in relevant markets" penalties [from 13-how-to-work-trade-centers-and-trade-routes].
- Expanding the Trade Center yourself right before founding a Company — those levels won't be Company-owned and miss the Company's Trade Advantage bonus [from 13-how-to-work-trade-centers-and-trade-routes].
- Picking Free Trade and then watching a runaway import drain you — you can't tariff under Free Trade, only subventise [from 15-world-market-and-trade-center].
- Picking Mercantilism while still dependent on imports — the −25% import advantage hurts more than the +25% export advantage helps [from 15-world-market-and-trade-center].
- Reading raw Trade Advantage as the price modifier — only **Relative** Advantage moves price; raw advantage matters only via your share of the global pool [from 15-world-market-and-trade-center][from 13-how-to-work-trade-centers-and-trade-routes].
- Reading the bottom buyer/seller breakdown on a goods page and including Treaty Port orders in your Market Price math — they belong to the cedant's Market, not yours; use the top totals or the main Market screen [from 12-treaty-port-and-market-price].
- Expecting a Treaty Port to merge the foreign Market into yours — it doesn't; goods imported into the port stay in the cedant's Market [from 12-treaty-port-and-market-price].
- Assuming your own tariffs apply inside your Treaty Port — they don't, in either direction [from 12-treaty-port-and-market-price].
- Trying to peacefully extract a Treaty Port from a hostile isolationist without first checking the acceptance score — even maxed-out subsidies often fall thousands of points short [from 12-treaty-port-and-market-price].

## See also

- **In this wiki:**
  - [Companies](../economy/companies.md)
  - [Building Balance Sheet](../economy/building-balance-sheet.md)
  - [Construction](../economy/construction.md)
  - [Treasury & Deficit](../economy/treasury-and-deficit.md)
  - [Shipbuilding](../economy/shipbuilding.md)
  - [Foreign Investment](../economy/foreign-investment.md)
  - [Standard of Living](../pops/standard-of-living.md)
  - [Power Blocs](../diplomacy/power-blocs.md)
  - [Small Nation Play](../diplomacy/small-nation-play.md)
  - [Japan – Great Wave](../case-studies/japan-great-wave/index.md)
- **Official wiki:**
  - [Markets](https://vic3.paradoxwikis.com/Markets)
  - [Goods](https://vic3.paradoxwikis.com/Goods)
  - [Companies](https://vic3.paradoxwikis.com/Companies)

## Sources

- [Treaty Port and Market Price Tutorial in Victoria 3](https://www.youtube.com/watch?v=B_RqWrgYmJI) — `notes/tutorials/12-treaty-port-and-market-price.md`
- [How to Work Trade Centers and Trade Routes in Victoria 3](https://www.youtube.com/watch?v=FAghv7otHAE) — `notes/tutorials/13-how-to-work-trade-centers-and-trade-routes.md`
- [World Market and Trade Center Tutorial in Victoria 3](https://www.youtube.com/watch?v=E6fTjF9wb_I) — `notes/tutorials/15-world-market-and-trade-center.md`
