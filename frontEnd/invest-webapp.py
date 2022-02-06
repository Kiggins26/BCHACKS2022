import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date

from stockDataGetter import *
from stockProjection import *



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

tickersInfo = []
if st.sidebar.button('run'):
        if tickerSymbol == "TSX":
            st.write("TSX "+str(investment_amount))
            #tickersInfo = tsxMarketInfo()
        if tickerSymbol == "SP500":
            st.write("sp500 " + str(investment_amount))
            #tickersInfo = sapMarketInfo()
        if tickerSymbol == "NASDAQ":
            st.write("nasdaq100"+str(investment_amount))
            #tickersInfo = nasdaqMarketInfo()
        #validList = getValidListOfStocks(tickersInfo,investment_amount)
        #st.write(getValidCombos(validList,investment_amount))

period = 365

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
tickerData = yf.Ticker("AMZN")
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

data = yf.download("AMZN", START, TODAY)
data.reset_index(inplace=True)


df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast

st.subheader('Forecast data')
st.write(forecast.tail())

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


tickerData = yf.Ticker("EA")
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

data = yf.download("EA", START, TODAY)
data.reset_index(inplace=True)


df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)


tickerData = yf.Ticker("AMD")
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

data = yf.download("AMD", START, TODAY)
data.reset_index(inplace=True)
data = yf.download("AMD", START, TODAY)
data.reset_index(inplace=True)


df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

    
