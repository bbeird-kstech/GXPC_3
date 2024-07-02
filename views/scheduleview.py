import tkinter as tk

class ScheduleView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="blue")
        self.label = tk.Label(self, text="Schedule", font=('Helvetica', 18, 'bold'), fg='black', bg='blue')
        self.label.pack(expand=True, fill='both')
        print("ScheduleView initialized")