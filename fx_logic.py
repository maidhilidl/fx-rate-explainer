"""
Core logic for the FX Rate & Trend Explainer.
Talks to the Frankfurter API (https://api.frankfurter.dev) — free, no key, no signup.
Source: European Central Bank + other central banks, aggregated by Frankfurter.
"""

import requests
from datetime import date, timedelta

BASE_URL = "https://api.frankfurter.dev/v1"

# A small allowlist isn't required by the API, but validating input ourselves
# lets us give a clean, friendly error instead of a raw API failure.


def get_supported_currencies() -> dict:
    """Return {code: full_name} for all currencies Frankfurter supports."""
    resp = requests.get(f"{BASE_URL}/currencies", timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_latest_rate(base: str, target: str) -> dict | None:
    """Fetch today's exchange rate. Returns None if currencies are invalid."""
    resp = requests.get(
        f"{BASE_URL}/latest",
        params={"base": base, "symbols": target},
        timeout=10,
    )
    if resp.status_code != 200:
        return None
    data = resp.json()
    if target not in data.get("rates", {}):
        return None
    return data


def get_historical_rate(base: str, target: str, days_ago: int = 30) -> dict | None:
    """Fetch the exchange rate from `days_ago` days before today."""
    target_date = date.today() - timedelta(days=days_ago)
    resp = requests.get(
        f"{BASE_URL}/{target_date.isoformat()}",
        params={"base": base, "symbols": target},
        timeout=10,
    )
    if resp.status_code != 200:
        return None
    data = resp.json()
    if target not in data.get("rates", {}):
        return None
    return data


def interpret_trend(pct_change: float) -> str:
    """Classify a % change into a plain-language trend label."""
    if pct_change > 1.0:
        return "strengthened"
    elif pct_change < -1.0:
        return "weakened"
    else:
        return "stayed roughly flat"


def explain_fx(base: str, target: str, days_ago: int = 30) -> dict:
    """
    Main entry point: takes a real user input (base, target currency),
    does real lookup + computation, and returns a synthesized answer.
    Handles the 'invalid currency' edge case gracefully.
    """
    base = base.strip().upper()
    target = target.strip().upper()

    if base == target:
        return {
            "ok": False,
            "message": f"{base} and {target} are the same currency — pick two different currencies to compare.",
        }

    latest = get_latest_rate(base, target)
    if latest is None:
        return {
            "ok": False,
            "message": f"Couldn't find a rate for '{base}' to '{target}'. "
                       f"Double check the currency codes (e.g. USD, INR, EUR, GBP, JPY).",
        }

    historical = get_historical_rate(base, target, days_ago)
    if historical is None:
        # Still give the user the latest rate even if history fails
        rate_now = latest["rates"][target]
        return {
            "ok": True,
            "base": base,
            "target": target,
            "rate_now": rate_now,
            "date_now": latest["date"],
            "message": f"1 {base} = {rate_now} {target} as of {latest['date']}. "
                       f"(Historical comparison unavailable for this pair.)",
        }

    rate_now = latest["rates"][target]
    rate_then = historical["rates"][target]
    pct_change = ((rate_now - rate_then) / rate_then) * 100
    trend = interpret_trend(pct_change)

    message = (
        f"1 {base} = {rate_now} {target} today ({latest['date']}). "
        f"That's {abs(pct_change):.2f}% {'higher' if pct_change >= 0 else 'lower'} than "
        f"{days_ago} days ago ({historical['date']}), when 1 {base} = {rate_then} {target}. "
        f"{target} has {trend} against {base} over that period."
    )

    return {
        "ok": True,
        "base": base,
        "target": target,
        "rate_now": rate_now,
        "rate_then": rate_then,
        "date_now": latest["date"],
        "date_then": historical["date"],
        "pct_change": round(pct_change, 2),
        "trend": trend,
        "message": message,
    }


if __name__ == "__main__":
    # Quick manual test cases
    print(explain_fx("USD", "INR"))
    print(explain_fx("USD", "XYZ"))  # invalid code -> should fail gracefully
    print(explain_fx("USD", "USD"))  # same currency -> should fail gracefully
