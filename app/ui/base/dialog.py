from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen


class DialogBase(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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


    def show_dialog(self):
        self.dialog.open()


    def close_dialog(self, *args):
        self.dialog.dismiss()
