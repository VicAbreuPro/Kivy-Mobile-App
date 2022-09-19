import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Kivy Version
kivy.require("1.11.0")

# Load KV file to Add equipment page
Builder.load_file('Equip_Add/equipmentadd.kv')


class EquipInfo(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Button to back to smart manager page
    def back_page(self):
        self.parent.parent.current = 'smart_page'

    # Button to Add a new equipment on smart manager list (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)
    def add_equip_page(self):
        self.parent.parent.current = 'equip_page'


class EquipmentAdd(App):
    def build(self):
        return EquipInfo()
