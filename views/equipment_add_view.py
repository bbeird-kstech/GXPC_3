import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from .base_view import BaseView


class EquipmentAddView(BaseView):
    def __init__(self, parent, controller=None):
        super().__init__(parent, controller)

        # Initialize buttons dictionary
        self.buttons = {
            "Submit": ctk.CTkButton(self, text="Submit", command=self.handle_submit),
            # Add more buttons as needed
        }

        self.labels = [ "client_inst_id",
                        "description",
                        "manufacturer",
                        "model",
                        "serial_number",
                        "num_cal_pts",
                       ]

        self.entries = {}
        self.dropdown_vars = {}  # Dictionary to hold StringVar for each dropdown
        self.combo_boxes = {}   # dictionary to hold ComboBoxes

        self.create_input_table()
        self.create_dropdown()
        self.create_buttons2()


    def set_controller(self, controller):
        self.controller = controller

    def create_input_table(self):
        for i, label in enumerate(self.labels):
            label_widget = ctk.CTkLabel(self, text=label)
            label_widget.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            var = tk.StringVar(self)
            var.trace_add("write", self.validate_inputs)  # Add trace to validate inputs on change
            entry = ctk.CTkEntry(self, textvariable=var)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            self.entries[label] = entry

    def create_dropdown(self):
        # Initialize Dropdowns with empty list
        dropdown_options = [
            ("units", ["*"]),
            ("cal_tol", ["*"]),
            ("proc_tol", ["*"]),
            ("frequency", ["*"]),
            ("criticality", ["*"]),
            ("client", ["*"])
        ]

        # Place dropdown below the last label +1
        dropdown_start_row = len(self.labels)

        for i, (label_text, options) in enumerate(dropdown_options):
            label = ctk.CTkLabel(self, text=label_text)
            label.grid(row=dropdown_start_row + i, column=0, padx=10, pady=5, sticky='w')

            var = tk.StringVar(self)
            var.set("")
            var.trace_add("write", self.validate_inputs)  # Add trace to validate inputs on change
            self.dropdown_vars[label_text] = var
            dropdown = ctk.CTkComboBox(self, variable=var, values=options)
            #dropdown.bind("<Button-2>", lambda event, lt=label_text: self.controller.populate_dropdown(lt))
            dropdown.grid(row=dropdown_start_row + i, column=1, padx=10, pady=5, sticky="e")
            self.combo_boxes[label_text] = dropdown
            #self.controller.populate_dropdown(label_text)

    def update_dropdown_options(self, label_text, new_options):
        print(f"attempting to update {label_text} with {new_options}")
        if label_text in self.combo_boxes:
            # self.combo_boxes[label_text].configure(values=new_options)
            combobox = self.combo_boxes[label_text]
            combobox.configure(values = new_options)
            combobox.set('')  # Clear current selection
            combobox.update_idletasks()

    def create_buttons2(self):
        self.button_configs = [
            {"text": "Submit", "command": self.handle_submit},
            {"text": "Clear All", "command": self.handle_clear},
            {"text": "Back", "command": self.handle_back},
            # Add more buttons as needed
        ]

        self.button_frame = ctk.CTkFrame(self)

        # Place the button frame below the dropdown + 1
        button_frame_row = len(self.labels) + len(self.dropdown_vars)
        self.button_frame.grid(row=button_frame_row, columnspan=2, pady=10)

        for i, config in enumerate(self.button_configs):
            button = ctk.CTkButton(self.button_frame, text=config["text"], command=config["command"])
            button.grid(row=0, column=i, padx=5, pady=5)

    def validate_inputs(self, *args):
        # Validate all entry fields and dropdowns
        all_valid = all(var.get().strip() != "" for var in self.entries.values())
        all_valid = all_valid and all(var.get().strip() != "" for var in self.dropdown_vars.values())

        # Enable or disable the Submit button based on validation
        if all_valid:
            self.buttons["Submit"].configure(state=tk.NORMAL)
        else:
            self.buttons["Submit"].configure(state=tk.DISABLED)


    def handle_submit(self):
        # gather data from the text boxes and dropdowns
        data = {label: self.entries[label].get() for label in self.labels}  # get all of the data from the text boxes
        data.update({label: self.dropdown_vars[label].get() for label in self.dropdown_vars})  # add the combobox selections

        # validate the data...for now, no empty fields
        if not self.validate_data(data):
            print("Validation failed.")
            return

        # pass data to the controller to save it to the database
        self.controller.save_equipment_data(data)
        print("Data submitted successfully.")

    def validate_data(self, data):
        # Example validation logic, you can customize it as per your requirements
        for value in data.values():
            if not value:  # Check if any value is empty
                return False
        return True

    def handle_clear(self):
        pass  # Implement logic for Modify button

    def handle_back(self):
        self.controller.show_view("Equipment")

    def clear_entries(self):
        # Helper function to clear all entry boxes
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        for var in self.dropdown_vars.values():
            var.set("")  # Clear dropdown selections