import requests
import streamlit as st

st.set_page_config(page_title="환율 조회")
st.title("환율 조회")
st.write("통화와 금액을 선택하고 환율을 조회하세요.")

currencies = ["USD", "KRW", "EUR", "JPY", "GBP", "CAD", "AUD", "CHF", "CNY"]
base = st.selectbox("기준 통화", currencies)
target = st.selectbox("변환할 통화", currencies, index=1)
amount = st.number_input("금액", min_value=0.0, value=100.0, step=1.0)

if st.button("환율 조회"):
    if base == target:
        st.info("같은 통화라 금액이 그대로예요.")
        st.metric("환산 금액", f"{amount:,.2f} {target}")
    else:
        try:
            response = requests.get(
                f"https://api.frankfurter.dev/v2/rate/{base}/{target}", timeout=10
            )
            response.raise_for_status()
            data = response.json()
            rate = data["rate"]
            date = data["date"]
        except (requests.RequestException, ValueError, KeyError):
            st.error("환율을 가져오지 못했어요. 잠시 뒤 다시 시도해 주세요.")
        else:
            st.metric("환산 금액", f"{amount * rate:,.2f} {target}")
            st.write(f"1 {base} = {rate:,.6g} {target}")
            st.caption(f"기준일 {date} · 출처 Frankfurter")
