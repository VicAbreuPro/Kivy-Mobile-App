import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kivy.require("1.11.0")

Builder.load_file('ProfilePage/profileapp.kv')


class ProfilePage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def back_page(self):
        self.parent.parent.current = 'initial_page'

    def edit_profile(self):
        self.parent.parent.current = 'profile_edit'


class ProfileApp(App):
    def build(self):
        return ProfilePage()
