---
sources:
  - ../../notes/tutorials/17-war-transvaal-naval-invades-the-british-mainland.md
wiki:
  - https://vic3.paradoxwikis.com/Warfare
generated_at: 2026-05-16
---

# War & Naval Invasions

## What it is

War in Victoria 3 is wrapped inside a **Diplomatic Play**: a structured escalation where each side adds **Wargoals**, sways third parties, and only then (if neither backs down) drops into shooting. The Play phase is where the war is largely won or lost — the Wargoals you pick define the **win conditions**, and the pause before unpause is your only free window to mobilize, balance Generals across Fronts, and queue Navy orders.

Once combat begins, the player's levers are: which Fronts to weight with manpower, whether each General is on **Advance** or **Defend**, what orders your Navies are running, and — when the geography demands it — **Naval Invasions** that bypass land Fronts to land Battalions directly on an enemy coast. A Naval Invasion is the answer when your Wargoals point at states you cannot reach overland.

## Mechanics

1. **Diplomatic Play maneuvering phase** — When a Play starts the game pauses; both sides add Wargoals and Sway third parties. *Decision rule:* do all military setup during this pause; Sway likely allies **before** adding Wargoals, because each added Wargoal raises Infamy and can scare off the very allies you want.

2. **Wargoal selection determines win conditions** — To push the enemy's war score below zero you must occupy either their capital state **or** every state tied to each of your Wargoals. *Decision rule:* never add a Wargoal you cannot realistically occupy. In particular, **War Reparations** requires occupying an *incorporated* state of the *target nation itself* — a subject's incorporated states do not count.

3. **Infamy threshold from stacking Wargoals** — Each added Wargoal adds Infamy. Crossing **25 Infamy** bumps you into the next Infamy tier and flips potential allies into refusal. *Decision rule:* before clicking the marginal Wargoal, check whether it pushes you past 25 — if allies matter, don't add it.

4. **Enlistment Efforts decree** — Adds **+5% Conscription Rate** and **+25% Training Rate** to a state. *Decision rule:* apply it to your highest-employment states before the war; it scales with employed workforce, so populous industrial states give the biggest manpower kick.

5. **Mobilization Options trade-offs** — *Transportation* options speed up front-to-front redeployment; *Medical Support* raises recovery rate (wounded returning to battle). *Decision rule:* skip Transportation on garrison armies that won't redeploy; always take Medical Support — recovery rate is a direct multiplier on effective manpower over a long war.

6. **Pre-war army filling** — Conscripts are not instant; hiring and mobilizing them costs real time. *Decision rule:* at the first pause of the Play, fill every General to their max Battalions, add extra Generals so no conscripts sit idle, and click Mobilize immediately. Time before unpause is **free** preparation — never waste it.

7. **Front manpower balancing** — Hovering the Front circles shows total manpower and average power (offense/defense weighted). *Decision rule:* if one Front is significantly outnumbered, shift Generals/armies. Quality offsets some imbalance but not large ones.

8. **General orders — Advance vs Defend** — A General on pure Defend never pushes — they only hold. *Decision rule:* if you start *losing ground* on a defensive Front, flip at least one General to **Advance Front** to claw it back. Pure-Defend is only correct on Fronts you genuinely intend to hold static.

9. **Naval commander orders (Intercept / Raid / Escort)** — Intercept engages enemy fleets in the same sea node; Raid sinks enemy Convoys; Escort protects yours. *Decision rule:* stack multiple commanders on one Navy so it can run several orders at once. Watch the red bottom-right notifications for sea nodes where your Convoys are being sunk and dispatch Escort/Intercept to that node.

10. **Defending against Naval Invasion** — Armies stationed at an HQ with orders on **Defend** automatically engage any Naval Invasion that lands in any state of that HQ. *Decision rule:* once a coastal region has no more active land Front, park a Defend army at that HQ — do not redeploy every Battalion to the remaining offensive Front.

11. **Naval Invasion sizing rule** — You can land **as many Battalions as you have Flotillas** in the invading Navy without penalty; the defender can stack their full HQ garrison against you. *Decision rule:* scout the target state's defender count first and pick the **weakest-defended coastal state**. The defender always has a structural edge, so attack where they're thinnest.

12. **Naval Invasion as a routing tool to inland HQs** — Coastal HQs often have a dotted "land crossing" line into an adjacent inland HQ. *Decision rule:* land in a weak coastal HQ, open a Front there, then march overland into the richer inland HQ (often the capital). You don't need a beach near the capital — you need a beach with a road to it.

13. **Navy repair downtime** — A defeated Navy returns to its HQ and all movement options grey out until a "ready" notification fires. *Decision rule:* never queue an invasion you can't escort. Wait for the repair notification before launching the next attempt; an unescorted landing is throwing Battalions into the sea.

14. **Companies as war prep** — Some Companies grant prosperity bonuses that reduce **military goods cost** or raise **army offense**. *Decision rule:* before declaring or expecting war, establish military-relevant Companies. Generic options worth roughly **−10% military goods cost** and **+5% army offense** are universally available — take them.

15. **Race-to-minus-100 endgame** — When neither side can be pushed below zero by Wargoal occupation, the war becomes a sprint: whoever first occupies enough enemy territory (capital especially) to drive the *other* side to −100 wins. *Decision rule:* once you've started occupying their capital, **stop** offensive pushes elsewhere and consolidate to defend *your* capital. Both clocks are ticking simultaneously.

16. **Naval invasion failure conditions** — the invasion fails if (a) the escorting fleet is defeated, or (b) you lose three land battles with zero landing progress accumulated. Each won battle adds a chunk of landing progress (~25-30% per battle in demos). (verify exact %) `[from beginner-tutorial ep07]`

17. **Battle deployment infrastructure cap.** Even after a successful landing, the first battle deploys fewer battalions than the army size if the target state's infrastructure is low. The deployment cap appears to scale with infrastructure. `[from beginner-tutorial ep07]`

## Game numbers & rules of thumb

Generalisable values from the demonstration scenario `[from 17-war-transvaal-naval-invades-the-british-mainland]`:

- Enlistment Efforts decree: **+5% Conscription Rate, +25% Training Rate** per state.
- Infamy tier jump at **25** — crossing it flips potential allies to refusal.
- War Reparations Wargoal needs an **incorporated** state of the target itself (or the capital) occupied to drive war score below zero — subject states do not satisfy this.
- Naval Invasion penalty-free cap: **Battalions ≤ Flotillas** in the invading Navy.
- Naval orders are stackable: assign multiple commanders to a single Navy and run **Intercept + Raid + Escort** in parallel.
- Default penalty (hitting your debt limit during war): **−5% army offense and defense**, and your construction queue pauses.
- The free preparation window is **Play-start to first unpause** — use it fully for mobilization, Generals, and Navy orders.

## Strategy & playbook

**The Play phase is the war.** Before any shot is fired, the Play pause is your single biggest lever. The order matters: (1) Sway potential allies; (2) only then add Wargoals, and only ones you can actually occupy; (3) keep total Infamy under the 25 threshold if those allies are decisive. Adding a Wargoal you cannot fulfill is worse than adding none — it locks the enemy's score above zero and forces you into a desperate war you didn't otherwise need.

**Mobilize like you're already at war.** During the same pause, apply Enlistment Efforts to your highest-employment states, fill every General to max Battalions, add extra Generals so no conscripts sit idle, take Medical Support on every army, take Transportation only on armies that will redeploy, and click Mobilize. None of this time costs you anything — the moment you unpause, conscripts and movement become real-time. Pre-war Company setup (military goods cost, army offense) compounds with all of the above.

**Run the land war by Front, not by army.** Hover the Front circles and rebalance whenever one side is heavily outnumbered. Offensive armies (main + cavalry) go to the Front with your Wargoals; defensive National Guard holds quiet Fronts. A General sitting on Defend will never push, so if you are losing ground on a Front you intended to hold, flip at least one to Advance Front. As soon as you fully clear a coastal region, do **not** dump every Battalion onto the remaining Front — leave a Defend army at that HQ to absorb the inevitable counter-invasion.

**Naval Invasions are how you reach Wargoals you can't walk to.** Stack commanders on each Navy so one Navy can Intercept, Raid, and Escort simultaneously. Watch the red Convoy-sunk alerts and dispatch Escort/Intercept to those sea nodes. For the landing itself, scout coastal states for the **weakest** garrison, match your landed Battalions to your Flotilla count to avoid the penalty, and prefer a coastal HQ with a dotted land crossing into the inland HQ you actually want — the beach is just the on-ramp. After a Navy is defeated it must repair at its HQ before it can move again, so never queue back-to-back invasions that you can't escort.

**Endgame: watch both clocks.** If the war can't be resolved by Wargoal-state occupation, it becomes a race to drive the *other* side to −100. The temptation is to throw everything at their capital, but if your own capital Front is thin you can lose first. Once you're occupying their capital, consolidate at home — both war scores collapse simultaneously and the loser is whoever runs out of defended territory first. Also watch your treasury: hitting the debt limit costs **−5% offense/defense** and pauses construction, which against a richer opponent becomes a doom spiral.

**Don't mobilize until late in the Diplomatic Play.** Mobilizing immediately consumes the full military-goods rate (small arms, artillery, ammunition jump instantly — not just grain). The 4-phase Play timer is your free prep window for fronts/generals/navies. Wait until phase 3-4 to mobilize. `[from beginner-tutorial ep06]`

**Don't "Force Diplomatic Play" against tiny single-state targets.** Without Force, a much weaker target may capitulate immediately with no war fought. Force is only needed if you want to add additional wargoals/maneuvers. `[from beginner-tutorial ep06]`

## Common pitfalls

- **War Reparations against an unreachable target.** A subject's incorporated states do *not* count — only the target nation's own. If the target has no reachable incorporated states, you can never push their war score below zero on that Wargoal.
- **Swaying allies after you've already raised Infamy.** Add Wargoals *after* finishing Sway attempts; crossing the 25 Infamy tier mid-Play can flip a likely ally into refusal.
- **Unexpected third Fronts from enemy subjects.** A small subject bordering you opens an extra attack vector. Scan the political map for subject borders before declaring.
- **Leaving a coastal HQ undefended after clearing its land Front.** The enemy will Naval Invade what was previously a quiet flank. Always assign a Defend army to that HQ before redeploying the rest.
- **Naval Invading with more Battalions than Flotillas.** Triggers the invasion penalty and wastes manpower; either shrink the landing army or wait for shipyard capacity.
- **Letting a war drag on against a richer opponent.** They can simply outlast you to default; once defaulted you lose 5% offense/defense and construction halts — a compounding spiral.
- **Pulling every army onto the offensive Front near the end.** If your own capital Front is thin, the race-to-−100 finishes against you first.

## See also

- **In this wiki:**
  - [Army](army.md)
  - [Navy](navy.md)
  - [Power Blocs](../diplomacy/power-blocs.md)
  - [Small Nation Play](../diplomacy/small-nation-play.md)
  - [Shipbuilding](../economy/shipbuilding.md)
  - [Companies](../economy/companies.md)
  - [Treasury & Deficit](../economy/treasury-and-deficit.md)
- **Official wiki:**
  - [Warfare](https://vic3.paradoxwikis.com/Warfare)
  - [Diplomatic plays](https://vic3.paradoxwikis.com/Diplomatic_plays)
  - [Wargoals](https://vic3.paradoxwikis.com/Wargoals)

## Sources

- `notes/tutorials/17-war-transvaal-naval-invades-the-british-mainland.md`
- [Warfare — Paradox Wiki](https://vic3.paradoxwikis.com/Warfare)
