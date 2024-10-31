

import customtkinter as ctk

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Available themes: "blue", "green", "dark-blue"

# Base Page class for all other pages to inherit from
class BasePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.frame = ctk.CTkScrollableFrame(self)
        self.frame.pack(fill="both", expand=True)

    def show(self):
        self.lift()

# Overview Page
class OverviewPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

        label = ctk.CTkLabel(self.frame, text="Overview Page", font=("Arial", 16))
        label.pack(pady=20)

        # Example content
        for i in range(30):  # Adding some example content
            ctk.CTkLabel(self.frame, text=f"Overview Item {i+1}").pack(pady=5)

# Portfolio Page
class PortfolioPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent)

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

        label = ctk.CTkLabel(self.frame, text="Ticker Manager Page", font=("Arial", 16))
        label.pack(pady=20)
        
        ticker_label = ctk.CTkLabel(self.frame, text="Manage Tickers", font=("Arial", 12))
        ticker_label.pack(pady=10)
        
        # Example of adding new ticker functionality
        ticker_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter Ticker")
        ticker_entry.pack(pady=5)
        
        add_button = ctk.CTkButton(self.frame, text="Add Ticker", command=lambda: print(f"Added ticker: {ticker_entry.get()}"))
        add_button.pack()

        # Adding more content for scrolling
        for i in range(10):  # More example tickers
            ctk.CTkLabel(self.frame, text=f"Ticker Item {i+1}").pack(pady=5)

# Main Application Class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Finance Management App")
        self.geometry("500x400")
        
        # Create a navigation frame for the sidebar menu
        nav_frame = ctk.CTkFrame(self, width=120, corner_radius=0)
        nav_frame.pack(side="left", fill="y")
        
        # Container frame to hold all pages
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(side="right", fill="both", expand=True)
        
        # Initialize each page and store it in the pages dictionary
        self.pages = {
            "Overview": OverviewPage(content_frame),
            "Portfolio": PortfolioPage(content_frame),
            "Transactions": TransactionsPage(content_frame),
            "Ticker Manager": TickerManagerPage(content_frame),
        }
        
        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)
        self.pages["Overview"].show()  # Show Overview page initially

        # Add sidebar buttons for navigation
        for page_name in self.pages:
            btn = ctk.CTkButton(nav_frame, text=page_name, command=lambda name=page_name: self.show_page(name))
            btn.pack(pady=10, padx=10, fill="x")
        
    def show_page(self, page_name):
        page = self.pages[page_name]
        page.show()

# Run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
