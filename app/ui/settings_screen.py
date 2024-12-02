from app.ui.base.drawer import DrawerBase
from app.ui.base.dialog import DialogBase
from app.ui.base.topbar import TopBarBase


class SettingsScreen(DrawerBase, DialogBase, TopBarBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'settings'
