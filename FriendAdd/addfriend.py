import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kivy.require("1.11.0")

Builder.load_file('FriendAdd/friendadd.kv')


class AddFriendPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def back_page(self):
        self.parent.parent.current = 'eco_page'


class FriendAdd(App):
    def build(self):
        return AddFriendPage()
