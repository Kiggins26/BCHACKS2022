import yfinance as yf
import streamlit as st
import itertools

@st.cache
def tsxMarketInfo():
    tickersInfo = []
    with open("./tsx.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append([ticker,stock.info])

    return tickersInfo 


@st.cache
def sapMarketInfo():
    tickersInfo = []
    with open("./sp500.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append([ticker,stock.info])

    return tickersInfo 


@st.cache
def nasdaqMarketInfo():
    tickersInfo = []
    with open("./nasdaq100.txt") as tsxFile:
        for line in tsxFile:
            ticker = line.split()[0]
            print(ticker)
            stock = yf.Ticker(ticker)
            tickersInfo.append([ticker,stock.info])

    return tickersInfo 

@st.cache
def getValidListOfStocks(stockList, investmentAmount):
    validList = []
    for stock in stockList:
        print(stock[1].info)
        if (stock.info['regularMarketPrice'] <= investmentAmount):
            validList.append(stock)
    return validList


@st.cache
def getValidCombos(validList, investmentAmount):
    perms = list(itertools.permutations(validList))
    validCombos =[]
    sum = 0
    cond = True

    for i in perms:
        for j in i:
            if sum > investmentAmount:
                cond = False
            sum = sum + j[1].info['regularMarketPrice']
        if cond == True:
            validCombos.append(i)
        cond = True
        
    return validCombos



