import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from InitialPage.init import InitialPage
from SimulatorPage.simulator import SimPage
from SimulationResult.result import SimPages
from SmartManagerPage.sm import SmartPage
from Equip_Add.equipadd import EquipInfo
from ProfilePage.profile import ProfilePage
from ProfileEdit.editprof import ProfileEdit
from EcoPage.ecofriends import EcoPage
from FriendAdd.addfriend import AddFriendPage
from ConfigPage.config import ConfigPage

# Kivy Version
kivy.require("1.11.0")


# MainClass to screen management
class MainWindow(BoxLayout):
    # Set the First page to no resize
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '600')

    # Class Attributes to link to another pages of App
    init_page = InitialPage()
    simulation_page = SimPage()
    sim_r = SimPages()
    smart_p = SmartPage()
    equip_inf = EquipInfo()
    prof_page = ProfilePage()
    edit_prof = ProfileEdit()
    eco_friends = EcoPage()
    eco_add = AddFriendPage()
    config = ConfigPage()

    # Class Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add pages with ids from screen manager as a widget
        self.ids.initial_page.add_widget(self.init_page)
        self.ids.simulator_page.add_widget(self.simulation_page)
        self.ids.sim_result_page.add_widget(self.sim_r)
        self.ids.smart_page.add_widget(self.smart_p)
        self.ids.equip_page.add_widget(self.equip_inf)
        self.ids.profile_page.add_widget(self.prof_page)
        self.ids.profile_edit.add_widget(self.edit_prof)
        self.ids.eco_page.add_widget(self.eco_friends)
        self.ids.add_friend_page.add_widget(self.eco_add)
        self.ids.config_page.add_widget(self.config)


class MainApp(App):
    def build(self):
        return MainWindow()


# Run Program
MainApp().run()
