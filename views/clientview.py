import tkinter as tk

class ClientView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue")
        self.label = tk.Label(self, text="Client", font=('Helvetica', 18, 'bold'), fg='white', bg='blue')
        self.label.pack(expand=True, fill='both')
        print("ClientView initialized")