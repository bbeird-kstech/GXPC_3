import tkinter as tk
from views.home_view import HomeView


class AppView(tk.Frame): # initializes the main application, watches for button presses.
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        parent.title("MVC Tkinter Example")

        # Create the left and right frames
        self.left_frame = tk.Frame(self, bg='gray')
        self.left_frame.pack(side='left', fill='y')

        self.right_frame = tk.Frame(self, bg='white')
        self.right_frame.pack(side='right', fill='both', expand=True)

        # List of button names
        self.button_names = ["Home", "Equipment", "Clients", "Schedule", "Setup", "Quit"]

        self.buttons = []
        for i, name in enumerate(self.button_names):
            button = tk.Button(self.left_frame, text=name, command=lambda i=i: self.on_button_click(i))
            button.pack(fill='x', pady=5, padx=5)
            self.buttons.append(button)

        self.pack(expand=True, fill='both')

        # Initialize HomeView
        self.home_view = HomeView(self.right_frame, self.controller)

    def on_button_click(self, index):
        if index < len(self.button_names):  # Check if the exit button (last button) is clicked
            button_name = self.button_names[index]
            if button_name == 'Quit':
                self.exit_application()
            else:
                self.controller.show_view(button_name)

    def exit_application(self):
        self.controller.exit_application()

    def show_view(self, view_name):
        self.controller.show_view(view_name)