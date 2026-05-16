---
source_transcript: ../../transcripts/tutorials/09-power-blocs.md
source_video: https://www.youtube.com/watch?v=yT3QQvEdcrI
generated_at: 2026-05-16
---

# Power Blocs — formation, leverage, cohesion
**Source:** [Power Blocs Tutorial in Victoria 3](https://www.youtube.com/watch?v=yT3QQvEdcrI) (35:47 runtime)

## Summary
A Power Bloc is a union of countries built around a Central Identity Pillar that grants Principles (shared bonuses) to all Members and extra perks to the Leader. You form one as a Great/Major/Unrecognized Major power, then expand it by accumulating Leverage on target nations until you can invite them. Maintaining the Bloc means watching Cohesion (which scales Mandate gain) and Member Prestige (which can trigger a Power Struggle for leadership).

## Core mechanics
1. **Formation requirements** — Need 500 Influence, country rank Great Power / Major Power / Unrecognized Major Power, and NOT be on Isolationism. DECISION RULE: don't bother forming until you meet all three; expect a relations hit with every other Bloc Leader on formation. `[01:35]` `[09:00]`
2. **Central Identity Pillar (locked in)** — Pick one of Trade League, Sovereign Empire, Ideological Union, Military Treaty, or Religious Convocation. It cannot be changed later — only by leaving and reforming the Bloc. DECISION RULE: choose based on the unique Leader diplomatic action you want (subjugate, force regime change, convert state religion) and your law profile. Without the Sphere of Influence DLC only Trade League is available to form. `[02:31]` `[10:31]` `[12:01]`
3. **Starting Mandate / Principles** — Each pillar locks you to one of two starting Mandates on formation; after that any Principle is available. Each Principle has 3 levels; you can swap a Principle out when you earn a new Mandate. DECISION RULE: never drop one of your two primary Principle options — losing both causes a Cohesion penalty. `[03:02]` `[04:31]`
4. **Earning Mandates** — Need 2,000 Mandate progress; weekly progress comes from Bloc rank, Member count weighted by rank, and a Cohesion multiplier. DECISION RULE: recruit high-rank Members (Great Powers worth +10 progress each) and keep Cohesion at "Stable" or better. `[07:00]` `[08:01]`
5. **Leverage Advantage vs Leverage Factor** — Leverage Advantage (visible map number) determines whether you can invite a country (need +200). Leverage Factor (hidden in tooltips) is what generates Advantage — each Bloc's Factor divided by the target's Total Factor gives its share of the target's 1,000-point Current Leverage pool. DECISION RULE: to invite, push your share of Factor at least 20 percentage points above the target's own resistance share. `[13:01]` `[15:30]` `[24:31]`
6. **Leverage Factor sources** — Interest in region (+100), Economic Dependence (buildings via investment rights + trade routes), Strategic Adjacency (+100 if you OR a subject share a strategic region with the target OR a subject of theirs), shared Cultural Traits (+150 if shared), penalty for low primary culture acceptance, Treaty articles (Trade Privileges, Power Bloc Embassy, Investment Rights ≈ +300 each), Diplomatic Mitigation from excess Influence, and Cohesion status bonus (e.g. +20% at Orchestrated). DECISION RULE: stack Treaty articles on the target — each adds to YOUR Factor and to the total pool, which simultaneously dilutes the target's own resistance share. `[15:30]` `[16:00]` `[16:32]` `[19:30]` `[20:00]`
7. **Drifting leverage** — Current Leverage moves toward Predicted Leverage by `(predicted − current) × 0.02` per week, with a minimum of ±1. DECISION RULE: don't expect immediate results; sustained Factor advantage matters more than burst actions. `[21:30]` `[22:31]`
8. **Leverage Resistance** — Base by rank (GP 1000, MP 750, Minor/UR Regional 500, Insignificant/Unrecognized 250) plus population and laws (e.g. Censorship gives +25%). DECISION RULE: negotiate Treaty articles that flip the target off resistance-granting laws (e.g. Censorship → Right of Assembly) to lower their share of the Factor pool. `[26:01]` `[26:33]`
9. **Inviting at +200 Advantage** — Once you hit +200, "Invite" unlocks but it's still a relations-based decision — bad relations can mean rejection, costing −50 relations on either side. DECISION RULE: keep relations healthy before pulling the trigger; refusing invitations from other Blocs also costs −50 and can escalate to a Diplomatic Play. `[28:31]` `[29:03]`
10. **Cohesion** — Tiers: Orchestrated, Controlled, Stable, Divided, Fractured. Each gives a different Mandate-progress modifier. Cohesion is itself a drifting number (±1/week). Inputs depend on pillar: Trade League = trade/GDP dependence of Members; Sovereign Empire = relations + Liberty Desire; Ideological Union = matching Government/Distribution-of-Power laws. DECISION RULE: as a Trade League Leader, actively trade with EVERY Member, especially the lowest-ranked, or eat large Cohesion hits. `[30:00]` `[31:01]`
11. **Cohesion penalties** — All Blocs get +30 base except Trade League (+15 base). Non-Leader-subject Members give a per-Member penalty: −1 (Trade League), −2 (most), −3 (Sovereign Empire). Leader not being a Great Power = −50% Cohesion. DECISION RULE: don't bloat Sovereign Empires with independent Members; prefer Members who are subjects of you or another Member. `[31:31]` `[32:02]`
12. **Power Struggle (prestige-based leadership challenge)** — Any Member with 20% more Prestige than the Leader can start a Power Struggle. Holding 15% more Prestige for 12 months (9 for an ex-Leader reclaiming) flips leadership. DECISION RULE: never invite a country with materially more Prestige than you — you'll trigger an immediate struggle. `[32:31]` `[33:30]`
13. **Power Bloc Statue** — Built in Development; every variant gives +3 Prestige plus type-specific state bonuses (e.g. Ideological Union: +5 Influence and +25% political strength; Military Treaty: +25% conscripts; Religious Convocation: +25% conversion and −10% turmoil effects; Sovereign Empire: −25% decree cost; Trade League: +10% loyalists from movements and +10% infrastructure from population). DECISION RULE: place in the state where the bonus pays back hardest (e.g. high-pop state for Trade League infrastructure). `[11:00]` `[11:33]`
14. **Leader diplomatic actions (5-year membership required)** — Sovereign Empire: subjugate a Member. Ideological Union: Force Regime Change (Member's government/distribution laws match yours). Religious Convocation: change a Member's state religion to yours. DECISION RULE: pick pillar based on the action you want to use; treat joining a Sovereign Empire Bloc with caution — you can be vassalized after 5 years. `[09:32]` `[10:01]` `[10:31]`

## Game numbers & rules of thumb
- Formation cost: 500 Influence; rank must be GP / Major / Unrecognized Major; not Isolationism `[01:35]`
- Mandate threshold: 2,000 progress points `[07:31]`
- Bloc rank Mandate bonus: 1st +5, 2nd +4, 3rd +3, 4th +2, rest +1 `[07:31]`
- Member Mandate contribution: Great Power +10, Major +5, Minor +2, Unrecognized Major +2, Unrecognized Regional +1 `[08:01]`
- Cohesion tiers: Orchestrated / Controlled / Stable / Divided / Fractured (Stable shown as −10% mandate progress) `[08:31]`
- Leverage Advantage required to invite: +200 (equivalent to ~20% more Factor share than the target's own) `[13:01]` `[25:00]`
- Total Current Leverage pool per target country ≈ 1,000 distributed across all Blocs and the target itself `[14:30]`
- Treaty article leverage: Trade Privileges / Power Bloc Embassy / Investment Rights each ≈ +300 to Factor `[19:30]`
- Strategic Adjacency or Interest in Region: +100 Factor each `[16:00]` `[16:32]`
- Shared cultural trait: +150 Factor; low primary-culture acceptance: penalty `[18:30]`
- Cohesion bonus to leverage generation: e.g. +20% at Orchestrated `[20:00]`
- Weekly leverage drift = (predicted − current) × 0.02, min ±1 `[21:30]` `[23:02]`
- Cohesion drift: ±1 per week toward target value `[31:01]`
- Base Leverage Resistance by rank: GP 1000, Major 750, Minor/UR Regional 500, Insignificant/UR 250 `[26:01]`
- Censorship gives +25% Leverage Resistance `[26:33]`
- Cohesion base: +30 most pillars, +15 Trade League `[31:31]`
- Non-Leader-subject Member penalty: −1 Trade League, −2 other, −3 Sovereign Empire `[32:02]`
- Power Struggle: trigger at +20% Prestige over Leader; hold +15% for 12 months (9 if reclaiming) `[32:31]` `[33:30]`
- Failed invite / rejection: −50 relations both ways `[28:31]` `[29:03]`
- Statue: +3 Prestige always; Sovereign Empire statue gives −25% decree cost `[11:00]` `[11:33]`

## Common pitfalls
- **Inviting a higher-Prestige Member** — They will instantly start a Power Struggle (e.g. France into a US Bloc was 24% > Leader). Check Prestige delta BEFORE spending Influence on Treaty articles. `[33:00]` `[34:00]`
- **Joining a Sovereign Empire** — After 5 years the Leader can subjugate you. Be wary of joining Britain or Russia's Blocs. `[09:32]`
- **Wasting Influence on Treaty articles for an unwinnable target** — Each article costs Influence (e.g. 50 for an Embassy). If the country will never realistically join or stay, that Influence is gone. `[34:00]`
- **Repeatedly rejecting another Bloc's invites** — Each rejection is −50 relations; multiple rejections turn the Bloc Leader hostile and can escalate to a Diplomatic Play. Prevent the +200 threshold from being reached instead. `[29:03]`
- **Swapping out a primary Principle** — Dropping one of your two starting Principles causes a Cohesion penalty. `[05:02]`
- **Letting a Trade League Member have no trade with you** — Single biggest Cohesion drain for Trade Leagues (example: Luxembourg cost −35 Cohesion). `[30:30]`

## Cheatsheet
1. Hit 500 Influence + GP/Major rank + not Isolationism, then pick a Central Identity Pillar matching the Leader action you want — you CANNOT change it later.
2. Pick a starting Principle aligned to your strategy (Construction L3, Foreign Investment L3, and Companies L3 are strong general picks); never drop a primary Principle.
3. To recruit a target: establish Interest in Region, stack a Treaty (Trade Privileges + Embassy + Investment Rights = ~+900 Factor), keep relations positive, and verify they have LESS Prestige than you.
4. Push Leverage Advantage past +200 — remember leverage drifts; consistent Factor share matters more than short bursts. Lower their resistance by negotiating them off Censorship-type laws.
5. Maintain Cohesion: trade actively with all Trade-League Members; for Sovereign Empires keep Members as subjects; don't overgrow past what Cohesion supports.
6. Build the Power Bloc Statue in a high-impact state for the +3 Prestige and pillar-specific bonus.

## See also
- [Power_blocs](https://vic3.paradoxwikis.com/Power_blocs)
- [Diplomacy](https://vic3.paradoxwikis.com/Diplomacy)
- [Subjects](https://vic3.paradoxwikis.com/Subjects)
