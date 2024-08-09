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
        # Define the order and configuration of input widgets for the left sub-frame
        self.input_fields = [
            {"type": "dropdown", "label": "client", "options": ["*"]},
            {"type": "entry", "label": "client_inst_id"},
            {"type": "entry", "label": "description"},
            {"type": "entry", "label": "manufacturer"},
            {"type": "entry", "label": "model"},
            {"type": "entry", "label": "serial_number"},
            {"type": "dropdown", "label": "frequency", "options": ["*"]},
            {"type": "dropdown", "label": "criticality", "options": ["*"]},
            {"type": "entry", "label": "num_cal_params"},  # This replaces num_cal_pts
        ]

        # Define the order and configuration of the 2nd frame input widgets
        self.input_fields_right = [
            {"type": "dropdown", "label": "Paramater", "options": ["*"]},
            {"type": "dropdown", "label": "units"},
            {"type": "entry", "label": "min_range"},
            {"type": "entry", "label": "max_range"},
            {"type": "entry", "label": "procedure_number"},
            {"type": "entry", "label": "num_cal_pts"},
        ]

        # Creating sub-frames within the parent frame (which is the right frame of the main application window)
        self.left_sub_frame = ctk.CTkFrame(self)
        self.left_sub_frame.grid(row=0, column=0, sticky="nsew")

        self.right_sub_frame = ctk.CTkFrame(self)
        self.right_sub_frame.grid(row=0, column=1, sticky="nsew")

        self.bottom_sub_frame = ctk.CTkFrame(self)
        self.bottom_sub_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.entries = {}
        self.dropdown_vars = {}  # Dictionary to hold StringVar for each dropdown
        self.combo_boxes = {}   # dictionary to hold ComboBoxes

        self.create_input_widgets()
        self.create_buttons()

    def set_controller(self, controller):
        self.controller = controller

    def create_input_widgets(self):
        for i, field in enumerate(self.input_fields):
            if field["type"] == "entry":
                self.create_entry_widget(field["label"], i)
            elif field["type"] == "dropdown":
                self.create_dropdown_widget(field["label"], field["options"], i)

    def create_entry_widget(self, label, row):
        label_widget = ctk.CTkLabel(self.left_sub_frame, text=label)
        label_widget.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        var = tk.StringVar(self)
        var.trace_add("write", self.validate_inputs)
        entry = ctk.CTkEntry(self.left_sub_frame, textvariable=var)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="e")
        self.entries[label] = entry

        if label == "num_cal_params":  # Bind event to the specific text box
            entry.bind('<KeyRelease>', self.populate_right_sub_frame)

    def create_dropdown_widget(self, label, options, row):
        label_widget = ctk.CTkLabel(self.left_sub_frame, text=label)
        label_widget.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        var = tk.StringVar(self)
        var.set("")
        var.trace_add("write", self.validate_inputs)
        dropdown = ctk.CTkComboBox(self.left_sub_frame, variable=var, values=options)
        dropdown.grid(row=row, column=1, padx=10, pady=5, sticky="e")
        self.dropdown_vars[label] = var
        self.combo_boxes[label] = dropdown

    def populate_right_sub_frame(self, event=None):
        # Clear the right sub-frame before populating
        for widget in self.right_sub_frame.winfo_children():
            widget.destroy()

        # Get the number from the textbox 'num_cal_params'
        num_rows = self.entries["num_cal_params"].get()

        # Ensure the input is a valid integer
        if num_rows.isdigit():
            num_rows = int(num_rows)

            # Create labels above each widget column
            for i, field in enumerate(self.input_fields_right):
                label_widget = ctk.CTkLabel(self.right_sub_frame, text=field["label"])
                label_widget.grid(row=0, column=i, padx=5, pady=5, sticky="w")  # Place labels in the first row

                # Dynamically create rows of input controls in the right sub-frame
                for row in range(1, num_rows + 1):  # Start from row 1 to leave row 0 for labels
                    for i, field in enumerate(self.input_fields_right):
                        if field["type"] == "entry":
                            self.create_entry_widget_right(field["label"], self.right_sub_frame, row, i)
                        elif field["type"] == "dropdown":
                            options = field.get("options", ["Option1", "Option2"])
                            self.create_dropdown_widget_right(field["label"], options, self.right_sub_frame, row, i)

    def create_entry_widget_right(self, label, parent, row, column):
        var = tk.StringVar(parent)
        entry = ctk.CTkEntry(parent, textvariable=var, width=100)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
        self.entries[label] = entry

    def create_dropdown_widget_right(self, label, options, parent, row, column):
        var = tk.StringVar(parent)
        var.set("")
        dropdown = ctk.CTkComboBox(parent, variable=var, values=options, width=100)
        dropdown.grid(row=row, column=column, padx=5, pady = 5, sticky="ew")
        self.dropdown_vars[label] = var
        self.combo_boxes[label] = dropdown

    def update_dropdown_options(self, label_text, new_options):
        """This method updates the options for a specific dropdown."""
        if label_text in self.combo_boxes:
            combobox = self.combo_boxes[label_text]
            combobox.configure(values=new_options)
            combobox.set('')  # Clear current selection
            combobox.update_idletasks()
            
    def create_buttons(self):
        self.button_configs = [
            {"text": "Submit", "command": self.handle_submit},
            {"text": "Clear All", "command": self.handle_clear},
            {"text": "Back", "command": self.handle_back},
        ]

        self.button_frame = ctk.CTkFrame(self.bottom_sub_frame)

        for i, config in enumerate(self.button_configs):
            button = ctk.CTkButton(self.button_frame, text=config["text"], command=config["command"])
            #button.grid(row=0, column=i, padx=5, pady=5)
            button.pack(side="left", padx=5, pady=5)

        self.button_frame.pack(fill="x", pady=10)

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