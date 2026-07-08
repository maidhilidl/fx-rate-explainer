# FX Rate & Trend Explainer

A tiny tool that answers: "how has currency A moved against currency B recently?" — in plain language, using live public data.

**Live demo:** [add your deployed Streamlit URL here]

## What it does
Type two currency codes (e.g. USD, INR). The tool fetches today's real exchange rate and the rate from N days ago (default 30) from the [Frankfurter API](https://frankfurter.dev) — a free, no-key public API aggregating rates from the European Central Bank and other central banks — then computes the % change and explains the trend in one sentence.

## Files
- `fx_logic.py` — the core logic: API calls, computation, interpretation, error handling
- `app.py` — the Streamlit front-end
- `requirements.txt` — dependencies
- `CITATION_LEDGER.md` — every factual claim in this project and its source
- `ONE_PAGER.md` — plain-language explanation of the project
- `WHAT_I_CUT.md` — scope decisions and why

## Run it locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy it (Streamlit Community Cloud, free)
1. Push this folder to a public GitHub repo.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "New app", pick this repo, branch `main`, main file path `app.py`.
4. Click "Deploy". Wait ~1-2 minutes.
5. Copy the live URL it gives you into this README and your submission.

## Option picked
Option 1 — API Tool + Chat/Form.
