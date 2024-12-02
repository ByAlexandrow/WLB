from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar


class TopBarBase(MDScreen):
    def __init__(self, title="BED", **kwargs):
        super().__init__(**kwargs)

        # Создаем MDTopAppBar
        self.top_app_bar = MDTopAppBar(
            title=title,
            elevation=4,
            left_action_items=[["account-circle-outline", lambda x: self.nav_drawer.set_state("toggle")]],
            right_action_items=[["tea", lambda x: self.show_dialog()]],
            pos_hint={"top": 1},
            md_bg_color=(43/255, 9/255, 181/255)
        )
        self.add_widget(self.top_app_bar)
