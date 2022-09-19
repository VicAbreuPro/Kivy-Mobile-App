import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kivy.require("1.11.0")

Builder.load_file('ConfigPage/configapp.kv')


class ConfigPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def edit_prof(self):
        self.parent.parent.current = 'profile_edit'

    def back_page(self):
        self.parent.parent.current = 'initial_page'


class ConfigApp(App):
    def build(self):
        return ConfigPage()
