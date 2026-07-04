#!/usr/bin/env python3
"""Create outreach previews and send only explicitly approved rows."""

from __future__ import annotations

import csv
import os
import re
import smtplib
import ssl
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "ops" / "leads.csv"
OUTBOX = ROOT / "ops" / "outbox"
FIELDS = ["company", "contact_name", "email", "website", "pain_signal", "offer", "status", "sent_at"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def message_for(row: dict[str, str]) -> tuple[str, str]:
    name = row.get("contact_name", "").strip() or "there"
    company = row.get("company", "").strip() or "your team"
    signal = row.get("pain_signal", "").strip()
    offer = row.get("offer", "").strip() or "Stripe billing-state audit"
    subject = f"A quick billing-state check for {company}"
    observation = f"I noticed {signal.rstrip('.')}" if signal else "I was looking at how your product handles subscriptions and usage"
    body = f"""Hi {name},

{observation}.

I run a focused {offer} for SaaS teams: one redacted customer lifecycle, a
state-gap diagnosis, and a short prioritized fix list. No Stripe login or
production access is required.

Would a two-sentence fit check be useful? If not, I will not follow up.

Best,
Pavel
https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/
"""
    return subject, body


def load_rows() -> list[dict[str, str]]:
    with LEADS.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save_rows(rows: list[dict[str, str]]) -> None:
    with LEADS.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def send(row: dict[str, str], subject: str, body: str) -> None:
    required = ["SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD", "OUTREACH_FROM"]
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise RuntimeError(f"Missing mail settings: {', '.join(missing)}")
    msg = EmailMessage()
    msg["From"] = os.environ["OUTREACH_FROM"]
    msg["To"] = row["email"]
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], int(os.getenv("SMTP_PORT", "465")), context=ssl.create_default_context()) as smtp:
        smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
        smtp.send_message(msg)


def main() -> None:
    OUTBOX.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    live_send = os.getenv("OUTREACH_SEND", "false").lower() == "true"
    previewed = sent = 0
    for index, row in enumerate(rows, start=2):
        status = row.get("status", "").strip().lower()
        email = row.get("email", "").strip()
        if status not in {"draft", "approved"}:
            continue
        if not EMAIL_RE.match(email):
            print(f"Skipping row {index}: invalid email")
            continue
        subject, body = message_for(row)
        slug = re.sub(r"[^a-z0-9]+", "-", row.get("company", "lead").lower()).strip("-")
        (OUTBOX / f"{index}-{slug or 'lead'}.txt").write_text(f"To: {email}\nSubject: {subject}\n\n{body}", encoding="utf-8")
        previewed += 1
        if status == "approved" and live_send:
            send(row, subject, body)
            row["status"] = "sent"
            row["sent_at"] = datetime.now(timezone.utc).isoformat()
            sent += 1
    if sent:
        save_rows(rows)
    print(f"Prepared {previewed} preview(s); sent {sent} approved message(s).")


if __name__ == "__main__":
    main()

