# Trial-to-Paid Leak Audit

Public landing page for a narrow Stripe diagnostic offer:

- trial-to-paid leak detection;
- first invoice after trial blind-spot explanation;
- free diagnostic checklist;
- direct checkout for a `$19` quick audit and `$49` action pack.

## Live intent

This repo is published on GitHub Pages as a fast public test.

- Audit page: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/
- Free checklist: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/checklist.html

## Checkout

- `$19` MRR Leak Audit Pack: https://buy.stripe.com/6oUdRb0JL37VeqU7A0aR200
- `$49` MRR Leak Action Pack: https://buy.stripe.com/dRm14p2RTeQD0A4f2saR201

## Important note

The page is live-first. The primary CTA now sends buyers directly to Stripe
checkout, with the `$49` action pack available as the first upsell.

Revenue only counts when Stripe shows a paid checkout. A published page,
comments, or prepared audit packet are not revenue.

## Revenue operations

The repository now includes a guarded operating loop:

- `scripts/site_health.py` checks the live page and every Stripe checkout;
- `ops/leads.csv` is the review queue for researched prospects;
- `scripts/outreach.py` creates personalized previews and sends only rows marked
  `approved` when `OUTREACH_SEND=true`;
- `.github/workflows/revenue-operations.yml` runs a daily health check and
  produces preview artifacts without sending mail.

To enable approved sending, configure `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`,
`SMTP_PASSWORD`, and `OUTREACH_FROM` in the execution environment. Keep
`OUTREACH_SEND` unset during research and review.

## AI cost variants

Additional local-ready variants now exist for the same AI-cost offer family:

- AI cost offer: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-leak-audit.html
- AI cost checklist: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-checklist.html
- Stripe AI billing gap: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/stripe-ai-billing-state-gap-audit.html
- Outcome-cost audit: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/outcome-cost-budget-guardrail-audit.html
- Workflow-cost checklist: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/workflow-cost-checklist.html
- AI cost sample report: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/ai-agent-cost-sample-report.html
