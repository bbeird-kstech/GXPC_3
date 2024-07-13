class ScheduleCon:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.add_view = None
        self.home_view = None

    def show_schedule_home_view(self):
        if self.home_view is None:
            self.home_view = ScheduleHomeView(self.main_controller.view.right_frame, self)
        return self.home_view

    def show_add_view(self):
        if self.add_view is None:
            self.add_view = ScheduleAddView(self.main_controller.view.right_frame, self)
        self.main_controller.show_view("ScheduleAdd")

#    def submit_add(self, data):
#        # Logic to handle submission of new equipment
#        print(f"Submitting data: {data}")