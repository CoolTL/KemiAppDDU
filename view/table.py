from nicegui import ui

class TablePage():
    """ Periodic table page """

    def __init__(self, layout, controller):
        self.controller = controller
        self.layout = layout
        # Dictionary of buttons
        self.buttons = {}
        # Setup this page
        self.setup_page()

    
    def button_pressed(self, element):
        """ This calls the controller to change the text """
        self.controller.generate_element_text(table_view=self, element=element)

    def set_element_text(self, message):
        """ This gets called by the controller to set the element text """
        self.element_message.set_content(message)        

    def populate_table(self, m):
        """ This function takes a multiplier for settings up the table """
        for i in range(0+18*m, 18+18*m):
                    if self.layout[i] != 0:
                        with ui.button(f"{self.layout[i].symbol}", on_click=lambda val=self.layout[i]: self.button_pressed(val)).classes('w-[62px] h-[62px] p-0') as button:
                            self.buttons[f"e{self.layout[i]}"] = button
                            # Atomic number in the corner
                            ui.label(self.layout[i].atomic_number).classes('absolute top-0 left-1 text-[10px] opacity-85')
                            # Full name underneath
                            ui.label(self.layout[i].name).classes('absolute top-8 text-[9px] opacity-90')
                    else:
                        ui.space()

    def setup_table(self):
        """ This method is seperate to make the code a bit cleaner """
        grid_style = "grid-cols-[25px_repeat(18,60px)]"
        
        with ui.grid().classes(f'gap-1.5 {grid_style}'):
            ui.label('') # Empty corner
            # Numbers at the top
            for i in range(1, 19):
                ui.label(i).classes('text-center font-bold')
            # First 7 rows
            for i in range(0, 7):
                ui.label(i+1).classes('flex items-center justify-center font-bold')
                self.populate_table(i)
            # Empty row
            for i in range(0, 19):
                ui.space().classes('h-[20px]')
            # Last two lines
            for i in range(7, 9):
                ui.label('')
                self.populate_table(i)
        

    def setup_page(self):
        # Back button
        ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/'))
        # Make all buttons the same size, NOTE: I haven't deleted this incase we need it later
        # ui.add_head_html('''
        # <style> .q-btn { width: 60px; } </style>
        # ''')
        
        # Periodic table setup
        with ui.card():
            self.setup_table()    

        # Message box for element information
        self.element_message = ui.markdown("There is no element selected currently.")
