import yfinance as yf
import streamlit as st

@st.cache
def tsxMarketInfo():
    tickersInfo = []
    with open("./tsx.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append(stock.info)

    return tickersInfo 


@st.cache
def sapMarketInfo():
    tickersInfo = []
    with open("./sp500.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append(stock.info)

    return tickersInfo 


@st.cache
def nasdaqMarketInfo():
    tickersInfo = []
    with open("./nasdaq100.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append(stock.info)

    return tickersInfo 

@st.cache
def getValidListOfStocks(stockList, investmentAmount)
    validList = []
    for stock in stockList:
        if (stock.info['regularMarketPrice'] <= investmentAmount):
            validList.append(stock)
    return validList

