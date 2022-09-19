import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Version Kivy
kivy.require("1.11.0")

# Load kv file of Class InitialPage
Builder.load_file('InitialPage/ecoworld.kv')


# Class of Initial Page
class InitialPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Button to Simulator Page
    def simulator_button(self):
        self.parent.parent.current = 'simulator_page'

    # Button to Smart Manager Page
    def smart_manager_button(self):
        self.parent.parent.current = 'smart_page'

    # Button to Profile Page
    def profile_button(self):
        self.parent.parent.current = 'profile_page'

    # Button to Eco Friends Page
    def eco_button(self):
        self.parent.parent.current = 'eco_page'

    # Button to Configuration Page
    def config_button(self):
        self.parent.parent.current = 'config_page'

    # Button to Exit Application
    @staticmethod  # define a static method
    def exit_button():
        exit(1)


class EcoWorld(App):
    def build(self):
        return InitialPage()

