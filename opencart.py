import tkinter as tk
from tkinter import ttk
import mysql.connector
from web import *
from sales import *
from clients import *
from transactions import *
from catalogues import *

class OpenCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenCart Application")

        self.db = mysql.connector.connect(
            host="localhost",
            user="patricia",
            password="passer",
            database="opencart"
        )

        # Creation ds onglets (une par option)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10)

        self.web_access_tab = WebAccessTab(self.notebook, self.db)
        self.block_sales_tab = BlockSalesTab(self.notebook, self.db)
        self.connected_clients_tab = ConnectedClientsTab(self.notebook, self.db)
        

    def run(self):
        self.root.mainloop()
        self.ongoing_transactions_tab = OngoingTransactionsTab(self.notebook, self.db)
        self.list_catalogues_tab = CatalogsTab(self.notebook, self.db)
