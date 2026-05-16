---
sources:
  - ../../notes/tutorials/19-military-army.md
wiki:
  - https://vic3.paradoxwikis.com/Land_warfare
generated_at: 2026-05-16
---

# Army (2025 mechanics)

## What it is
The Army is Victoria 3's land force, but mechanically it is a supply-chain problem first and a tactical instrument second. Battalions are the unit cells; Barracks (and Conscription Centers, on mobilization) are the buildings that staff them; Generals organize them; Army Model laws set the ceilings; and every Battalion type, mobilization toggle, and Production Method binds your Army to specific input goods on your Market. You win wars by structuring this supply chain so it survives the spike when you mobilize — and by shaping fronts via Naval Invasions and Strategic Objectives, because direct tactical control is deliberately limited.

## Mechanics

1. **Battalion upgrades are one-way** — Each Battalion is Infantry, Cavalry, or Artillery; upgrading to a higher unit type (e.g. Skirmish Infantry) permanently rewrites its input goods. *Decision rule:* before upgrading, compare the new input goods against your Market. If you cannot afford the supply burden, leave it unupgraded — the only reversal is disband-and-rebuild.

2. **Veterancy grows with age** — Battalions accumulate offence/defence bonuses over time. *Decision rule:* when disbanding to cut costs, always delete the newest, lowest-veterancy Battalions first.

3. **Manpower vs Battalion count** — Manpower is the actual pop count in an Army; two armies with the same Battalion count can have very different Manpower after casualties. *Decision rule:* when deciding whether to engage, weigh offence/defence AND Manpower — never Battalion count alone.

4. **General organization cap** — Each General organizes 30 Battalions at base rank; exceed the cap and the Army bleeds organization. *Decision rule:* promote (half the bureaucracy cost of hiring) when bureaucracy is tight; hire fresh when you also want to shift Interest Group power.

5. **Officers require Primary Culture pops** — Barracks officers come from middle/upper strata and need full (level 5) cultural acceptance, which in practice means Primary Culture. *Decision rule:* do not build Barracks in states with few or no Primary Culture pops, or accept the No Organized Training PM and a worse training rate.

6. **Army Model law shapes the standing/conscript mix** — The law sets Barracks max level per state, conscription cap per state, conscription rate, and total conscript Battalions. *Decision rule:* low-population economies should lean conscript-heavy (National Militia / Mass Conscription / Peasant Levies) so pops remain in industry; pop-rich nations can absorb Professional Army.

7. **Mobilization options are goods costs that only bite on mobilization** — Supplies, supplements, transportation, and medical add Battalion bonuses and add their input goods to your Barracks only after mobilization (and add ~60% to overall Army goods cost). *Decision rule:* before mobilizing, audit your Market for every selected good, especially supplement crops, and pre-build trade routes or shift PMs if a spike would break supply.

8. **Pick the cheapest supplement available** — Tobacco, Liquor, and Opium each cost 0.5 units per Battalion; Chocolate costs 1.0 Sugar per Battalion. *Decision rule:* prefer Tobacco/Liquor/Opium over Chocolate whenever they exist in your Market.

9. **First Aid governs Recovery Rate** — Injured soldiers either die, become dependents (lost to workforce), or return to the line at a speed driven by Recovery Rate. *Decision rule:* unlock and enable First Aid as soon as available — high Recovery Rate keeps Manpower up mid-war.

10. **Conscripts are pulled from civilian jobs** — Adding conscripts in a state spawns a Conscription Center that hires those pops away from buildings, but only after mobilization. *Decision rule:* always keep a real standing Army; conscripts are reinforcements layered onto regulars, never the whole force.

11. **Cavalry + Artillery ≤ Infantry** — If combined Cavalry and Artillery Battalions exceed Infantry in an Army, the Army takes an organization penalty. *Decision rule:* recount the inequality whenever you add or upgrade units.

12. **Multi-Army doctrine** — Specialize Armies by role: *Main* = Infantry + Artillery with one offensive and one defensive General; *Cavalry* = Infantry + Cavalry on offensive orders (e.g. Rapid Advance) for breakthroughs; *National Guard* = Infantry (± Artillery), defensive orders only, the natural home for conscripts; *Landing* = Infantry + Cavalry sized for Naval Invasions, no conscripts. *Decision rule:* assign each Army a single role and lock its General orders to match — do not mix offence and defence inside one Army.

13. **General orders are conditional bonuses** — Advance Front boosts advancement speed and offence; Defend Front boosts defence; specialty orders (e.g. Rapid Advance) need composition or trait prerequisites such as ≥30% Cavalry. *Decision rule:* build the Army composition to unlock the order you want, not the other way round.

14. **Strategic objectives steer pathfinding** — Marking a state as Strategic Objective in the military lens makes Generals push toward it. *Decision rule:* use objectives to drive landed Armies toward link-ups with other fronts instead of nibbling adjacent provinces.

15. **Manufacture extra fronts** — A war starts with the fronts your borders create, but Naval Invasions force the enemy to split forces to defend new ones. *Decision rule:* against a higher-Manpower opponent, plan at least one Naval Invasion of an Incorporated State to halve the effective force-ratio on the main front.

16. **Naval Invasion sizing** — One Army plus one Navy per invasion; Naval Invasion efficiency drops below 100% once Battalions exceed Flotillas. *Decision rule:* size the Landing Army to the chosen Navy's Flotilla count and never exceed it.

17. **Naval Invasions can be lost** — The enemy Navy can intercept (losing at sea ends the invasion); on land, losing three battles ends it. *Decision rule:* only invade with naval superiority or against a country with no Navy in range, and have a reinforcement plan if the landing holds.

18. **Strategic Objective (right-click)** — right-click a state and select Strategic Objective to make your fronts prioritise pushing toward that state. The one player-side pathing control on top of Advance/Defend orders, useful for racing to an enemy capital. `[from beginner-tutorial ep17]`

## Game numbers & rules of thumb
Generalisable values from `[from 19-military-army]`:

- Skirmish Infantry consumes 1 Ammunition + 2 Small Arms per Battalion — input goods scale per Battalion.
- Mobilizing an Army increases its goods consumption by roughly 60%.
- Base General organization cap = 30 Battalions; promotion costs half the bureaucracy of hiring.
- Army Model Barracks max level per state: Peasant Levies 25, Professional Army 100, National Militia 5, Mass Conscription 100.
- Army Model conscription bonuses (cap / rate): Peasant Levies +25 / +4%, Professional Army +50 / +1%, National Militia +100 / +5%, Mass Conscription +100 / +3%.
- Peasant Levies grants −10% military goods cost (buyer-side only — producers still receive full price) and −25% weekly unit experience gain.
- Professional Army grants +100% weekly unit experience gain; Mass Conscription grants +100% training rate.
- Basic Supplies: +25% to current input goods plus 0.5 Grain per Battalion.
- Supplements: Tobacco / Liquor / Opium = 0.5 unit per Battalion; Chocolate = 1.0 Sugar per Battalion.
- Forced March: free at game start, costs morale, grants formation speed and mobilization speed.
- Naval Invasion: 1 Army + 1 Navy; 100% efficiency only while Battalions ≤ Flotillas; 3 lost land battles ends the invasion.

## Strategy & playbook

**Start from your pop budget, not your map.** The Army Model law is the single biggest lever you pull, and it should match your population. A low-pop nation that runs Professional Army strips industry of workers to staff a force that is still small; a pop-rich nation on Peasant Levies eats the −25% experience penalty for no good reason. Pick the law that lets your Battalions exist without crippling your construction queue, then live with the trade-offs (lower experience under militia laws, higher Market cost under Professional Army).

**Treat Barracks like any other building chain.** Build them in Primary Culture states so officer jobs actually fill, run General Training as the default PM, and only upgrade Battalion types when you have verified the new input goods on your Market. Upgrading without the supply is the single most common self-inflicted wound — there is no downgrade button. A smaller Army of supplied Line Infantry beats a bigger Army of unsupplied Skirmish Infantry.

**Organize four Armies by role, not by geography.** A Main Army (Infantry + Artillery, one offensive and one defensive General) anchors your primary front. A Cavalry Army (Infantry + Cavalry, locked to offensive orders like Rapid Advance) exploits gaps. A National Guard (Infantry, defensive orders) absorbs conscripts on home soil so mobilization does not strip border garrisons. A Landing Army (Infantry + Cavalry, no conscripts, sized to your Navy's Flotillas) handles Naval Invasions. Inside every Army, keep Cavalry + Artillery ≤ Infantry, and promote a General before any Army crosses the 30-Battalion cap.

**Audit mobilization before the war, not during it.** The ~60% cost spike from supplies, supplements, transportation, and medical only appears on mobilization, which is exactly when your Market is least forgiving. Pre-pick the cheapest supplement available (Tobacco / Liquor / Opium at 0.5/Battalion, never Chocolate at 1.0 Sugar if you have a choice), enable First Aid as soon as researched for the Recovery Rate, and walk through every mobilization good against your stockpile and trade routes. Over-mobilizing conscripts pulls pops out of buildings — your war economy can collapse from your own draft.

**Win fronts by making more of them.** Direct tactical control is thin; the real operational tool is front manufacture. Against a larger opponent, the question is not "can I win the main front" but "where can I land an Army to force the enemy to split." Pick a weakly defended Incorporated State, ensure naval superiority along the route, size the Landing Army to your Flotillas, and once ashore use Strategic Objectives in the military lens to push toward a link-up with your main front rather than wandering province-by-province.

**Mobilization options stack with Armed Forces fervor**: Extra Supplies (+25% goods for +10% offense and defense) plus fervor can push wartime goods consumption ~50% above peacetime. Sizing rule: build arms factories to roughly 2/3 of mobilized demand, not 1/1 of peacetime. `[from beginner-tutorial ep13, ep17]`

## Common pitfalls
- Upgrading Battalions you cannot supply — disband-and-rebuild is the only reversal.
- Building Barracks in states with no Primary Culture pops, then wondering why officers will not hire.
- Treating mobilization input goods as free — 50 mobilized Battalions on Chocolate is 50 extra Sugar overnight.
- Forgetting that conscripts leave civilian jobs when mobilized — over-mobilization wrecks the war economy.
- Mobilizing conscripts past an Army's General organization cap and quietly losing organization.
- Stuffing every Battalion onto the single starting front against a higher-Manpower enemy instead of opening a second front via Naval Invasion.
- Letting a Landing Army idle after the invasion is done — always reassign it to a front.
- Naval-invading with more Battalions than Flotillas and eating an efficiency penalty for free.

## See also
- **In this wiki:**
  - [Navy](navy.md)
  - [War and naval invasions](war-and-naval-invasions.md)
  - [Construction](../economy/construction.md)
  - [Treasury and deficit](../economy/treasury-and-deficit.md)
  - [Citizenship and acceptance](../laws-and-politics/citizenship-and-acceptance.md)
  - [Passing laws](../laws-and-politics/passing-laws.md)
- **Official wiki:**
  - [Land warfare](https://vic3.paradoxwikis.com/Land_warfare)
  - [Conscription](https://vic3.paradoxwikis.com/Conscription)
  - [Commanders](https://vic3.paradoxwikis.com/Commanders)

## Sources
- `../../notes/tutorials/19-military-army.md` — Victoria 3 Military Tutorial Part One: Army in 2025 (51:22 runtime).
