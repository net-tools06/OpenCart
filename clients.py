import tkinter as tk
from tkinter import ttk


class ConnectedClientsTab:
    def __init__(self, notebook, db):
        self.db = db
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Clients connectes")

        connected_clients_label = tk.Label(self.tab, text="Clients connectes:")
        connected_clients_label.pack()
        self.connected_clients_listbox = tk.Listbox(self.tab, width=30)
        self.connected_clients_listbox.pack()

        list_connected_clients_button = tk.Button(self.tab, text="Liste des clients connectes", command=self.list_connected_clients)
        list_connected_clients_button.pack()

    def list_connected_clients(self):
        cursor = self.db.cursor()

        query = "SELECT user_id, ip FROM oc_session WHERE session_id IS NOT NULL"
        cursor.execute(query)
        connected_clients = cursor.fetchall()

        self.connected_clients_listbox.delete(0, tk.END)

        for client in connected_clients:
            client_info = f"User ID: {client[0]}, IP: {client[1]}"
            self.connected_clients_listbox.insert(tk.END, client_info)

        cursor.close()