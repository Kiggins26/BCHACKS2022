import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# App title
st.markdown('''
# Student investent app 
Helping students make investment decisions with whatever money they have.
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Investment parameters')
investment_amount = st.sidebar.number_input("Investment amount",1)

# Retrieving tickers data
market_list = ["TSX","SP500","NASDAQ"]
tickerSymbol = st.sidebar.selectbox('Market', market_list) # Select ticker symbol

if st.sidebar.button('run'):
        if tickerSymbol == "TSX":
            st.write("TSX "+str(investment_amount));
        if tickerSymbol == "SP500":
            st.write("sp500 " + str(investment_amount))
        if tickerSymbol == "NASDAQ":
            st.write("nasdaq100"+str(investment_amount))
    
