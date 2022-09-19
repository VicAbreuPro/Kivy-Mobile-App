import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kivy.require("1.11.0")

Builder.load_file('ProfileEdit/editpage.kv')


class ProfileEdit(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def back_page(self):
        self.parent.parent.current = 'profile_page'


class EditPage(App):
    def build(self):
        return ProfileEdit()
