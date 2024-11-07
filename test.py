import tkinter as tk
from tkinter import ttk
import pandas as pd
import customtkinter as ctk

import utils


ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Available themes: "blue", "green", "dark-blue"


# Sample data
data_test = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Occupation": ["Engineer", "Doctor", "Artist", "Lawyer"]
}
df_test = pd.DataFrame(data_test)




