

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
    "ticker":           ["TUI1", "VWCE"],
    "ticker_full":      ["TUI1.DE", "VWCE.DE"],
    "exchange_name":    ["Xetra", "Xetra"],
    "exchange_code":    ["DE", "DE"],
    "name":             ["TUI Group", "Vanguard FTSE All-World"],
    "description":      ["", ""]
})

# save example stocks data
df_stocks.to_csv("data_stocks.csv", index=False, sep=";", decimal=".")

print(df_stocks)



# Set the start and end date
start_date = '2020-01-01'
end_date = '2024-10-15'



def add_ticker(ticker_full: str):
    new_ticker = yf.Ticker(ticker_full)
    
    name = new_ticker.history_metadata["shortName"]
    currency = new_ticker.history_metadata["currency"]
    exchange_name = new_ticker.history_metadata["fullExchangeName"]
    instrument_type = new_ticker.history_metadata["instrumentType"] # ETF / EQUITY
    
    print(name, currency, exchange_name)

add_ticker("AFR0.F") # air france


tickers = df_stocks["ticker_full"].to_list()

# Get the data
data: pd.DataFrame = yf.download(tickers, start_date, interval="1wk", group_by="column")
data: pd.DataFrame = data["Close"] # get closing prices

print(data)




print()
