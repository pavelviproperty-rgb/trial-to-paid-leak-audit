#!/usr/bin/env python3
"""Fail if the public offer or a checkout link is unavailable."""

from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URLS = [
    "https://pavelviproperty-rgb.github.io/trial-to-paid-leak-audit/",
    "https://buy.stripe.com/6oUdRb0JL37VeqU7A0aR200",
    "https://buy.stripe.com/dRm14p2RTeQD0A4f2saR201",
    "https://buy.stripe.com/00w9AVdwxeQDfuY9I8aR206",
    "https://buy.stripe.com/8x26oJ0JL9wj4QkaMcaR207",
]

failed = []
for url in URLS:
    try:
        request = Request(url, headers={"User-Agent": "revenue-health-check/1.0"})
        with urlopen(request, timeout=20) as response:
            print(response.status, response.geturl())
            if response.status >= 400:
                failed.append(url)
    except (HTTPError, URLError, TimeoutError) as error:
        print("FAILED", url, error)
        failed.append(url)

if failed:
    raise SystemExit(f"{len(failed)} revenue link(s) unavailable")

