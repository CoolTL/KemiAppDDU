from nicegui import ui

class MainPage():
    """ Main page """

    def __init__(self, layout):
        self.layout = layout
        # Dictionary of buttons
        self.buttons = {}
        # Setup this page
        self.setup_page()

    
    def generate_element_text(self, element):
        self.element_message.set_content(f"Element: {element}")

    def populate_table(self, m):
        """ This function takes a multiplier for settings up the table """
        for i in range(0+18*m, 18+18*m):
                    if self.layout[i] != 0:
                        self.buttons[f"e{self.layout[i]}"] = ui.button(f"{self.layout[i]}", on_click=lambda val=self.layout[i]: self.generate_element_text(val))
                    else:
                        ui.space()

    def setup_table(self):
        """ This method is seperate to make the code a bit cleaner """
        with ui.column():
            with ui.row().classes('w-full'):
                self.populate_table(0)
            with ui.row().classes('w-full'):
                self.populate_table(1)
            with ui.row().classes('w-full'):
                self.populate_table(2)
            with ui.row().classes('w-full'):
                self.populate_table(3)
            with ui.row().classes('w-full'):
                self.populate_table(4)
            with ui.row().classes('w-full'):
                self.populate_table(5)
            with ui.row().classes('w-full'):
                self.populate_table(6)
            ui.space()
            with ui.row().classes('w-full'):
                self.populate_table(7)
            with ui.row().classes('w-full'):
                self.populate_table(8)
        

    def setup_page(self):
        # Make all buttons the same size
        ui.add_head_html('''
        <style> .q-btn { width: 60px; } </style>
        ''')
        
        # Make all the buttons not be in caps so that the elements are displayed correctly
        ui.button.default_props('no-caps')

        # Periodic table setup
        self.setup_table()    

        # Message box for element information
        self.element_message = ui.markdown("There is no element selected currently.")
