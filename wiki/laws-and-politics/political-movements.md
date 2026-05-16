---
sources:
  - ../../notes/tutorials/20-political-movements.md
wiki:
  - https://vic3.paradoxwikis.com/Political_movements
generated_at: 2026-05-16
---

# Political Movements

## What it is
Political Movements are the post-Sphere-of-Influence (Pivot of Empire) layer through which you steer domestic politics. You no longer bolster or suppress Interest Groups directly — you act on movements instead. Each movement has an **Ideology**, a list of **Laws** it endorses or opposes, a **Support** number (the weighted political strength of Pops backing it), and an **Activism** number (how riled up those Pops are). Activism is what turns a quiet faction into law-pushing pressure, then into Radicals, then into a Revolution or Secession. Manipulating movements — bolster/suppress, who can vote, and which laws you choose to enact — is the main lever for shaping your country.

## Mechanics

1. **Support vs Activism** — Support is the total political strength of Pops backing the movement; Activism is how riled up they are. *Decision rule:* glance at Activism in the outliner. Under 25% the movement is inert on laws; at >=25% it affects law enactment; at >=50% it spawns Radicals every month; at ~75% it goes Insurrectionary and the Revolution / Secession warning appears. Watching Support alone is the classic mistake — a small but furious movement still revolts.

2. **Movement law stances (endorse / oppose / indifferent)** — Each movement lists the Laws it cares about. *Decision rule:* only movements that explicitly list the law you are enacting will help or hinder it; indifferent or unlisted = no effect. Use endorsing movements to push laws through and steer around opposing ones.

3. **Bolster / Suppress (now applied to movements, not IGs)** — Bolster increases a movement's attraction for new Pops; Suppress reduces it. *Decision rule:* Bolster movements whose endorsed laws you want to pass; Suppress movements blocking your agenda. This is your day-to-day political dial.

4. **Distribution of Power scales Support** — Pops contribute political strength according to the suffrage law. Under Census Suffrage, literacy adds up to +30 to political strength on top of the wealth check. *Decision rule:* if a movement's supporters are wealthy and literate, an open suffrage law strengthens them; if its base is poor peasants, restrictive suffrage neuters it. Suffrage shifts are a slow-acting but powerful counter-lever.

5. **Interest Group pressure & agitator leadership** — A movement "pressures" any IG that contains supporting Pops, weighted by their political strength. *Decision rule:* to install an Agitator as an IG's leader, that IG must appear in the movement's Pressured Interest Groups list — push the movement until the IG is captured.

6. **Revolution vs Secession assessment** — When the warning box appears it lists how many armies, conscripts, and states the rebels will take with them. *Decision rule:* compare rebel armies + states to your standing army + mobilisable conscripts. Small Revolutions can be allowed to fire and crushed cheaply; large Secessions usually cannot.

7. **Lock on armies / conscripts after the box appears** — Once the Revolution warning is up you can add conscripts but cannot remove armies or conscripts. *Decision rule:* never preemptively assign conscripts to states that might secede, and finalise conscript placement *before* a hot law starts enactment.

8. **Cancel-the-law escape hatch** — Stopping enactment before the Revolution bar hits 100% defuses the revolt, but imposes a 24-month cooldown on that law and may anger another movement that endorsed it. *Decision rule:* cancel only if the would-be rebel front is bigger than any opposing movement's reaction; otherwise ride it out. After the bar reaches 100%, cancelling no longer stops the war — your only exit is winning it.

## Game numbers & rules of thumb
- Activism >=25%: movement contributes to the enact / stall chance of its listed laws `[from 20-political-movements]`.
- Activism >=50%: movement generates Radicals every month `[from 20-political-movements]`.
- Activism ~75%: movement turns Insurrectionary; Revolution or Secession box appears `[from 20-political-movements]`.
- Census Suffrage wealth threshold to vote: wealth rating 15 `[from 20-political-movements]`.
- Census Suffrage literacy bonus: up to +30 political strength from literacy `[from 20-political-movements]`.
- Cancelling enactment imposes a 24-month cooldown before retrying that law `[from 20-political-movements]`.
- IGs currently in active Revolution cannot be added to government `[from 20-political-movements]`.
- Once the Revolution bar reaches 100%, cancelling the law no longer stops the war `[from 20-political-movements]`.

## Strategy & playbook

**Treat the outliner like a thermometer.** Every few months scan your active movements for Activism, not Support. A 5%-Support movement at 60% Activism is a Radical-spawning machine; a 30%-Support movement at 10% Activism is wallpaper. Anything trending past 25% deserves a click to see which laws it lists, and anything past 50% deserves an immediate plan: are you going to pass its law, suppress it, or out-empower it with a rival movement?

**Before you enact a hot law, audit every movement that lists it.** Open each, note endorse vs oppose, and add up political strength on both sides. Bolster the loudest endorsing movement (and, if you have time, shift suffrage in a direction that empowers its Pops); Suppress the loudest opposing one. This pre-work is what determines whether enactment crawls, stalls, or fires off a Revolution mid-bar.

**Place armies and conscripts BEFORE the Revolution box can appear.** The lock is one-way: once the warning is up you can only add, never remove. So never preemptively garrison conscripts in border or culturally-distinct states that might secede — they will leave with the rebels and there is no clawback. Treat the pre-enactment moment as your last chance to redistribute force.

**Use the cancel button strategically, not panickedly.** Cancelling defuses one revolt but costs you 24 months of cooldown on that law and can ignite a rival endorsing movement. Cancel only when the rebel bloc clearly outguns you AND no equally large movement was counting on the law passing. Often the right move with a small Revolution is to let it fire and crush it — Revolutions are how you cleanly purge an IG you cannot otherwise dislodge (IGs currently in revolt cannot enter government, but a defeated revolt leaves them weaker than a stalled law would).

**Agitators and IG capture.** If you have recruited an Agitator and want them to lead an IG, your job is to inflate the movement they joined until that IG appears in the movement's Pressured Interest Groups list. That single relationship — movement pressures IG, IG can then be led by movement's Agitator — is the cleanest way to swap a hostile IG leader for a friendly one.

## Common pitfalls
- Garrisoning conscripts in states that end up in the secession bloc — they leave with the rebels and cannot be pulled back.
- Cancelling a law to defuse one Revolution and accidentally triggering a different movement that endorsed the same law.
- Watching Support and ignoring Activism — tiny-Support movements with high Activism still spawn Radicals and revolt.
- Trying to push a law through a movement that is only "indifferent" to it — you get no enact bonus.
- Letting the Revolution bar climb to 100% while still hoping to cancel; past 100%, only winning the war ends it.
- Cancelling a law and assuming you can immediately re-try — the 24-month cooldown can be longer than the next rebel bar takes to fill.

## See also
- **In this wiki:**
  - [Passing Laws](passing-laws.md)
  - [Citizenship and Acceptance](citizenship-and-acceptance.md)
  - [Cultural Fervor](cultural-fervor.md)
  - [Slavery Abolition](slavery-abolition.md)
  - [Standard of Living](../pops/standard-of-living.md)
  - [Japan: The Great Wave](../case-studies/japan-great-wave/index.md)
- **Official wiki:**
  - https://vic3.paradoxwikis.com/Political_movements
  - https://vic3.paradoxwikis.com/Revolutions
  - https://vic3.paradoxwikis.com/Interest_groups

## Sources
- `notes/tutorials/20-political-movements.md`
- https://vic3.paradoxwikis.com/Political_movements
