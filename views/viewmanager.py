import tkinter as tk
from views.homeview import HomeView
from views.equipmentview import EquipmentHomeView, EquipmentAddView
from views.clientview import ClientView
from views.scheduleview import ScheduleView
from views.setupview import SetupView


class ViewManager:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Initialize all views
        self.views = {
            'Home': HomeView(self.root),
            'Equipment': EquipmentHomeView(self.root, self.controller),
            'EquipmentAdd': EquipmentAddView(self.root, self.controller),
            'Clients': ClientView(self.root),
            'Schedule': ScheduleView(self.root),
            'Setup': SetupView(self.root)
        }

        # Current view holder
        self.current_view = None
        print("ViewManager initialized with views: Home, Equipment, EquipmentAdd, Clients, Schedule, Setup")

    def show_view(self, view_name):
        print(f"Attempting to show view: {view_name}")
        if self.current_view:
            print(f"Hiding current view: {self.current_view}")
            self.current_view.pack_forget()  # Hide current view

        self.current_view = self.views.get(view_name)
        if self.current_view:
            print(f"Showing view: {view_name}")
            self.current_view.pack(expand=True, fill='both')  # Show new view
        else:
            print(f"View {view_name} not found!")