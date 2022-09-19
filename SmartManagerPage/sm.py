import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Kivy Version
kivy.require("1.11.0")

# Load Kv file to Smart Manager page
Builder.load_file('SmartManagerPage/smartmanager.kv')


class SmartPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Button to back to Initial Page
    def back_page(self):
        self.parent.parent.current = 'initial_page'

    # Button to Add Equipment Page
    def add_equip_page(self):
        self.parent.parent.current = 'equip_page'


class SmartManager(App):
    def build(self):
        return SmartPage()
