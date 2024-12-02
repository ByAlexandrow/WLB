from kivy.uix.screenmanager import Screen
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer, MDNavigationDrawerMenu, MDNavigationDrawerHeader,
    MDNavigationDrawerLabel, MDNavigationDrawerItem, MDNavigationDrawerDivider
)
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'
        self.screen_manager = MDScreenManager()
        self.add_widget(self.screen_manager)

        # Добавляем экраны в MDScreenManager
        self.screen_manager.add_widget(Screen(name='inbox'))
        self.screen_manager.add_widget(Screen(name='sent'))
        self.screen_manager.add_widget(Screen(name='label1'))
        self.screen_manager.add_widget(Screen(name='label2'))

        # Создаем MDTopAppBar
        self.top_app_bar = MDTopAppBar(
            title="WLB",
            elevation=4,
            left_action_items=[["account-circle-outline", lambda x: self.nav_drawer.set_state("toggle")]],
            right_action_items=[["tea", lambda x: self.show_dialog()]],
            pos_hint={"top": 1}
        )
        self.add_widget(self.top_app_bar)

        # Создаем MDLabel
        self.label = MDLabel(
            text="Customize the app for yourself\nYou can even set a password\nAnd rename the app",
            halign="center",
            pos_hint={"center_y": .5},
        )
        self.add_widget(self.label)

        # Создаем MDDialog
        self.dialog = MDDialog(
            title="Tea Time",
            text="Would you like some tea?",
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
            ],
        )

        # Создаем MDNavigationDrawer
        self.nav_drawer = MDNavigationDrawer(
            id='nav_drawer',
            radius=(0, 16, 16, 0)
        )
        self.add_widget(self.nav_drawer)

        # Создаем MDNavigationDrawerMenu
        self.nav_drawer_menu = MDNavigationDrawerMenu()
        self.nav_drawer.add_widget(self.nav_drawer_menu)

        # Добавляем элементы в MDNavigationDrawerMenu
        self.nav_drawer_menu.add_widget(MDNavigationDrawerHeader(
            title="User Name",
            text="your status will be here",
            spacing="4dp",
            padding=("12dp", "16dp", 0, "12dp")
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerLabel(text="Base"))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Businesses",
            text="Businesses",
            on_release=lambda x: self.switch_screen('inbox')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Habits",
            text="Habits",
            on_release=lambda x: self.switch_screen('sent')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Rest",
            text="Rest",
            on_release=lambda x: self.switch_screen('sent')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerDivider())
        self.nav_drawer_menu.add_widget(MDNavigationDrawerLabel(text="Customization"))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Achievements",
            text="Achievements",
            on_release=lambda x: self.switch_screen('label1')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Security",
            text="Security",
            on_release=lambda x: self.switch_screen('label2')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="Settings",
            text="Settings",
            on_release=lambda x: self.switch_screen('label3')
        ))

    def switch_screen(self, screen_name):
        self.screen_manager.current = screen_name
        self.nav_drawer.set_state("close")
    

    def show_dialog(self):
        self.dialog.open()


    def close_dialog(self, *args):
        self.dialog.dismiss()
