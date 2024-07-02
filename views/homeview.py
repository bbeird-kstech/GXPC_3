import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue")
        self.label = tk.Label(self, text="Home", font=('Helvetica', 18, 'bold'), fg='white', bg='blue')
        self.label.pack(expand=True, fill='both')
        # Debugging: Print statements to check initialization
        print("HomeView initialized")