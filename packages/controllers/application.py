from .menus_controller import HomeMenuController


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start_application(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller.run()
