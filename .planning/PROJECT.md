# Billing Leakage Radar

## What This Is

A read-only, one-time diagnostic for founders and revenue-ops owners of small SaaS and AI businesses on Stripe. The operator uploads a redacted export; the tool cross-checks payment state, entitlement access, trial conversion, and AI API cost in a single ranked report — then shows the smallest fix for each leak. Sold as a $49 diagnostic, upsell to a $199 action pack.

## Core Value

A buyer recovers more in one fixed subscription or avoided AI runaway than the $49 price — this must be demonstrably true before anything else is built.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Instrumented landing page: checkout-start, purchase, and intake events tracked
- [ ] Private-beta page live with sitemap submitted
- [ ] Deterministic sample report generated from a redacted fixture (no live Stripe connection required)
- [ ] Stripe checkout links active for $49 diagnostic and $199 action pack
- [ ] Intake form collects enough context to produce a report (company, AI provider, monthly spend, pricing model, problem)
- [ ] Programmatic SEO: 6 narrow-problem pages indexed and returning HTTP 200

### Out of Scope

- OAuth / live Stripe API integration — build only after at least one paid signal; static intake proves demand first
- Automatic refunds, plan changes, or write access to customer systems — diagnostic is read-only by design
- Email sending from the product itself — current outreach is manual/approved via `ops/leads.csv`
- Multi-tenant dashboard or recurring monitoring UI — only if 3+ paid users request it
- Enterprise compliance claims (SOC 2, procurement) — non-user segment
- Paid advertising — no spend until organic or direct conversion is proven
- Consumers and large enterprises — outside ICP

## Context

The site is a fully static HTML funnel hosted on GitHub Pages (vipavel.shop on Vercel). No build step, no external JS dependencies. Stripe checkout happens via external `buy.stripe.com` links already live. A Python health-check script and a guarded outreach script run daily via GitHub Actions. Revenue is $0 today — this is an unvalidated hypothesis.

The core insight: Stripe records payment state, but access, entitlements, usage, and AI cost live in separate systems. No existing tool cross-checks all four for small teams in a single pass. The wedge is specificity — not another analytics dashboard, but a narrow diagnostic with a ranked output and a dollar-impact estimate per finding.

Distribution plan is two-phase: (1) SEO + direct community outreach before integration, (2) Stripe App Marketplace after OAuth prototype and review approval.

14-day validation window opens when the landing page goes live with event tracking.

## Constraints

- **Tech stack**: Static HTML + vanilla JS only — no framework, no build process; keeps gross margin above 85%
- **Write access**: None to customer systems — intake is read-only, report is generated locally or server-side from redacted export
- **Distribution gate**: No bulk unsolicited email — outreach requires manual approval of every row in `ops/leads.csv`
- **Timeline**: 14-day live test window; kill or reposition on explicit kill criteria (see below)
- **Budget**: No paid ads until first organic conversion; variable costs are model/API calls and Stripe fees only
- **Stripe App Marketplace**: Requires a working read-only OAuth app and passing review — unknown timeline, do not block demand validation on it

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Static intake before OAuth | Proves operators will share data and pay before investing in integration work | — Pending |
| $49 entry price | Low enough to be impulse-buyable; one recovered subscription exceeds cost | — Pending |
| GitHub Pages + Stripe links only | Zero infra cost, immediate deployment, no auth surface | ✓ Good |
| Programmatic SEO as pre-Marketplace channel | Captures specific search intent (failed payments, trial drop, AI cost spike) without ad spend | — Pending |
| Kill criteria defined before launch | Prevents sunk-cost trap; forces honest read of early signal | ✓ Good |
| No monitoring tier until 3+ users request it | Avoids building recurring infra for unvalidated demand | — Pending |

### Kill criteria (explicit)
- 100 qualified visits → zero checkout starts: kill or reposition
- 10 checkout starts → zero payment after one pricing revision: kill or reposition
- Do not infer demand from page views alone

---
*Last updated: 2026-07-19 after initial research phase — hypothesis unvalidated, no revenue recorded*
