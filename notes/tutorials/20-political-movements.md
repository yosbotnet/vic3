---
source_transcript: ../../transcripts/tutorials/20-political-movements.md
source_video: https://www.youtube.com/watch?v=qtLKNqSe-CA
generated_at: 2026-05-16
---

# Political Movements
**Source:** [Political Movements Tutorial in Victoria 3](https://www.youtube.com/watch?v=qtLKNqSe-CA) (16:45 runtime)

## Summary
Since the Sphere of Influence DLC (Pivot of Empire), you no longer bolster or suppress Interest Groups directly — you act on Political Movements instead. Movements have an Ideology, a list of Laws they endorse or oppose, a Support number (weighted political strength of supporting Pops), and an Activism number that determines whether the movement helps pass laws, generates Radicals, or escalates into a Revolution or Secession. Manipulating movements (bolster/suppress, distribution of power, choice of which laws to enact) is now the main lever to steer your country's politics.

## Core mechanics
1. **Support vs Activism** — Support is the total political strength of Pops backing the movement; Activism is how riled up they are. DECISION RULE: glance at Activism in the outliner — under 25% the movement is inert on laws; at >=25% it affects law enactment; at >=50% it spawns Radicals; at ~75% it goes Insurrectionary (Revolution/Secession). `[01:31]` `[02:01]` `[06:01]` `[09:00]`
2. **Movement law stances (endorse / oppose / indifferent)** — Each movement lists the Laws it cares about. DECISION RULE: only movements that list the law you are enacting will help or hinder it; indifferent or unlisted = no effect. Use endorsing movements to pass laws and avoid provoking opposing movements. `[02:01]` `[06:01]`
3. **Bolster / Suppress (now on movements, not IGs)** — Bolster increases a movement's attraction for new Pops; Suppress reduces it. DECISION RULE: Bolster movements whose endorsed laws you want to pass; Suppress movements blocking your agenda. `[06:31]` `[15:30]`
4. **Distribution of Power scales Support** — Pops only contribute political strength based on the suffrage law; census suffrage also adds up to 30 points from literacy. DECISION RULE: if a movement's supporters are wealthy/literate, a more open suffrage law strengthens them; if its base is poor peasants, restrictive suffrage neuters it. `[03:31]` `[04:00]` `[05:31]`
5. **Interest Group pressure & agitator leadership** — A movement "pressures" any IG that contains supporting Pops, weighted by political strength. DECISION RULE: to install an Agitator as an IG's leader, the IG must be pressured by the movement that Agitator joined. `[07:01]` `[16:01]`
6. **Revolution vs Secession assessment** — When the warning box appears it lists how many armies, conscripts, and states the rebels will take. DECISION RULE: compare rebel armies/states to your standing army + mobilisable conscripts; small Revolutions can be allowed to fire and crushed cheaply, large Secessions usually cannot. `[10:02]` `[10:30]`
7. **Lock on armies/conscripts after the box appears** — Once the Revolution warning is up you can add conscripts but cannot remove armies or conscripts. DECISION RULE: never preemptively assign conscripts to states that might secede, and finalise conscript placement before letting a hot law begin enactment. `[11:32]` `[12:00]`
8. **Cancel-the-law escape hatch** — Stopping enactment before the Revolution bar hits 100% defuses it, but triggers a 24-month cooldown on that law and may anger another movement that endorses it. DECISION RULE: cancel only if the would-be rebel front is bigger than any opposing movement's reaction; otherwise ride it out. `[13:01]` `[13:32]` `[14:01]`

## Game numbers & rules of thumb
- Activism >=25%: movement contributes to enact / stall chance of its listed laws. `[06:01]`
- Activism >=50%: movement generates Radicals every month. `[02:01]` `[06:31]`
- Activism ~75%: movement turns Insurrectionary (Revolution or Secession box appears). `[06:31]` `[09:30]`
- Census Suffrage wealth threshold to vote: wealth rating 15. `[04:00]` `[04:30]`
- Census Suffrage literacy bonus: up to +30 political strength from literacy. `[04:00]`
- Cancelling enactment imposes a 24-month cooldown before retrying that law. `[14:32]`
- IGs currently in active Revolution cannot be added to government. `[12:30]` `[13:01]`
- Once Revolution bar reaches 100%, cancelling the law no longer stops the war. `[13:32]`

## Common pitfalls
- Assigning conscripts to states that end up in the secession bloc — they leave with the rebels and you cannot pull them back. `[12:00]`
- Cancelling a law to defuse one Revolution and accidentally triggering a different movement that endorsed the law. `[13:32]` `[14:01]`
- Watching only Support and ignoring Activism — Support can be tiny but a high-Activism movement still spawns Radicals and revolts. `[01:31]` `[02:01]`
- Trying to use a movement to push a law it is merely "indifferent" to — it gives no enact bonus. `[03:01]` `[06:31]`
- Letting the Revolution bar climb to 100% while still hoping to cancel; after 100% the only exit is winning the war. `[13:32]`
- Cancelling a law and assuming you can immediately re-try — the 24-month cooldown can be longer than the rebel bar takes to fill. `[14:32]`

## Cheatsheet
1. Check the outliner every few months; flag any movement with Activism approaching 50%.
2. Before enacting a hot law, open every movement that lists it — note who endorses, who opposes, and how strong each is.
3. Bolster endorsing movements (and consider a suffrage shift that empowers their Pops) before starting enactment; Suppress the loudest opposing one.
4. Finalise army and conscript placement, keeping conscripts OUT of states likely to secede, before the Revolution box can appear.
5. When the Revolution warning pops, compare its armies/states to yours: small ones — let them fire and crush them; large ones — cancel the law (accepting the 24-month cooldown) only if no rival endorsing movement will revolt in response.
6. To install an Agitator as an IG leader, push the relevant movement until that IG appears in its Pressured Interest Groups list.

## See also
- https://vic3.paradoxwikis.com/Political_movements
- https://vic3.paradoxwikis.com/Revolutions
- https://vic3.paradoxwikis.com/Interest_groups
