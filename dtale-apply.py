from dtale.views import startup

startup(data_id="1", data=df)
# you can add more data_id then switch on dtale

st.markdown('<a href="/dtale/main/1" target="_blank">Open dtale</a>', unsafe_allow_html=True)

# dtale-streamlit run app.py
