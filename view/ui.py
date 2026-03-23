from nicegui import ui

class MainPage():
    """ Main page """

    def __init__(self):

        # This is temp
        self.layout= [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
 3,4,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10,
 11,12,0,0,0,0,0,0,0,0,0,0,13,14,15,16,17,18,
 19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
 37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,
 55,56,0,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,
 87,88,0,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
 0,0,0,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,
 0,0,0,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103
 ]
        self.setup_page()

    
    def generate_element_text(self):
        self.element_message.set_content("Test")

    def populate_table(self, m):
        """ This function takes a multiplier for settings up the table """
        for i in range(0+18*m, 18+18*m):
                    if self.layout[i] != 0:
                        i = ui.button(self.layout[i], on_click=self.generate_element_text)
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


        self.element_message = ui.markdown("There is no element selected currently.")

page = MainPage()
ui.run()
