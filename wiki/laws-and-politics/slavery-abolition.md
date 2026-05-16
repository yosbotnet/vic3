---
sources:
  - ../../notes/tutorials/03-how-to-ban-slavery-in-the-usa-without-starting-a-civil-war.md
wiki:
  - https://vic3.paradoxwikis.com/Laws
generated_at: 2026-05-16
---

# Slavery Abolition (Applied Case-Study)

## What it is
A worked example of pushing a Law through against a Political Movement strong enough to start a civil war. The USA's slavery debate is the canonical test case — the pro-slavery Movement is large, the Southern Slaver IG is entrenched, and Activism drifts toward secession early — but the technique is general. Any time you want a Law that a powerful Movement opposes (monarchy under a republican Movement, atheism under a religious Movement, free trade under protectionist agrarians), the same race plays out: enact the Law before opposing Activism hits 100% and the secession counter completes. The page below extracts the decision rules that win that race in any nation.

## Mechanics

1. **Movement Activism thresholds** — Activism drives a Movement through staged consequences: 25% adds the Movement's support to your enactment Success Chance (endorsing) or Stall Chance (opposing); 75% spawns a secession counter starting at 0%; 100% lets that counter reach 100% and trigger a Diplomatic Play for war. DECISION RULE: before you touch a contentious Law, read both the hostile Movement's current Activism and its drift target. If drift is above 75%, plan the whole campaign as a race — your enactment must finish before the secession counter catches up.

2. **Suppress hostile / Bolster friendly** — Suppress lowers an opposing Movement's support over time, shrinking its eventual Stall contribution. Bolster raises a friendly Movement's support, growing its Success contribution. Both cost Authority. DECISION RULE: start the suppress/bolster pair months before you queue the Law so support shifts have time to compound. Do not refuse the action over a small Authority loss — the swing on Success/Stall is worth more than the marginal enactment-speed penalty.

3. **Surplus Authority shortens enactment time** — Spare Authority cuts enactment time, capped at -25%. DECISION RULE: don't sink Authority into low-value events, but don't hoard it either — suppress/bolster come first.

4. **Opposing IG happiness multiplier** — An opposing IG's Stall contribution is multiplied by 1.5x while that IG is unhappy. Pre-loading them to +10/+20 approval flips the multiplier off and can collapse Stall. DECISION RULE: immediately before the contentious Law, pass a Law the opposing IG strongly endorses. The +10 approval is locked in for the entire enactment of the next Law, then decays over 60 months.

5. **Distribution-of-Power happiness swing** — Changing a Distribution-of-Power Law gives every IG ±5 happiness per level of distance from the new Law, capped at ±10. The bonus persists through enactment and decays over 60 months. DECISION RULE: chain a friendly Distribution-of-Power Law back-to-back into the hostile Law so the +10 buffer overlaps the entire enactment window.

6. **Slow the revolution clock** — National Guard gives -10% revolution and secession progress speed; raising the Home Affairs institution to level 2 gives -20% and an extra -6% Movement Activism on both sides. DECISION RULE: pass National Guard and raise the institution before opening the contentious Law. The slower the clock ticks, the more events you can absorb.

7. **Save negotiations for the Law that needs them** — During enactment you negotiate with IGs for amendments that add Success or reduce Stall. Each negotiation round caps the Success gain at +3%, even if the amendment is worth more. Burning negotiations on an easy Law leaves you bankrupt on the hard one. DECISION RULE: bank negotiations; spend them on the contentious Law, and spend them defensively — if Success drops to 0% and an event is about to fire a -10% setback, negotiate FIRST to push Success above zero and dodge the setback.

8. **End-of-discussion compression** — When Success + Debate + Stall exceed 100%, an end-of-discussion factor compresses Stall (the case-study sees Stall pinned to 1%). DECISION RULE: pile on every Success modifier you can. At very high Success, raw opposition no longer matters.

9. **Amenability halves negotiation cost** — An IG at 100 amenability accepts negotiation demands at half cost; 75 is the upper edge of the "neutral" band. DECISION RULE: when several IGs are valid negotiation targets, hit the highest-amenability one first to buy more Success per unit cost.

10. **Replace hostile IG leaders via Agitators** — An IG's ideology often rides on its leader's. Inviting an Agitator who pulls the IG into their Movement lets you swap the leader; a different leader can flip the IG from opposing to neutral. DECISION RULE: pick an Agitator whose other endorsements don't conflict with the Law in flight (no radicals during a franchise restriction, etc.) and start the replacement early.

11. **Illegitimate cabinets still enact if a Movement endorses the Law** — Loading multiple parties into government to unlock more negotiation partners normally illegitimates the government and blocks enactment, EXCEPT when an endorsing Political Movement provides legitimacy. DECISION RULE: during the hostile-Law push, form the widest cabinet you can and lean on the bolstered friendly Movement for legitimacy. After the Law passes, reshuffle.

12. **Secession counter is event-pushable** — Secession only starts at 75% Activism and drifts toward current Activism (capped there) — it cannot complete unless Activism is at 100%. But events can add or subtract directly from the counter. With Activism near 100%, a single +5% event swing can finish the secession and start the war. DECISION RULE: while a hostile Movement is near 100% Activism, always pick the event option that lowers the secession counter, even if it costs something else.

13. **Political Lobbies as a quiet happiness lever** — A Lobby's Appeasement feeds into its members' IG happiness. DECISION RULE: take events that raise Lobby Appeasement when the hostile IG belongs to that Lobby — it's a passive way to keep them content through enactment.

14. **Don't unwind useful "bad" modifiers prematurely** — A thematically negative amendment that lowers the hostile Movement's Activism (a Fugitive Slave Act lowering pro-slavery Activism, for instance) is mechanically helping you while the parent Law is in flight. DECISION RULE: defer cleanup of these amendments until after the main Law passes.

## Game numbers & rules of thumb
- Movement Activism 25% → support contributes to Success/Stall.
- Movement Activism 75% → secession counter spawns at 0%.
- Movement Activism 100% → secession counter can complete and trigger war.
- Surplus Authority enactment-time bonus: capped at -25%.
- Distribution-of-Power Law change: ±5 happiness per Law-level distance, capped at ±10.
- Post-enactment IG happiness bonus decays over 60 months.
- National Guard: -10% revolution & secession progress speed.
- Home Affairs institution level 2: -20% revolution & secession speed, -6% Movement Activism (both sides).
- Unhappy opposing IG: Stall contribution × 1.5 (vs ×1.0 when content).
- IG amenability ≥ 75 is upper "neutral"; at 100 amenability, negotiation cost is halved.
- Max Success gain per negotiation round: +3%.
- Law-debate-failed event setback: -10% Success Chance.
- Secession counter drift cap: current Movement Activism.
- After the hostile Movement is gone, removing the opposing ideology from the relevant IG via Journal completion: ~10 years.

## Strategy & playbook

**Stage 1 — scout and slow the clock.** Open the Politics screen and read the hostile Movement's Activism and drift target. If drift sits below 25%, the Law is barely contested and you can push it through normally. Between 25% and 75% you have time but should still pre-stack. Above 75%, you're racing — and the first move is always to slow the clock, not speed the Law. Pass National Guard, queue the Home Affairs institution to level 2. The combined -20% revolution/secession speed plus -6% Activism on both sides buys the weeks you'll need for every later trick to take effect.

**Stage 2 — shift the support balance.** Suppress the hostile Movement, Bolster the friendly Movement. Both cost Authority; both compound over time, which is why you start them long before the Law is queued. If a friendly Movement doesn't exist yet, an Agitator endorsing the target Law can seed one. While you wait, replace hostile IG leaders. An IG that opposes only because of one leader's ideology can become neutral after an Agitator-driven leadership swap — and an opposing IG that becomes neutral cuts Stall at the root, before any of the multipliers above even matter.

**Stage 3 — happiness pre-loading.** Right before queuing the contentious Law, pass a cheap Law the opposing IG strongly endorses. A friendly Distribution-of-Power change is the workhorse here: ±5 per level, capped at ±10, locked in through the next enactment, decaying over 60 months. The point is to get the opposing IG to "content" or better, killing the ×1.5 Stall multiplier for the whole enactment window. This single swing often outweighs three rounds of negotiation.

**Stage 4 — coalition and negotiate.** Now form the widest cabinet you can. Loading multiple parties into government usually breaks legitimacy and freezes enactment, but a bolstered friendly Movement endorsing the Law restores legitimacy and unlocks negotiation with IGs across the aisle. Queue the contentious Law. Negotiate with the highest-amenability IG first (half cost at 100 amenability), capped at +3% Success per round. Bank one or two negotiations for emergencies — when Success drops to 0% and a -10% setback event is about to fire, you negotiate FIRST to push Success above zero and dodge the setback entirely.

**Stage 5 — event triage during enactment.** Once enactment starts, every event choice is a math problem. Protect: opposing IG happiness (no flavor picks that crash their approval), friendly Movement Activism ≥ 25% (below that, you lose its whole Success contribution), and the secession counter (always pick the option that lowers it when hostile Activism is near 100%). At sufficient Success the end-of-discussion factor pins Stall to ~1% regardless of opposition, so the dominant strategy is: pile Success modifiers, refuse Authority sinks, and let the timer expire in your favor. After the Law passes you still owe a Journal-driven cleanup (roughly 10 years to remove the residual ideology from the IG), but the secession risk is over.

## Common pitfalls
- **Taking the thematically "right" event choice.** Choosing to abolish slavery in a territory during the enactment can crater the opposing IG's approval and re-engage the ×1.5 Stall multiplier. During enactment, optimize for happiness math, not flavor.
- **Spending negotiations on easy Laws.** Negotiations are a finite war chest. Save them for the Law that actually has a Stall problem, and save at least one for defensive use against -10% setback events.
- **Leaving a hostile leader in place.** A single ideologically extreme leader can hold the IG in opposition all by themselves. If you don't start the Agitator-and-swap chain early, you'll arrive at enactment carrying avoidable Stall.
- **Accepting "free" Success boosts that lock in bad Laws.** Government-petition events (censorship, etc.) often dangle a big enactment-time bonus but bind you to a Law you'll regret and burn legitimacy you need for the coalition cabinet.
- **Forgetting the secession counter can be event-pushed.** Even with Activism "safely" below 100%, a +5% event can finish the secession counter. Always reduce the counter when offered.
- **Letting the friendly Movement decay.** Once enactment starts, friendly Activism tends to drift down. If it drops below 25% you lose its entire Success contribution. Refuse events that cut its Activism while the Law is in flight.

## See also
- **In this wiki:** [Passing Laws](passing-laws.md), [Political Movements](political-movements.md), [Citizenship and Acceptance](citizenship-and-acceptance.md), [Cultural Fervor](cultural-fervor.md), [Standard of Living](../pops/standard-of-living.md)
- **Official wiki:**
  - [Political_movements](https://vic3.paradoxwikis.com/Political_movements)
  - [Laws](https://vic3.paradoxwikis.com/Laws)
  - [Interest_groups](https://vic3.paradoxwikis.com/Interest_groups)

## Sources
- `../../notes/tutorials/03-how-to-ban-slavery-in-the-usa-without-starting-a-civil-war.md` — derived from the "How to Ban Slavery in the USA Without Starting a Civil War in Victoria 3" video tutorial.
