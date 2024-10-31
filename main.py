

import yfinance as yf
import pandas as pd


# stock exchange code translation
exchange_codes = {
    "France": "F",
    "Xetra": "DE",
    "Germany": "DE"
}



# csv file - stocks
df_stocks = pd.DataFrame(data={
    "id": [1, 2],
    "ticker":           ["TUI1.DE", "VWCE.DE"],
    "exchange_name":    ["Xetra", "Xetra"],
    "exchange_tag":  ["?", "?"],
    "name_short":       ["TUI Group", "Vanguard FTSE All-World"],
    "name_long":        ["TUI Group", "Vanguard FTSE All-World"],
    "currency":         ["EUR", "EUR"],
    "instrument_type":  ["EQUITY", "EQUITY"],
    "description":      ["", ""]
})

# save example stocks data
df_stocks.to_csv("data_stocks.csv", index=False, sep=";", decimal=".")

print(df_stocks)



# Set the start and end date
start_date = '2020-01-01'



def add_ticker(df_stocks: pd.DataFrame, ticker: str):
    new_ticker = yf.Ticker(ticker)
    
    try:
        name_short = new_ticker.history_metadata["shortName"]
        name_long = new_ticker.history_metadata["longName"]
        currency = new_ticker.history_metadata["currency"]
        exchange_tag = new_ticker.history_metadata["exchangeName"]
        exchange_name = new_ticker.history_metadata["fullExchangeName"]
        instrument_type = new_ticker.history_metadata["instrumentType"] # ETF / EQUITY
    except Exception as e:
        print(f"Ticker {ticker} not found at Yahoo Finance")
        print(f"Error code:\n {e}")
        return
    

    df_stocks.loc[len(df_stocks)] = [
        max(df_stocks["id"]) + 1,
        ticker,
        exchange_name,
        exchange_tag,
        name_short,
        name_long,
        currency,
        instrument_type,
        ""
    ]

    print(f"Ticker {ticker} added")

add_ticker(df_stocks, "AFR0.F") # air france

add_ticker(df_stocks, "FAKE.F")

print(df_stocks)


tickers = df_stocks["ticker"].to_list()

# Get the data
data: pd.DataFrame = yf.download(tickers, start_date, interval="1wk", group_by="column")
data: pd.DataFrame = data["Close"] # get closing prices

print(data)




print()
