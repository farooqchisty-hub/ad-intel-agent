# BFCM 2026: the CPMA optimization cycle (Meta + Google)

PushOwl BFCM 2026, 16 Oct to 30 Nov 2026 11:59 pm PT. Design written 16 Oct 2026 from the code on branch `cpma-video-bfcm` (repo `~/claude fc/ad-intel`), live CPMA settings and the bfcm-dash API (both read only). Nothing was changed.

## The answer in one paragraph

BFCM does **not** run on CPMA's general rules. It runs on its own BFCM rulebook, layered on CPMA's shared safety layer and verdict maths. Two reasons. First, CPMA does not optimize Google at all today: it reads Google, its only Google write is a budget change limited to "AGENT · Search" campaigns, and even that is switched off by `google_hold`. Its "general Google rules" are a Search-on-installs program at $20/$25 that has never run on a live campaign and does not cover Demand Gen, YouTube, remarketing or a claim goal. Second, CPMA's general Meta rules (engine.js) are built for an evergreen account: monthly pacing, 2-week fatigue baselines, weekly test batches, 7-day settled windows. A 45-day window with a fixed creative set, CPMs rising into November and a hard code deadline needs different timings, an envelope-based scale ladder, a cross-channel layer and a guaranteed stop. Keep: account lock, holds, caps, activation rules, the Bayesian verdict, the $15/$19 targets. Override: cadence, pacing, budget autonomy, the response to a ceiling breach, the Google goal, creative production. Add: a 15-minute guard, a hard stop, a Google BFCM loop, cross-channel reallocation and a conversion feedback loop.

---

## 0. What CPMA does today (facts, with file:line)

### Meta
- Schedule: crons `0 6 * * 1`, `30 3 * * *`, `30 11 * * *` (wrangler.toml:62). Every non-Monday tick sends `sync` (30 days), then `recommend` +5 min, `engine` +30 s, `bfcm_engine` +30 s (index.js:1484-1486, 1739-1749). Tue and Fri mornings also send `bfcm_sweep` (index.js:1496).
- `bfcmEngine` (bfcm.js:545-605) on program objects only: verdicts at $15 target / $19 ceiling, auto-pause losing ads, graduation cards (testing to prospecting), P0 phase/claims cards, auto-pause an ad set over $19 across 3 settled days with $60+ spent. It has no budget moves, no pacing, no fatigue rule, no reactivation, no spend or disapproval alarms, and no end-of-window logic.
- Separation: every BFCM object carries `ad_objects.program='bfcm26'` (tagPrograms, bfcm.js:527-536); the evergreen engine, legacy recommendations and learnloop filter it out (engine.js:25, recommend.js:104).
- Targets: `campaigns.targets` = $15 / $19 (campaign.js:43), apart from `settings.targets.meta` (also 15/19 since 15 Oct).
- Safety: 20 changes and 40 creates a day across the account (safety.js:19), one-UTC-day overrides up to 150 (safety.js:106-115); activation only of objects the agent created (execute.js:29-32); budget step 20%, 72 h cooldown, 5 budget changes and 10 pauses a day, +50% a week max (recommend.js:22-27, execute.js:24-57); Go live is all or nothing and refuses without a confirmed installer exclusion (golive.js:10-16).
- Live state, 16 Oct 00:30 UTC: campaign 120250862061510614 built, 31 ads PAUSED (the same 6 launch creatives in prospect_en $170, prospect_eu $60 and retarget $40; 13 in testing $30). Go live card `0543dcf8-1ce` waiting; it needs 40 changes, so the go-live day needs `write_cap_override` 45. `meta_hold` off, `google_hold` on. Autonomy: pause_losers, budget_down, pause_ceiling, reactivate_late auto; go_live, graduate, budget_up approve. bfcm-dash: all sources green, BFCM spend 0.

### Google: reads yes, optimizes no
- Reads: `syncGoogle` on every sync (sync.js:259-315) for every non-MagicFit campaign. "Installs" there = all_conversions of `owl_portal_connect_shopify` + `App Install (GA4)` (brand.js:93). The `BFCM claim` action (7847048606) is not read.
- Writes: treg's only Google write is `google-ads.budget.update` (checked in the treg catalog today: no pause, no create, no conversion upload). CPMA restricts it to "AGENT · Search" campaigns, 20% a step, 72 h apart, $150/day max (gsearch.js:36, 703-730).
- Held: `google_hold` on since 4 Oct. Google writes are refused in `tregCall` (treg.js), every `gsearch_*` job is skipped (index.js:1710-1712), `googleChecks` is skipped (engine.js:129), `google_budget` cards are refused (kanban.js:213).
- The "general Google rules" are the gsearch.js Search install program: keyword verdicts on the Meta maths at $20/$25 (gsearch.js:33, 527-562), daily search-term negatives (564-590), Monday budget shift between agent Search campaigns (592-620), monthly RSA, country and device reviews (622-690), plus `googleChecks` (engine.js:255-281: install goal must be primary; `google_cut` card after 14 days at 2.5x target with 0 installs) and `securityWatch` (gsearch.js:150-205: unknown campaign, foreign domain, budget over $150).
- None of it touches the BFCM Google campaigns (Demand Gen video $65, Demand Gen images $35, Search $30, Remarketing $20, bidding on claims). There are no BFCM Google campaigns in the account yet (bfcm-dash registry empty).

### Gaps the BFCM cycle has to close (found in the code)
1. **No hard stop.** Nothing pauses at 30 Nov 23:59 PT. `phaseNow()` reads the UTC date (bfcm.js:242, campaign.js:231-234), so phase checks switch off at 1 Dec 00:00 UTC, which is 30 Nov 4:00 pm PT, eight hours before the real end. The 5 Nov flip likewise lands at 4 Nov 4:00 pm PT.
2. **Cron trap.** `scheduled()` treats every cron other than Monday's as a full sync run (index.js:1484). A new 15-minute cron without its own branch would fire sync, recommend, engine and the gsearch jobs 96 times a day.
3. **The core ad set can switch itself off.** The ceiling rule auto-pauses `prospect_en` ($170/day, 57% of Meta) on one bad 3-day window (bfcm.js:590-602), which in late November means the campaign stops at peak.
4. **The testing ad set cannot reach verdicts.** 13 ads share $30/day; the winner rule needs 10 installs (bfcm.js:209), about $150 per ad. Most testing ads would never be judged inside the window.
5. **No program alarms.** Spend, CPI-spike and disapproval alarms are evergreen only (engine.js:181-193).
6. **Creative production conflicts with the fixed set.** `bfcmSweep` asks an LLM for new variants every Tue and Fri (bfcm.js:684-764) although c1 runs unchanged to 30 Nov.
7. **Evergreen Google rules would misfire on BFCM.** `googleObjective()` labels any non-CaaS, non-Owl-Portal campaign "installs" (goals.js:49-54), so once the hold lifts `googleChecks` would post `google_cut` cards on claim-optimized BFCM campaigns, and `securityWatch` would raise "campaign the agent doesn't know" critical alerts.
8. **One shared write budget.** Evergreen and BFCM share 20 changes a day, so a busy evergreen day could block a BFCM action.

---

## 1. General vs BFCM: rule by rule

Keep = runs unchanged on BFCM. Override = BFCM gets its own value. Add = CPMA has no such rule for BFCM today.

| # | CPMA rule (where) | BFCM | Value for BFCM and why |
|---|---|---|---|
| 1 | Program separation, `program='bfcm26'` (bfcm.js:527-536, engine.js:25, recommend.js:104) | Keep + Add | Extend tagging to Google BFCM campaigns (names start `BFCM26 · `) so no evergreen rule ever judges them. |
| 2 | Targets $15 / $19 (campaign.js:43) | Keep (Meta) | Farooq's numbers. Holding a fixed ceiling while CPMs rise is handled by rules 6 and 10, not by moving the target. |
| 3 | Google targets $20 / $25 on installs (settings.targets.google, gsearch.js:33) | Override | Google BFCM is judged on cost per **stitched install** at $15 / $19, and day to day on cost per claim against a derived claim target = $15 x measured claim-to-install rate (starts at $6 = $15 x 40%, recomputed weekly once 50 claims exist). Claims are what Google bids on; installs are what we buy. |
| 4 | Verdict too_early: 3 days and $15 (bfcm.js:206) | Keep | Short enough for a 6-week window. |
| 5 | Ad loser: no install after $38 (2x ceiling), or 3+ installs and P(CPI < $19) < 10% (bfcm.js:207-208); auto-pause (bfcm.js:564-570) | Keep | Cheap, evidence-based, ad level only, no learning reset of the ad set. |
| 6 | Ad set over $19 for 3 settled days with $60+: auto-pause (bfcm.js:590-602) | Override (prospecting) | Prospecting ad sets step **down 20%** instead; a pause needs a P0 card and only when still over $19 after 72 h at the lower budget with P(CPI < $19) < 10%. Testing and retargeting keep the auto-pause. Reason: a noisy 3-day window in November must not switch off 57% of Meta. |
| 7 | Winner: 10+ installs and P(beats $15) > 80% (bfcm.js:209), graduation card (bfcm.js:571-577, 608-630) | Override (testing) | Testing graduates at 5+ installs and P(beats $15) >= 70%. $30/day over 13 ads cannot produce 10 installs per ad in time. Graduations batch on Tue/Fri (one learning reset per batch); last batch Tue 17 Nov. |
| 8 | Settled data only (2-day lag, engine.js:52, bfcm.js:541) | Override | Asymmetric. Cuts and pauses use settled data (late installs can rescue an ad). Raises may use fresh data, because late installs only ever lower CPI, so fresh data can only make a raise harder to earn. From 27 Nov 00:00 PT no CPI-based cuts at all: data from then cannot settle before the end. |
| 9 | Reactivate an agent-paused ad on late installs: 3+ installs, P >= 40%, within 7 days (engine.js:86-97) | Add | Same thresholds, program ads only. Install lag is real on the App Store pixel. |
| 10 | Budget ladder: +15% card if CPI <= 0.8x target with 30+ installs over 7 settled days; -20% auto over 1.3x (engine.js:136-162) | Override | Raise +20% when P(CPI < $15) >= 80% over the last 5 days with 10+ installs, executed **automatically inside the phase envelope** Farooq approved, card above it. Cut -20% (prospecting) per rule 6. 30 installs over 7 settled days would only allow a raise every other week; the window has six. |
| 11 | Budget guardrails: step 20%, cooldown 72 h, 5 budget changes and 10 pauses a day, +50% a week, min age 3 days (recommend.js:22-26, execute.js:49-57) | Keep, one override | Cooldown drops to 48 h from 24 Nov (fewer days left, a reset costs less than a missed day). Add a 96 h learning lock after go-live per ad set. |
| 12 | `execute_budget_up: false`: raises never execute (recommend.js:27) | Override | True for BFCM inside the approved envelope only. A raise waiting up to 8 h for the next run plus a click is a lost day in peak. |
| 13 | Monthly pacing against $10k/$20k (engine.js:164-168) | Override | Window pacing against the plan ($450/day, $20,250 for 45 days) and a window cap of $24,000. Month boundaries mean nothing in a window that spans October and November. |
| 14 | Spend alarm 1.5x daily plan, CPI spike 2x target (engine.js:183-186) | Add | Program version in the 15-minute guard: Meta warn at 1.4x of live budgets, stop at 1.9x (Meta may legitimately spend up to 1.75x on a day); Google stop at 2.1x (Google may spend up to 2x). Plus a budget-mismatch check: a platform budget that differs from CPMA's record is an outside edit (the Nov 2025 Google compromise ran $5k to $10k days). |
| 15 | Disapproval alarm (engine.js:187-191) | Add | Program ads too; a disapproved launch ad silently removes delivery. |
| 16 | Fatigue: frequency > 3 or CPI +30% vs the ad's first 2 weeks, for 5 days (engine.js:115-126; recommend.js fatigue 3.5 + CTR -30%) | Override | Prospecting 7-day frequency > 2.5, retargeting > 5, or link CTR down 30% against the ad's first 5 days with CPI up 25%. Action: rotate in a benched c1 creative (no new creative). A 2-week baseline is a third of the window. |
| 17 | Write caps 20 changes / 40 creates (safety.js:19) | Keep + Add | BFCM gets its own daily budget (20 changes, 10 creates) so evergreen work cannot starve it. Stop-path writes (pause, archive, budget floor) are exempt from caps. Go-live day: `write_cap_override` 45. |
| 18 | Kill switch blocks every write, pauses included (safety.js:72-73, execute.js:24) | Override | Stop-path writes pass the kill switch (they can only reduce spend). Everything else stays blocked. The account lock always applies. |
| 19 | `google_hold` fail-closed (safety.js:42-51) | Override | Stays on for evergreen. `except_programs: ["bfcm26"]` lets BFCM Google budget writes through, only on registered BFCM campaigns. |
| 20 | Google budget write: agent Search campaigns, 20%, 72 h, $150 max (gsearch.js:703-730) | Override | Same limits on registered BFCM campaigns, plus a `floor` mode ($1/day) that works as CPMA's Google stop, since treg cannot pause Google. |
| 21 | `googleChecks` google_cut card (engine.js:270-279) | Override | Excludes program objects. BFCM Google is judged by rule 3. |
| 22 | `securityWatch` (gsearch.js:150-205) | Keep + Add | Keeps watching everything. Campaigns named `BFCM26 · ` within the domain list and envelope are registered as known (no false critical alert). |
| 23 | Google Search optimizer: keyword verdicts, negatives, Monday shift, monthly RSA/geo/device (gsearch.js:513-690) | Override | For the BFCM Search campaign: daily negatives card (same logic, scoped to BFCM ids), weekly shift between BFCM Google campaigns. No RSA, geo or device reviews inside 6 weeks. |
| 24 | Phase/claims P0 card (bfcm.js:578-588) | Keep, fix | Phase dates computed in PT, not UTC. |
| 25 | `bfcmSweep` LLM proposals Tue/Fri (bfcm.js:684-764) | Override | Proposals off (c1 is fixed). Keep the results table and the competitor BFCM-offer watch. |
| 26 | Weekly test batch and Monday graduation (engine.js:197-235) | Keep apart | Evergreen only; BFCM has its own graduation. |
| 27 | Go live (golive.js) | Keep + Add | The same card, plus Meta ad set `end_time` written in the same targeting refresh (no extra writes). |
| 28 | Decisions twice a day, 03:30 and 11:30 UTC (wrangler.toml:62) | Keep + Add | Decisions stay twice daily. A 15-minute guard is added for tripwires only (15-minute data is too noisy to optimize on). |
| 29 | Alerts: 6 h dedupe, Slack when `SLACK_ALERT_WEBHOOK` is set (safety.js:154-168) | Keep | Confirm the secret exists before go-live; critical alerts must reach Slack. |

---

## 2. The cycle

### 2.1 Cadence

| Cadence | CPMA job | Reads | Decides | Writes on its own | Cards for Farooq |
|---|---|---|---|---|---|
| Every 15 min | `bfcm_guard` (new cron) | bfcm-dash `/api/summary` (health, pacing, LP funnel, alerts, Meta ad set status and budgets), one GAQL read of BFCM Google campaigns (status, budget, cost today), LP HTTP check | Tripwires only: deadline, LP down, spend runaway, outside budget edit, dashboard stale, tracking silent, disapproval | Stop path: pause the Meta campaign and/or floor Google budgets | P0 card + Slack on every trip; restore card |
| Twice daily, 03:30 and 11:30 UTC | `sync` > `recommend` > `engine` > `bfcm_engine` > `bfcm_google` (new) | perf_daily: Meta ads and ad sets; Google BFCM campaigns with claims and installs | Ad verdicts, loser pauses, ceiling response, late reactivation, fatigue flags, phase claims, Google cost per claim | Ad pauses; testing/retarget ad set pauses; prospecting -20%; reactivations; Google -20% | Graduations, rotations, prospecting pause, Google pause |
| Daily, 03:30 UTC (09:00 IST) | `bfcm_budget`, `bfcm_digest` (new) | Fresh 5-day and settled 3-day CPI per ad set and campaign; window pacing; envelope; dashboard lenses; feedback-loop health | Raises; window pacing; claim target refresh | +20% inside the envelope (Meta and Google) | Raise above envelope; daily digest to Slack |
| Every 3 days (Tue, Fri 03:30 UTC) | `bfcm_sweep` (results only), `bfcm_rotate` (new) | Trait table; testing spend shares; frequency and CTR per ad | Graduation batch, fatigue rotation, testing pruning | None (anything going live needs a click) | One batch card per run |
| Weekly (Mon 03:30 UTC) | `bfcm_xchannel`, `bfcm_google_weekly` (new) | 7 settled days, GA4 lens and first-party lens by channel; Google search terms; goal-stage criteria | Meta vs Google shift; shift between Google campaigns; negatives; Google goal stage; next phase envelope | Shift between Google campaigns (20% step) | Cross-channel shift, envelope, goal stage, negatives CSV |

Runs in UTC: 03:30 is 8:30 pm PT the evening before, 11:30 is 4:30 am PT. Both land outside US business hours, so a change has the whole US day to deliver.

### 2.2 Learning-phase protection
- **Meta.** No budget change on an ad set for 96 h after go-live, and for 72 h (48 h from 24 Nov) after any significant change to it: a budget step, an ad added (graduation, rotation), an ad paused that held over 30% of its spend, a targeting change. Ad-level loser pauses are allowed once the ad passes its 3-day verdict gate. Graduations and rotations batch on Tue/Fri so a prospecting ad set resets at most twice a week. No new ads or targeting changes from Fri 20 Nov 00:00 PT.
- **Google.** No budget change for 7 days after a campaign is enabled (stops excepted). Goal changes only on the Monday card and never after Tue 10 Nov 00:00 PT. Search negatives any day (not a learning event).
- **Learning Limited is expected** for prospect_eu and testing (under 50 installs a week). CPMA does not treat it as a fault there.

### 2.3 Meta scale and cut rules

| Rule | Condition | Action | Who |
|---|---|---|---|
| Raise | Out of lock; P(CPI < $15) >= 80% over the last 5 days (fresh data allowed), 10+ installs; new budget inside the phase envelope | +20% | CPMA alone inside the envelope; card above it |
| Cut, prospecting | Settled 3-day CPI > $19 with $60+ spent | -20% | CPMA alone |
| Pause, prospecting | Still > $19 after 72 h at the lower budget, P(CPI < $19) < 10% | Pause ad set | P0 card |
| Pause, testing or retargeting | Settled 3-day CPI > $19 with $60+ spent | Pause ad set | CPMA alone (as today) |
| Retargeting saturation | 7-day frequency > 6 | -20% (pool is used up) | CPMA alone |
| Ad loser | No install after $38, or 3+ installs and P(CPI < $19) < 10% | Pause ad | CPMA alone |
| Late reactivation | Ad CPMA paused in the last 7 days now has 3+ installs and P(CPI < $15) >= 40% | Reactivate | CPMA alone |
| Testing prune | D0+7: testing ads with under 5% of the ad set's spend | Pause the starved ones, keep the 6 with most delivery (they stay benched) | Card |
| Graduation | Testing ad with 5+ installs and P(beats $15) >= 70% | Add to both prospecting ad sets, pause its testing ad | Card, batched Tue/Fri, last 17 Nov |
| Peak freeze | From 27 Nov 00:00 PT | No CPI-based cuts; tripwires and disapprovals only | |

### 2.4 Google rules
- **Bidding goal:** BFCM claim (see section 4 for the ladder to installs).
- **Daily:** cost per claim per campaign over 5 days. After the 7-day lock: -20% (CPMA alone) when it is over 2x the claim target with $100+ spent.
- **Weekly:** cost per stitched install (GA4 lens and first-party lens) vs $15 / $19. Raise +20% inside the envelope when cost per claim is at or under target and stitched CPI is at or under $19. Pause card (Google UI, done by the main session in Farooq's Chrome) when stitched CPI > $28.50 (1.5x ceiling) over 7 settled days with $300+ spent, or 0 stitched installs after $500.
- **Search $30:** daily negatives card with Editor rows (gsearch negatives logic, scoped to the BFCM campaign).
- **Demand Gen:** weekly card listing assets Google labels Low, to remove in the UI; none from 20 Nov.
- **Remarketing $20:** judged on claims; capped by the envelope.
- **Between Google campaigns:** Mondays, move 20% of the weaker campaign's budget to the stronger one when both lenses agree (the evergreen Monday shift, gsearch.js:592-620, applied to BFCM ids).

### 2.5 Creative fatigue and rotation inside the fixed c1 set
c1 has 19 unique creatives, all with built Meta creatives (`structure.creatives`). Rotation never needs production:
1. **Bench** = c1 creatives not running in a given ad set, ranked by their testing verdict (P(beats $15)), then by spend share.
2. **Tired ad** (rule 16) in prospecting or retargeting: the Tue/Fri card proposes "swap A for B": create an ad from B's existing Meta creative in that ad set (PAUSED), activate it on approval, pause A. Same mechanics as `bfcmGraduate` (bfcm.js:608-630).
3. **Rested ads** may come back into retargeting after 10 days off; retargeting audiences turn over fast.
4. **Bench empty and over 60% of the live set tired** before 20 Nov: one card telling Farooq the set is exhausted. Producing new creative is his call; c1 rules stand by default.

### 2.6 Cross-channel reallocation (Meta vs Google)
- **Currency:** stitched cost per install per channel = channel spend / installs on the GA4 lens (`shopify_app_install` in sessions with utm_campaign bfcm2026, split by utm_source), checked against the first-party lens (LP email matched to a store that installed after the lead). Both channels send traffic to the same LP and App Store link with UTMs, so both lenses measure Meta and Google with the same instrument. Platform numbers are never compared across channels (Meta counts installs including 1-day view; Google counts claims).
- **Rule (Mondays from 2 Nov, 7 settled days):** shift when both lenses agree one channel is at least 25% cheaper per install and each channel has 15+ GA4-lens installs; or when Google has under 5 stitched installs on $700+ of spend.
- **Size:** 10% of the weaker channel's daily budget (20% in the second case). Floors: Meta $150/day, Google $75/day. A shift never grows the combined envelope.
- **Redemptions:** once the redemption feed has 30+ channel-attributed redemptions in 14 days, the currency becomes cost per redemption (same rule).
- **Approval:** a card (money moving between platforms). CPMA executes both legs.

### 2.7 Caps and envelopes

| Cap | Value | Enforcement |
|---|---|---|
| Phase envelope, combined daily max (Meta / Google) | Learn 300 / 150 (no raises); Optimize 345 / 172; Scale 420 / 200; Peak and final 450 / 210, retargeting up to $80 inside Meta's | Farooq approves each envelope once on a card (4 clicks for the campaign); inside it CPMA raises alone |
| Window cap | $24,000 combined (plan $20,250) | At 90% projected: no raises. At 100% actual: stop path |
| Per object | Google campaign <= $150/day; Meta ad set +50% a week max | Existing code |
| Spend runaway | Meta 1.9x of live budgets today, Google 2.1x | Guard: stop path + P0 |
| Outside budget edit | Platform budget differs from CPMA's record | Guard: P0; stop that object if above envelope |
| Writes | BFCM 20 changes, 10 creates a day; stop-path writes exempt | safety.js program budget |
| Pauses / budget changes | 10 pauses, 5 Meta + 4 Google budget changes a day | Existing caps |

At the maximum envelope the window spends about $23,400, inside the $24,000 cap.

---

## 3. Phase calendar

| Phase | Dates (PT; UTC in brackets) | What CPMA does | Farooq |
|---|---|---|---|
| Pre-flight | Fri 16 Oct to go-live (D0) | Pre-go-live items in section 6 ship; Google campaigns built PAUSED and registered; envelopes seeded | Approve the Go live card |
| Learn | D0 to D0+4 (Meta); D0 to D0+7 (Google) | Guard every 15 min; ad verdicts from day 3; no budget moves; daily digest | Nothing unless a P0 |
| Optimize | D0+4 to Wed 4 Nov | Full rules; testing prune D0+7; graduations Tue/Fri; Google goal stage 2 when criteria are met; first cross-channel shift Mon 2 Nov | Envelope card (Optimize); batch cards twice a week |
| Scale | Thu 5 Nov 00:00 (08:00 UTC) to Mon 23 Nov | 30% off monthly opens, so conversion should rise: raises inside the Scale envelope; last graduation Tue 17 Nov; no Google goal change after Tue 10 Nov; structure freeze Fri 20 Nov 00:00 | Scale envelope card on Mon 2 Nov |
| Peak | Tue 24 Nov to Fri 27 Nov (Thanksgiving 26, Black Friday 27) | No structural changes; raises only on strong fresh data; cuts by step-down; no CPI cuts from 27 Nov | Peak envelope card on Mon 23 Nov |
| Final 72 h | Sat 28 Nov 00:00 (08:00 UTC) to Mon 30 Nov 23:59 (Cyber Monday) | Retargeting to $80 (pre-approved in the envelope); prospecting raises only at P >= 80%; guard every 15 min; 8:00 pm PT stop-readiness Slack | On call Cyber Monday |
| Hard stop | Mon 30 Nov 23:59 PT = Tue 1 Dec 07:59 UTC = 13:29 IST | Everything BFCM stops (below) | Nothing to do |
| Wind-down | 1 Dec to 5 Jan | Verify zero delivery; hand warm pools to evergreen; reports | Approve the evergreen handoff |

### How the stop at 30 Nov 23:59 PT is guaranteed (four independent layers)
1. **Meta, platform side.** `end_time = 2026-12-01T07:59:00Z` on all 4 ad sets, written inside the Go live targeting refresh (same call, no extra writes). Meta stops them itself even if CPMA, treg or Cloudflare are down. The guard reads it back after go-live and alerts if it is missing.
2. **Google, platform side.** Each BFCM campaign carries an end date, and one Google Ads automated rule (Once, 1 Dec 2026 13:00 account time Asia/Calcutta = 30 Nov 11:30 pm PT, Pause, label `BFCM26`) pauses all of them. It stops 29 minutes early by design, so Google never runs past the deadline even if CPMA is dead.
3. **CPMA stop job.** The 07:45 UTC guard tick enqueues `bfcm_stop` with a delay landing at 07:59:00 UTC. It pauses the Meta campaign (1 write) and floors every BFCM Google budget to $1, past the kill switch and the write caps, then sets `campaigns.status='ended'`. Guard ticks at 08:15 and 08:30 verify zero spend since 08:00 UTC and re-run the stop if anything still delivers.
4. **People.** At 30 Nov 8:00 pm PT a Slack message shows each layer's state. Manual kill: `POST /api/bfcm/stop {"confirm":"STOP BFCM26"}`.

### After 30 Nov
- **Retargeting stops with everything.** Its ads carry the deal and BFCM2026, which is dead after the deadline. No exceptions.
- **Warm pools go to evergreen.** From 1 Dec a card proposes adding the BFCM warm audiences (LP visitors 30d, listing viewers, install clickers) to the evergreen Warm ad set with non-offer creative, installers and redeemers excluded. Google remarketing lists follow once `google_hold` lifts.
- **Objects stay PAUSED for 14 days** (data, audits), then are archived on a card (never deleted).
- **Reports:** media report Tue 8 Dec (Meta's 7-day click window closes 7 Dec 23:59 PT); redemption and first-charge report Tue 5 Jan (new stores pay after their $0 month).

---

## 4. Feedback loop

### Today
- Meta optimizes Purchase on PushOwl New Pixel 816424380854185, sent server-side by the App Store listing. That is already an install signal; installs need no CAPI from us.
- Google optimizes BFCM claim (7847048606), fired on the Webflow page at email submit. App Install (GA4) (6686119911) arrives only when the gclid survives into the App Store session.
- Missing: redemptions on either platform, and a Google signal tying claimers to installs.

### Design
All senders live in **bfcm-dash**, which already holds the stitch (emails, store domains, click IDs). CPMA never holds personal data. It reads health counts, makes the decisions and posts the cards.

| Feed | What | How | Needs |
|---|---|---|---|
| A. Google stitched installs | New conversion action "BFCM install (stitched)" (Import, clicks, count One, secondary at creation). Rows: LP leads with a gclid whose email matched a store that installed after the claim. Later "BFCM redeem (stitched)" the same way. | bfcm-dash serves `/export/google-offline.csv` (Google Click ID, Conversion Name, Conversion Time with the TimeZone parameter, Email for consented rows) behind HTTP basic auth. Google Ads fetches it daily: Uploads > Schedules > HTTPS. No developer token, no treg write. | Conversion action + schedule in the Google UI (main session) |
| B. Enhanced conversions for leads | The claim tag sends the email as user-provided data at claim time, so uploads match without a gclid (iOS, cross-device). | `gtag('set','user_data',{email})` before the conversion event in `bfcm-lp/docs/webflow-embed.html`, republished in Webflow | EC for leads on, customer data terms accepted (UI) |
| C. Meta redemptions | Custom events `BFCMRedeem` and `BFCMFirstCharge` to the PushOwl Pixel dataset 569439912209998 (the LP pixel where Lead fires; never the New Pixel, so Purchase stays = install) with em (sha256), fbc built from the stored fbclid and click time, external_id (sha256 of shop domain), event_id for dedupe | bfcm-dash posts to the Conversions API with a dataset access token generated in Events Manager (not a System User; treg has no CAPI route) | Secret `META_CAPI_TOKEN`; the engineering redemption event |

**Meta keeps Purchase as its goal for the whole window.** Redemptions run at tens a week, which is too few for Meta to learn from, and switching the event resets learning. They feed reporting and CPMA's redemption lens.

**Consent.** US and CA rows send under a privacy-policy notice. UK and EEA rows (FR, DE, IT, ES) send only with recorded consent: the pushowl.com consent state passed through the LP bridge, or an explicit tick. Everything else stays out of uploads and counts only in aggregate. Needs one privacy-notice line and Farooq's OK. bfcm-leads already stores gclid, fbclid, click_ids, marketing_optin and ip_country (bfcm-leads/src/index.js:276-302).

### Google goal ladder (claims to installs)
| Stage | Bidding goal | Switch when | Window |
|---|---|---|---|
| 1 | BFCM claim only: instant, high volume, no lag | At launch | D0 |
| 2 | Claim + BFCM install (stitched) as a second primary action. Installers count twice, so bidding leans to them without losing claim volume | Upload schedule healthy 5 days running, 15+ stitched Google installs in 14 days, gclid on at least 60% of Google claims | Earliest D0+7, latest Mon 9 Nov (Monday card) |
| 3 | Stitched install only | 50+ stitched installs in 30 days per campaign | Only before Tue 10 Nov. Unlikely at $150/day, so expect to stay on stage 2 |

No Google goal change after 10 Nov 00:00 PT, because a new learning period would overlap Black Friday week. CPMA's part: feed health in the daily digest (rows exported, conversions recorded on the stitched action by GAQL), the Monday goal-stage card, and stitched installs in its Google verdicts. The goal change itself is a UI step done by the main session after Farooq approves.

---

## 5. Guardrails

### Approval matrix
| Action | CPMA alone | Card (Farooq) |
|---|---|---|
| Stop path (deadline, tripwires, window cap) | Yes, past the kill switch and caps | Restore after a tripwire |
| Ad loser pause, late reactivation | Yes | |
| Testing/retargeting ad set pause; prospecting -20%; Google -20% | Yes | |
| Prospecting ad set pause; Google campaign pause (UI) | | Yes (P0) |
| Raises inside the phase envelope | Yes | |
| Raises above the envelope; the envelope itself (4 per campaign) | | Yes |
| Graduation, rotation, testing prune (switch ads on) | | Yes, batched Tue/Fri |
| Cross-channel shift | | Yes, Mondays |
| Google goal stage; DG asset removal; negatives | | Yes (UI done by the main session) |
| Go live (Meta card); enabling Google campaigns | | Yes |
| Evergreen handoff and archive after 30 Nov | | Yes |

### Alerting
- **Critical:** Slack + board P0. Stop path ran, LP down, budget edited outside CPMA, a stop layer missing (no `end_time`), disapproval of a launch ad, writes blocked (treg/Meta connection), CPMA guard silent.
- **Warn:** Slack. Tracking silent, dashboard stale, ceiling step-downs, pacing over 110% or under 80%, feedback upload failing.
- **Info:** board only. Routine actions, with the reason on each card.
- **Daily digest, 03:30 UTC (09:00 IST), Slack:** spend vs plan, installs on three lenses, CPI, claims, redemptions, actions taken, cards waiting.
- **Single source of action:** the dashboard banner keeps its alerts for display; CPMA is the only system that acts. bfcm-dash checks CPMA's guard heartbeat through the service binding and alerts if no tick for 45 min.

### Failure modes
| Failure | Detected by (cadence) | Automatic response | Farooq |
|---|---|---|---|
| Meta install tracking breaks (Purchase stops while GA4/Intercom installs continue) | 0 platform installs in 6 h of US daytime with $75+ spent and installs on other lenses (15 min) | **Freeze optimization, keep delivery.** No CPI-based pauses or raises until 6 h of installs return | Warn; check the App Store pixel |
| Google claim tag breaks | 0 BFCM claim conversions while the LP beacon logs 5+ Google-sourced submits (daily) | Freeze Google budget moves | Warn; main session checks the Webflow embed |
| LP down or claim box broken | Dashboard LP-broken alert, or the LP or its iframe page not 200 / marker missing, for 2 ticks (30 min) | Stop path (Meta campaign paused, Google floored); auto-restore is not allowed | P0; restore card once the check passes |
| Code BFCM2026 rejected in the app | No redemption event or "BFCM2026 used" tag 24 h after 30+ BFCM installs; engineering `code_error` event if they add it | With an explicit `code_error` event: stop path. Otherwise P0 card "pause all?" | Decides; engineering fixes |
| Dashboard stale | `health.last_ok_at` > 45 min (warn), > 3 h | After 3 h: freeze cross-channel and redemption decisions; platform rules keep running on CPMA's own sync | Warn |
| treg or Meta connection lost | `connectionCheck` at each sync (safety.js:128-151) | Writes blocked; Meta `end_time` and the Google rule still stop the campaign on time | Critical; reconnect treg |
| CPMA cron stops | bfcm-dash sees no guard heartbeat for 45 min | Platform-side stops still hold | Critical |
| Budget runaway or outside edit | Guard (15 min) | Stop that object if above envelope | P0 |
| Disapproval | Guard (15 min) | Ad stays off; no resubmission unchanged | P0 card |
| Window cap reached | Daily pacing; guard at 100% | No raises at 90% projected; stop path at 100% | Raise the cap or accept |

---

## 6. Implementation plan

Farooq said "implement all and take campaigns live once done". Order: **G** items ship before go-live; **F** items ship after, each before the date its rule first fires. Sizes: S small, M medium, L large. All code runs on Cloudflare (cron + queues); the Mac only edits and deploys.

### Settings (new keys in D1 `settings`, editable via the existing `POST /api/settings`, deep-merged)
```json
"bfcm26_ops": {
  "guard": true,
  "end_at": "2026-12-01T07:59:00Z",
  "go_live_at": null,
  "learning_lock_hours": 96,
  "google_learning_days": 7,
  "cooldown_hours": { "default": 72, "from_2026-11-24": 48 },
  "scale": { "step": 0.2, "p_beats": 0.8, "min_installs": 10, "fresh_days": 5 },
  "cut": { "step": 0.2, "settled_days": 3, "min_spend": 60, "prospect_pause_after_hours": 72 },
  "graduate": { "min_installs": 5, "p_beats": 0.7, "last_batch": "2026-11-17" },
  "fatigue": { "freq_prospect": 2.5, "freq_retarget": 5, "ctr_drop": 0.3, "cpi_rise": 0.25, "retarget_saturation_freq": 6 },
  "no_cpi_cuts_from": "2026-11-27T08:00:00Z",
  "structure_freeze_from": "2026-11-20T08:00:00Z",
  "google_goal_change_until": "2026-11-10T08:00:00Z",
  "tripwires": { "meta_spend_x_warn": 1.4, "meta_spend_x_stop": 1.9, "google_spend_x_stop": 2.1, "lp_down_ticks": 2, "dash_stale_min": 45, "dash_freeze_min": 180, "tracking_silent_hours": 6, "tracking_min_spend": 75 },
  "window_cap_usd": 24000,
  "xchannel": { "from": "2026-11-02", "min_gap": 0.25, "min_installs": 15, "step": 0.1, "floors": { "meta": 150, "google": 75 } },
  "sweep_proposals": false
}
"bfcm26_envelope": { "phase": "learn", "meta_max_daily": 300, "google_max_daily": 150, "retarget_max_daily": 40, "approved_by": "go_live", "approved_at": null }
"bfcm26_google": { "customer_id": "8465254800", "name_prefix": "BFCM26 · ", "label": "BFCM26", "claim_action_id": "7847048606", "ga4_install_action_id": "6686119911", "stitched_action_id": null, "goal_stage": 1, "claim_target_usd": 6, "campaigns": {} }
"google_hold": { "on": true, "except_programs": ["bfcm26"] }
"write_cap_override": { "day": "<go-live UTC day>", "cap": 45 }
```
Runtime state that the guard writes (not hand-edited): `bfcm26_ops_state` {last_tick_at, trips[], stop_queued_at, stopped_at, end_time_verified, lp_down_ticks}.

### Must ship before go-live

| ID | What | Files and exact changes | Size |
|---|---|---|---|
| G1 | 15-minute cron and guard job | `wrangler.toml` default env: `crons = ["0 6 * * 1", "30 3 * * *", "30 11 * * *", "*/15 * * * *"]` (not in vitalvogue envs). `src/index.js` `scheduled()`, **first statement, before line 1484**: `if (event.cron === "*/15 * * * *") { await env.JOBS.send({ type: "bfcm_guard" }); return; }`. Without it the new cron runs a full sync 96 times a day. `queue()`: `bfcm_guard` > `bfcmGuard(env)`, `bfcm_stop` > `stopAll(env, m.reason)`. New `src/lib/bfcm_ops.js`: `bfcmGuard(env)` (no-op until `go_live_at` is set; writes an `events` row `kind='bfcm_guard'` every tick as heartbeat). | M |
| G2 | Hard stop, layers 1 and 3 | `bfcm.js` `refreshProgramTargeting` (bfcm.js:511-523): add `end_time: ops.end_at` to the same `meta-ads.x.adset-update` params. `bfcm_ops.js` `stopAll(env, reason)`: Meta campaign PAUSED via `setStatus(env, {id, level:"campaign", status:"PAUSED", stop:true})`; Google `floorAll(env)`; for `deadline` set `campaigns.status='ended'`; `action_log` + critical alert. Guard: at the first tick where `now >= end_at - 15 min` with no `stop_queued_at`, `env.JOBS.send({type:"bfcm_stop", reason:"deadline"}, {delaySeconds: secondsUntil(end_at)})`; after `end_at`, verify every tick and re-run if anything delivers. `execute.js` `setStatus`: a `stop` flag for status PAUSED skips the kill switch and pause cap. `safety.js` `assertWriteAllowed(env, endpointId, params, opts)`: `opts.stop` skips the kill switch and daily caps (never the account lock). `treg.js` `tregCall`: pass `opts` through. | M |
| G3 | Google program plumbing | New `src/lib/bfcm_google.js`: `registry(env)` (Google `ad_objects` with `program='bfcm26'`, level campaign); `applyBfcmGoogleBudget(env, {campaignId, toUsd, mode:"step"\|"floor"\|"restore", recId, reason})`, modeled on gsearch.js:703-730 (validateOnly first; registry member; not a shared budget; step <= 20% unless floor/restore; cooldown; <= envelope share and <= $150; `floor` = $1 and saves the prior budget in `action_log.before`); `floorAll(env)`. `safety.js` `googleHeld(env, {program})` returns false when `google_hold.except_programs` includes the program; `treg.js` passes `opts.program` for `google-ads.budget.update`. `bfcm.js` `tagPrograms`: also `UPDATE ad_objects SET program='bfcm26' WHERE platform='google' AND (name LIKE 'BFCM26 ·%' OR campaign_id IN (SELECT id FROM ad_objects WHERE platform='google' AND level='campaign' AND name LIKE 'BFCM26 ·%'))`. `engine.js` `googleChecks` query (engine.js:271-273): add `AND COALESCE(o.program,'')=''`. `gsearch.js` `securityWatch`: names starting `BFCM26 · ` with allowed domains and budget <= $150 get origin `bfcm26`, acked=1, info alert only. `index.js`: `POST /api/bfcm/google/register {campaign_ids}` (confirms by GAQL, tags program, acks in `gsearch_known`, fills `bfcm26_google.campaigns`). | M |
| G4 | Guard tripwires and program alarms | `wrangler.toml`: `[[services]] binding = "BFCM_DASH"`, `service = "bfcm-dash"` (Worker to Worker on the same workers.dev account needs a service binding, not a public fetch). Secret `BFCM_DASH_VIEW_KEY` (from ~/.bfcm_dash_view). `bfcm_ops.js` checks: LP (dashboard LP-broken alert, or `fetch` of the pushowl.com deal page and the GitHub Pages LP: 200 + marker, `lp_down_ticks` 2 > stop path), spend runaway (today's spend vs live budgets, hour-prorated), outside budget edit (dashboard `meta.adsets[].daily_budget` and GAQL budgets vs `ad_objects`), dashboard stale, tracking silent (freeze flag in `bfcm26_ops_state` that `bfcmEngine` and `bfcm_budget` read), disapprovals on program ads, `end_time` read-back once after go-live, window cap at 100%. Direct Meta read as a fallback when the dashboard is stale. | M |
| G5 | PT phase dates | `bfcm.js:242` `phaseNow = () => phaseFor(new Intl.DateTimeFormat("en-CA", { timeZone: "America/Los_Angeles" }).format(new Date()))?.id \|\| null` | S |
| G6 | Prospecting ceiling response | `bfcm.js:590-602`: for `role === "bfcm_prospect"` call `setBudget(env, {id, level:"adset", toUsd: cur*0.8, reason})` (kind `bfcm_ceiling_cut`, auto); pause only through a P0 `pause_ad` card when still > ceiling 72 h after the cut and P(< ceiling) < 10%. Testing and retarget unchanged. Add `bfcm_ceiling_cut: ["undo","open_ads_manager"]` to kanban.js `BY_KIND`. | S |
| G7 | Sweep proposals off | `bfcm.js` `bfcmSweep`: skip steps 3 (LLM) and the inserts (bfcm.js:707-751) unless `bfcm26_ops.sweep_proposals === true`; keep results, traits and the competitor watch in `bfcm26_sweep_last`. Must land before Tue 20 Oct 03:55 UTC, the first post-build sweep. | S |
| G8 | Go-live wiring, status and manual kill | `golive.js`: when `rec.program`, set `bfcm26_ops.go_live_at`, `campaigns.status='live'`, `bfcm26_envelope.approved_at`. `index.js`: `GET /api/bfcm/ops` (ops, envelope, state, last 20 guard ticks, end_time read-back, stop status); `POST /api/bfcm/stop {"confirm":"STOP BFCM26"}` > `stopAll(env, "manual")`. | S |
| G9 | Tests | Extend `bfcm.sim.test.mjs` / `bfcm.test.mjs`: the `*/15` cron enqueues only `bfcm_guard`; a guard at 2026-12-01T07:45Z enqueues `bfcm_stop` with delay 840; `stopAll` pauses with the kill switch on and caps used up; Google floor goes through under `google_hold` with the exception and is refused without it; `googleChecks` ignores program rows; the targeting refresh carries `end_time`; a prospecting ceiling breach cuts 20% and does not pause; phaseNow at 2026-11-05T07:00Z is still `early`. Run `node --test src/lib/*.test.mjs`. | S |

**Go-live runbook (in order; the main session does every step, Farooq approves):**
1. Deploy G1 to G9; set `BFCM_DASH_VIEW_KEY`; confirm `SLACK_ALERT_WEBHOOK` exists (`npx wrangler secret list`, names only).
2. Seed the settings above.
3. Watch 4 consecutive `bfcm_guard` heartbeats (`GET /api/bfcm/ops`) and confirm no extra `sync` events.
4. Google: build the 4 campaigns PAUSED, named `BFCM26 · <type>`, labelled `BFCM26`, goal BFCM claim, end date 1 Dec, budgets 65/35/30/20. Create the automated rule (Once, 1 Dec 13:00 account time, Pause, label BFCM26). Register with `POST /api/bfcm/google/register`.
5. Set `write_cap_override` for the go-live UTC day (cap 45).
6. Farooq approves Go live card `0543dcf8-1ce` (no rebuild needed: the targeting refresh now carries `end_time`).
7. Enable the 4 Google campaigns in the UI.
8. First guard tick after go-live: delivery started, `end_time` read back on all 4 ad sets, Google end dates read by GAQL, envelope `learn` stamped.

### Ships after go-live (needed by the date shown)

| ID | What | Files, jobs, keys | Needed by | Size |
|---|---|---|---|---|
| F1 | Budget ladder, learning lock, envelopes | `bfcm_ops.js` `bfcmBudget(env)` (Meta via `setBudget`, Google via `applyBfcmGoogleBudget`), `learningLocked(env, objectId)` (from `action_log`: budget steps, activations in that ad set, targeting). New job `bfcm_budget`, sent by the 03:30 run (index.js chain after `bfcm_engine`). Card kind `bfcm_envelope` with ACTIVATING action `bfcm_envelope_approve` (kanban.js `ACTIONS`, `BY_KIND`, `ACTIVATING`), writing `bfcm26_envelope`. Cooldown by `cooldown_hours`; `no_cpi_cuts_from` honoured. | D0+4 (first possible raise) | M |
| F2 | Late reactivation, fatigue, rotation, testing prune, relaxed graduation | `bfcm.js` `bfcmEngine`: reactivation block (copy engine.js:86-97 with `program=?`); graduation thresholds from `bfcm26_ops.graduate`. New `bfcm_rotate` job (Tue/Fri, beside `bfcm_sweep` at index.js:1496): cards `bfcm_rotate` (action creates an ad from the bench creative's existing Meta creative, PAUSED; activates on approval; pauses the tired ad, same pattern as bfcm.js:608-630) and `bfcm_prune_test` at D0+7. kanban.js entries for both (ACTIVATING). | D0+7 | M |
| F3 | Google BFCM loop | `bfcm_google.js` `bfcmGoogleSync(env)`: GAQL per BFCM campaign and day: cost, all_conversions by action for claim, GA4 install and stitched install into `perf_daily` (`leads` = claims, `installs` = GA4 + stitched). `bfcmGoogleEngine(env)`: cost per claim vs `claim_target_usd`, step-down and raise, pause cards (UI steps + Editor CSV), daily negatives card for the Search campaign (gsearch.js:564-590 logic with a campaign-id filter), weekly DG Low-asset card, Monday shift between Google campaigns, weekly claim-target refresh. Job `bfcm_google` chained after `bfcm_engine` (index.js:1749); job `bfcm_google_weekly` Mondays. | D0+7 (Google learning ends) | L |
| F4 | Daily digest and window pacing | `bfcm_ops.js` `bfcmDigest(env)`, job `bfcm_digest` from the 03:30 run (+2400 s): Slack + board card; window pacing vs `window_cap_usd`, the no-raise flag at 90% projected. | D0+1 | S |
| F5 | Separate BFCM write budget | Migration `schema9_bfcm_ops.sql`: `ALTER TABLE write_log ADD COLUMN program TEXT;`. `recordWrite` stores `opts.program`; `writeBudget(env, creating, program)` caps program writes at 20 changes / 10 creates and evergreen as today; stop-path writes uncounted. | Mon 2 Nov (Scale) | S |
| F6 | Cross-channel reallocation | Job `bfcm_xchannel`, Mondays 03:30 (+1800 s). Reads dashboard `channels[]` (`ga4_installs`, `first_party_installs`, spend by channel) for 7 settled days; card kind `bfcm_xchannel` (ACTIVATING) whose action applies Meta `setBudget` pro rata across prospecting ad sets and `applyBfcmGoogleBudget` across Google campaigns, honouring floors and the envelope. | Mon 2 Nov | M |
| F7 | Feedback loop | **bfcm-dash:** `GET /export/google-offline.csv` (basic auth, secret `GOOGLE_EXPORT_BASIC`), consent-gated rows; Meta CAPI sender for `BFCMRedeem`/`BFCMFirstCharge` (secret `META_CAPI_TOKEN`), triggered by the engineering event. **Google UI:** conversion action "BFCM install (stitched)", Uploads > Schedules > HTTPS daily, EC for leads on, customer data terms. **LP:** `user_data` email in `bfcm-lp/docs/webflow-embed.html`, Webflow republish. **CPMA:** feed health in the digest; Monday card kind `bfcm_google_goal` (stage 2/3 criteria, UI steps); `bfcm26_google.stitched_action_id`. | Google part Mon 26 Oct (earliest stage 2); Meta part when engineering ships | L |
| F8 | Redemption lens | `bfcm_xchannel` and verdict tie-breaks switch to cost per redemption at 30+ attributed redemptions in 14 days (dashboard `redemptions`, `channels`) | After F7 + engineering | S |
| F9 | Wind-down | `bfcm_winddown`, fired by the first guard tick after 1 Dec 09:00 UTC: final verification, evergreen handoff card, archive card dated 15 Dec, report cards 8 Dec and 5 Jan; the guard then goes idle. | Wed 25 Nov | S |

### Defaults that ship unless Farooq changes them
- Phase envelopes and the $24,000 window cap (section 2.7).
- Prospecting steps down instead of pausing itself (rule 6).
- Testing graduates at 5 installs / 70% (rule 7).
- The Google automated rule fires at 30 Nov 11:30 pm PT (29 minutes early).
- Consent gating for UK/EEA uploads, and one privacy-notice line (needs his OK before F7 sends data).
