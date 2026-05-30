---
sources:
  - ../../notes/tutorials/18-military-navy.md
  - ../../notes/comprehensive-tutorial-2025/05-war.md
wiki:
  - https://vic3.paradoxwikis.com/Naval_warfare
generated_at: 2026-05-16
---

# Navy (2025 mechanics)

## What it is
The Navy in Victoria 3 is primarily a **logistics arm**, not a battlefleet. Its three jobs, in order of impact on the war: (1) keep overseas armies supplied via **Convoys**, (2) **Raid** enemy supply routes to collapse the enemy's morale recovery, and (3) defeat hostile fleets in Sea Nodes. Outside war, the Navy is a major source of **Power Projection -> Prestige -> Rank -> lower interest rate**, so the spend partially recoups itself through cheaper Treasury debt. Navy units are **Flotillas** built in **Naval Bases**, fed by **Military Shipyards**, and led by **Commodores** through **Grand Admirals** with much larger command caps than land Generals.

## Mechanics — numbered

1. **Flotilla** — The basic naval unit, analogous to a battalion. The single most decisive number is **Manpower**, not Flotilla count: two Navies with the same number of Flotillas but different Manpower will be wildly mismatched. *Decision rule:* rebuild Manpower at port before re-engaging; never field "paper" Flotillas at low strength.

2. **Naval Commander ranks** — A **Commodore** organizes 20 Flotillas at base; promotion ladder runs up through **Grand Admiral**, who organizes up to 100. Exceeding command cap silently drops Organization across the whole Navy. *Decision rule:* size each Navy to its Commander's cap and promote before adding more Flotillas.

3. **Ship type ratio** — Three categories: **Light Ships**, **Capital Ships**, **Support Vessels** (Support unlocked with Submarines). **Capital + Support combined must not exceed Light Ships**, or Organization drops. *Decision rule:* at base tech keep Light >= Capital (e.g. 10 Frigates + 10 Man-o-Wars in a 20-Flotilla Commodore Navy); bias toward extra Light Ships if the Capital input good is scarce on the Market.

4. **Military Shipyard supplies the Navy** — A single building type produces the goods consumed by every ship Production Method, but each Shipyard can run only **one PM at a time** (e.g. Man-o-Wars OR Ironclads, never both simultaneously). *Decision rule:* don't upgrade Capital Ships to Ironclads until you have **Monitors** tech (so Light Ships also use Ironclads goods), OR import the missing good off the Market, OR build a second Shipyard on the other PM.

5. **Upgrades require HQ stationing** — Clicking "Upgrade" while a Navy sits in a Sea Node does nothing. *Decision rule:* pull Navies back to an HQ before applying any ship-type or PM upgrade.

6. **Naval Base hiring uses primary culture** — Officer professions need very high cultural acceptance; without **Multiculturalism** they effectively only hire from the **primary culture**. *Decision rule:* build Naval Bases in primary-culture coastal states until Multiculturalism is passed.

7. **State traits for naval industry** — Dockland-style coastal state modifiers give **+15% Military Shipyard throughput and +15 Flotilla cap** in that state. *Decision rule:* concentrate Shipyards and Naval Bases in these states first; they pay double dividends.

8. **Naval Orders** — The order menu has four roles: **Interception / Coordinated Interception** (start naval battles in a Sea Node), **Escort Convoys** and **Organize Merchant Convoys** (protect your own trade and military supply), and **Convoy Raiding** (disrupt the enemy's). *Decision rule:* match the order to the node's role — your supply route -> Escort; enemy supply route -> Raid; enemy fleet present and you can win -> Interception.

9. **Convoy Raiding wins wars** — Cutting an enemy supply route slashes their armies' **morale recovery**, so they break and retreat from battles faster. *Decision rule:* prioritize raiding key import nodes (Small Arms, Artillery, etc.) over fleet-vs-fleet brawls whenever possible — it does more damage per Flotilla than winning a naval battle.

10. **Overseas supply needs Convoys** — Armies in an HQ or on a contiguous land front cost zero Convoys; armies projected overseas consume Convoys scaled by battalion count and Sea Nodes traversed. *Decision rule:* route armies through allied territory to minimize Sea Nodes used, and check Convoy headroom before committing.

11. **Convoy cost formula** — Raw cost = `battalions x 10 x (1 + 0.1 x (sea_nodes - 1))`, then multiplied down by the Commander's supply-efficiency trait (the displayed efficiency is **truncated**, so actual savings are slightly better than shown). *Decision rule:* a 90-battalion army across 8 Sea Nodes is roughly 1,500 raw Convoys — only send it if your pool can absorb that on top of existing trade.

12. **Navy -> Power Projection -> Prestige -> debt cost** — Each Flotilla contributes more Power Projection (and thus Prestige) than a battalion does on the army side. Higher Prestige raises **Rank**, which lowers your **interest rate** on Treasury debt. *Decision rule:* count a chunk of Navy upkeep as debt-service reduction, not pure military spend.

13. **A Navy's ship count is your Naval Invasion capacity** — You can land at most as many regiments as the invading Navy has ships (6 ships → 6 regiments); exceeding it incurs a heavy invasion-efficiency penalty (see [War & Naval Invasions](war-and-naval-invasions.md)). *Decision rule:* purpose-build a transport Navy sized to the landing you intend — a small, cheap Navy is enough to seize a lightly defended coast. The [Belgium case study](../case-studies/belgium-conquer-colonize-react.md) takes the Congo with a six-ship landing of six regiments. (2025 comprehensive tutorial, [1:50:00])

## Game numbers & rules of thumb
- Commodore (lowest naval rank) caps at 20 Flotillas; Grand Admiral (highest) caps at 100 `[from 18-military-navy]`.
- No naval conscripts — Navy Manpower comes only from Naval Base employment `[from 18-military-navy]`.
- A Frigate (Light) consumes 1 Man-o-War good; a Man-o-War (Capital) consumes 3 Man-o-Wars goods — the good name is always the next-tier ship name `[from 18-military-navy]`.
- Ironclad Capital Ships need 3 Ironclads goods; Monitor Light Ships need 1 Ironclads good `[from 18-military-navy]`.
- One Military Shipyard = one Production Method at a time (Man-o-Wars OR Ironclads, never both) `[from 18-military-navy]`.
- Man-o-Wars goods are generally cheaper / more available on the world Market than Ironclads goods `[from 18-military-navy]`.
- Dockland-style state modifier: +15% Shipyard throughput, +15 max Flotillas in that state `[from 18-military-navy]`.
- Convoy supply cost: `battalions x 10 x (1 + 0.1 x (sea_nodes - 1)) x commander_efficiency` `[from 18-military-navy]`.
- Naval pathing picks the route with the **fewest** Sea Nodes — allied transit can dramatically shorten supply lines `[from 18-military-navy]`.
- Naval Invasion capacity: at most one regiment landed per ship in the invading Navy (e.g. 6 ships → 6 regiments) (2025 comprehensive tutorial, [1:50:00]).

## Strategy & playbook

**Early-game (sailing-era) build-out.** Survey your coast for dockland-style state modifiers and build your first **Military Shipyard** and **Naval Base** there, in a primary-culture state. Officer slots will sit empty in low-acceptance states and your Shipyard throughput will be 15% behind in non-dockland states — these two decisions compound. Stand up one Commodore Navy at 20 Flotillas (10 Frigates + 10 Man-o-Wars) before you try anything more ambitious. This is enough to escort one trade lane or raid one weak rival, and it generates respectable Power Projection for the price.

**Tech transitions are the trap.** The single most common naval blow-up is upgrading Capital Ships to **Ironclads** before researching **Monitors**. One Shipyard runs one PM — switch the PM to Ironclads and your Frigates (still on Man-o-Wars goods) starve; keep the PM on Man-o-Wars and your new Ironclads starve. The clean path is: research Monitors first, then flip the Shipyard PM to Ironclads so both ship tiers use the new good. The dirty paths are (a) import the missing good off the Market, or (b) build a second Shipyard on the other PM. Whichever path you pick, **pull the Navy back to its HQ** before clicking Upgrade or nothing happens.

**Wartime: orders matter more than ship counts.** Before war breaks out, identify the two or three Sea Nodes your economy depends on (imports of Small Arms, Artillery, Sulfur, etc.) and the enemy's equivalents. In war, assign **Escort Convoys** to yours and **Convoy Raiding** to theirs. Convoy Raiding is the highest-leverage naval action in the game: it doesn't kill enemy troops directly, it kills their **morale recovery**, so their armies break out of battles faster and retreat further. A modest raiding squadron behind enemy lines often does more than a "decisive battle" fleet does up front. Use **Interception** only on nodes where you can actually win the fleet engagement.

**Power-projecting overseas.** The Convoy formula punishes long routes superlinearly through the +10% per Sea Node multiplier. Before shipping a big army, check the route preview — a 90-battalion expedition across 8 nodes is roughly 1,500 Convoys, and that's on top of your peacetime trade Convoys. If you don't have headroom, the army arrives but its morale never recovers and it routs on first contact. Route through allied territory whenever pathing allows; it can halve the node count. Commander supply-efficiency traits help, and remember the displayed efficiency is truncated (a "0.6" trait is closer to 0.67), so your real Convoy spend is slightly lower than the tooltip suggests.

**Navy as a finance ministry.** Even outside war, holding a sizeable Navy is a debt-cost play. Power Projection from Flotillas feeds Prestige, Prestige feeds Rank, and Rank lowers your interest rate. If you're running consistent deficits to fund Construction, a Grand-Admiral-sized standing fleet can pay for a meaningful slice of its own upkeep through cheaper bond service. Treat the line item half as military, half as Treasury hygiene.

## Common pitfalls
- Upgrading Capital Ships to Ironclads before researching **Monitors** — one Shipyard PM can't feed both tiers and your fleet starves of inputs.
- Clicking **Upgrade** while the Navy is parked in a Sea Node — nothing happens until you move it to an HQ.
- Building Naval Bases in low-acceptance states pre-Multiculturalism — Officer slots sit empty on "qualifications" and the Base never fills out.
- Letting **Capital + Support exceed Light Ships** — silent Organization penalty across the whole Navy.
- Trying to garrison every Sea Node on a long trade lane (e.g. opium to East Asia) — impossible; keep a mobile Navy and react to enemy Raids instead.
- Sending a big army overseas without checking **Convoy headroom** — they arrive but never recover morale and rout on first contact.
- Doing manual Convoy math off the **truncated** commander supply-efficiency number — actual cost is slightly lower than what the tooltip displays.
- Treating Navy purely as a combat arm — ignoring its Power Projection / Prestige / interest-rate contribution leaves real money on the table.

## See also
- **In this wiki:**
  - [Army](army.md)
  - [War and naval invasions](war-and-naval-invasions.md)
  - [Shipbuilding](../economy/shipbuilding.md)
  - [Trade](../economy/trade.md)
  - [Treasury and deficit](../economy/treasury-and-deficit.md)
  - [Citizenship and acceptance](../laws-and-politics/citizenship-and-acceptance.md)
- **Official wiki:**
  - [Naval_warfare](https://vic3.paradoxwikis.com/Naval_warfare)
  - [Commanders](https://vic3.paradoxwikis.com/Commanders)
  - [Warfare](https://vic3.paradoxwikis.com/Warfare)

## Sources
- `notes/tutorials/18-military-navy.md` — Victoria 3 Military Tutorial Part Two: Navy in 2025 (26:41 runtime).
- `../../notes/comprehensive-tutorial-2025/05-war.md` — The Comprehensive Victoria 3 Tutorial (2025) | Iberian Twilight, by Tarkusarkusar, 2025-12-16 (chapter 5, War).
