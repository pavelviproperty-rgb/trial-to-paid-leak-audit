# Owner action runbook

Actions that require the owner's authenticated sessions (Stripe, Vercel).
Agents on this machine currently have no browser and no Stripe/Vercel CLI,
so these cannot be automated here. Each item lists exact steps and a
verification command an agent can run afterwards.

## 1. Stripe: redirect both payment links to buyer intake (handoff item 1)

For each of the two current links:

- `$49` AI Agent Cost Leak Audit — `https://buy.stripe.com/00w9AVdwxeQDfuY9I8aR206`
- `$199` AI Agent Cost Action Pack — `https://buy.stripe.com/8x26oJ0JL9wj4QkaMcaR207`

Steps in the Stripe dashboard (workspace `vipavel`):

1. Payment links → open the link → `...` → Edit.
2. Section "After payment" → select "Don't show confirmation page" →
   set redirect URL to:
   `https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/intake.html`
3. Save. Repeat for the second link.
4. Optional but recommended: append `?session_id={CHECKOUT_SESSION_ID}` to the
   redirect URL so a future intake version can reference the purchase.

Verification (agent can run after you confirm):

```sh
python3 scripts/site_health.py   # both links must stay HTTP 200
```

A full end-to-end check requires one real or test checkout; per policy the
redirect is only "operational" after a real completed purchase lands on
intake.html.

## 2. Vercel: locate the `stripe-decline-codes` source (handoff item 2)

`vipavel.shop` == Vercel project `stripe-decline-codes` (verified by identical
etag/last-modified). Source is not on GitHub and not on this machine.

1. In the Vercel dashboard (team `team_Sg8SkBhfVW6dQ21A3ePp4Shm`), open the
   project → Settings → Git to see if any repo is connected.
2. If no Git connection: Deployments → latest → "Download" (or run
   `vercel pull` / `vercel env pull` from a logged-in CLI) to recover sources,
   then commit them to a new private repo so agents can iterate.

Decision needed from owner: keep the decline-code reference as the homepage
(it is useful SEO content that already links to both payment links) and expose
the Profit Ops funnel at a path or subdomain, or replace the homepage. Agent
recommendation: keep the homepage, add a visible banner/link to the funnel,
and revisit after first sales.

## 3. Brevo SMTP secrets → GitHub Actions (handoff item 3)

Repo → Settings → Secrets and variables → Actions → add:
`SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `OUTREACH_FROM`
(values from the Brevo dashboard; never commit them). Live sending also
requires `OUTREACH_SEND=true` on the workflow run and per-row `approved`
status in `ops/leads.csv`.

## 4. Outreach first batch

Review PR #5 (`claude/icp-leads-2026-07`): check the two draft previews, fill
missing emails for the two `research` rows if desired, merge, then mark rows
`approved` only when you want them sent.
