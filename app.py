

import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
import pandastable as pt

import utils
import test


# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Available themes: "blue", "green", "dark-blue"





# Base Page class for all other pages to inherit from
class BasePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame = ctk.CTkScrollableFrame(self)
        self.load_page()

    def hide(self):
        self.frame.pack_forget()
    
    def show(self):
        self.frame.pack(fill="both", expand=True)
        self.lift()

# Overview Page
class OverviewPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

    def load_page(self):

        label = ctk.CTkLabel(self.frame, text="Overview Page", font=("Arial", 16))
        label.pack(pady=20)

        # Example content
        for i in range(30):  # Adding some example content
            ctk.CTkLabel(self.frame, text=f"Overview Item {i+1}").pack(pady=5)

# Portfolio Page
class PortfolioPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

    def load_page(self):

        label = ctk.CTkLabel(self.frame, text="Portfolio Page", font=("Arial", 16))
        label.pack(pady=20)
        
        example_list = ["Stock A: 100 shares", "Stock B: 50 shares"]
        for item in example_list:
            ctk.CTkLabel(self.frame, text=item).pack()

        # Adding more content for scrolling
        for i in range(10):  # More example content
            ctk.CTkLabel(self.frame, text=f"Additional Portfolio Item {i+1}").pack()

# Transactions Page
class TransactionsPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

    def load_page(self):
        label = ctk.CTkLabel(self.frame, text="Transactions Page", font=("Arial", 16))
        label.pack(pady=20)
        
        example_transactions = ["Bought 100 shares of Stock A", "Sold 20 shares of Stock B"]
        for transaction in example_transactions:
            ctk.CTkLabel(self.frame, text=transaction).pack()

        # Adding more transaction examples
        for i in range(15):  # More example transactions
            ctk.CTkLabel(self.frame, text=f"Transaction {i+1}").pack()

# Ticker Manager Page
class TickerManagerPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

    def load_page(self):
        label = ctk.CTkLabel(self.frame, text="Ticker Manager Page", font=("Arial", 16))
        label.pack(pady=20)
        
        data = utils.load_stock_list()
        #ticker_table = ttk.Treeview(self.frame, columns=data.columns)
        #ticker_table.pack()
        
        
        #for i, row in data.iterrows():
        #    ticker_table.insert("", tk.END, values=list(row))
        

        utils.Table(self.frame, data, orientation="both")
        
        #table_frame = ctk.CTkFrame(self.frame)
        #table_frame.pack()

        #pandas_table = pt.Table(table_frame, dataframe=data)
        #pandas_table.show()

        ticker_label = ctk.CTkLabel(self.frame, text="Manage Tickers", font=("Arial", 12))
        ticker_label.pack(pady=10)
        
        # Example of input field for adding new ticker functionality 
        ticker_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter Ticker")
        ticker_entry.pack(pady=5)
        
        add_button = ctk.CTkButton(self.frame, text="Add Ticker", command=lambda: print(f"Added ticker: {ticker_entry.get()}"))
        add_button.pack()


# Main Application Class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Finance Management App")
        self.geometry("500x400")
        
        # create a navigation frame for the sidebar menu
        nav_frame = ctk.CTkFrame(self, width=120, corner_radius=0)
        nav_frame.pack(side="left", fill="y")
        
        # container frame to hold all pages
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(side="right", fill="both", expand=True)
        
        # initialize each page and store it in the pages dictionary
        self.pages = {
            "Overview": OverviewPage(content_frame),
            "Portfolio": PortfolioPage(content_frame),
            "Transactions": TransactionsPage(content_frame),
            "Ticker Manager": TickerManagerPage(content_frame),
        }
        
        # place all pages in the app (only the one on top is always visible)
        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)
        

        # add sidebar buttons for navigation
        self.menu_buttons = {}
        for page_name in self.pages:
            btn = ctk.CTkButton(nav_frame, text=page_name, command=lambda name=page_name: self.show_new_page(name))
            btn.pack(pady=10, padx=10, fill="x")
            self.menu_buttons[page_name] = btn
        

        # select initial page
        self.current_page_name = "Overview"
        self.pages[self.current_page_name].show()
        self.show_new_page(self.current_page_name)


    def show_new_page(self, new_page_name):
        
        print(f"Showing page {new_page_name}, previous page {self.current_page_name}")
        
        self.pages[self.current_page_name].hide()

        page = self.pages[new_page_name]
        page.show()
        
        # change disabled button so it is disabled for currently selected page
        self.menu_buttons[self.current_page_name].configure(state="normal") # enable old page button
        self.menu_buttons[new_page_name].configure(state="disabled") # disable new page button
        self.current_page_name = new_page_name # set new page as current page


# Run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
