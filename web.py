import tkinter as tk
from tkinter import ttk


class WebAccessTab:
    def __init__(self, notebook, db):
        self.db = db
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Acces web")

        user_id_label = tk.Label(self.tab, text="ID utilisateur:")
        user_id_label.pack()
        self.user_id_entry = tk.Entry(self.tab)
        self.user_id_entry.pack()
        control_button = tk.Button(self.tab, text="Controller acces web", command=self.control_web_access)
        control_button.pack()
        self.result_label = tk.Label(self.tab, text="")
        self.result_label.pack()

    def control_web_access(self):
        user_id = self.user_id_entry.get()
        cursor = self.db.cursor()
        query = "SELECT * FROM oc_user WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        if user:
            self.result_label.config(text=f"Acces web autorise pour l'utilisateur {user_id}")
        else:
            self.result_label.config(text=f"Acces web non autorise pour l'utilisateur: {user_id}")

        cursor.close()