import tkinter as tk
from viewmanager import ViewManager
from .equipmentview import EquipmentAddView


class AppView:

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.parent.title("MVC Tkinter Example")

        # Create the left and right frames
        self.left_frame = tk.Frame(self.parent, bg='gray')
        self.left_frame.pack(side='left', fill='y')

        self.right_frame = tk.Frame(self.parent, bg='white')
        self.right_frame.pack(side='right', fill='both', expand=True)

        # List of button names
        self.button_names = ["Home", "Equipment", "Clients", "Schedule", "Setup", "Quit"]

        self.buttons = []
        for i, name in enumerate(self.button_names):
            button = tk.Button(self.left_frame, text=name, command=lambda i=i: self.on_button_click(i))
            button.pack(fill='x', pady=5, padx=5)
            self.buttons.append(button)

        self.equipment_add_view = EquipmentAddView(self.parent, self.controller)

        # Initialize view manager
        self.view_manager = ViewManager(self.right_frame, self.controller)

        # Start with the first view
        self.show_view("Home")

    def on_button_click(self, index):
        if index < len(self.button_names):  # Check if the exit button (last button) is clicked
            button_name = self.button_names[index]
            if button_name == 'Quit':
                self.exit_application()
            else:
                self.show_view(button_name)

    def exit_application(self):
        self.parent.destroy()

    def show_view(self, view_name):
        if view_name == "EquipmentAddView":
            self.equipment_add_view(fill=tk.BOTH, expand=1)
        else:
            self.view_manager.show_view(view_name)
