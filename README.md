# FX Rate & Trend Explainer

A tiny tool that answers one question: **how has a currency moved against another recently?** — in plain language, using live public data.

**Live demo:** https://fx-rate-explainer-yczrshht84tprbvqmclevc.streamlit.app/

## What it does

Type two currency codes (e.g. USD, INR). The tool fetches today's real exchange rate and the rate from N days ago (default 30) from the [Frankfurter API](https://frankfurter.dev/) — a free, no-key public API aggregating official reference rates from the European Central Bank and other central banks — then computes the percentage change and explains the trend in one plain-language sentence, rather than a raw number.

If an invalid currency code is entered, the tool fails gracefully with a clear message instead of crashing.

## How it's built

- `fx_logic.py` — core logic: the two API lookups, the percentage-change computation, and the trend interpretation
- `app.py` — the Streamlit front-end
- `requirements.txt` — dependencies
- `CITATION_LEDGER.md` — every factual claim made in this project's documentation, with its source
- `ONE_PAGER.md` — a plain-language explainer of the project for a non-technical reader
- `WHAT_I_CUT.md` — scope decisions made to finish this within the time budget, and why

Deployed on **Streamlit Community Cloud**, connected directly to this repo's `main` branch — no separate hosting setup, no server to maintain.
