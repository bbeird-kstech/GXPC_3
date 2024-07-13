import tkinter as tk
from views.equipment_home_view import EquipmentHomeView
from views.equipment_add_view import EquipmentAddView


class EquipmentCon:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.add_view = None
        self.home_view = None
        self.combo_list = None

    def show_equipment_home_view(self):
        if self.home_view is None:
            self.home_view = EquipmentHomeView(self.main_controller.view.right_frame, self)
        return self.home_view

    def show_add_view(self):
        if self.add_view is None:
            self.add_view = EquipmentAddView(self.main_controller.view.right_frame, self)
        self.main_controller.show_view("EquipmentAdd")

    def populate_dropdown(self, label_text):
        if label_text == "units":
            self.combo_list = self.main_controller.database.get_units()
        elif label_text == "cal_tol":
            self.combo_list = self.main_controller.database.get_caltol()
        elif label_text == "proc_tol":
            self.combo_list = self.main_controller.database.get_proctol()
        elif label_text == "frequency":
            self.combo_list = self.main_controller.database.get_calfreq()
        elif label_text == "criticality":
            self.combo_list = self.main_controller.database.get_criticality()
        elif label_text == "client":
            self.combo_list = self.main_controller.database.get_client_names()

        self.add_view.update_dropdown_options(label_text, self.combo_list)

    def save_equipment_data(self, data):
        print("this is where we write the data")
        # need to use the client name to lookup the client id.
        client_name = data.pop("client", None)
        if client_name is None:
            print("Client name not provided.")
            return

        # Lookup the client by name to get the ID
        client_id = self.main_controller.database.get_client_id_by_name(client_name)
        if not client_id:
            print(f"No client found with the name {client_name}.")
            return

        # Assuming you have a client_id column in the Equipment table
        data['client'] = client_id

        if self.main_controller.database.save_new_equipment(data):
            print("Equipment saved to database with client ID")
        else:
            print("failed to save equipment")
