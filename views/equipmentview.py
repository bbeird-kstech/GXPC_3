import tkinter as tk


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
        self.create_input_table()
        self.create_buttons2()

    def create_input_table(self):
        for i, label in enumerate(self.labels):
            label_widget = tk.Label(self, text=label)
            label_widget.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            self.entries[label] = entry

    def create_buttons2(self):
        button_configs = [
            {"text": "Submit", "command": self.handle_submit},
            {"text": "Clear All", "command": self.handle_clear},
            {"text": "Back", "command": self.handle_back},
            # Add more buttons as needed
        ]

        button_frame = tk.Frame(self)
        button_frame.grid(row=len(self.labels), columnspan=2, pady=10)

        for i, config in enumerate(button_configs):
            button = tk.Button(button_frame, text=config["text"], command=config["command"])
            button.grid(row=0, column=i, padx=5, pady=5)

    def handle_submit(self):
        pass

    def handle_clear(self):
        pass  # Implement logic for Modify button

    def handle_back(self):
        self.controller.show_view("Equipment")
