import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kivy.require("1.11.0")

Builder.load_file('EcoPage/ecop.kv')


class EcoPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def back_page(self):
        self.parent.parent.current = 'initial_page'

    def add_friend_button(self):
        self.parent.parent.current = 'add_friend_page'


class EcoApp(App):
    def build(self):
        return EcoPage()
