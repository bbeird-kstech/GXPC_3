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
        print("going to show_view in home_con")
        self.main_controller.show_view("EquipmentAdd")

    def populate_dropdown(self, label_text):
        if label_text == "Units:":
            pass
        elif label_text == "Cal Tol.:":
            pass
        elif label_text == "Proc Tol.:":
            pass
        elif label_text == "Frequency:":
            pass
        elif label_text == "Criticality:":
            pass
        elif label_text == "Client:":
            self.combo_list = self.main_controller.database.get_client_names()

        self.add_view.update_dropdown_options(label_text, self.combo_list)