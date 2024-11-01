
import pandas as pd

import os


stock_list_location = "data_stocks.csv"

def save_stock_list(data_frame: pd.DataFrame) -> None:
    try:
        data_frame.to_csv(stock_list_location, index=False, sep=";", decimal=".", header=True)
        print("Stock list saved")
    except Exception as e:
        print(f"Stock list not saved, error:\n{e}")


def load_stock_list() -> pd.DataFrame:
    
    if os.path.isfile(stock_list_location):
        data_frame = pd.read_csv(stock_list_location, sep=";", decimal=".", header=True)
        print("Stock list loaded")
    else:
        data_frame = pd.DataFrame(columns=
                                   ["id",
                                    "ticker",
                                    "exchange_name",
                                    "exchange_tag",
                                    "name_short",
                                    "name_long",
                                    "currency",
                                    "instrument_type",
                                    "description"
                                    ]
        )
        save_stock_list(data_frame)
        print("Stock list not found, new file created")
    
    return data_frame
