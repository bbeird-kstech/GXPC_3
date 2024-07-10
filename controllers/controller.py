import tkinter as tk
from views.views import AppView
from database.db import Database

class AppController:
    def __init__(self):
        print("initializing AppController")
        self.root = tk.Tk()
        self.view = AppView(self.root, self)
        self.database = Database()
        self.root.attributes("-fullscreen", True)  # Open in fullscreen

    def run(self):
        self.root.mainloop()

    def show_view(self, view_name):
        print(f"Showing view: {view_name}")
        self.view.show_view(view_name)
        if view_name == "EquipmentAdd":
            self.populate_client_dropdown()

    def populate_client_dropdown(self):
        print("Populating client dropdown")
        client_names = self.database.get_client_names()
        print(f"Client names retrieved: {client_names}")
        self.view.equipment_add_view.update_dropdown_options("Client:", client_names)

