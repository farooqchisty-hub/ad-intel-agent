# Ad Studio statics launch: handoff to CPMA

Farooq, 14 Nov 2026: launch the final 20 Ad Studio statics through the CPMA agent, across 5 ad sets. All 20 come from batch 2 (the edgy, copy-led set selling "clone 3 winning ads, free"). Where an ad had 3 options, the most distinctive one was picked.

## Priority: hooks around the 3 free ads

Farooq, 14 Nov: "I really want to prioritize and include ads with hooks around free ads. Those three free ads."
- **AS1 · 3 free ads (priority)** is the lead ad set and goes first in the build:
  - L01 "Free: 3 ads that already won." (Black Friday, headphones and soda winners)
  - L02, the same hook with GHOST, Huel and BARK winners
  - L03 "Pick one." (the button says "Clone 3 winning ads free")
  - L04 "No brief. No shoot. No card. Just clone."
- **Every AS1 ad leads with the free offer** in the image and in the first line of the primary text ("Your first 3 ads are free.").
- **AS2 continues the free hook:** L05 "They paid for 165 days. You pay $0." and L06 "Their winner. Your product. Zero dollars."
- **All 20 ads close on the offer:** every Meta headline or description says the first 3 clones are free.
- **Budget:** give AS1 more than the others, so the free-offer hooks get the most delivery. Default $45/day for AS1 and $30/day for each of the other 4 ($165/day); confirm with Farooq.
- **The loop:** in the CPMA loop and the day 7 review, AS1 is the last ad set to cut. Raise a card rather than pause it.

Everything you need is in this folder, `/Users/farooq.chisty/claude fc/ad-intel-pages/ad-studio-statics/launch/`:
- `launch_statics.json`: the 5 ad sets, the 20 ads, image files, feed copy and source evidence. This is the source of truth.
- `img/`: final images, used exactly as they are. Every ad has `Lxx-4x5.jpg` (1080x1350) and `Lxx-1x1.jpg`.
- `index.html`: the visual review page. Live at https://farooqchisty-hub.github.io/ad-intel-agent/ad-studio-statics/launch/

## Confirm with Farooq before building

Ask these in one message, with the defaults stated.
1. **Budget:** $45/day for AS1 (the free-ads priority set) and $30/day for each of the other 4, so $165/day. The $30 mirrors the live video campaign.
2. **Video campaign:** keep `as_launch2` (campaign 120251261230240614, 4 x $30/day) running alongside. The default is yes, so total Ad Studio spend is $285/day.
3. **Monthly budget:** raise CPMA's monthly budget (settings.targets.meta.monthly_budget, now 3650) to match. $285/day is about $8,700 a month.
4. **When:** build in the next Meta window, or now under the logged `launch_build` exemption. Last time he chose "now".

## The campaign (program `as_launch3`, Ad Studio silo)

Copy the ad set budget setup from `as_launch2` (`tenants/adstudio/launch_plan_abo.json` in the CPMA repo).
- **Campaign:** "AGENT · Ad Studio (MF) · Prospecting · Sign-ups · Statics · Nov 2026". Objective OUTCOME_SALES. No campaign budget, and `is_adset_budget_sharing_enabled` false. Keep "(MF)" in the name: the PushOwl silo filters on it.
- **5 ad sets,** named and grouped exactly as in `launch_statics.json`: AS1 3 free ads (priority), AS2 The receipt, AS3 The clock, AS4 The call-out, AS5 The forbidden truth. Each gets 4 ads and its own daily budget, bid LOWEST_COST_WITHOUT_CAP.
- **Ad set settings, same as `as_launch2`:**
  - Optimisation: OFFSITE_CONVERSIONS on `MagicfitSignUp`, PushOwl Pixel 569439912209998.
  - Attribution: 7-day click, 1-day view, 1-day engaged view.
  - Locations: US, CA, GB, DE, FR, IT, ES.
  - Audience: open (Advantage+ audience), age 18 to 65, Facebook and Instagram only.
  - Exclusion: audience 120251179656850614.
- **Identity:** Brevo PushOwl Page 485637907956703 and Instagram 17841470064475542.
- **Each ad:**
  - An image ad using `img/Lxx-4x5.jpg`. Add `Lxx-1x1.jpg` for square placements if the builder supports placement asset customisation; otherwise ship 4:5 only.
  - Primary text, headline and description taken from the manifest. CTA SIGN_UP, linking to https://ads.brevo.com/ with the manifest's `url_tags`.
  - Every Advantage+ creative enhancement OFF, as on the video ads.
  - Ad name `ASx · <ad set> · Lxx`.

## CPMA work this needs

The Ad Studio builder (`src/lib/adstudio.js`) only handles films today. Before building:
1. **Ingest the 20 images** into the Ad Studio silo Library as `kind static` creatives in R2, ids `as-l01` to `as-l20`. They are already final and approved: no generation, no edits.
2. **Teach the builder static ads:**
   - The preflight should accept `r2_key` where it checks for a video file.
   - The image goes through `creativeMedia`, whose static path returns `picture`, then `storySpec` with `link_data`.
   - Plan entries can reuse the `film` field with the `l01`-style ids, or add an `image` field.
3. **Write the plan** `tenants/adstudio/launch_plan_statics.json` from the manifest. Include `program: "as_launch3"`, `max_ads_per_adset: 4`, `approve_pauses_days: 7` and no `replaces`, so the video campaign keeps running.
4. **Point the program and lift the caps:** set `settings.adstudio_program` to `as_launch3`. Add `program_write_caps.as_launch3`: about 25 creates (1 campaign, 5 ad sets, 20 creatives, 20 ads, so lift it for the build day) and 30 changes.
5. **Deploy and verify:** run the tests, then deploy the Ad Studio worker only (`wrangler deploy --env adstudio`) from a clean worktree. The main checkout may hold another session's uncommitted BFCM edits.
6. **Build paused:** dry-run with `GET /api/adstudio/plan?program=as_launch3`, then `POST /api/adstudio/build {"confirm":"BUILD AS_LAUNCH3", ...}`. Check everything on Meta with one read, then leave the Go live card for Farooq. The loop already watches every live `as_` program.

## Checks before the Go live card

- **Claims still true on launch day:**
  - L09 "Day 691. Still running." needs that ad still live on Ad Radar. If it has stopped, drop L09 and tell Farooq.
  - Every other day count is the run length when captured on 12 and 13 Nov. Those numbers only grow, so "has run 372 days" stays true.
- **Copy rules:** no em or en dashes, no "Shopify" or "Klaviyo", USD only. The manifest already passes; re-check anything you change.
- **Sources:** the evidence links (Ad Radar and Meta Ad Library) are in the manifest for each ad that shows a real winner.

## Don't

- Generate, edit or re-render any image.
- Add ads beyond these 20.
- Translate anything: English only.
- Switch anything on without Farooq's Go live.
- Touch PushOwl or BFCM campaigns.
