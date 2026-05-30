---
sources:
  - ../../notes/tutorials/14-companies-and-prosperity.md
  - ../../notes/comprehensive-tutorial-2025/01-economics.md
wiki:
  - https://vic3.paradoxwikis.com/Companies
generated_at: 2026-05-16
---

# Companies

## What it is
Companies are the post-1.9 hub of the economic game: pick which buildings to bundle under one roof, hand them an Executive, give them Charters, and chase Prosperity to unlock a Prestige Good. They are not a passive bonus stack — every Company you slot in is a *commitment* to keep a building family on the best Production Methods, fully staffed, and globally competitive. Treat each Company slot as a strategic axis you have decided to specialize in.

## Mechanics
1. **Executive** — Each Company comes with a character who joins an Interest Group (giving it political weight, like a general) and applies trait bonuses to every Company building. *Decision rule:* between otherwise-equal Company candidates, pick the one whose Executive trait matches your plan (Throughput, construction speed, popularity). Accept event swaps that improve traits or popularity.
2. **Prosperity = target vs current** — Current Prosperity walks toward a continuously recalculated *target*. Prosperous turns on at 100 and turns off below 75. *Decision rule:* do not try to "rush" Prosperity directly — push the target up via productivity and staffed levels and let current drift up to meet it.
3. **Productivity component** — Up to ±50 of the target comes from how the Company's weighted-average building productivity compares to the *global* average for those building types. *Decision rule:* keep the best Production Methods on, prevent input shortages, and avoid expanding into states where the building will run poorly.
4. **Staffed-levels component** — Up to +50 of the target comes from +1 per fully-staffed building level, scaled by the actual employment ratio. Built-but-empty levels contribute nothing. *Decision rule:* only build a Company building when there are pops to fill it. An empty level is worse than no level.
5. **Executive popularity** — Adds ±1 to the target per 5 popularity points. *Decision rule:* a deeply unpopular Executive is a real drag — accept swap events when offered.
6. **Rate of change** — Above-global productivity gives +0.2/week base plus 4% per fully-staffed level; below-global flips to −1/week base plus only 2% per fully-staffed level. *Decision rule:* if you are below average, *fix productivity first*; adding levels at this stage bleeds Prosperity faster.
7. **Charters: free slots, then 100 Authority** — Each country has a number of free active charters from tech/laws; beyond that each charter costs 100 Authority per turn. Without Charters of Commerce DLC only Trade Rights exists. *Decision rule:* spend free slots first; only pay 100 Authority when the bonus is clearly load-bearing.
8. **Trade Rights** (free, no DLC) — Lets the Company build Trade Centers that inherit its Throughput bonus and give trade advantage on the Company's goods. *Decision rule:* hand this to the Company whose good you want to dominate world markets in.
9. **Investment Rights** — Lets the Company build a Regional HQ in a foreign state once it owns 5 building levels there, drawing from the *host's* Investment Pool while returns flow back to *your* Investment Pool. *Decision rule:* point this at wealthy neighbors to siphon their capital home; avoid markets with bad input prices, because you cannot set PMs on foreign buildings.
10. **Colonization Rights** — Company colonizes a designated state; on completion it becomes a chartered Company Subject under you, inheriting construction-efficiency bonuses. *Decision rule:* match the Company's specialty to the target state's resource (e.g. rubber Company for rubber-rich colony).
11. **Industry Rights** — Adds one extra related building type to the Company's list (e.g. a fish Company gains Food Industries). One Industry Rights charter per Company. *Decision rule:* pick the downstream consumer of your Company's output to vertically integrate.
12. **Monopoly Rights** — Only the Company and the government may build the named building type; private builders are locked out. *Decision rule:* monopolize building types you want built fast under Company bonuses — but only when government plus Company capacity can actually keep pace with demand.
13. **Prestige Good unlock** — Reaching Prosperous opens a Journal Entry; finishing it usually requires staying Prosperous and ranking top-3 globally on the relevant good for 36 (cumulative, not consecutive) months. *Decision rule:* once Prosperous, defend your top-3 ranking — expand production, sign trade routes, or politically/militarily disrupt rival producers.
14. **Foreign buildings — no PM control** — Buildings the Company owns abroad run whatever PM the host runs, which can sandbag your global productivity average. *Decision rule:* be very conservative with Investment Rights into volatile or backward markets.
15. **Company-owned buildings get +15% Throughput** — A building owned by a Company carries a flat +15% Throughput bonus (on top of any Executive trait), meaning more output per worker and per Construction Point on every level it holds. *Decision rule:* the more of a building family a Company owns, the more total Throughput across your economy — so prefer Company ownership over private/government ownership for any building family you've committed a slot to (2025 comprehensive tutorial, [14:03]).
16. **Companies build at higher construction efficiency than you** — When a Company builds its own buildings via the private queue, it spends *fewer* Construction Points per level than the player does, so Company expansion is cheaper than government construction of the same building. *Decision rule:* once a Company exists for a building family, let it build those levels (privatise/monopolise so it picks them up) rather than spending government CP yourself (2025 comprehensive tutorial, [15:02]).

## Game numbers & rules of thumb
- Prosperous threshold: ≥100 to gain, <75 to lose `[from 14-companies-and-prosperity]`.
- Productivity component cap: ±50 of target — no extra return past the cap `[from 14-companies-and-prosperity]`.
- Staffed-levels cap: +50 of target, +1 per fully-staffed level scaled by employment ratio `[from 14-companies-and-prosperity]`.
- Executive popularity: ±1 target per 5 popularity points `[from 14-companies-and-prosperity]`.
- Weekly drift: +0.2 if productivity ≥ global average, −1 if below; per-level bonus is 4% vs 2% on the same condition `[from 14-companies-and-prosperity]`.
- Productivity is a weighted average across all the Company's buildings, weighted by levels `[from 14-companies-and-prosperity]`.
- Foreign Regional HQ unlocks at 5 owned building levels in that country `[from 14-companies-and-prosperity]`.
- Charter cost beyond free slots: 100 Authority each `[from 14-companies-and-prosperity]`.
- Investment Pool returns from a foreign Regional HQ flow to the owner, not the host `[from 14-companies-and-prosperity]`.
- Practical Company-slot ceiling: 9 (5 Society tech tier, +1 from a Power Bloc Corporate State + Companies principle, +2 from canal Companies) `[from 14-companies-and-prosperity]`.
- Company-owned building Throughput bonus: **+15%** flat, on every level the Company owns (2025 comprehensive tutorial, [14:03]).
- **What a Prestige Good actually does:** +Throughput to any building using it as an input; extra Trade Advantage when traded; +SoL to pops that consume it (if it's a consumable good); +army stats if it's a military prestige good. Prestige Goods can be renamed for flavour (2025 comprehensive tutorial, [18:00]).

## Strategy & playbook
Treat your Company slots like ministries: each one is a permanent commitment to a building family. Before slotting in a Company, ask "am I going to actually build a lot of these buildings, on the best PM, with the labour to staff them?" If the answer is no, pick something else. The Society tech line (Corporate Charters → Joint-Stock Companies → Investment Banks → Corporate Governance → Macroeconomics) is your slot pipeline — rush at least Corporate Charters early so your initial industrial push is wrapped in Company bonuses from the start.

For each active Company, run a tight loop: best Production Method available, ensure full staffing *before* adding more levels, watch the employment ratio when you swap PMs (a labour-hungry PM tanks staffed-levels immediately). The big trap is "I need more Prosperity → I will build more". The math punishes that: unstaffed levels add nothing, drag your productivity average toward the host state's averages, and if you are below the global productivity line you are losing 1 Prosperity per week regardless. Fix productivity first, then scale.

Slot scarcity and per-Company maximization are two different decisions. The slot decision is conservative — only commit a slot to a building family you'll genuinely build out (above). But *once* a Company is committed, give it as much of that economy as it will take: every building level under the Company carries the +15% Throughput bonus, so more Company-owned levels means more total Throughput across your economy. The mechanism is to **privatise** (and where appropriate monopolise) the relevant buildings so the Company auto-acquires them — you don't hand-pick each one. The Belgium run does exactly this, handing John Cockerill the iron mines and privatising them so the company buys them up ([../case-studies/belgium-conquer-colonize-react.md](../case-studies/belgium-conquer-colonize-react.md)) (2025 comprehensive tutorial, [1:36:01]).

Charters are where the strategic flavour lives. Trade Rights is the export Company's tool — give it to whichever Company makes a good you want to be the world supplier of. Industry Rights is for vertical integration: a fish Company that also runs Food Industries captures the margin twice. Monopoly Rights is double-edged — yes, the Company builds those buildings fast and well, but private builders are locked out, so if you cannot keep building you create a goods shortage. Reserve it for things you genuinely intend to push.

New-player charter priority (when you don't yet know what you want): take **monopoly** and **industry** charters first — monopolies keep your prices and profits high, and industry charters give the Company a downstream building family to integrate. Trade-rights charters matter once you have a Company whose good you want to dominate world markets in (they let it own Trade Centers); investment charters only pay off once you actually hold foreign-investment rights; and colonization charters are essentially roleplay-only — skip them unless you're playing for the flavour (2025 comprehensive tutorial, [16:30]).

Investment Rights is the most underrated tool: planted in a wealthy neighbour, a Regional HQ uses *their* Investment Pool to build there, and the returns reinvest into *your* pool. This is a one-way capital pipe. The catch is that foreign buildings run the host's PMs — so avoid Investment Rights into countries with bad input prices for that building, because the inefficient foreign branch will drag your whole Company's productivity average and Prosperity with it. Colonization Rights is the colonial complement: pair a resource-specialist Company with a state rich in that resource and you get a chartered Company Subject inheriting the construction bonus.

Once a Company hits Prosperous, the Prestige Good Journal Entry is the prize: stay Prosperous and stay top-3 globally on the named good for a cumulative 36 months. This is a defensive game more than an offensive one — expand production, sign trade deals that bring your good abroad, and if a rival is close, consider whether a Diplomatic Play or a trade-route disruption is worth it. Once locked, the Prestige Good is permanent flavour income for your run.

## Common pitfalls
- **Spamming buildings to "boost" Prosperity** — empty levels add 0 to the staffed-levels component and can pull productivity down.
- **Ignoring the ±50 productivity cap** — past a point, more above-average productivity is wasted; spend effort elsewhere.
- **Swapping to a labour-heavy PM right before checking Prosperity** — employment ratio drops instantly, target and rate both fall.
- **Investment Rights into a bad-input-price market** — the foreign branch runs an inefficient PM you cannot change, dragging the parent Company down.
- **Burning Authority on a paid charter while free slots sit unused** — always hover the charter UI to see free-slot count first.
- **Confusing chartered Company Subject with a foreign-owned Company** — Company Subjects are still *your* subjects; you can impose law changes on them.
- **Trying to reach Prosperity on a small/tall Company** — the staffed-levels component effectively requires industrial scale.

## See also
- **In this wiki:** [Construction](construction.md), [Building balance sheet](building-balance-sheet.md), [Trade](trade.md), [Treasury and deficit](treasury-and-deficit.md), [Foreign investment](foreign-investment.md), [Power blocs](../diplomacy/power-blocs.md), [Standard of living](../pops/standard-of-living.md), [Japan: the Great Wave](../case-studies/japan-great-wave/index.md)
- **Official wiki:** [Companies](https://vic3.paradoxwikis.com/Companies), [Buildings](https://vic3.paradoxwikis.com/Buildings), [Production_methods](https://vic3.paradoxwikis.com/Production_methods)

## Sources
- `notes/tutorials/14-companies-and-prosperity.md`
- `../../notes/comprehensive-tutorial-2025/01-economics.md`
