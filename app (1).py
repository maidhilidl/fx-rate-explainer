import streamlit as st
from fx_logic import explain_fx, get_supported_currencies

st.set_page_config(page_title="FX Rate & Trend Explainer", page_icon="💱")

st.title("💱 FX Rate & Trend Explainer")
st.write(
    "Type two currency codes to get today's real exchange rate, "
    "plus how it's moved over the last 30 days — explained in plain language."
)

with st.expander("See supported currency codes"):
    try:
        currencies = get_supported_currencies()
        st.write(", ".join(f"**{code}** ({name})" for code, name in currencies.items()))
    except Exception:
        st.write("Common codes: USD, EUR, GBP, INR, JPY, AUD, CAD, CHF, CNY")

col1, col2 = st.columns(2)
with col1:
    base = st.text_input("From currency", value="USD", max_chars=3).upper()
with col2:
    target = st.text_input("To currency", value="INR", max_chars=3).upper()

days_ago = st.slider("Compare against how many days ago?", min_value=7, max_value=90, value=30)

if st.button("Get the rate", type="primary"):
    if not base or not target:
        st.warning("Please enter both currency codes.")
    else:
        with st.spinner("Fetching live rates..."):
            result = explain_fx(base, target, days_ago=days_ago)

        if not result["ok"]:
            st.error(result["message"])
        else:
            st.success(result["message"])
            if "pct_change" in result:
                c1, c2, c3 = st.columns(3)
                c1.metric(f"1 {result['base']} =", f"{result['rate_now']} {result['target']}")
                c2.metric(f"{days_ago} days ago", f"{result['rate_then']} {result['target']}")
                c3.metric("Change", f"{result['pct_change']}%")

st.divider()
st.caption(
    "Data source: [Frankfurter API](https://frankfurter.dev), which aggregates official "
    "reference rates from the European Central Bank and other central banks. "
    "No API key required. This tool is for informational purposes, not financial advice."
)
