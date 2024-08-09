"""
Home Controller

Initializes Views, handles view switching.
"""
#import tkinter as tk
import customtkinter as ctk
from views.app_view import AppView
from views.home_view import HomeView
from views.equipment_home_view import EquipmentHomeView
from equipment_con import EquipmentCon
from clients_con import ClientsCon
from schedule_con import ScheduleCon
from setup_con import SetupCon
from database.db import Database

class HomeCon:

    def __init__(self):
        #self.root = tk.Tk()
        self.root = ctk.CTk()
        # Set full-screen mode
        self.root.attributes("-fullscreen", True)

        self.view = AppView(self.root, self)
        self.database = Database()
        self.equipment_con = EquipmentCon(self)
        self.clients_con = ClientsCon(self)
        self.schedule_con = ScheduleCon(self)
        self.setup_con = SetupCon(self)
        self.current_view = None


        self.show_view("Home")

############################################
#           Main Entry Point
    def run(self):
        self.root.mainloop()

############################################
#           Manage Views
    def show_view(self, view_name):                 # the home controller launches the main view
        print(f"Attempting to show view: {view_name}")
        if self.current_view is not None:
            self.current_view.hide()

        if view_name == "Home":
            self.current_view = self.view.home_view
        elif view_name == "Equipment":
            self.current_view = self.equipment_con.show_equipment_home_view()
        elif view_name == "EquipmentAdd":
            self.current_view = self.equipment_con.add_view
        elif view_name == "Clients":
            self.current_view = self.clients_con.show_clients_home_view()
        elif view_name == "Schedule":
            self.current_view = self.schedule_con.show_schedule_home_view()
        elif view_name == "Setup":
            self.current_view = self.setup_con.show_setup_home_view()
            # Add other views as needed

        if self.current_view:
            self.current_view.show()

###################################################
#           Exit the Application
    def exit_application(self):
        self.root.destroy()

##############################################
#        Save these in case I need to refer to them
    #def populate_dropdown(self):
    #    print("Populating client dropdown")
    #    client_names = self.database.get_client_names()
    #    print(f"Client names retrieved: {client_names}")
    #    self.view.equipment_add_view.update_dropdown_options("Client:", client_names)

    #def get_client_names(self):
    #    # Replace with actual database query to fetch client names
    #    return self.database.get_client_names()