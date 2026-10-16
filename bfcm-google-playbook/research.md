# PushOwl BFCM 2026: Google Ads research and playbook

Prepared 16 Oct 2026. Research only: no ad account was touched, no browser was used.
Scope: the four Google campaigns being built for the BFCM2026 offer (16 Oct to 30 Nov 2026, ends 11:59 pm PT).

**Confidence labels used throughout**
- VERIFIED: Google's own documentation, or first-party data we pulled ourselves (Ads Transparency Center via ScrapeCreators, keyword data, our own account teardown).
- VENDOR: agency, tool or vendor claim (methodology not audited).
- ANECDOTE: a single practitioner report.
- INFERENCE: our reasoning from the evidence; treat it as a hypothesis.

**Data spend:** about $1.30 on treg (about 450 ScrapeCreators Google ad library calls at $0.00188, 5 SE Ranking keyword batches; DataForSEO calls failed and were not charged).

---

# Part 1: Research findings

## 1. BFCM timing for merchant tools (when do store owners install?)

| # | Finding | Source | Confidence |
|---|---|---|---|
| 1.1 | A 2026 Shopify agency freeze calendar: build window closes Fri 16 Oct, **install window closes Fri 30 Oct** (app installs and removals), configuration locked Fri 13 Nov, code freeze Fri 20 Nov, thaw Tue 1 Dec. Its rule: "close the install window a month before the sale"; installing an app in freeze week is a high-risk change; anything not ready by the freeze date waits for December. | https://craftshift.com/shopify-code-freeze-black-friday/ (26 Aug 2026) | VENDOR |
| 1.2 | Other agencies put the cutoff for checkout, theme and app changes around 13 Nov, or a holiday freeze from about 1 Nov (no new apps). Shopify's own merchant checklist has no freeze date. | https://athoscommerce.com/blog/bfcm-code-freeze-and-publishing-pause/ , https://weltpixel.com/blogs/news/black-friday-conversion-tracking-freeze-what-to-lock-and-when-2026 | VENDOR |
| 1.3 | Klaviyo tells switchers to migrate mid-August to mid-September; a new branded sending domain needs at least 30 days of warm-up. So a merchant who switches email platforms after mid-October cannot fully warm a new domain before Black Friday. | https://www.klaviyo.com/blog/migrate-to-klaviyo-before-bfcm , https://help.klaviyo.com/hc/en-us/articles/20413890435355 | VERIFIED (Klaviyo's own guidance) |
| 1.4 | Implication of 1.3: in late October the "switch your email platform" pitch is weakest, while web push (no list, no warm-up), SMS and WhatsApp can still be switched on for this BFCM. Web push and cart recovery are the "works this Black Friday" angles. | Our reasoning | INFERENCE |
| 1.5 | Competitor flighting, seen in the Ads Transparency Center: **Omnisend 2025** BFCM creatives were first shown 10 to 22 Oct 2025 and every US BFCM image and video ad **stopped on 15 Nov 2025**, 13 days before Black Friday; from 1 Dec they ran "final call before Dec 31" switcher ads. **Privy 2025** Black Friday videos ran 11 Oct to 7 Nov (one to 29 Nov). **Attentive 2025** new creatives 28 Oct to 21 Nov. **Omnisend 2026** BFCM ads first shown 14 to 25 Sep 2026; **Klaviyo 2026** BFCM search ads first shown 5 Oct 2026, its first-month offer ads 2 to 3 Oct 2026. | Our pull (Section 2) | VERIFIED (dates); the reason they stop early is INFERENCE |
| 1.6 | No public data exists on Shopify app installs by month or on Oct vs Nov install timing for marketing apps. Our own Partner dashboard (installs by week, Oct to Dec 2025) is the only way to settle it. | Search returned nothing usable | GAP |
| 1.7 | Black Friday themed merchant searches are tiny: "black friday marketing" 140/mo US now; the SE Ranking series shows about 260 in Nov 2025. The series looks smoothed, so it cannot confirm a weekly spike. | SE Ranking via treg (Section 3) | VERIFIED volume, LOW confidence on seasonality |

**Synthesis (INFERENCE):** merchants decide and install in a window that runs from now to about 13 Nov; from 20 Nov they are executing, not installing. Big competitors front-load (Omnisend stopped its 2025 BFCM flight on 15 Nov). Our offer pulls the other way: monthly plans join on 5 Nov, which is the moment the offer becomes easy for small stores. So the money should peak **26 Oct to 15 Nov**, hold through 26 Nov, and in the final 72 hours go mostly to warm audiences (remarketing, brand search), not cold prospecting.

## 2. Competitor BFCM ads on Google (pulled 16 Oct 2026)

Method: ScrapeCreators Google ad library through treg, 18 domains (Klaviyo, Omnisend, Privy, Mailchimp, Yotpo, Gorgias, Attentive, Postscript, Drip, Sendlane, Recart, Brevo, PushOwl, AfterShip, Justuno, PushEngage, SMSBump, Okendo), windows 10 Oct to 3 Dec 2025 and 10 Sep to 16 Oct 2026, then ad detail for every creative first shown inside a window (about 350 creatives). **2024 is a gap:** every 2024 window returned zero ads for every brand, so the library does not serve creatives that stopped before about late 2025. Region lists below are where impressions were recorded, not targeting.

| Brand | What ran (dates, formats) | Hook and offer | Landing page |
|---|---|---|---|
| Omnisend 2025 | Image ads (Demand Gen style, CTA "See more") 17 Oct to 15 Nov, US; videos 15 s, 31 s, 1 min 31 s, 10 Oct to 15 Nov, US; search in DE, FR, ES 17 Oct to 6 Nov | "Get Set Up For BFCM", "The move's on us. The deal's on you.", "We don't just migrate. We move you in.", "30% OFF for 12 months + MIGRATION PACKAGE"; 15 s video: "Switch to Omnisend without the meltdown and get 30% off for 3 months!"; search: "The Smart Switch Before BFCM" | Dedicated /bfcm-2025/ plus competitor-specific pages (/migrate-from-yotpo/, /yotpo-bfcm2025/) |
| Omnisend 2026 (live now) | Images since 22 Sep, videos 27 s and 43 s since 25 Sep, US | "Cut BFCM costs. Same results. Smaller bill. We migrate you in 5 days, for free.", "Email & SMS. Now even for less-er.", "Not Your First BFCM Rodeo", "Last chance 30% off for 3 months" | omnisend.com/bfcm/: 30% off for 3 months, code BLACK-FRIDAY-2026, valid to 1 Dec 2026, free 5-day migration. Also image ads that go **straight to its App Store listing** (apps.shopify.com/omnisend) |
| Klaviyo 2026 (live now) | US search RSAs since 5 Oct; offer RSAs since 2 to 3 Oct (US, AU); image ads US/CA/AU since 10 Sep | "Get Ready for Black Friday", "Black Friday Campaign Builder", "AI Powered Marketing for BFCM"; **"$1 First Month Email Plan", "Get $19 Off Your First Month"**, "Join 205,000+ brands" | Terms page: $19 off the first month of the $20 Email plan, new paid accounts only, auto-applied, ends 11:59 pm ET 30 Nov 2026 (https://www.klaviyo.com/legal/$19-off-promotion) |
| Klaviyo 2025 | BFCM only as sitelinks/callouts on WhatsApp and AI ads in EU ("Win BFCM with Klaviyo", "Domina BFCM con Klaviyo") | No discount | klaviyo.com |
| Privy 2025 | Search from 3 Oct; BF videos 14 to 35 s from 11 Oct; image ads; nothing on Google in the current 2026 window | Every search headline: "Try Free for 15 Days"; videos: "Black Friday is almost here, turn browsers into buyers before the busiest weekend", "This BFCM, don't leave sales on the table"; lead magnet "Free Black Friday Playbook: 40+ Templates"; after BF: "Black Friday might be over, but the holiday season is in full swing" | /bfcm-playbook, /contact |
| Yotpo 2025 | Search to 10 Dec; gated report videos 47 s to 1 min 25 s | "Turn BFCM Shoppers into Fans", "Win Big This Black Friday"; "The BFCM Alter-Ego Report" | /gated/bfcm-on-tour/ |
| Attentive 2025 | 28 Oct to 21 Nov: search, video, image case studies | "iOS Update? No Problem", "Victoria Beckham achieves 49x global ROI", "UNTUCKit 30%+ lift"; demo ask | /book-demo |
| Mailchimp | 2025: no BF offer, "Better prices and tools than the competition"; 2026 since 5 Oct: videos "Turn Shoppers Into Buyers", "More ROI, Less Complexity" (US + EU) | Price and AI positioning | mailchimp.com |
| AfterShip 2025 | Video and image | "Own BFCM, Don't Survive It", "Turn BFCM chaos into year-round growth" | aftership.com |
| Gorgias, Postscript, Drip, Sendlane, Recart, Justuno, PushEngage, SMSBump | No BFCM creative on Google in either window | | |
| PushOwl domain, Oct to Nov 2025 | Only MagicFit ads (mostly India and Pakistan) | No PushOwl BFCM offer ran on Google last year, so **there is no internal baseline** | |

**Takeaways**
- T1 (VERIFIED pattern): the dominant merchant BFCM play is "discount plus we do the switch for you" (Omnisend both years). Our extras (migration, strategy call, ads, credits) fit this pattern; lead with the service, not only the number.
- T2 (VERIFIED, important): **Klaviyo is running a first-month-for-about-$1 offer in US search until 30 Nov**, the same shape as our "first bill is on us". Ours is stronger ($0, then 30% off, plus extras) but we cannot name them; our headline must say "$0 first bill" plainly and add the "then 30% off" half, or we look like the copy.
- T3 (VERIFIED): competitor merchant videos are 15 to 43 s (15, 27, 31, 35, 43 s). Our 30 to 45 s videos fit; a 15 s cutdown of the best one matches what Omnisend and Privy run.
- T4 (VERIFIED): Omnisend and Privy ran their BFCM video and image creative in the US only; EU got search only.
- T5 (VERIFIED): dedicated BFCM landing pages everywhere, plus per-competitor conquest pages (Omnisend vs Yotpo). Omnisend also sends some Google traffic straight to its App Store listing.
- T6 (VERIFIED): colder audiences get a lead magnet (Privy playbook, Yotpo report), not just a discount.

## 3. Keyword demand and CPC (SE Ranking via treg, Oct 2026 values)

Format: monthly searches / CPC. "No bid data" means too little advertiser competition to estimate.

| Keyword | US | UK | CA | DE | FR |
|---|---|---|---|---|---|
| web push notifications | 540 / $5.08 | 210 / $3.18 | 140 / $3.52 | 390 / $2.62 | 260 / $2.97 |
| browser push notifications | 140 / $5.82 | 40 / $2.84 | 20 / no bid data | 50 / $2.14 | n/a |
| push notification app | 320 / $5.23 | 70 / $4.53 | 30 / $1.77 | 50 / $1.89 | 10 / no bid data |
| web push notification service | 70 / no bid data | 10 / no bid data | n/a | n/a | 10 / no bid data |
| push notifications for ecommerce | 10 / no bid data | n/a | n/a | n/a | n/a |
| abandoned cart email | 360 / $4.59 | 210 / $4.12 | 90 / $1.38 | 40 / $1.88 | 30 / no bid data |
| abandoned cart recovery | 210 / $7.00 | 50 / $2.99 | 10 / $3.39 | n/a | n/a |
| cart abandonment software | 110 / $11.79 | 10 / no bid data | n/a | n/a | n/a |
| abandoned cart app | 10 / no bid data | n/a | n/a | n/a | n/a |
| ecommerce email marketing | 480 / $20.23 | 110 / $12.77 | 40 / no bid data | 50 / $11.43 | 20 / $5.84 |
| ecommerce email marketing software | 140 / $48.94 | 20 / no bid data | n/a | n/a | n/a |
| email marketing app | 260 / $11.63 | 40 / $22.01 | 40 / $19.83 | n/a | 10 / no bid data |
| ecommerce marketing automation | 320 / $4.28 | 70 / no bid data | 10 / no bid data | 10 / $4.59 | 10 / no bid data |
| sms marketing | 3,200 / $16.02 | 480 / $9.86 | 210 / $5.92 | 210 / $4.00 | 590 / $7.43 |
| sms marketing app | 70 / $8.93 | 10 / no bid data | n/a | n/a | n/a |
| sms marketing for ecommerce | 90 / no bid data | n/a | n/a | n/a | n/a |
| whatsapp marketing | 320 / $5.67 | 320 / $5.77 | 70 / $4.83 | 390 / $6.95 | 90 / $4.35 |
| black friday marketing | 140 / no bid data | 40 / no bid data | 10 / no bid data | 40 / no bid data | 20 / no bid data |
| black friday email marketing | 110 / no bid data | n/a | n/a | n/a | n/a |
| black friday email templates | 110 / no bid data | n/a | n/a | n/a | n/a |
| black friday marketing ideas | 110 / no bid data | 20 / $16.92 | 10 / no bid data | 10 / no bid data | n/a |
| black friday sms | 110 / no bid data | n/a | n/a | n/a | 10 / no bid data |
| pushowl (brand) | 210 / $6.91 | 70 / $4.31 | n/a | n/a | 70 / $3.45 |
| klaviyo alternative | 390 / $19.98 | 70 / $21.18 | n/a | 40 / $18.12 | n/a |
| klaviyo pricing | 1,000 / $20.87 | 20 / $21.12 | 320 / $19.77 | 170 / $5.66 | 140 / $5.81 |
| mailchimp alternative | 260 / $12.98 | 260 / $7.07 | 40 / $8.42 | 170 / $11.85 | 20 / no bid data |
| omnisend alternative | 50 / $11.12 | n/a | n/a | n/a | n/a |
| email marketing software | 27,800 / $61.06 | 20 / $19.39 | 320 / $10.82 | 10 / $7.29 | 30 / $9.14 |
| email marketing platform | 6,600 / $27.63 | 10 / $13.69 | 20 / $14.11 | 90 / $8.07 | 50 / $7.28 |
| sms marketing platform | 1,300 / $22.50 | 70 / $11.11 | 110 / $19.29 | 20 / $6.10 | 10 / no bid data |
| shopify email marketing (reference only, we cannot bid) | 150 / $7.95 | 140 / $6.73 | 110 / $2.53 | 50 / $6.51 | n/a |
| shopify abandoned cart (reference only) | 210 / $3.87 | 50 / no bid data | 30 / no bid data | 10 / no bid data | n/a |

Findings (VERIFIED data, INFERENCE on use):
- 3.1 Three of the five planned themes have almost no search demand: "abandoned cart app" 10/mo US, "black friday marketing app" no data, "sms marketing for store" no data. Exact or phrase match on the planned phrases will barely serve.
- 3.2 The themes with real volume at sane CPCs are web push (about $2.60 to $5.80), abandoned cart email/recovery ($1.40 to $7), push notification app, WhatsApp marketing ($4.30 to $7) and Black Friday marketing/email/SMS (no bid data = cheap, low competition). "ecommerce email marketing" works but costs $11 to $20.
- 3.3 Avoid the generic SaaS heads: "email marketing software" ($61), "email marketing platform" ($28), "sms marketing platform" ($22.50), "ecommerce email marketing software" ($49). They would eat the $30/day in two clicks.
- 3.4 English queries in DE and FR are real for web push and WhatsApp (DE 390 and 390/mo) at the cheapest CPCs in the set.
- 3.5 Brand "pushowl" has 210/mo in the US at $6.91 CPC, which means someone is bidding on it. Meta at $300/day will push more people to search the brand.
- 3.6 Competitor terms carry volume ("klaviyo pricing" 1,000/mo US, "klaviyo alternative" 390) at about $20. Bidding on them as keywords is a separate decision from ad text (our rule bans the name in ad text only).

## 4. Demand Gen best practices (current Google guidance)

| # | Finding | Source | Confidence |
|---|---|---|---|
| 4.1 | **Budget floor:** "Set a daily budget of $100 or more" with Maximize strategies, or at least 10x target CPA with target strategies (newest wording). Older Google pages say 15x or 20x CPA, "$100 per day, per ad group" to avoid a cold start, and $500 per ad group per day for efficient performance. A Google PM called $100/day the "bare minimum" on 1 Oct 2026. | https://support.google.com/google-ads/answer/14693848 , https://support.google.com/google-ads/answer/14718973 , https://support.google.com/google-ads/answer/13695777 , https://ppc.land/google-pm-calls-100-a-day-the-floor-for-a-demand-gen-campaign/ | VERIFIED (PM quote VENDOR) |
| 4.2 | **50 conversions:** "Do not evaluate performance until the campaign has generated at least 50 conversions"; "wait 50 conversions before making changes." | answer/14693848 , https://support.google.com/google-ads/answer/12563349 | VERIFIED |
| 4.3 | **Target CPA timing:** start on Maximize conversions and shift to tCPA "after your campaign received at least 50 conversions." No proxy or Maximize clicks warm-up: start on conversion bidding from day one. | https://support.google.com/google-ads/answer/14509385 | VERIFIED |
| 4.4 | **Learning length:** Google gives no fixed number of days; the 2023 guide asks for a 4 to 6 week test. Google said at GML (May 2026) that only 40% of Demand Gen conversions happen in the first 30 days. | https://services.google.com/fh/files/blogs/external_demandgen_implementation_guide.pdf ; ppc.land (Oct 2026) | VERIFIED / VENDOR |
| 4.5 | **Change pace:** flex bids and budgets "by 5 to 10% (and no more than 15%) per week"; "Changing settings forces the campaign to relearn." | answer/14693848 | VERIFIED |
| 4.6 | **Consolidation:** merge ad groups with fewer than 30 conversions in 30 days; combine similar audience themes; use "a dedicated ad group for Remarketing/Retention." | answer/14693848 | VERIFIED |
| 4.7 | **Creative benchmark per campaign:** at least one ad with 3 vertical, 3 square and 3 horizontal images, and 1 vertical, 1 square and 1 horizontal video. | answer/14693848 | VERIFIED |
| 4.8 | **Image ad specs:** up to 20 images per ad ("upload 3 of each aspect orientation"): 1.91:1 (1200x628), 1:1 (1200x1200), 4:5 (960x1200), 9:16 (1080x1920, optional, recommended for Shorts). Up to 5 headlines (40 characters, at least 3) and 5 descriptions (90 characters, at least 3); business name 25 characters. | https://support.google.com/google-ads/answer/17140672 , https://support.google.com/google-ads/answer/13704860 | VERIFIED |
| 4.9 | **Video specs:** 16:9, 1:1, 4:5, 9:16; minimum 5 s; videos under 10 s cannot serve in-stream; up to 5 videos and 5 logos per video ad. | answer/13704860 , https://support.google.com/google-ads/answer/13695389 | VERIFIED |
| 4.10 | **Refresh:** pause an asset only if it is low performing and has had at least 14 days to ramp; add new assets before removing old ones, a small share at a time. | answer/14693848 | VERIFIED |
| 4.11 | **Channels:** "Do not restrict your campaigns to specific channels." Channels: YouTube in-stream, in-feed and Shorts, Discover, Gmail, Display (added Apr 2025) and Maps. Display campaigns are being folded into Demand Gen (migration tool June 2026). | answer/14693848 , https://developers.google.com/google-ads/api/docs/demand-gen/channel-controls , https://support.google.com/google-ads/answer/17051545 | VERIFIED |
| 4.12 | **Lookalikes:** still available, Demand Gen only; since March 2026 they act as signals, not hard limits. | answer/14509385 ; https://searchengineland.com/google-shifts-lookalike-to-ai-signals-in-demand-gen-469400 | VERIFIED / VENDOR |
| 4.13 | **Google's performance claims:** 3 of the 4 "Performance Four" practices gave "over 40% more conversions" (Apr 2024 to Dec 2025 data); adding image ads to video gave "20% more conversions at the same cost per action"; 58% higher ROAS than Video Action Campaigns (Nielsen, Google-commissioned). | answer/14693848 , https://support.google.com/google-ads/answer/15110871 , https://blog.google/products/ads-commerce/new-demand-gen-features-2025/ | VERIFIED (Google's own claims) |
| 4.14 | **Goals:** one conversion goal per campaign works best (2023 guide); a campaign can use its own custom goal; shallow actions should be non-biddable. No page states outright that a one-action custom goal works in Demand Gen, but nothing forbids it. | answer/14509385 , https://support.google.com/google-ads/answer/9143218 | VERIFIED / INFERENCE |
| 4.15 | **Assets:** sitelinks are available in Demand Gen; lead form assets are not (Search, PMax, Display only), so the landing-page email box stays the conversion. | answer/13695777 , https://support.google.com/google-ads/answer/9423234 | VERIFIED |
| 4.16 | **Our own account:** when one ad held a 16:9 brand film plus vertical videos, Demand Gen put most of the spend on the 16:9 film (77% of video spend across the account) even though its view rate was 6 to 7% vs 24 to 41% for the verticals. Different concepts in one ad hide the winner. | ad-intel-pages/pushowl-yt-teardown | VERIFIED (first party) |

## 5. YouTube creative for merchant lead gen

| # | Finding | Source | Confidence |
|---|---|---|---|
| 5.1 | Video Action Campaigns are gone: no new ones from Apr 2025, all upgraded to Demand Gen by Apr 2026. Demand Gen is the only conversion video campaign. | https://support.google.com/google-ads/answer/15110871 | VERIFIED |
| 5.2 | Google's creative checks: prominent brand logo in the first 5 seconds; high-quality human voiceover; at least one 16:9, one 9:16 and one 1:1 video per ad group. | https://support.google.com/google-ads/answer/13812351 | VERIFIED |
| 5.3 | ABCD (Attention, Branding, Connection, Direction): ads following it showed a 30% lift in short-term sales likelihood (Google and Kantar, 2021); YouTube is "almost entirely a sound-on experience"; end with a clear next step. | https://business.google.com/us/think/future-of-marketing/youtube-video-ad-creative/ | VERIFIED (Google's claim) |
| 5.4 | Shorts: "For action-oriented ads, use 10 to 30 second vertical videos"; sound (music, voiceover or both) "increase[s] conversions by over 20%"; horizontal videos show with blurred bars; the Demand Gen CTA button appears 3 s in; give a 40-character headline and a 90-character description. No captions rule beyond "consider text overlays". | https://support.google.com/google-ads/answer/16041697 | VERIFIED |
| 5.5 | Our account: vertical creator videos held 24 to 41% view rate vs 6 to 7% for 16:9 films; the "paying for ghost subscribers" angle kept 41% and 45% watched to the end; "Abandoned carts are costing you thousands" had the best CTR (4.2%) despite showing the product only at 34 s; the 2025 BFCM video was the weakest vertical (17.9%) and still carries a "14-day free trial" line. | ad-intel-pages/pushowl-yt-teardown | VERIFIED (first party) |
| 5.6 | Competitor merchant BFCM videos: 15 to 43 s; hooks name the timing ("Black Friday is almost here, turn browsers into buyers before the busiest weekend", Privy) or the bill ("Cut BFCM costs. Same results. Smaller bill.", Omnisend). | Section 2 | VERIFIED |
| 5.7 | No B2B or SaaS YouTube case study with lead-gen numbers for merchant audiences turned up. | Searches | GAP |

## 6. Search during BFCM

| # | Finding | Source | Confidence |
|---|---|---|---|
| 6.1 | Seasonality adjustments are supported on Search, Shopping, Demand Gen and Display only with Target CPA or Target ROAS (PMax and App with any strategy). Google calls them "ideal for short events of 1 to 7 days" and says they "may not work as well" for more than 14 days at a time. Not suitable for a 46-day promo, and not usable on Maximize conversions at all. | https://support.google.com/google-ads/answer/10369906 | VERIFIED |
| 6.2 | Optmyzr (19 Nov 2025, 4,000 to 5,900 accounts per year, 2022 to 2024 BFCM windows): accounts using seasonality adjustments saw CPC inflation of +32% to +37% vs +16% to +17% without, and ROAS fell 10% to 17% with them vs roughly flat without. Adjustments "effectively doubled CPC inflation." | https://www.optmyzr.com/blog/bfcm-seasonality-adjustments-study/ | VENDOR |
| 6.3 | Data exclusions are only for conversion tracking outages, "not recommended for excluding irregular performance periods, such as promotional periods." Exclude about 90% of the clicks tied to the bad data; do not remove an exclusion once applied. Demand Gen is not listed. | https://support.google.com/google-ads/answer/10276486 , https://support.google.com/google-ads/answer/10370710 | VERIFIED |
| 6.4 | RSA countdown syntax: `{COUNTDOWN(yyyy-MM-dd HH:mm:ss,daysBefore)}` and `{GLOBAL_COUNTDOWN(yyyy-MM-dd HH:mm:ss,daysBefore)}`. Default start 5 days before the end; output up to 8 characters; keep at least 3 headlines without a countdown; ads with countdowns stop showing after the end date. Still supported in 2026. | https://support.google.com/google-ads/answer/6193743 | VERIFIED |
| 6.5 | Time zone conflict: the Help Center says COUNTDOWN follows the searcher's time zone and GLOBAL_COUNTDOWN the account's; the API doc says the reverse. For one hard PT deadline, use GLOBAL_COUNTDOWN with the deadline written in the account's time zone, and test with Ad Preview. | Help Center vs https://developers.google.com/google-ads/api/docs/ads/customize-responsive-search-ads | VERIFIED conflict; choice is INFERENCE |
| 6.6 | Broad match "pairs particularly well with Smart Bidding" (Google cites about 25% more conversions when moving phrase to broad in tCPA campaigns) but notes "additional budget may be required." At $30/day broad mostly competes for the same small budget. | https://support.google.com/google-ads/answer/10195720 | VERIFIED; fit is INFERENCE |
| 6.7 | AI Max for Search (May 2025, opt-in): broad plus keywordless matching, text customization, final URL expansion. Google claims 14% more conversions at similar CPA, but says it "won't be effective if campaigns are limited by budget." Final URL expansion and generated text are also a compliance risk for our banned words. | https://support.google.com/google-ads/answer/15910366 | VERIFIED; risk is INFERENCE |
| 6.8 | Account-level negative keywords: up to 1,000 per account, applied across Search, PMax and more. Shared lists: 20 lists, 5,000 keywords each. Brand exclusions work across match types. | https://support.google.com/google-ads/answer/2453983 , https://support.google.com/google-ads/answer/13729701 | VERIFIED |
| 6.9 | Shopify partners may not use Shopify trademarks (including misspellings and long-tail terms such as "Shopify dropshipping app") in PPC without written permission, and must add "Shopify" as a negative keyword. | https://help.shopify.com/en/partners/partner-program/shopify-branding | VERIFIED (Shopify's own help page) |
| 6.10 | Brand bidding evidence is mixed (a 3-week holdout found about 1% traffic loss without brand ads; another on/off test found 75% more signups with them on). The deciding factor is whether competitors bid on the brand; the $6.91 brand CPC in 3.5 says someone does. | https://www.polaranalytics.com/case-studies/willpowders-brand-search-polar-incrementality-testing , https://www.closedloop.com/we-paused-ppc-brand-bidding-heres-what-happened-next/ | VENDOR |

## 7. Bidding and budget

| # | Finding | Source | Confidence |
|---|---|---|---|
| 7.1 | Target CPA can start with no conversion history; Google evaluates on "the last 30 days, including at least 30 conversions." | https://support.google.com/google-ads/answer/6268632 | VERIFIED |
| 7.2 | Learning: "It can take a few conversion cycles (1 to 2 typically)"; Learning is triggered by a new or reactivated strategy, a setting change, or a composition change (campaigns, ad groups, keywords added or removed). A September 2026 report says the page now reads "up to around 50 conversion events or three conversion cycles." | https://support.google.com/google-ads/answer/13020501 ; https://www.techwyse.com/news/platform-updates/google-ads-smart-bidding-learning-period-50-conversions | VERIFIED / VENDOR |
| 7.3 | Demand Gen: "Set a daily budget of $100 or more" with Maximize strategies, or at least 10x target CPA with target strategies; "Do not evaluate performance until the campaign has generated at least 50 conversions"; "Changing settings forces the campaign to relearn"; "slowly flex bids and budgets by 5 to 10% (and no more than 15%) per week"; merge ad groups with fewer than 30 conversions in 30 days; give assets 14 days before pausing low performers. | https://support.google.com/google-ads/answer/14693848 | VERIFIED |
| 7.4 | Demand Gen implementation guide: run Maximize conversions until more than 50 conversions, then move to target CPA. | https://services.google.com/fh/files/blogs/external_demandgen_implementation_guide.pdf | VERIFIED (snippet) |
| 7.5 | No Google number exists for a "safe" Search budget change; practitioners use 20 to 30% per change. | https://www.dotidot.io/post/google-ads-learning-period-tips-to-avoid-resets | VENDOR |
| 7.6 | Overdelivery: up to 2x the average daily budget on a given day, never more than 30.4x in a month (excess credited). | https://support.google.com/google-ads/answer/2375423 | VERIFIED |
| 7.7 | A campaign end date ends at 11:59 pm in the **account's** time zone; exact hour ends need an automated rule (frequency "Once", action "Pause campaigns"). | https://support.google.com/google-ads/answer/2404203 , https://support.google.com/google-ads/answer/2497710 | VERIFIED |
| 7.8 | Changing a goal or conversion action sends Smart Bidding back to learning (1 to 2 conversion cycles); set budgets to their intended level before changing conversion tracking. | https://support.google.com/google-ads/answer/14571185 | VERIFIED |

## 8. Measurement: proxy claim vs true install and redemption

| # | Finding | Source | Confidence |
|---|---|---|---|
| 8.1 | **Upload path:** "Starting June 15, 2026, UploadClickConversions requests will fail if the developer token hasn't previously sent requests. Use the Data Manager API instead." Offline imports and lead uploads are moving to Data Manager. | https://developers.google.com/google-ads/api/docs/conversions/upload-clicks , https://support.google.com/google-ads/answer/15713840 | VERIFIED |
| 8.2 | Create the offline conversion action **before** the clicks you want to import ("Otherwise, you won't be able to import your early conversions"), then wait 4 to 6 hours before the first upload. Auto-tagging required. | https://support.google.com/google-ads/answer/7012522 | VERIFIED |
| 8.3 | gclid conversions can be uploaded up to 90 days after the click, email-matched ones up to 63 days. "Upload conversions at least daily," and keep daily uploads for one to two conversion cycles before counting an action in the Conversions column (observe first, then promote). | https://support.google.com/google-ads/answer/10029210 | VERIFIED |
| 8.4 | Enhanced conversions for leads: the Google tag captures hashed user-provided data (email) on the lead form, later outcomes are imported keyed on the same hashed email, ideally with the gclid too. It also enables engaged-view and cross-device conversions. Google reports a median 10% more conversions when first-party data goes with gclids. | https://support.google.com/google-ads/answer/15713840 , https://support.google.com/google-ads/answer/14274408 | VERIFIED |
| 8.5 | Google's upgrade playbook: run the new lead action alongside for "the longer of 3 conversion cycles or 4 weeks," then swap primary and secondary. On a 46-day flight that is most of the promo. | https://support.google.com/google-ads/answer/15479791 | VERIFIED; fit is INFERENCE |
| 8.6 | Best practice is to bid on a qualified or converted lead stage and to create one conversion action per funnel stage, with values if you want value bidding. | https://support.google.com/google-ads/answer/10029210 | VERIFIED |
| 8.7 | gbraid (web ad click into an iOS app) and wbraid (in-app ad click to a web page) replace gclid on some iOS traffic; custom variables don't work with them. YouTube app clicks on iOS can arrive with wbraid, so the LP must store gclid, gbraid and wbraid. | https://developers.google.com/google-ads/api/docs/conversions/upload-clicks | VERIFIED definitions; storage advice INFERENCE |
| 8.8 | No Google page explicitly confirms offline import credit for Demand Gen clicks, but Demand Gen uses the same goals as other performance campaigns and reports conversions up to 90 days after the click; view-based credit needs enhanced conversions for leads. | https://support.google.com/google-ads/answer/14715303 | VERIFIED quotes; attribution INFERENCE |
| 8.9 | Conversion delay: recent days understate conversions; bid strategy reports show predicted late conversions. Judge installs and redemptions on cohorts at least 3 to 7 days old. | https://support.google.com/google-ads/answer/6239119 | VERIFIED; window INFERENCE |

## 9. Benchmarks

| # | Benchmark | Source | Confidence |
|---|---|---|---|
| 9.1 | **Our own account** (Demand Gen, YT ROW + India + remarketing, 1 Apr to 14 Oct 2026): CPM about $1.80 to $3.30 (heavy India and ROW mix); 16:9 brand films 6 to 7% view rate, 9:16 creator videos 24 to 41% view rate; CTR 1.5% to 4.2%. When an ad held both a 16:9 film and verticals, Demand Gen pushed 77% of spend to the 16:9 films. US/UK/CA will cost several times more. | ad-intel-pages/pushowl-yt-teardown (15 Oct 2026) | VERIFIED (first party) |
| 9.2 | YouTube CPM: $5 to $10 for most advertisers; Shorts about $4; in-feed $3 to $8 with 1 to 3% CTR; Oct to Nov $5 to $7+, Dec average $5.70, Cyber Week peak $6.93. | https://www.storegrowers.com/youtube-ads-benchmarks/ (Feb 2026, Strike Social and Lenos data) | VENDOR |
| 9.3 | Demand Gen planning ranges: CTR 0.75% to 1.2%, CPC $1.40 to $2.00 (0.35% to 0.75% CTR and $2.00 to $2.75 CPC at launch); ecommerce: CTR 0.5% to 2%, CPC $0.30 to $1.50, view rate 15% to 35%. | https://affectgroup.com/blog/demand-gen-benchmarks-ctr-and-cpc-planning-ranges/ , https://www.storegrowers.com/demand-gen-benchmarks/ | VENDOR |
| 9.4 | Search, US, Apr 2025 to Mar 2026: all industries CPC about $5.42, CVR 8.18%; Business Services CPC $5.87, CTR 6.10%, CVR 4.85%, cost per lead $93.69. At $30/day that is about 5 clicks a day. | WordStream/LocaliQ 2026 via https://megadigital.ai/en/blog/google-ads-benchmarks/ | VENDOR |
| 9.5 | BFCM CPC inflation (retail samples): +16% to +17% in the BFCM window without seasonality adjustments (Optmyzr); +24% YoY Black Friday 2025 in Europe (Smarter Ecommerce); +22% MoM 17 Nov to 16 Dec 2024 (Triple Whale); plan for +25 to 30% (Triple Whale). No clean B2B split exists. | https://www.optmyzr.com/blog/bfcm-seasonality-adjustments-study/ , https://smarter-ecommerce.com/en/smec-market-observer/2025/black-friday-2025-recap , https://www.optmyzr.com/bfcm-google-ads-2025-budget-automation-guide/ | VENDOR |
| 9.6 | Meta CPM: +3% in 1 to 15 Nov 2025 and +11% in 16 to 30 Nov 2025 (agency sample). | https://geistm.com/blog/meta-rate-trends-q4-2025/ | VENDOR |
| 9.7 | Our category search terms compete with app vendors, not retailers, so Search inflation should be mild; Demand Gen and YouTube share inventory with retail, so expect their CPMs to rise most from about 20 Nov. | Reasoning from 9.2 and 9.5 | INFERENCE |

---

# Part 2: Google playbook for PushOwl BFCM 2026

Everything below is a recommendation built from Part 1. Labels in brackets point to the evidence: [4.1] means finding 4.1. Unlabelled numbers are our proposal.

## A. Changes vs what is being built (apply these first)

| # | Being built | Change to | Why |
|---|---|---|---|
| A1 | Demand Gen video ($65/day) and Demand Gen image ($35/day) as **two campaigns** | **One Demand Gen prospecting campaign at $100/day** with two ad groups: Video and Image (copy and paste the built ad groups into one campaign) | Google's floor is $100/day per Demand Gen campaign on Maximize [4.1]; one bid strategy learns from twice the claims [4.2, 4.6]; images plus video in one campaign gave 20% more conversions at the same CPA [4.13] |
| A2 | Remarketing $20/day | Keep as its **own campaign** (so its money is guaranteed in the final 72 hours); $20 to 4 Nov, $25 from 5 Nov, $40 from 27 Nov. Audiences fill from Meta's $300/day of LP traffic too, so the list will not be small | Control of the closing push; Google's alternative is a remarketing ad group inside the Demand Gen campaign [4.6] |
| A3 | Search $30/day on "abandoned cart app", "web push for store", "ecommerce email marketing app", "sms marketing for store", "black friday marketing app"; brand only "if none" | Keep $30/day but **rebuild the keywords** around themes that have volume (Section D), **add a brand ad group now**, phrase and exact only, AI Max off, Search Partners and Display expansion off | Three of the five planned phrases have about zero searches [3.1]; "pushowl" has 210/mo in the US at $6.91, so someone bids on it [3.5]; broad and AI Max need budget we don't have [6.6, 6.7] |
| A4 | Target CPA after about 30 claims | **Stay on Maximize conversions for the whole flight by default.** Optional tCPA only if the Demand Gen campaign has 50 or more claims **and** it is on or before 1 Nov | Google: tCPA after at least 50 conversions [4.3]; any change relearns [4.5, 7.2]; a relearn inside the 5 to 15 Nov peak is the worst timing |
| A5 | 3 vertical videos, 30 to 45 s, each its own ad | Keep **one ad per concept** but put that concept's other versions in the same ad: a 15 to 20 s cutdown, and 1:1 and 16:9 versions when they exist. Never put two different concepts in one ad | Google benchmark is one ad with vertical, square and horizontal [4.7, 5.2]; 10 to 30 s for action [5.4]; in our account mixed-concept ads hid the winner [4.16] |
| A6 | 16 statics (1:1, 1.91:1, 4:5) | Package them so at least one image ad has 3 images of each ratio [4.7, 4.8]; 4 ads max (one per narrative or pair of narratives); add 9:16 versions of the 3 best if fast | Google's benchmark; 9:16 opens Shorts inventory for images |
| A7 | Channel controls not specified | Leave every channel on except Maps at launch; review Display on 26 Oct with install data and cut it only on evidence | Google: don't restrict [4.11]; Maps is irrelevant for a merchant app; Display is the likeliest source of cheap, low-intent email submits (INFERENCE) |
| A8 | (not planned) | **No seasonality adjustments** at any point | 46 days is far past Google's 1 to 7 day use; incompatible with Maximize conversions; doubled CPC inflation in Optmyzr's study [6.1, 6.2] |
| A9 | Old campaigns untouched | Remove the BFCM 2025 video (sJj-H--7F88, says "14-day free trial") from the live YouTube campaigns today, and exclude the 7 BFCM countries from "YT ROW" until 30 Nov (exclusion, not a pause) | It breaks the "free trial" rule beside BFCM2026, and YT ROW would bid against the new campaigns in the same auctions [5.5]. **Needs Farooq's OK** (he asked not to pause campaigns) |
| A10 | Installs and redemptions only in our dashboard | Create the two import conversion actions **before launch**, turn on enhanced conversions for leads on the claim, and upload daily (Section H) | Imports only work for clicks made after the action exists [8.2] |
| A11 | Budget flat at $150/day | Same $150/day envelope, reshaped: hold Demand Gen at the $100 floor through the peak, trim it from 20 Nov, shift money to remarketing and Search for the last 4 days (Section E). Optional +$610 scale if the numbers earn it | Merchants install before about 13 Nov [1.1 to 1.5]; video CPMs peak in Cyber Week [9.2] |

## B. Final structure

| Campaign | Budget | Bid strategy and goal | Ad groups | Geo, language |
|---|---|---|---|---|
| BFCM26 DG Prospecting (Demand Gen) | $100/day | Maximize conversions; campaign goal = **BFCM claim only** (custom goal, not account default) | Video (3 ads), Image (up to 4 ads) | 7 countries, English |
| BFCM26 DG Remarketing (Demand Gen) | $20 to $40/day | Maximize conversions; BFCM claim only | One ad group, video and image ads | 7 countries, English |
| BFCM26 Search | $30 to $35/day | Maximize conversions; BFCM claim only | Web push, Cart recovery, BFCM planning, Ecommerce channels, Brand (+ optional Competitor) | 7 countries; all languages (keywords are English); presence targeting ("people in") |

Account housekeeping: auto-apply recommendations off for these campaigns; auto-tagging on; final URLs carry utm_source=google, utm_medium=cpc (Search) or paid_video / paid_display (Demand Gen), utm_campaign, utm_content={adgroupid}, utm_term={keyword} so the dashboard stitch sees the same IDs as Google.

## C. Assets per campaign

**DG Prospecting: Video ad group (3 ads)**
- One ad per concept. Each ad: the 9:16 master (30 to 45 s), its 15 to 20 s cutdown, and its 1:1 and 16:9 versions when made (up to 5 videos per ad [4.9]). If cutdowns aren't ready, launch with the masters and add them in one batch by 26 Oct.
- First 5 seconds: the offer or the pain, plus the PushOwl logo on screen [5.2, 5.3]; human voiceover, sound on [5.3, 5.4]; product shown in use before 15 s (our 52 s video showed it at 34 s) [5.5].
- Text: 5 headlines (40 characters), 5 descriptions (90), every long headline slot the builder offers; logo; business name; CTA from the builder's list ("Sign up" or "Get started"); sitelinks: How to claim, Plans and pricing, Book a strategy call, Migration help [4.15].
- Hooks with evidence: "paying for ghost subscribers" (41% view rate, our best) [5.5]; abandoned-cart money (best CTR) [5.5]; timing before the busiest weekend (Privy) and smaller bill (Omnisend) [5.6]. Lead with "Your first bill is on us", then "30% off after".

**DG Prospecting: Image ad group (up to 4 ads)**
- At least one ad with 3 x 1:1, 3 x 1.91:1, 3 x 4:5; up to 20 images per ad [4.7, 4.8]. Group the 16 statics by narrative; add 9:16 versions of the top 3 when possible.
- 5 headlines, 5 descriptions, logo (square and landscape), business name (25 characters max).

**DG Remarketing (one ad group)**
- Same videos (cutdowns first) and the 6 strongest statics, with deadline headlines. Planned refreshes: 4 Nov evening (monthly plans join 5 Nov), 19 Nov ("ends 30 Nov"), 26 Nov ("final days").

**Search RSAs (one per ad group, 15 headlines, 4 descriptions)**
Example headlines that pass our rules (30 characters max, no "Shopify", "Klaviyo", "50%", "free month", "free trial", "try free"):
- Your First Bill Is On Us (24)
- Then 30% Off Annual Plans (25), swap to **30% Off Monthly Or Annual** (25) from 5 Nov 00:00 PT
- Web Push, Email, SMS, WhatsApp (30)
- Recover Abandoned Carts (23)
- Set Up Before Black Friday (26)
- Plans From $19/Month (20)
- Migration Done For You (22)
- Strategy Call Included (22)
- Use Code BFCM2026 In The App (28)
- BFCM Deal Ends Nov 30 (21)
- Deal Ends In {GLOBAL_COUNTDOWN(...)} (21 max), with at least 3 headlines that have no countdown [6.4]

Example descriptions (90 characters max): "Your first bill is on us, then 30% off annual plans. New stores, claim by Nov 30." / "Web push, email, SMS and WhatsApp in one app built for ecommerce stores." / "New paying stores also get migration, a strategy call, BFCM ads and $200 in ad credits." / "Install, open Plans, enter BFCM2026. Offer ends Nov 30 at 11:59 pm PT."

Also add a **promotion asset** (30% off, code BFCM2026, 16 Oct to 30 Nov) and the same 4 sitelinks. (INFERENCE: promotion assets add a sale tag and are free to add.)

**Countdown and time zone (do this before launch):** check the account time zone (Admin, Account settings). Daylight saving ends 1 Nov, so the deadline 30 Nov 11:59 pm PT = 1 Dec 07:59 UTC = **1 Dec 13:29 IST**; the monthly switch 5 Nov 00:00 PT = 5 Nov 08:00 UTC = 13:30 IST. If the account runs on PT: `{GLOBAL_COUNTDOWN(2026-11-30 23:59:00,7)}`. If IST: `{GLOBAL_COUNTDOWN(2026-12-01 13:29:00,7)}`. Check it in Ad Preview because Google's two docs disagree on which customizer follows which clock [6.5].

## D. Audience signals, keywords, negatives

**DG Prospecting audience signals** (signals, not limits, since March 2026 [4.12])
1. Lookalike (narrow) seeded from a Customer Match list of installed PushOwl stores' owner emails (all plans).
2. Custom segment, "people who searched for": abandoned cart email, web push notifications, push notification app, sms marketing for ecommerce, whatsapp marketing for ecommerce, ecommerce email marketing, email marketing for online store, black friday email templates, black friday marketing ideas, klaviyo pricing, klaviyo alternative, omnisend pricing, privy pricing, mailchimp alternative. **No "shopify" terms** anywhere, audiences included, because Shopify's partner rule covers trademark use in paid search [6.9] (INFERENCE that audiences are safest treated the same way).
3. Custom segment, "people who browse websites like": klaviyo.com, omnisend.com, privy.com, attentive.com, postscript.io, mailchimp.com, yotpo.com, gorgias.com, judge.me, loox.io.
4. Exclusions: Customer Match of existing paid customers (they never get BFCM2026) and of existing installed stores (free stores get the offer by email and Intercom, so don't pay to reach them cold); BFCM claimers (converters, 30 days).

**DG Remarketing audiences:** BFCM LP visitors, 30 days, all traffic sources (Meta visitors included); pushowl.com visitors, 30 days; YouTube viewers of our BFCM videos, 30 days. Exclude BFCM claimers and the Customer Match lists above. Lists need 100 active users to serve (Google lowered the bar from 1,000 in 2025, VENDOR: https://searchengineland.com/google-lowers-audience-size-limits-across-ads-466816).

**Search keywords (phrase and exact)** [3.1 to 3.6]

| Ad group | Keywords | Expected CPC |
|---|---|---|
| Web push | web push notifications, web push notification, browser push notifications, website push notifications, push notifications for website, push notification app, web push notification service, push notifications for online store | $2 to $6 |
| Cart recovery | abandoned cart email, abandoned cart emails, abandoned cart recovery, abandoned cart sms, cart abandonment software, cart recovery app, recover abandoned carts | $1.40 to $12 |
| BFCM planning | black friday marketing, black friday email marketing, black friday email templates, black friday email campaign, black friday sms, black friday marketing ideas, bfcm marketing, cyber monday email | low (no bid data) |
| Ecommerce channels | ecommerce email marketing, email marketing for ecommerce, ecommerce marketing automation, sms marketing for ecommerce, sms marketing app, [whatsapp marketing] (exact only), whatsapp marketing for ecommerce, email marketing for online store | $4 to $20 |
| Brand | [pushowl], [push owl], pushowl pricing, pushowl black friday, brevo pushowl | about $4 to $7 |
| Competitor (optional, **needs Farooq's OK**, own $10/day campaign if approved) | klaviyo alternative(s), omnisend alternative, mailchimp alternative, klaviyo pricing | about $11 to $21 |

Do not bid on: email marketing software ($61), email marketing platform ($28), sms marketing platform ($22.50), ecommerce email marketing software ($49), plain "sms marketing" (mostly local businesses) [3.3].

**Negative keyword list "BFCM26 negatives"** (shared list on Search; "shopify" variants also at account level [6.8, 6.9])
- Partner rule: shopify, shopfy, shoppify, shopifiy, sh0pify, myshopify, shopify's
- Platforms we don't serve with this offer: woocommerce, wordpress, wix, squarespace, bigcommerce, magento, etsy, amazon, ebay, hubspot, salesforce
- People trying to stop notifications: disable, block, stop, turn off, remove, unsubscribe, allow, settings, chrome, safari, firefox, iphone, android, spam, virus, malware, scam, pop up blocker
- Developers: api, sdk, firebase, fcm, apns, github, javascript, react, flutter, node, npm, code, service worker, vapid, open source, self hosted, php, laravel
- Jobs and courses: job, jobs, career, salary, hiring, course, certification, training, internship, freelance
- Non-ecommerce SMS buyers: church, restaurant, real estate, realtor, dental, salon, gym, school, political, nonprofit, bank, insurance, clinic
- Free-only SMS seekers and support queries: free bulk sms, free sms, receive sms, login, log in, sign in, customer service number, cancel
- Do **not** add "free" on its own: a $0 first bill is our offer.

## E. Dated budget calendar (16 Oct to 30 Nov 2026)

Base plan stays inside the $150/day envelope (flat would be $6,900; this totals about $6,805).

| Phase | Dates | DG Prospecting | DG Remarketing | Search | Daily total | What happens |
|---|---|---|---|---|---|---|
| 1 Learn | 16 to 25 Oct (10 d) | $100 | $20 | $30 | $150 | Launch the day the build passes QA: every day lost is a day of the install window [1.1]. No edits for 7 days except negatives, disapprovals, broken tags. Sanity check day 3, first read day 7 |
| 2 Build | 26 Oct to 4 Nov (10 d) | $100 | $20 | $30 | $150 | Weekly change window Mon 26 Oct and Mon 2 Nov: Display decision [A7], country exclusions, asset adds, optional tCPA gate (A4, last chance 1 Nov). Evening of 4 Nov: add the monthly-offer ads and swap Search headlines (new ads, don't edit the old ones) |
| 3 Peak | 5 to 15 Nov (11 d) | $100 | $25 | $30 | $155 | Monthly plans join the offer 5 Nov 00:00 PT. Merchants' configuration lock is about 13 Nov [1.1]. No bid strategy or goal changes |
| 4 Hold | 16 to 26 Nov (11 d) | $100, then **$85 from 20 Nov** (minus 15%, Google's weekly limit [4.5]) | $25 | $30 | $155 then $140 | Merchants in code freeze from about 20 Nov [1.1]; retail pushes video CPMs up [9.2, 9.7]. Refresh 19 Nov ("ends 30 Nov"), countdown starts showing 23 Nov |
| 5 Final 72 h+ | 27 to 30 Nov (4 d) | $50 | $40 | $35 | $125 | Warm audiences and brand search carry the deadline; refresh 26 Nov ("final days"). End at 30 Nov 11:59 pm PT (Section G) |
| **Total** | 46 days | $4,295 | $1,110 | $1,400 | **$6,805** | |

**Optional scale (+$610, total about $7,415; needs Farooq's OK):** only if, on 2 Nov, Demand Gen has 50 or more claims, CPA at or under target and install rate holding (Section F). Then Demand Gen $115 from 2 Nov, $130 from 9 Nov, $110 from 20 Nov, $50 from 27 Nov. Each step is 15% or less per week [4.5]. Search scales only if it is "limited by budget" with CPA at or under target, by 20% at most per change [7.5].

## F. Daily monitoring and decision thresholds

**Set the target first (from our own stitch, not from Google):**
r = installs ÷ claims for Google traffic, measured on claim cohorts at least 3 days old [8.9] (use the blended LP rate until Google has 30 claims).
Claim CPA target = $15 × r and claim CPA ceiling = $19 × r (same CPI target and ceiling as Meta). Example: r = 0.5 gives a $7.50 target and $9.50 ceiling. If a tCPA is ever set, it must be at least budget ÷ 10 [4.1].

**Daily checks (10 minutes, every morning PT)**
- Per campaign and ad group: spend vs budget, impressions, CPM, CTR, clicks, LP sessions (UTM), claims, claim rate per session, cost per claim.
- From the dashboard: installs and redemptions by campaign, ad group and ad (via gclid and UTMs), CPI, cost per redemption.
- Search terms report: add negatives daily.
- Demand Gen channel report (YouTube, Discover, Gmail, Display) and asset report (video view rate, image CTR).
- Health: claim tag firing (claims vs LP sessions), disapprovals (trademark terms), learning status, "limited by budget", overdelivery.

**Breakage rules (act the same day)**
- Google LP sessions above 50 in a day and 0 claims: the tag is broken. Fix it; on Search add a data exclusion for the outage window [6.3]. Note: the LP is the ad-intel-pages GitHub Pages iframe, so every push goes live; re-test a claim after each push.
- Any disapproval for "Shopify" or competitor names: fix copy within the hour; never appeal with the term kept.
- A search term with $15 or more spend, 0 claims and off-topic: negative it.

**Weekly decisions (Mondays 26 Oct, 2 Nov, 9 Nov, 16 Nov, 23 Nov; batch all changes into that one window)**
- **Scale:** claim CPA at or under target over 7 days, 25 or more claims in those 7 days, and r at or above its baseline: raise Demand Gen up to 15% (only within an approved scale budget), or move money from the weaker campaign.
- **Cut:** claim CPA above 1.3x ceiling over 14 days with 30 or more claims, or stitched CPI above $30 (2x the Meta target) with 15 or more installs: cut that campaign 15% and move the money to the best one. Search below half the Demand Gen install rate after $400 spend: keep only Brand, Web push and Cart recovery.
- **Channel:** a Demand Gen channel with 20 or more claims and an install rate under half the campaign average: exclude it from the Image ad group (Display is the first suspect).
- **Country:** a country with $150 or more spend and claim CPA above 2x the campaign average: exclude it (one change, in the window, not mid-week).
- **Creative:** give every asset 14 days before pausing [4.10]. After that, pause a video whose vertical view rate is under 15% after 5,000 impressions (our verticals run 24 to 41% [5.5]) or any asset at 2x the ad group's claim CPA with $100 or more spend. Always add the replacement before removing the old one [4.10].
- **Refresh dates:** 4 Nov evening, 19 Nov, 26 Nov.
- **Do not judge Demand Gen before 50 claims** [4.2]; before that, only breakage rules apply.

## G. Ending cleanly at 11:59 pm PT on 30 Nov

1. Confirm the account time zone (Section C). End dates stop at 11:59 pm in the **account** time zone [7.7].
2. If the account is on PT: set end date 30 Nov on all three campaigns.
3. If it is on IST (or anything else): set an automated rule, frequency "Once", **1 Dec 13:29 IST**, action "Pause campaigns" on the three BFCM campaigns, plus an end date of 1 Dec as a backstop [7.7]. Overdelivery can reach 2x the daily budget on the last day; that's normal [7.6].
4. Countdown headlines stop on their own at the deadline [6.4].
5. At the deadline the LP claim box must switch to an "offer ended" state so late clicks don't claim a dead code.
6. Keep uploading installs and redemptions until at least 31 Dec; gclid imports work up to 90 days after the click [8.3].

## H. Offline conversion plan (claim stays the bidding goal; installs and redemptions guide the money)

1. **Before launch:** create two conversion actions, "BFCM install (import)" (category Qualified lead) and "BFCM redemption (import)" (category Converted lead), source "Other data sources or CRMs", count One, click-through window 30 days (install) and 60 days (redemption). Make both **secondary** and keep them out of the BFCM goal. Wait 4 to 6 hours before the first upload [8.2, 8.6].
2. **Enhanced conversions for leads on the claim:** turn it on for the "BFCM claim" action and accept the customer data terms (an account admin must). The email is typed inside the GitHub Pages iframe, so the frame bridge must hand the parent page a normalized (trimmed, lower-case) SHA-256 of the email, and the Webflow embed calls `gtag('set', 'user_data', {sha256_email_address: hash})` before the conversion event [8.4]. This lets imports match by email even when the click ID is missing.
3. **Store every click ID:** the LP already forwards gclid; make sure gbraid and wbraid are captured and stitched too [8.7].
4. **Upload daily** [8.3] from the BFCM dashboard: click ID (gclid, gbraid or wbraid), hashed email, conversion time with time zone, action name. Fastest path with no API work: a Google Sheet the dashboard writes to, set up as a **scheduled upload** in Google Ads. If engineering builds an API upload, it has to use the **Data Manager API**, because the old upload call now fails for developer tokens that never sent uploads before [8.1].
5. **Use it to steer, not to bid:** from day 3, read install and redemption counts per campaign, ad group, ad and channel in "All conversions" and in the dashboard. They drive Section F's cut, scale and channel rules.
6. **Do not switch the bidding goal mid-flight.** Google's own swap needs the longer of 3 conversion cycles or 4 weeks [8.5], which lands after the peak, and every goal change relearns [7.8]. Single exception: if by 29 Oct the Demand Gen campaign has 50 or more uploaded installs in 14 days and uploads land within 24 hours, switching that campaign's goal to installs on 2 Nov is defensible. Otherwise keep the claim to the end and make installs (or redemptions) the primary goal for the evergreen campaigns from December.
7. **Dedupe with Meta:** Google's Conversions column will credit remarketing and engaged views for claims that Meta started. The dashboard's last-click UTM stitch is the source of truth for channel CPI.

## I. Open items for Farooq or an account admin

1. Approve A9 (remove the BFCM 2025 video, exclude BFCM countries from YT ROW).
2. Confirm the account time zone (decides Section G and the countdown string).
3. Accept the enhanced conversions customer data terms.
4. Decide on the optional competitor-keyword campaign (keywords only; names never in ad text).
5. Decide on the optional +$610 scale budget, to be triggered only by the 2 Nov numbers.
6. Pull Shopify Partner installs by week for Oct to Dec 2025 to confirm the install-timing curve [1.6].

## Known gaps

- 2024 competitor ads are not retrievable from the ad library; only late 2025 and 2026 creatives were available.
- No public data on Shopify app installs by month; SE Ranking's monthly series is smoothed, so Black Friday search seasonality is low confidence.
- No B2B merchant YouTube case study with lead-gen numbers; no clean November CPC split between B2B and retail.
- Countdown customizer time-zone behaviour is contradictory in Google's docs; test in Ad Preview.
- No Google page explicitly confirms offline-import credit for Demand Gen clicks; the plan assumes it works through gclid/wbraid and enhanced conversions for leads.
