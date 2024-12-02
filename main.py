from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.uix.screenmanager import MDScreenManager
from app.ui.main_screen import MainScreen
from app.ui.settings_screen import SettingsScreen
from kivy.core.text import LabelBase


LabelBase.register(name='Mulish-SemiBold', fn_regular='fonts/Mulish-SemiBold.ttf')

class BED(MDApp):
    def build(self):
        screen_manager = MDScreenManager()
        screen_manager.transition = NoTransition()

        # Добавляем экраны в MDScreenManager
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(Screen(name='businesses'))
        screen_manager.add_widget(Screen(name='habits'))
        screen_manager.add_widget(Screen(name='rest'))
        screen_manager.add_widget(Screen(name='achievements'))
        screen_manager.add_widget(Screen(name='security'))
        screen_manager.add_widget(SettingsScreen(name='settings'))

        return screen_manager


if __name__ == '__main__':
    BED().run()
