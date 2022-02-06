import yfinance as yf
import streamlit as st

@st.cache
def tsxMarketInfo(investmentAmount):
    tickersInfo = []
    with open("./tsx.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            if (stock.info['regularMarketPrice'] <= investmentAmount):
                tickersInfo.append(stock.info)

    return tickersInfo 


@st.cache
def sapMarketInfo(investmentAmount):
    tickersInfo = []
    with open("./sp500.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            if (stock.info['regularMarketPrice'] <= investmentAmount):
                tickersInfo.append(stock.info)

    return tickersInfo 


@st.cache
def nasdaqMarketInfo(investmentAmount):
    tickersInfo = []
    with open("./nasdaq100.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            if (stock.info['regularMarketPrice'] <= investmentAmount):
                tickersInfo.append(stock.info)

    return tickersInfo 


nasdaqMarketInfo(10000000)
