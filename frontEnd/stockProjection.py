import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2018-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

period = 365

@st.cache
def getBestFiveOptions(validPerm):
    
    stockMap = {}

    for i in validPerm:

        sum = 0

        for j in i:
            ticker = j[0]
            print(ticker)
            data = yf.download(ticker,START,TODAY)
            data.reset_index(inplace=True)
            
            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)



            sum = sum + (forecast.yhat_lower.sum())
        stockMap[i] = sum
    #return dict(sorted(stockMap.items(),key = lambda item:item[1])
