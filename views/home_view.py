import tkinter as tk
from .base_view import BaseView


class HomeView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = tk.Label(self, text="Home View")
        label.pack()

    def show(self):
        self.pack(expand=True, fill='both')

    def hide(self):
        self.pack_forget()