# import tkinter as tk
import customtkinter as ctk

class BaseView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def show(self):
        self.pack(expand=True, fill='both')

    def hide(self):
        self.pack_forget()