---
source_transcript: ../../transcripts/tutorials/12-treaty-port-and-market-price.md
source_video: https://www.youtube.com/watch?v=B_RqWrgYmJI
generated_at: 2026-05-16
---

# Treaty Ports & Market Price formation
**Source:** [Treaty Port and Market Price Tutorial in Victoria 3](https://www.youtube.com/watch?v=B_RqWrgYmJI) (20:12 runtime)

## Summary
Market Prices are driven by the ratio of Buy Orders to Sell Orders, capped at +/-75% of base price. A Treaty Port is a small state ceded by one country to another that sits in the cedant's Market (not the owner's), is exempt from tariffs/subventions/embargos, and lets the owner profit from both ends of trade while gaining Trade Advantage and access to otherwise-closed Markets. Knowing both mechanics matters whenever you trade with isolationist nations or want to read the goods UI correctly.

## Core mechanics
1. **Market Price formula (surplus)** — When Sell Orders > Buy Orders, price = (surplus / Buy Orders) * -75%, floored at -75%. DECISION RULE: if you want to raise the price of a Good you produce, suppress oversupply (cut production methods, export it, or stop subsidising). `[02:31]`
2. **Market Price formula (deficit)** — When Buy Orders > Sell Orders, price = (deficit / Sell Orders) * +75%, capped at +75%. DECISION RULE: to lower a scarcity price, add Sell Orders (build more producers or open imports) — adding only a few Buy Orders barely moves it because the denominator is Sell Orders. `[04:01]`
3. **Treaty Port belongs to the cedant's Market** — The state is owned by you but sits in the other country's Market; trade in that Trade Center moves their Goods, not yours. DECISION RULE: target Treaty Ports at countries whose Market you otherwise can't reach (isolationists). `[06:30]`
4. **Tariff/subvention/embargo exemption** — Treaty Port Trade Centers ignore all tariffs, subventions and embargos, including your own. DECISION RULE: don't expect tariff income from your Treaty Port routes; value them for access, not tax. `[06:00]`
5. **Law Variants unlock partial access** — Isolationism can come as a variant (e.g. Canton System) that allows Trade Centers only in one state. DECISION RULE: check the target's exact law variant before assuming they're fully closed — a Treaty Port can still be the only window in. `[07:02]`
6. **Treaty Port Trade Advantage scales with cedant exports** — You get Trade Advantage on any Good the cedant exports that you import, scaled by the cedant Market's share of world exports of that Good. DECISION RULE: prefer Treaty Ports in big exporting Markets; the bigger their slice of the world export, the more bonus you get. `[09:30]`
7. **Profits flow home** — Trade Centers in your Treaty Port are owned by your Financial Districts (split with the local FDs in the port, which are also your pops); dividends and reinvestment go to your pops/Investment Pool, taxed by you. DECISION RULE: treat the Treaty Port as a domestic investment site, not foreign aid. `[10:31]`
8. **Double-dip on cross-trade** — A Trade Route from the Treaty Port to your home Market makes profit on the export leg (in their Market) and the import leg (in yours). DECISION RULE: actively route Goods between the Treaty Port and home to capture both legs. `[11:34]`
9. **Goods UI is misleading with Treaty Ports** — On a Good's overview the top totals exclude Treaty Port volumes, but the bottom buyer/seller breakdown includes them. DECISION RULE: when calculating Market Price effects, trust the top numbers (or the main Market screen) and ignore the bottom breakdown rows tagged to the Treaty Port state. `[16:31]`
10. **Acquiring a Treaty Port** — Draft a Treaty with the Treaty Port article and offer money, or in war use the diplomatic demand "take a Treaty Port" / "investment rights", then add the war goal "enforce Treaty Article -> enforce Treaty Port". DECISION RULE: try the peaceful Treaty first; if score is hopelessly negative even at max subsidy, escalate via Force Diplomatic Play. `[17:31]`

## Game numbers & rules of thumb
- Market Price is bounded by -75% to +75% of base price. `[03:01]`
- Surplus price = (Sell - Buy) / Buy * -0.75. `[03:01]`
- Deficit price = (Buy - Sell) / Sell * +0.75. `[04:33]`
- Trade Advantage from a Treaty Port scales with the cedant Market's share of world exports of that Good (e.g. 6% of world small-arms exports -> ~12 Trade Advantage in the importing Trade Center). `[09:30]`
- Peaceful Treaty Port subsidies cap around £34.4k/week — if the AI score is still deeply negative at that cap, peaceful acquisition is off the table. `[18:00]`
- Existing Treaty Port example (Macau): £150/week for 99 years — cheap compared to wartime cost. `[05:32]`

## Common pitfalls
- Reading the bottom breakdown on a Good page and including Treaty Port sell/buy orders in your Market Price math — they don't count for your Market. `[14:31]`
- Expecting a Treaty Port to merge the foreign Market into yours; it doesn't — Goods imported into the port stay in the cedant's Market. `[08:01]`
- Assuming your own tariffs apply inside your Treaty Port — they don't, in either direction. `[06:00]`
- Trying to peacefully extract a Treaty Port from a hostile/isolationist nation without first checking the acceptance score; even maxed-out subsidies often fall thousands short. `[18:00]`

## Cheatsheet
1. To move a Market Price: add Sell Orders to drop a deficit price, add Buy Orders (or cut production) to raise a surplus price — remember the cap is +/-75%.
2. Pick Treaty Port targets that are isolationist and/or large exporters so you get both Market access and big Trade Advantage.
3. Build a Trade Center in the Treaty Port and route Goods back home to double-dip profits on export and import legs.
4. When reading a Good overview with Treaty Ports involved, use the top totals or the main Market screen — ignore the bottom breakdown for math.
5. Try Draft Treaty -> Treaty Port article first; if score is hopeless, use Force Diplomatic Play with the "take a Treaty Port" demand and the "enforce Treaty Port" war goal.

## See also
- [Markets](https://vic3.paradoxwikis.com/Markets)
- [Diplomatic_plays](https://vic3.paradoxwikis.com/Diplomatic_plays)
- [Wargoals](https://vic3.paradoxwikis.com/Wargoals)
