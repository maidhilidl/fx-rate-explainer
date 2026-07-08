# Citation Ledger — FX Rate & Trend Explainer

| Claim | Source URL | Source type | One-line paraphrase |
|---|---|---|---|
| Frankfurter provides free exchange rate data with no API key or signup required | https://frankfurter.dev | API documentation | The provider's docs state the public API needs no authentication to use |
| Frankfurter's rates are aggregated from the European Central Bank and other national central banks | https://frankfurter.dev | API documentation | The docs describe rates as sourced from ~84 central banks and blended from official references |
| Frankfurter's historical data goes back to 1948 | https://frankfurter.dev | API documentation | The provider states its historical coverage starts in 1948 |
| Frankfurter supports fetching a rate for any specific past date, not just the current day | https://api.frankfurter.dev/v1/ (docs) | API documentation | The docs show a dated endpoint pattern (e.g. `/v1/1999-01-04`) for historical lookups |
| Rates returned for "today" may still update intraday as new data is published | https://frankfurter.dev | API documentation | The docs note that same-day rates are not final and can shift as new figures arrive |

**Note on scope:** the exchange rate figures the tool displays at runtime (e.g. "1 USD = 108.98 INR") are live computed outputs of the API call itself, not authored claims — they change every time the tool is run and are sourced live, in real time, from the API listed above.
