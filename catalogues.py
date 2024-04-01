import tkinter as tk
import mysql.connector
from tkinter import ttk


class CatalogsTab:
    def __init__(self, notebook, db):
        self.db = db
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Cataloges")

        catalogs_label = tk.Label(self.tab, text="Catalogue:")
        catalogs_label.pack()

        self.catalogs_tree = ttk.Treeview(self.tab)
        self.catalogs_tree["columns"] = ("id", "nom", "description")
        self.catalogs_tree.column("#0", width=200, minwidth=200, anchor=tk.W)
        self.catalogs_tree.column("id", width=100, minwidth=100, anchor=tk.W)
        self.catalogs_tree.column("nom", width=200, minwidth=200, anchor=tk.W)
        self.catalogs_tree.column("description", width=300, minwidth=300, anchor=tk.W)

        self.catalogs_tree.heading("#0", text="Categorie", anchor=tk.W)
        self.catalogs_tree.heading("id", text="ID", anchor=tk.W)
        self.catalogs_tree.heading("nom", text="Nom", anchor=tk.W)
        self.catalogs_tree.heading("description", text="Description", anchor=tk.W)

        self.catalogs_tree.pack(pady=20)

        list_catalogs_button = tk.Button(self.tab, text="Lister Catalogues", command=self.list_catalogs)
        list_catalogs_button.pack()

    def list_catalogs(self):
        cursor = self.db.cursor()

        query = "SELECT category_id, name, description FROM oc_category_description WHERE language_id = 1"  # Changer le language_id si necessaire
        cursor.execute(query)
        categories = cursor.fetchall()

        self.catalogs_tree.delete(*self.catalogs_tree.get_children())


        for category in categories:
            self.catalogs_tree.insert("", "end", text=category[1], values=(category[0], category[1], category[2]))

            query = "SELECT product_id, name, description FROM oc_product_description WHERE language_id = 1 AND category_id = %s"  # Changer le language_id si necessaire
            cursor.execute(query, (category[0]))
            products = cursor.fetchall()

            for product in products:
                self.catalogs_tree.insert(category[1], "end", text=product[1], values=(product[0], product[1], product[2]))

        cursor.close()

