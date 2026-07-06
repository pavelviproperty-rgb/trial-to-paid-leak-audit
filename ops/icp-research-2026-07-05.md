# ICP research batch — 2026-07-05

First evidence-backed batch for the review queue (`ops/leads.csv`).
Nothing here is approved for sending. Statuses used:

- `draft` — public contact email found on the company's own site; the outreach
  script will generate a preview file only.
- `research` — company and pain signal verified, but no public email found.
  Inert for the script until a contact is confirmed and status is changed.

## Method

1. Queried Hacker News (Algolia API) for founder-authored posts about Stripe
   usage-based billing, LLM/token costs, and recent Show HN / Launch HN AI-agent
   products (2025–2026).
2. Kept only leads where the company is identifiable and the pain signal is the
   founder's own public statement or the product's own cost surface.
3. Checked each company's site for a published contact email (no guessing,
   no scraping of personal data). Placeholder or missing emails were left blank.
4. Excluded billing vendors (Credyt, Kelviq, Skope, Autumn, ParityDeals) —
   they are competitors/adjacent, not buyers.

## Leads in this batch

| Company | Evidence | Why relevant |
| --- | --- | --- |
| Tonic Fabricate | [HN 47180267](https://news.ycombinator.com/item?id=47180267) — founder post on Stripe's 20-item cap breaking multi-model token billing | Exact offer match: Stripe metering + AI cost-per-outcome. Caveat: company is larger than the core small-team ICP. |
| Mirrors | [HN 48768200](https://news.ycombinator.com/item?id=48768200) — replays production agent traces (re-runs inference at scale) | Token-cost-sensitive by design; early stage, billing maturity unknown. |
| Manufact (YC S25) | [HN 48762862](https://news.ycombinator.com/item?id=48762862) — MCP cloud launch | Early-stage AI infra; usage-to-billing mapping is core to their product. No public email yet. |
| TaskPeace | [HN 48775484](https://news.ycombinator.com/item?id=48775484) — solo founder, ~40 sites run by coding agents, new Stripe checkout | High personal token spend + brand-new billing. No public email yet. |

## Follow-up candidates (not yet leads)

- HN commenter `Katlaszlo` on 47180267: "I faced the same issue working around
  stripe" — company not identified yet.
- Broader market context (bill-shock reports, 500–1000% cost underestimation at
  production scale) supports the offer but names no specific companies:
  [HackerNoon on Stripe UBB for AI](https://hackernoon.com/why-stripe-usage-based-billing-is-fundamentally-broken-for-ai-products),
  [PYMNTS on AI pricing breaking SaaS billing](https://www.pymnts.com/artificial-intelligence-2/2026/cfos-scramble-as-ai-pricing-breaks-traditional-saas-billing-model/).

## Owner review checklist

- [ ] Confirm each pain signal reads accurately and non-creepy in the preview.
- [ ] Fill or confirm contact emails for Manufact and TaskPeace (then set `draft`).
- [ ] Mark any row `approved` only if you want it in the first live batch.
- [ ] Live sending still requires `OUTREACH_SEND=true` plus SMTP secrets in
      GitHub Actions — never in the repo.
