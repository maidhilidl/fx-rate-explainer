# What I Cut and Why

Given the time budget, I deliberately left out:

1. **A saved watchlist / multiple currency pairs at once** — the brief asks for one clear, finished interaction, and adding persistence (accounts, saved state) would have meant either a database or fragile local storage, which risked breaking the "no login, works cold" requirement.
2. **Charting the full historical trend line** — I show a before/after comparison (today vs. N days ago) rather than a full time-series graph. A single interpreted comparison answers the actual question ("is it up or down, and by how much") without the extra complexity of a charting library and its edge cases (missing dates, weekends/holidays with no published rate).
3. **Support for amount conversion (e.g. "convert $500")** — the tool answers a rate/trend question, not a calculator question. Adding amount conversion would have doubled the UI surface for a feature that's one extra input field away if I extend it later, but wasn't the core question I chose to answer well.
4. **Currency code autocomplete/validation UI** — I show the full supported list in a collapsible section and validate on submit, rather than building a searchable dropdown, to keep the front-end simple and fast to finish.

I prioritized finishing one interaction end-to-end (real input → real lookup → real computation → plain-language answer → graceful failure) over adding more surface area.
