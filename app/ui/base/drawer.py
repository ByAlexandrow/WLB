from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer, MDNavigationDrawerMenu, MDNavigationDrawerHeader,
    MDNavigationDrawerLabel, MDNavigationDrawerItem, MDNavigationDrawerDivider
)


class DrawerBase(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        self.nav_drawer_menu.add_widget(MDNavigationDrawerDivider())
        self.nav_drawer_menu.add_widget(MDNavigationDrawerLabel(text="Base"))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="briefcase-variant",
            text="Businesses",
            on_release=lambda x: self.switch_screen('businesses')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="calendar-check",
            text="Habits",
            on_release=lambda x: self.switch_screen('habits')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="palm-tree",
            text="Rest",
            on_release=lambda x: self.switch_screen('rest')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerDivider())
        self.nav_drawer_menu.add_widget(MDNavigationDrawerLabel(text="Customization"))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="trophy",
            text="Achievements",
            on_release=lambda x: self.switch_screen('achievements')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="lock",
            text="Security",
            on_release=lambda x: self.switch_screen('security')
        ))
        self.nav_drawer_menu.add_widget(MDNavigationDrawerItem(
            icon="cog",
            text="Settings",
            on_release=lambda x: self.switch_screen('settings')
        ))


    def switch_screen(self, screen_name):
        self.manager.current = screen_name
        self.nav_drawer.set_state("close")
