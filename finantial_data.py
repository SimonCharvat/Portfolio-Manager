
import yfinance as yf
import pandas as pd
import os

import utils

def donwload_data(ticker: str, start_date: str):
    # Get the data
    data: pd.DataFrame = yf.download(ticker, start_date, interval="1wk", group_by="column")
    data: pd.DataFrame = data["Close"] # get closing prices


def get_stock_data(ticker: str, start_date: str):
    
    data_file_path = f"data_{ticker}.csv"

    end_date = utils.get_yesterdays_date()

    if os.path.isfile(data_file_path):
        df_price_old = pd.read_csv(data_file_path, sep=";", decimal=".", header=0)
        print(f"Loaded price data file for {ticker}")
    else:
        df_price_old = pd.DataFrame(columns=["date", "price"]
        )


    donwload_data(ticker, start_date)
    

