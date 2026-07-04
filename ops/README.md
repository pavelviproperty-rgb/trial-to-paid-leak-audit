# Revenue operations

This directory is the human approval boundary for outreach.

1. Add researched prospects to `leads.csv` with `status=draft`, their public
   `source_url`, a specific `pain_signal`, and a short relevance note.
2. Run `python3 scripts/outreach.py` to create previews in `ops/outbox/`.
3. Set `do_not_contact=true` for opt-outs, known customers, or exclusions.
4. Review each preview and change only acceptable rows to `status=approved`.
5. Configure the mail secrets described in the main README.
6. Set `OUTREACH_SEND=true` only when approved messages should be sent.

The sender never emails `draft`, blank, `sent`, or `do_not_contact` rows. A
successful send changes the row to `sent` and records the UTC timestamp.
