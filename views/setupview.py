import tkinter as tk

class SetupView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue")
        self.label = tk.Label(self, text="Setup", font=('Helvetica', 18, 'bold'), fg='white', bg='blue')
        self.label.pack(expand=True, fill='both')
        print("SetupView initialized")