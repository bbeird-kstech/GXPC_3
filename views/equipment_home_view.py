import tkinter as tk
from .base_view import BaseView


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
        print("going to show_add_view")
        self.controller.show_add_view()

    def handle_modify(self):
        pass  # Implement logic for Modify button

    def handle_archive(self):
        pass  # Implement logic for Archive button

    def handle_restore(self):
        pass  # Implement logic for Restore button