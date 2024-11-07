
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

from typing import Union, Tuple, Optional, Any
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

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
        data_frame = pd.read_csv(stock_list_location, sep=";", decimal=".", header=0)
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




class Table():
    def __init__(
            self,
            master: Any,
            df: pd.DataFrame,
            orientation: Literal["vertical", "horizontal", "both"] = "vertical"   
            ) -> None:

        match orientation:
            case "both":
                self._orientation_horizontal = True
                self._orientation_vertical = True
            case "vertical":
                self._orientation_horizontal = False
                self._orientation_vertical = True
            case "horizontal":
                self._orientation_horizontal = True
                self._orientation_vertical = False


        # dimensions independent of scaling
        #self._desired_width = width  # _desired_width and _desired_height, represent desired size set by width and height
        #self._desired_height = height

        # Create a frame to hold the Treeview and scrollbar
        
        outer_frame = ctk.CTkScrollableFrame(master, orientation="vertical")
        outer_frame.pack(fill="x", expand=False)

        inner_frame = ctk.CTkScrollableFrame(outer_frame, orientation="horizontal")
        inner_frame.pack(fill="x", expand=False)


        # Define columns, including the 'Edit' button column
        columns = ["Edit"] + list(df.columns)

        # Add Treeview
        tree = ttk.Treeview(inner_frame, columns=columns, show='headings')
        tree.pack()

        # Set up column headings and make them resizable
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100, stretch=True)

        # Insert data into the Treeview with an Edit button at the beginning of each row
        for i, row in df.iterrows():
            # Add 'Edit' button text in the first column
            row_values = [f"Edit {i+1}"] + list(row)
            
            # Insert the row into Treeview
            tree.insert("", "end", iid=i, values=row_values)

            # Bind edit action to 'Edit' button
            tree.tag_bind(f"Edit {i+1}", '<ButtonRelease-1>', lambda e, i=i: self.edit_row(i))

    # Custom function for the Edit button
    def edit_row(row_index):
        print(f"Edit row {row_index}:")
