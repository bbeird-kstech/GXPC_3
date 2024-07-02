import tkinter as tk
from viewmanager import ViewManager


class AppView:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("MVC Tkinter Example")

        # Create the left and right frames
        self.left_frame = tk.Frame(self.root, bg='gray')
        self.left_frame.pack(side='left', fill='y')

        self.right_frame = tk.Frame(self.root, bg='white')
        self.right_frame.pack(side='right', fill='both', expand=True)

        # List of button names
        self.button_names = ["Home", "Equipment", "Clients", "Schedule", "Setup", "Quit"]

        self.buttons = []
        for i, name in enumerate(self.button_names):
            button = tk.Button(self.left_frame, text=name, command=lambda i=i: self.on_button_click(i))
            button.pack(fill='x', pady=5, padx=5)
            self.buttons.append(button)

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
        self.root.destroy()

    def show_view(self, view_name):
        self.view_manager.show_view(view_name)
