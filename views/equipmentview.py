import tkinter as tk
from tkinter import ttk


class BaseView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='blue')
        self.controller = controller

    def show(self):
        self.pack(expand=True, fill='both')

    def hide(self):
        self.pack_forget()


class EquipmentHomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.create_buttons()

    def create_buttons(self):
        button_configs = [
            {"text": "Add", "fg": "white", "bg": "blue", "command": self.handle_add},
            {"text": "Modify", "fg": "white", "bg": "blue", "command": self.handle_modify},
            {"text": "Archive", "fg": "white", "bg": "blue", "command": self.handle_archive},
            {"text": "Restore", "fg": "white", "bg": "blue", "command": self.handle_restore},
            # Add more buttons as needed
        ]

        for config in button_configs:
            button = tk.Button(self, text=config["text"], command=config["command"], fg=config["fg"], bg=config["bg"],)
            button.pack(pady=10)

    def handle_add(self):
        self.controller.show_view("EquipmentAdd")

    def handle_modify(self):
        pass  # Implement logic for Modify button

    def handle_archive(self):
        pass  # Implement logic for Archive button

    def handle_restore(self):
        pass  # Implement logic for Restore button


class EquipmentAddView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.labels = ["Manufacturer:",
                       "Model Number:",
                       "Serial Number:",
                       "Description:",
                       "Number Of Calibration Points:",
                       ]

        self.entries = {}
        self.dropdown_vars = []  # List to hold StringVar for each dropdown
        self.create_input_table()
        self.dropdown_var = tk.StringVar(self)
        self.create_dropdown()
        self.create_buttons2()

    def create_input_table(self):
        for i, label in enumerate(self.labels):
            label_widget = tk.Label(self, text=label)
            label_widget.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            self.entries[label] = entry

    def create_dropdown(self):
        # Example options for dropdown list
        dropdown_options = [
            ("Units:", ["C", "F", "%RH", '"H20"', "PSI", "RPM", "SEC", "MIN"]),
            ("Cal Tol.:", ["0.1", "0.001", "5.0"]),
            ("Proc Tol:", ["0.2", "0.002", "10.0"]),
            ("Frequency:", ["Monthly", "3 Months", "6 Months", "12 Months"]),
            ("Criticality:", ["GMP Critical", "GMP Non-Critical", "Non-GMP"]),
            ("Client:", ["Your Mom", "Your Pop", "Acme Rockets"])
        ]

        # Place dropdown below the last label +1
        dropdown_start_row = len(self.labels)

        for i, (label_text, options) in enumerate(dropdown_options):
            label = tk.Label(self, text=label_text)
            label.grid(row=dropdown_start_row + i, column=0, padx=10, pady=5, sticky='w')

            var = tk.StringVar(self)
            var.set(options[0])
            self.dropdown_vars.append(var)
            dropdown = ttk.Combobox(self, textvariable=var, values=options)
            dropdown.grid(row=dropdown_start_row + i, column=1, padx=10, pady=5, sticky="e")

    def create_buttons2(self):
        button_configs = [
            {"text": "Submit", "command": self.handle_submit},
            {"text": "Clear All", "command": self.handle_clear},
            {"text": "Back", "command": self.handle_back},
            # Add more buttons as needed
        ]

        button_frame = tk.Frame(self)

        # Place the button frame below the dropdown + 1
        button_frame_row = len(self.labels) + len(self.dropdown_vars)
        button_frame.grid(row=button_frame_row, columnspan=2, pady=10)

        for i, config in enumerate(button_configs):
            button = tk.Button(button_frame, text=config["text"], command=config["command"])
            button.grid(row=0, column=i, padx=5, pady=5)

    def handle_submit(self):
        pass

    def handle_clear(self):
        pass  # Implement logic for Modify button

    def handle_back(self):
        self.controller.show_view("Equipment")
