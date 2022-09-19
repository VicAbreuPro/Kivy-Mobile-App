import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Kivy Version
kivy.require("1.11.0")

# Load the kv file to Simulation Result Page
Builder.load_file('SimulationResult/resultapp.kv')


class SimPages(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Button to back to simulation page
    def back_page(self):
        self.parent.parent.current = 'simulator_page'


class ResultApp(App):
    def build(self):
        return SimPages()
