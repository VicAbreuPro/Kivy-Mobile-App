import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from SimulatorPage import function

# Kivy version
kivy.require("1.11.0")

# Load kv File to Simulator Page
Builder.load_file('SimulatorPage/simulatorapp.kv')


class SimPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.global_consume = None

    # Use information input to save on auxiliary variables
    def update_info(self):

        # Input Data Variables
        monthly_consume = self.ids.m_consume.text

        equipment_1 = self.ids.n_equip_1.text
        equipment_1_c = self.ids.m_consume_1.text
        equipment_2 = self.ids.n_equip_2.text
        equipment_2_c = self.ids.m_consume_2.text
        equipment_3 = self.ids.n_equip_3.text
        equipment_3_c = self.ids.m_consume_3.text
        equipment_4 = self.ids.n_equip_4.text
        equipment_4_c = self.ids.m_consume_4.text
        equipment_5 = self.ids.n_equip_5.text
        equipment_5_c = self.ids.m_consume_5.text
        equipment_6 = self.ids.n_equip_6.text
        equipment_6_c = self.ids.m_consume_6.text
        equipment_7 = self.ids.n_equip_7.text
        equipment_7_c = self.ids.m_consume_7.text
        equipment_8 = self.ids.n_equip_8.text
        equipment_8_c = self.ids.m_consume_8.text

        # Condition to insert or not the value of Monthly Consume
        if monthly_consume != '':
            function.equip_list.append(int(monthly_consume))
        else:
            function.equip_list.insert(0, int(0))  # In case of no insertion, monthly consume = 0

        # Verifications of no insertions on equipments data inputs
        if equipment_1 != '':
            if equipment_1_c != '':
                function.equip_list.append(equipment_1)
                function.equip_list.append(int(equipment_1_c))
        if equipment_2 != '':
            if equipment_2_c != '':
                function.equip_list.append(equipment_2)
                function.equip_list.append(int(equipment_2_c))
        if equipment_3 != '':
            if equipment_3_c != '':
                function.equip_list.append(equipment_3)
                function.equip_list.append(int(equipment_3_c))
        if equipment_4 != '':
            if equipment_4_c != '':
                function.equip_list.append(equipment_4)
                function.equip_list.append(int(equipment_4_c))
        if equipment_5 != '':
            if equipment_5_c != '':
                function.equip_list.append(equipment_5)
                function.equip_list.append(int(equipment_5_c))
        if equipment_6 != '':
            if equipment_6_c != '':
                function.equip_list.append(equipment_6)
                function.equip_list.append(int(equipment_6_c))
        if equipment_7 != '':
            if equipment_7_c != '':
                function.equip_list.append(equipment_7)
                function.equip_list.append(int(equipment_7_c))
        if equipment_8 != '':
            if equipment_8_c != '':
                function.equip_list.append(equipment_8)
                function.equip_list.append(int(equipment_8_c))

        # Calculation of total consume in simulation (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)
        self.consume_equip(function.equip_list)

    # Function to calculate the simulation calculation (TO BE FINISHED IN A FULLY FUNCTIONAL VERSION!)
    def consume_equip(self, equip_list_aux):
        function.save_list_info(equip_list_aux)
        self.global_consume = function.consume_total(equip_list_aux)
        self.result_page()

    # Button to simulate the inputs and show in a result page
    def result_page(self):
        self.parent.parent.current = 'sim_result_page'

    # Button to back to Initial Page of App
    def back_page(self):
        self.parent.parent.current = 'initial_page'


class SimulatorApp(App):
    def build(self):
        return SimPage()
