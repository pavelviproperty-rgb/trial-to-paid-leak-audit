# VIPAVEL AI Profit & Revenue Ops

Public conversion funnel for a combined AI cost and Stripe revenue diagnostic:

- AI cost-per-outcome and retry waste;
- metered billing and pricing gaps;
- trial, webhook, entitlement, and failed-payment risks;
- direct checkout for a `$49` diagnostic and `$199` action pack.

## Live intent

This repo is published on GitHub Pages as a fast public test.

- Audit page: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/
- Free checklist: https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/checklist.html

## Checkout

- `$49` AI Agent Cost Leak Audit: https://buy.stripe.com/00w9AVdwxeQDfuY9I8aR206
- `$199` AI Agent Cost Action Pack: https://buy.stripe.com/8x26oJ0JL9wj4QkaMcaR207

## Important note

The primary CTA sends buyers directly to the existing Stripe checkout, with the
`$199` action pack and a custom implementation sprint as expansion paths.

After purchasing, buyers can use `intake.html` to prepare a structured intake
email without storing sensitive answers in a third-party form service.

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
