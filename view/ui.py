from nicegui import ui

class MainPage():
    """ Main page """

    def __init__(self):
        self.setup_page()
    
    def generate_element_text(self):
        self.element_message.set_content("Test")

    def setup_page(self):
        # Make all buttons the same size
        ui.add_head_html('''
        <style> .q-btn { width: 60px; } </style>
        ''')
        
        # Make all the buttons not be in caps so that the elements are displayed correctly
        ui.button.default_props('no-caps')

        # Periodic table setup
        with ui.column():
            with ui.row().classes('w-full'):
                ui.button('H', on_click=self.generate_element_text)
                ui.space()
                ui.button('He')
            with ui.row().classes('w-full'):
                ui.button('Li')
                ui.button('Be')
                ui.space()
                ui.button('B')
                ui.button('C')
                ui.button('N')
                ui.button('O')
                ui.button('F')
                ui.button('Ne')
            with ui.row().classes('w-full'):
                ui.button('Na')
                ui.button('Mg')
                ui.space()
                ui.button('Al')
                ui.button('Si')
                ui.button('P')
                ui.button('S')
                ui.button('Cl')
                ui.button('Ar')
            with ui.row().classes('w-full'):
                ui.button('K')
                ui.button('Ca')
                ui.button('Sc')
                ui.button('Ti')
                ui.button('V')
                ui.button('Cr')
                ui.button('Mn')
                ui.button('Fe')
                ui.button('Co')
                ui.button('Ni')
                ui.button('Cu')
                ui.button('Zn')
                ui.button('Ga')
                ui.button('Ge')
                ui.button('As')
                ui.button('Se')
                ui.button('Br')
                ui.button('Kr')
            with ui.row().classes('w-full'):
                for i in range(0, 18):
                    ui.button(i)


        self.element_message = ui.markdown("There is no element selected currently.")

page = MainPage()
ui.run()
