import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns 
import yfinance as yf
import datetime as dt



st.title("Finance Application")
End_date = dt.datetime.now()
Start_date = End_date - dt.timedelta(days=365*2)

Msft = yf.Ticker("MSFT")
st.write(Msft)
Hist = Msft.history(period='max')
st.dataframe(Hist)

GAFAM =['GOOG','MSFT','META','AAPL','AMZN']
Df = yf.download(GAFAM)
st.write(Df.head())

Balance = Msft.balance_sheet
st.write(Balance)

Actions = Msft.actions
st.write(Actions)

Calendrier = Msft.calendar
st.dataframe(Calendrier)


st.subheader("Cashflow Microsoft")
Cashflow = Msft.cash_flow
st.dataframe(Cashflow)
st.line_chart(Cashflow)


st.subheader("Historique de Microsoft")
Historique = Msft.history(period="24mo")
st.dataframe(Historique)

st.line_chart(Historique)