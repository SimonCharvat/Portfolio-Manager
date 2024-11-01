
import pandas as pd

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
