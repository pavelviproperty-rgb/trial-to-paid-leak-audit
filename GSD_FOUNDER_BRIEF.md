# GSD founder brief — Billing Leakage Radar

Status: hypothesis, not validated revenue.
Date: 2026-07-19

## 1. Vision

Make revenue leakage visible and actionable for small SaaS and AI businesses before it becomes churn or margin collapse.

## 2. Who is the user?

Primary ICP: founder, head of engineering, or revenue-ops owner of a subscription or usage-based SaaS using Stripe and at least one AI API.

Trigger: failed renewals, trial conversion drop, entitlement mismatch, or AI usage cost spike.

Non-user: consumers, large enterprises needing procurement/SOC2 before a pilot, and businesses not using Stripe.

## 3. What painful problem exists?

Stripe records payment state, while access, usage, and AI cost live elsewhere. The operator cannot quickly answer: who paid but lost access, who failed to renew, which trial leaked, and whether AI cost exceeds collected revenue.

## 4. Why now?

AI makes usage-based cost and margin volatility more common. Stripe explicitly supports third-party apps in its App Marketplace, creating a potential distribution surface.

## 5. Proposed solution

Read-only Stripe-connected diagnostic that outputs a ranked leakage report with evidence, estimated monthly impact, confidence, and the smallest fix. Start as a paid report; only build OAuth/API integration after demand.

## 6. Alternatives and competition

Stripe Dashboard, billing-recovery tools, analytics tools, internal SQL, and agencies already solve pieces. Our wedge is cross-checking payment state + entitlements + usage cost in one narrow report for small teams.

## 7. Why would anyone pay?

One recovered subscription or one avoided AI-cost runaway can exceed the $49 diagnostic price. This is an assumption until a buyer pays.

## 8. Acquisition

Primary: Stripe App Marketplace after a working integration and review approval.

Pre-integration test: problem-specific SEO pages and direct opt-in from public founder/operator communities, without bulk unsolicited email.

## 9. Business model

Diagnostic: $49 one-time. Action pack: $199 one-time. Later: $29–99/month monitoring only if at least three paid users repeat or request it.

## 10. Unit economics

Initial gross margin target: >85% before founder time, using static intake + automated report generation. Main variable costs are model/API calls and payment fees. No paid ads until organic or direct conversion is proven.

## 11. MVP scope

Included: redacted export intake, deterministic checks, ranked report, Stripe checkout, event tracking, and one follow-up CTA.

Excluded: automatic refunds, plan changes, email sending, write access, multi-tenant dashboard, and enterprise compliance claims.

## 12. Success metric

Within 14 days of a live test: 100 qualified visits, 10 high-intent actions (checkout start or intake), and at least 1 paid diagnostic. Strong signal: 3+ paid diagnostics or 1 customer requesting recurring monitoring.

## 13. Kill criteria

Kill or reposition if 100 qualified visits produce zero checkout starts, or 10 checkout starts produce zero payment after one pricing/offer revision. Do not infer demand from page views alone.

## 14. Unknowns and fastest verification

- Unknown: whether Stripe App Marketplace approval is attainable for this scope. Verify by building a minimal read-only app and checking current review requirements.
- Unknown: whether operators will share billing exports. Verify with a redacted sample workflow and a paid pilot.
- Unknown: whether $49 is the correct price. Test $49 diagnostic vs. $99 team diagnostic only after first conversion signal.
- Unknown: actual search demand. Verify with Search Console and tagged checkout events after deployment.

## 15. 1–7 day execution slice

1. Instrument landing page, checkout-start, purchase, and intake events.
2. Publish the private-beta page and submit the sitemap.
3. Create a deterministic sample report from a redacted fixture.
4. Build the smallest read-only Stripe OAuth prototype only if a paid or explicit beta signal appears.
5. Review metrics daily; stop when kill criteria are met.

## Facts vs. assumptions

Facts: the current site and Stripe links are live; the repository has no recorded leads or payments; GSD recommends explicit research, planning, execution, verification, and reassessment phases.

Assumptions: Stripe users have a painful cross-system leakage problem; a narrow diagnostic can be sold before full integration; App Marketplace distribution will outperform generic SEO.

Hypothesis: Billing Leakage Radar is the strongest current test because it combines a specific money problem, existing Stripe infrastructure, and a plausible native distribution channel.
