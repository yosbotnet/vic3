---
source_transcript: ../../transcripts/tutorials/03-how-to-ban-slavery-in-the-usa-without-starting-a-civil-war.md
source_video: https://www.youtube.com/watch?v=brIfnN0CgYk
generated_at: 2026-05-16
---

# Passing Hostile Laws Against a Strong Political Movement

**Source:** [How to Ban Slavery in the USA Without Starting a Civil War in Victoria 3](https://www.youtube.com/watch?v=brIfnN0CgYk) (39:18 runtime)

## Summary
When a powerful Political Movement opposes a Law you want to enact, passing it becomes a race against that movement's Activism reaching 100% and triggering a secession war. The general technique is to suppress the hostile movement, bolster the supporting movement, raise the opposing Interest Group's approval just before enactment, and pre-stack modifiers (institutions, government composition, sympathetic leaders) that slow revolution speed and boost enactment success. This applies to any contentious Law, not just slavery.

## Core mechanics

1. **Movement Activism thresholds** — Activism drives a Political Movement through escalating stages. At 25% the movement's support is added to your enactment Success Chance (if endorsing) or Stall Chance (if opposing). At 75% a secession starts. At 100% activism, the secession counter can also reach 100%, which triggers the Diplomatic Play for war. DECISION RULE: before touching a Law that a strong movement opposes, identify its current Activism and its drift target; if drift is heading above 75%, you must finish enactment before the secession counter catches up `[01:00]` `[01:31]`.

2. **Suppress hostile movements / Bolster friendly movements** — Suppressing lowers the opposing movement's support over time (reducing its eventual Stall contribution); Bolstering raises support of the friendly movement (increasing Success contribution). Both cost Authority. DECISION RULE: start suppressing/bolstering well before you queue the Law so the support shift has time to take effect; accept a small Authority hit because the swing on Success/Stall is worth more than a few % enactment-time `[02:30]` `[03:00]`.

3. **Authority and enactment time** — Surplus Authority lowers enactment time, capped at -25% `[03:00]`. DECISION RULE: when offered event choices, avoid sinking Authority unnecessarily, but do not refuse Suppress/Bolster over a small Authority loss — the support swing matters more.

4. **Approval of the opposing Interest Group** — An opposing IG's contribution to Stall is multiplied by 1.5x when they are unhappy. Pre-loading them to +10/+20 approval before enactment keeps that multiplier off and can drop Stall dramatically `[27:31]`. DECISION RULE: immediately before the contentious Law, pass a Law the opposing IG strongly endorses. The +10 approval is locked in for the whole enactment of the new Law (then decays over 60 months) `[04:30]`.

5. **Distribution-of-Power happiness swing** — Changing a Distribution-of-Power Law gives IGs ±5 happiness per level of distance from the new Law, capped at ±10. The bonus persists through enactment and decays over 60 months after passage `[04:30]`. DECISION RULE: chain a friendly Distribution-of-Power Law into the hostile Law back-to-back so the +10 buffer overlaps the entire enactment window.

6. **Slow the revolution clock with National Guard / Home Affairs** — National Guard gives -10% revolution and secession progress speed; expanded to level 2 it gives -20%. This buys time during the race. DECISION RULE: pass National Guard (or equivalent slowing Law) and raise the institution before starting the contentious Law `[05:01]` `[12:30]`.

7. **Law negotiation timing** — During enactment you can negotiate with IGs for amendments that add Success Chance (or reduce Stall). Save negotiations for the contentious Law where you need them most; if Success drops to 0% and an event is about to fire a setback, negotiate FIRST to push Success above zero and dodge the setback `[06:31]`.

8. **Endgame-of-discussion modifier** — When Success + Debate + Stall totals exceed 100%, an "end of discussion" factor cuts Stall down (the video sees Stall pinned at 1%). DECISION RULE: pile on every Success modifier you can — at very high Success, Stall collapses regardless of raw opposition `[28:00]`.

9. **IG amenability halves negotiation cost** — At 100 amenability, an IG's negotiation demands cost half as much; 75 is the upper edge of the "neutral" band. DECISION RULE: when multiple IGs can be negotiated with, negotiate with the highest-amenability one first to spend less for the same Success boost `[26:30]`.

10. **Stay under the 3% Success cap per negotiation** — Each negotiation can only push Success up by 3% per round even if the offered amendment is worth more. DECISION RULE: don't waste a high-cost negotiation when Success is already near 100% — pocket that IG for later if Success starts slipping `[27:31]`.

11. **Replace hostile IG leaders via Agitators** — An IG's ideology often comes from its leader. Inviting an Agitator who pulls the IG into their Political Movement creates leverage to replace the leader; a different leader can flip the IG from opposing to neutral on your Law. DECISION RULE: invite an Agitator whose endorsements don't conflict with the Law you're currently passing (e.g. avoid radicals if you're passing a restrictive franchise Law) `[14:00]` `[15:01]`.

12. **Illegitimate government can still enact if a Movement endorses the Law** — Putting both parties in government to enable broader negotiations normally makes the government illegitimate and blocks Law enactment, EXCEPT when a Political Movement endorses the Law (it provides legitimacy). DECISION RULE: form a wide coalition cabinet during the hostile-Law push specifically to unlock negotiation with IGs from multiple parties; lean on a bolstered friendly Movement for legitimacy `[24:01]` `[24:32]`.

13. **Secession counter mechanics** — Secession only starts at 75% Activism and drifts toward current Activism (capped there). It cannot reach 100% unless Activism is at 100%. Events can add/subtract directly from the secession counter — these become critical when Activism is near 100%, because a single +5% event can push secession over the line and start the war `[34:30]`.

14. **Political Lobbies as a happiness lever** — A Political Lobby's Appeasement adds to its members' IG happiness. DECISION RULE: take any event that raises Lobby Appeasement if the hostile IG might join it; lobbies are a passive way to keep a difficult IG content `[19:01]`.

15. **Don't unwind useful "negative" modifiers prematurely** — A bad Law amendment that lowers the hostile movement's Activism (e.g. fugitive slave act lowering pro-slavery Activism) is, perversely, working in your favor while you're trying to ban the parent Law. DECISION RULE: defer cleanup of these amendments until after the main Law passes, even though they're thematically against your goal `[11:30]`.

## Game numbers & rules of thumb
- Movement Activism 25% → support added to Success/Stall Chance `[01:00]`
- Movement Activism 75% → secession movement begins; counter starts at 0% `[01:31]`
- Movement Activism 100% → secession counter can reach 100% and trigger war `[01:31]`
- Surplus Authority reduces enactment time, capped at -25% `[03:00]`
- Distribution-of-Power Law change: ±5 happiness per Law-level distance, capped at ±10 `[04:30]`
- Post-enactment IG happiness bonus decays over 60 months `[04:30]`
- National Guard Law: -10% revolution & secession progress speed; level 2 institution: -20% `[05:01]` `[12:30]`
- Home Affairs level 2 also gives -6% Political Movement Activism (applies to both for and against movements) `[12:30]`
- Unhappy opposing IG: stall contribution × 1.5 (vs ×1.0 when not unhappy) `[27:31]`
- IG amenability ≥ 75 is neutral upper bound; at 100 amenability, negotiation costs are halved `[26:30]`
- Max Success increase per negotiation round: 3% `[27:31]`
- Secession counter drifts only up to current Movement Activism `[29:31]`
- Law-debate-failed event setback: -10% Success Chance `[06:31]`
- Slavery-debate Journal Entry completion (after movement gone): 10 years to remove the pro-slavery ideology from the relevant IG `[38:30]`

## Common pitfalls
- **Reflexively taking the "good" event option** — Choosing the thematically correct option (e.g. abolish slavery in territories) can crash your opposing IG's approval and tank Stall Chance. During enactment, optimize for happiness/Activism math, not flavor `[08:32]` `[11:30]`.
- **Negotiating away your best cards early** — Burning negotiations on an easy Law leaves you with nothing to spend when Success drops on the hostile Law. Hold negotiations for the Law that actually needs them `[05:30]`.
- **Letting a hostile-IG-aligned old leader linger** — A single leader's ideology can keep an IG opposing your Law. If you don't queue a replacement (Agitator, election) early, you'll arrive at enactment with avoidable Stall `[13:32]`.
- **Accepting "free" Success boosts that cost long-term legitimacy** — Government-petition events (e.g. censorship) can give big enactment-time bonuses but lock in a Law you'll regret and cost legitimacy you need for later coalition cabinets `[16:31]`.
- **Forgetting the secession counter can be event-pushed** — Even if max Activism is "safe" (<100%), event-driven +5% jumps to the secession counter can still end your run. Always pick the option that reduces the counter when offered `[34:30]`.
- **Ignoring the friendly Movement's Activism during enactment** — Once enactment starts, the friendly Movement's Activism tends to drop. If it falls below 25% you lose its entire support contribution to Success. Refuse events that cut its Activism while the Law is in flight `[28:30]`.

## Cheatsheet
1. Identify hostile Movement Activism and target; start Suppressing hostile + Bolstering friendly Movements immediately.
2. Pass slowing infrastructure first: National Guard → upgrade Home Affairs institution to level 2.
3. Queue a Distribution-of-Power (or other) Law that the opposing IG strongly endorses to land +10 happiness right before the main Law.
4. Replace any opposing IG leaders whose ideology drives opposition (invite Agitator, wait, swap).
5. Form the widest legitimate cabinet possible (lean on friendly Movement for legitimacy if needed) so you can negotiate with IGs across parties; negotiate with highest-amenability IGs first; cap each round at +3% Success.
6. During enactment, pick event options that protect: opposing IG happiness, friendly Movement Activism ≥25%, low secession-counter progress — even if the option seems thematically wrong.

## See also
- [Political Movements](https://vic3.paradoxwikis.com/Political_movements)
- [Laws](https://vic3.paradoxwikis.com/Laws)
- [Interest Groups](https://vic3.paradoxwikis.com/Interest_groups)
