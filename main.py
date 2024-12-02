from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from app.ui.main_screen import MainScreen


class WLB(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(MainScreen(name='main'))

        return self.screen_manager

if __name__ == '__main__':
    WLB().run()
