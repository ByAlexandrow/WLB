from kivymd.uix.label import MDLabel

from app.ui.base.drawer import DrawerBase
from app.ui.base.dialog import DialogBase
from app.ui.base.topbar import TopBarBase


class MainScreen(DrawerBase, DialogBase, TopBarBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'

        # Создаем MDLabel с пользовательским шрифтом и цветом
        self.label = MDLabel(
            text="BED",
            halign="center",
            pos_hint={"center_y": .8},
            font_size='35sp',
            color=(43/255, 9/255, 181/255),
            font_name='Mulish-SemiBold'
        )
        self.add_widget(self.label)

        # Создаем MDLabel с дефолтным шрифтом и цветом
        self.label = MDLabel(
            text="better every day",
            halign="center",
            pos_hint={"center_y": .75},
            font_size='20sp',
            color=(43/255, 9/255, 181/255)  # Устанавливаем цвет
        )
        self.add_widget(self.label)

        # Создаем MDLabel с дефолтным шрифтом и цветом
        self.label = MDLabel(
            text="1. Customize the app\n\n2. Set a password\n\n3. Use the app\n\n4. Be Better Every Day",
            halign="center",
            pos_hint={"center_y": .45},
            font_size='16sp',
            color=(43/255, 9/255, 181/255)  # Устанавливаем цвет
        )
        self.add_widget(self.label)

        # Создаем MDLabel с дефолтным шрифтом и цветом
        self.label = MDLabel(
            text="© 2024 Alexandrow",
            halign="center",
            pos_hint={"center_y": .05},
            font_size='14sp',
            color=(43/255, 9/255, 181/255)  # Устанавливаем цвет
        )
        self.add_widget(self.label)
