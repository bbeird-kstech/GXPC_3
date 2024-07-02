import tkinter as tk
from views.views import AppView

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = AppView(self.root, self)
        self.root.attributes("-fullscreen", True)  # Open in fullscreen

    def run(self):
        self.root.mainloop()

    def show_view(self, view_name):
        self.view.show_view(view_name)

