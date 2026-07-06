# VIPAVEL Money Stack — Claude/Codex Handoff

Last verified: 2026-07-04 (America/Los_Angeles)

## Coordination rule

- Canonical implementation repository: `trial-to-paid-leak-audit` on `main`.
- Pull before editing. Work in a new `claude/*` or `codex/*` branch and use a PR.
- Do not overwrite unrelated working-tree changes.
- Never put credentials, API keys, bank details, cookies, or session tokens in Git,
  chat, issue bodies, reports, or generated outreach.
- Email automation is preview-first. A lead must be reviewed and explicitly marked
  `approved`; live sending also requires `OUTREACH_SEND=true` and configured secrets.
- Security checks may only target customer-owned systems with explicit permission.

## Current business direction

Primary offer: **VIPAVEL AI Profit & Revenue Ops** for small AI/SaaS companies.

Offer ladder:

1. `$49` Profit Leak Diagnostic.
2. `$199` Action Pack.
3. Custom implementation sprint after a valuable issue is confirmed.
4. Planned recurring Profit Guard monitoring; not yet created in Stripe.

The diagnostic combines AI cost-per-outcome, retries/model waste, Stripe usage
metering, pricing, trials, webhooks, entitlements, failed payments, and revenue
recovery. Current Stripe revenue was verified as `$0` when audited; infrastructure
was ready but had not produced sales.

## Canonical GitHub repositories

Account: `pavelviproperty-rgb`

- Main revenue repo: https://github.com/pavelviproperty-rgb/trial-to-paid-leak-audit
- Private operating-system repo: https://github.com/pavelviproperty-rgb/PavelOS
- Public repo: https://github.com/pavelviproperty-rgb/mayak
- Public source repo: https://github.com/pavelviproperty-rgb/mayak-source

Merged revenue work:

- PR 1, revenue operations: https://github.com/pavelviproperty-rgb/trial-to-paid-leak-audit/pull/1
- PR 2, client intake: https://github.com/pavelviproperty-rgb/trial-to-paid-leak-audit/pull/2
- PR 3, outreach safety: https://github.com/pavelviproperty-rgb/trial-to-paid-leak-audit/pull/3

Current main commits:

- `478b634` — guarded outreach aligned with Profit Ops.
- `f21d6ac` — privacy-first client intake.
- `fd8056b` — revenue operations workflow.

## Public properties

- Primary domain: https://vipavel.shop/
- Canonical GitHub Pages funnel: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/
- Buyer intake: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/intake.html

Landing pages and assets:

- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-leak-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-checklist.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-sample-report.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-ai-billing-state-gap-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-ai-billing-state-gap-sample-report.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-metered-billing-gap-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-webhook-entitlement-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/successful-outcome-billing-gap-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/outcome-cost-budget-guardrail-audit.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/workflow-cost-checklist.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-billing-alternatives.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/checklist.html
- https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/sample-report.html

Local operating dashboard:

- `/Users/p/Documents/Money/monetization-dashboard.html`

## Verified Stripe payment links

- `$19` MRR Leak Audit Pack:
  https://buy.stripe.com/6oUdRb0JL37VeqU7A0aR200
- `$49` MRR Leak Action Pack:
  https://buy.stripe.com/dRm14p2RTeQD0A4f2saR201
- `$49` AI Agent Cost Leak Audit / current entry offer:
  https://buy.stripe.com/00w9AVdwxeQDfuY9I8aR206
- `$199` AI Agent Cost Action Pack / current upsell:
  https://buy.stripe.com/8x26oJ0JL9wj4QkaMcaR207

Stripe UI previously showed four additional active products: PageSpeed `$199`,
SSL `$99`, Port/.env `$199`, and DMARC `$149`. Their payment-link URLs were not
captured and must be read from the authenticated Stripe account rather than
guessed.

## Accounts and infrastructure

Account identifiers are safe to share inside this handoff; credentials are not.

- Stripe account/workspace: `vipavel` / VIPAVEL. Eight active payment links were
  observed. Do not give third-party tools unrestricted or write-capable Stripe keys.
- Brevo organization: `VIPAVEL LLC`.
  - Verified sender: `Pavel | VIPAVEL LLC <info@vipavel.shop>`.
  - `vipavel.shop` DKIM and DMARC were green when audited.
  - Free allowance observed: 300 emails/day.
  - Campaigns: 0; contacts: 1 at audit time.
- Gmail/Google account used in prior outreach: `vipavelart@gmail.com`.
- Domain: `vipavel.shop`.
  - DNS nameservers observed: `launch1.spaceship.net`, `launch2.spaceship.net`.
  - Vercel A record observed: `76.76.21.21`.
  - Brevo DNS authentication records were present.
- Vercel team id: `team_Sg8SkBhfVW6dQ21A3ePp4Shm`.
- Mercury: user reports it is connected. Banking/account details have not been
  inspected or copied and must remain owner-controlled.

Vercel projects observed as production-ready:

- `customer-success-toolkit`
- `stripe-decline-codes`
- `lp-`
- `ai-cost-transparency`
- `developer-tools-and-resources`
- `lp--productivity-tips-for-en`
- `lp-serverless-security`
- `lp-shopify-integration-with-`
- `dreamtales-ai`
- `ats-resume-auditor`
- `llm-spend-audit`
- `ai-spend-calculator`
- `mrr-leak-calculator`

Verified 2026-07-06: `vipavel.shop` is served by the Vercel project
`stripe-decline-codes` (identical `etag` and `last-modified` between
`https://vipavel.shop/` and `https://stripe-decline-codes.vercel.app/`).
The homepage is the "Stripe Decline Code Reference" tool, which links to the
two active Stripe payment links and to `mrr-leak-calculator.vercel.app`.
Its source is NOT in any `pavelviproperty-rgb` GitHub repo and was not found
on the local machine — it was deployed from another device or via CLI upload.
Do not assume the GitHub Pages repo is the current Vercel source. To edit the
homepage, locate the source on the original device or pull the deployment
from the authenticated Vercel dashboard/CLI.

## Automation already implemented

- `.github/workflows/revenue-operations.yml`: scheduled health check and outreach
  preview artifact generation. It does not enable live sending by itself.
- `scripts/site_health.py`: checks the public funnel and the two current Stripe
  offer links.
- `scripts/outreach.py`: prepares personalized previews and sends only approved
  rows when the separate live-send flag and SMTP secrets are present.
- `ops/leads.csv`: review queue with source, pain signal, relevance, status, and
  `do_not_contact` fields.
- `intake.html`: buyer-side structured email generator. Answers stay in the
  browser until the buyer chooses to open and send the email.

## Current checks

- Main funnel: HTTP 200.
- Buyer intake: HTTP 200.
- `$49` and `$199` current Stripe links: HTTP 200.
- GitHub Pages has occasionally reported a transient deployment failure while
  the legacy Pages build still completed. Check both Actions status and the live
  URL before changing deployment configuration.

## Immediate next work

1. Stripe post-purchase redirect to buyer intake: owner reports it was
   configured in the dashboard on 2026-07-06. External check the same day:
   both links HTTP 200 and their checkout pages render a
   `redirect_success_page_layout` marker. The exact target URL is not visible
   without auth, so per policy this stays "configured, not operational" until
   the first completed checkout actually lands on `intake.html`.
2. Vercel source for `vipavel.shop` identified: project `stripe-decline-codes`
   (see Public properties note). Remaining: recover the source (Deployments →
   latest → Source in the dashboard), commit it to a repo, and use
   "Connect Git Repository" — dashboard confirms no project has Git connected.
   Decision still open: funnel as homepage banner/link vs subdomain.
3. Configure Brevo SMTP/API credentials only in GitHub Actions secrets. Never
   paste them into source or this handoff.
4. Build a small, evidence-backed ICP list of AI/SaaS companies using Stripe.
   Generate drafts only. Do not send until the user reviews the first batch.
5. Create the recurring Profit Guard product only after first demand or explicit
   user approval of pricing and billing terms.

## Access and permission policy

Claude and Codex may use already-authorized sessions to inspect and implement
the stack. Owner intervention is required for sign-in/2FA, payment or banking
actions, new paid subscriptions, permission changes, and final campaign launch.
Do not export passwords, session cookies, API keys, Mercury details, or unrestricted
Stripe credentials between agents. Coordinate via Git commits, PRs, this handoff,
and secret names—not secret values.
