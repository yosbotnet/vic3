---
sources:
  - ../../notes/tutorials/09-power-blocs.md
wiki:
  - https://vic3.paradoxwikis.com/Power_blocs
generated_at: 2026-05-16
---

# Power Blocs

## What it is
A Power Bloc is a Leader-headed union of countries built around a **Central Identity Pillar** (Trade League, Sovereign Empire, Ideological Union, Military Treaty, or Religious Convocation). Members share **Principles** (cumulative bonuses), and the Leader gains a unique pillar-locked diplomatic action (subjugation, forced regime change, conversion). Running a Bloc is a continuous balancing act between **Leverage** (the recruitment lever), **Cohesion** (the upkeep number that scales Mandate income), and **Prestige** (which gates leadership challenges). It is the single largest mid- and late-game lever a Great Power has for projecting influence without conquest.

## Mechanics
1. **Formation gate** — 500 Influence, country rank Great Power / Major Power / Unrecognized Major Power, and NOT on Isolationism. Forming costs relations with every other Bloc Leader. *Decision rule:* don't form until all three thresholds are met and you have a target Pillar already in mind — you're paying a global relations bill the moment you press the button.
2. **Central Identity Pillar (locked)** — Pillar choice is permanent unless you dissolve and reform the Bloc. Without the Sphere of Influence DLC only Trade League is available to form. *Decision rule:* pick the Pillar for the **Leader action** you'll actually use (Sovereign Empire = subjugate; Ideological Union = Force Regime Change; Religious Convocation = convert state religion), not for its Principles — Principles are swappable, Pillars are not.
3. **Mandates and Principles** — Each Pillar locks you to a choice between two starting Mandates; subsequent Mandates can pick any Principle. Each Principle has 3 levels. *Decision rule:* **never drop one of your two primary Principle options** — losing both inflicts a permanent Cohesion penalty for as long as it's missing.
4. **Earning Mandates** — Need 2,000 progress per Mandate. Weekly progress = (Bloc rank bonus + sum of Member contributions) × Cohesion multiplier. *Decision rule:* a single Great Power Member is worth five Minor Members for Mandate income — recruit high-rank first if your Cohesion can hold them.
5. **Leverage Advantage vs Leverage Factor** — *Advantage* is the visible map number (need **+200** to invite). *Factor* is the hidden generator: your Factor ÷ total Factor (yours + every other Bloc's + the target's own resistance) = your share of the target's 1,000-point Current Leverage pool. *Decision rule:* aim to hold ~20 percentage points more Factor share than the target itself — that's what +200 Advantage represents.
6. **Stacking Factor** — Sources: Interest in Region (+100), Strategic Adjacency (+100, counts via your subjects or theirs), Shared Cultural Trait (+150), Economic Dependence (buildings via Investment Rights + trade routes), Treaty articles (Trade Privileges / Power Bloc Embassy / Investment Rights ≈ **+300 each**), Diplomatic Mitigation from spare Influence, Cohesion bonus (+20% at Orchestrated). *Decision rule:* Treaty articles are the dominant lever — each one **adds to your Factor AND dilutes the target's own resistance share** in the same step.
7. **Leverage drift** — Current Leverage moves toward Predicted Leverage by `(predicted − current) × 0.02` per week, minimum ±1. *Decision rule:* recruitment is a **months-long campaign**, not a burst — stack Factor early and wait, don't expect to flip a target by article spam in the same year.
8. **Leverage Resistance** — Base by rank: GP 1,000 / Major 750 / Minor or UR Regional 500 / Insignificant or UR 250, modified by population and laws (Censorship gives +25%). *Decision rule:* negotiate Treaty articles that flip the target off resistance-granting laws (Censorship → Right of Assembly is the canonical swap).
9. **Inviting at +200** — Invite is relations-gated even when unlocked. A rejection costs −50 relations both ways; refusing another Bloc's invite also costs −50 and can escalate to a Diplomatic Play. *Decision rule:* fix relations BEFORE pulling the trigger — never spend hundreds of Influence on articles and then get refused for low relations.
10. **Cohesion** — Tiers: Orchestrated / Controlled / Stable / Divided / Fractured, each with a Mandate-progress modifier. Cohesion drifts ±1/week toward its target value. Inputs depend on Pillar: Trade League = trade/GDP dependence of every Member; Sovereign Empire = relations + Liberty Desire; Ideological Union = matching Government / Distribution-of-Power laws. *Decision rule:* if you lead a **Trade League, actively trade with every Member**, especially the smallest — a single neglected Member can drain tens of Cohesion points.
11. **Cohesion penalties** — Base modifier: +30 most Pillars, +15 Trade League. Each non-Leader-subject Member: −1 (Trade League), −2 (most), −3 (Sovereign Empire). Leader not being a GP = −50% Cohesion. *Decision rule:* Sovereign Empires should be built from subjects, not from independent Members — every free Member is double the penalty of a Trade League.
12. **Power Struggle** — Any Member with **+20% Prestige over the Leader** can start a Power Struggle. Holding **+15% Prestige for 12 months** (9 if reclaiming) flips leadership. *Decision rule:* check the Prestige delta **before** spending Influence to recruit — inviting a higher-Prestige country (e.g. France into a US-led Bloc with +24% Prestige) hands them the Bloc on a timer.
13. **Power Bloc Statue** — Built in Development. Every variant gives +3 Prestige; type-specific state bonuses include Ideological Union (+5 Influence, +25% political strength), Military Treaty (+25% conscripts), Religious Convocation (+25% conversion, −10% turmoil effects), Sovereign Empire (−25% decree cost), Trade League (+10% loyalists from movements, +10% infrastructure from population). *Decision rule:* place in the state where the **state-scoped** bonus pays back hardest (Trade League statue in your highest-pop state, Military Treaty in your largest conscription state, etc.).
14. **Leader diplomatic actions (5-year membership required)** — Sovereign Empire: subjugate a Member. Ideological Union: Force Regime Change. Religious Convocation: change a Member's state religion. *Decision rule:* if you JOIN a Sovereign Empire Bloc, you can be vassalized after 5 years — treat Britain's or Russia's Blocs accordingly.

## Game numbers & rules of thumb
- Formation: 500 Influence, GP / Major / UR Major rank, not Isolationism `[from 09-power-blocs]`
- Mandate threshold: 2,000 progress; rank bonus 1st +5, 2nd +4, 3rd +3, 4th +2, rest +1 `[from 09-power-blocs]`
- Member Mandate contribution: GP +10, Major +5, Minor +2, UR Major +2, UR Regional +1 `[from 09-power-blocs]`
- Invite threshold: **+200 Leverage Advantage** ≈ 20pp more Factor share than the target's own resistance `[from 09-power-blocs]`
- Total Current Leverage pool per target ≈ 1,000 points split across all Blocs and the target itself `[from 09-power-blocs]`
- Treaty articles: Trade Privileges / Power Bloc Embassy / Investment Rights each ≈ +300 Factor `[from 09-power-blocs]`
- Strategic Adjacency or Interest in Region: +100 Factor each; shared cultural trait +150 `[from 09-power-blocs]`
- Leverage drift: `(predicted − current) × 0.02` per week, min ±1 `[from 09-power-blocs]`
- Cohesion drift: ±1 per week toward target value `[from 09-power-blocs]`
- Base Leverage Resistance by rank: GP 1000 / Major 750 / Minor or UR Regional 500 / Insignificant or UR 250 `[from 09-power-blocs]`
- Censorship: +25% Leverage Resistance `[from 09-power-blocs]`
- Cohesion base: +30 most Pillars, +15 Trade League; non-Leader-subject Member penalty −1 / −2 / −3 (TL / most / SE); non-GP Leader −50% Cohesion `[from 09-power-blocs]`
- Power Struggle: triggers at +20% Prestige over Leader; flip threshold +15% Prestige for 12 months (9 if reclaiming) `[from 09-power-blocs]`
- Failed invite / rejection: −50 relations both ways `[from 09-power-blocs]`
- Statue: +3 Prestige always, plus pillar-specific state bonus `[from 09-power-blocs]`
- **Multilateral Alliances tech gates the 1-ally limit.** Before that tier-4 tech, a country can hold exactly one Alliance at a time. Plan your one ally for the war you actually intend to fight. (verify tech tier on current patch) `[from beginner-tutorial ep16]`

## Strategy & playbook
**Pillar selection is the first and most permanent decision you make.** Because the Pillar is locked the moment you form, choose by **Leader action** and **Cohesion source**, not by Principles. If your endgame plan is to vassalize Belgium, the Netherlands, and Portugal for their colonies, that's Sovereign Empire. If you want to flip Spain's government to match yours to unlock a personal union path, that's Ideological Union. If you have no specific Leader action in mind and just want a reliable economic engine, Trade League is forgiving (low base Cohesion cost, no subject requirement) and remains the only option without the Sphere of Influence DLC. Whatever you pick, **assume you'll never change it** — your Pillar dictates your Cohesion math for the rest of the campaign.

**Recruitment is a Factor-stacking and Resistance-shrinking problem solved simultaneously.** The 1,000-point Current Leverage pool is shared between you, every other Bloc bidding on the target, and the target itself. You need ~20pp more share than the target. The fastest move is a full Treaty stack — Trade Privileges + Power Bloc Embassy + Investment Rights gives roughly +900 Factor and simultaneously dilutes everyone else's share, including the target's. Layer that on top of Interest in Region (+100), Strategic Adjacency (+100 if you or a subject border a strategic region the target or a subject of theirs holds), and a shared cultural trait (+150) and you can dominate a Minor's leverage chart inside 2–3 years. Use Influence Mitigation from any excess Influence you're not spending elsewhere. Crucially, negotiate articles that **also flip the target's laws** — getting them off Censorship cuts their Resistance by 25%, doubling your effective lead.

**Cohesion is the upkeep tax that decides whether the Bloc is a Mandate machine or dead weight.** Mandate progress is multiplied by Cohesion tier — at "Stable" you're losing ~10% progress, at Fractured you barely earn Mandates at all. The Pillar dictates your maintenance work: Trade League Leaders must actively maintain trade routes with **every** Member, especially the smallest (a Luxembourg with no trade dependence can singlehandedly cost 30+ Cohesion). Sovereign Empire Leaders must keep Liberty Desire low and recruit through subject relationships rather than free Members (−3 per non-subject Member adds up fast). Ideological Union Leaders should only invite countries already running compatible laws or accept that Force Regime Change is a multi-decade fix. **Build the Power Bloc Statue early** — the +3 Prestige is permanent insurance against Power Struggles, and the pillar-specific state bonus often pays for itself in one state.

**The Prestige check is the single most-missed mistake.** Before you spend a single Influence point on Treaty articles, look at the target's Prestige relative to yours. If they're already +20%, recruiting them hands them grounds for an immediate Power Struggle, and if they hit +15% Prestige for 12 months they take your Bloc. The canonical disaster is a US Trade League inviting France: France enters with materially more Prestige and starts the leadership challenge on day one. Either build your own Prestige first (statue, wars won, Companies, GDP) or accept that this Member is for someone else's Bloc.

**Treat the Bloc as portfolio management.** Every Member contributes Mandate income (good), but also a Cohesion penalty if they're not your subject (bad), and may dilute your average Prestige share. Stop growing when adding the next Member drops you a Cohesion tier — the Mandate gain from the new Member won't make up for the multiplier loss across the whole Bloc. Recruit Great Powers and Major Powers preferentially (5× the Mandate contribution of a Minor) and use Minors mainly when they're your existing subjects (no Cohesion penalty) or when they unlock Strategic Adjacency on a more important target.

**Per-target leverage tooltip:** hover a target country on the Power Bloc map to see your bloc's current AND predicted leverage vs all competing blocs, with per-week countdown. Identify the marginal rival and target *their* leverage source (improve relations to break adjacency, etc.) rather than only stacking your own. `[from beginner-tutorial ep09]`

**Rivalry as an influence injection.** Declaring a Rival gives a one-shot ~400 Influence boost on top of ongoing per-week generation. Useful when a few hundred influence short of a formation cost or large diplomatic action — pick a country that will be your rival anyway. `[from beginner-tutorial ep09]`

## Common pitfalls
- **Inviting a higher-Prestige Member.** Triggers an immediate Power Struggle. Check the Prestige delta BEFORE spending Influence on Treaty articles. `[from 09-power-blocs]`
- **Joining a Sovereign Empire Bloc.** After 5 years the Leader can subjugate you. Be wary of Britain's and Russia's Blocs unless you're a willing junior.
- **Burning Influence on an unwinnable target.** Each Treaty article costs Influence (≈50 for an Embassy). If the country can't realistically join (better Bloc closer, hostile relations, too high resistance), that Influence is gone.
- **Reflexively rejecting another Bloc's invites.** Each rejection is −50 relations; repeated rejections turn the rival Leader hostile and can escalate to a Diplomatic Play. Cut off their **Factor** so they never hit +200 in the first place.
- **Swapping out a primary Principle.** Dropping one of your two starting Principles inflicts an ongoing Cohesion penalty until restored.
- **Trade League Member with no trade.** Single largest Cohesion drain a Trade League can suffer — actively place trade routes with every Member, including the smallest. `[from 09-power-blocs]`

## See also
- **In this wiki:**
  - [Small Nation Play](small-nation-play.md) — flip side: how to survive being a Bloc target.
  - [Foreign Investment](../economy/foreign-investment.md) — Investment Rights treaty articles drive both Factor and Economic Dependence.
  - [Trade](../economy/trade.md) — Trade routes are the Cohesion lifeblood for Trade League Bloc Leaders.
  - [Companies](../economy/companies.md) — Companies feed Prestige, which gates Power Struggles.
  - [War and Naval Invasions](../military/war-and-naval-invasions.md) — failed invites and rejected demands can escalate into Diplomatic Plays.
  - [Passing Laws](../laws-and-politics/passing-laws.md) — your law profile constrains which Pillars and Principles work for you.
- **Official wiki:**
  - [Power_blocs](https://vic3.paradoxwikis.com/Power_blocs)
  - [Diplomacy](https://vic3.paradoxwikis.com/Diplomacy)
  - [Subjects](https://vic3.paradoxwikis.com/Subjects)

## Sources
- `../../notes/tutorials/09-power-blocs.md`
