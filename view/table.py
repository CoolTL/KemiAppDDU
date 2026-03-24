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
        self.controller.generate_element_text(element=element)

    def set_element_text(self, message):
        """ This gets called by the controller to set the element text """
        self.element_message.set_content(message)        

    def populate_table(self, m):
        """ This function takes a multiplier for settings up the table """
        for i in range(0+18*m, 18+18*m):
                    if self.layout[i] != 0:
                        with ui.button(f"{self.layout[i].symbol}", on_click=lambda val=self.layout[i]: self.button_pressed(val)).classes('w-[62px] h-[62px] p-0') as button:
                            self.buttons[self.layout[i]] = button
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

    def color_table(self):
        """ This method makes the colors of the buttons correct """
        # Defining the series colors because mendeleev doesn't have them
        SERIES_COLORS = {
            "Nonmetals": "#7fffd4",            # Light Green/Teal
            "Noble gases": "#c0ffff",          # Light Blue
            "Alkali metals": "#ff6666",        # Red/Pink
            "Alkaline earth metals": "#ffdead", # Light Orange/Tan
            "Metalloids": "#cccc99",           # Olive/Grey
            "Halogens": "#ffff99",             # Yellow
            "Poor metals": "#cccccc",          # Silver/Grey
            "Transition metals": "#ffc0cb",    # Pink
            "Lanthanides": "#ffbfff",          # Purple/Violet
            "Actinides": "#ff99cc",            # Darker Pink/Magenta
        }
        for button in self.buttons:
            self.buttons[button].set_background_color(SERIES_COLORS.get(button.series))

    def setup_page(self):
        with ui.row():
            # Back button
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/'))
            # Search bar
            self.search_bar = ui.input(label="Search for element", placeholder="Start typing").props('rounded outlined dense')

        with ui.row():
            # Periodic table setup
            with ui.card():
                self.setup_table()    
                # Color the table
                self.color_table()
                
            # Message box for element information
            with ui.card():
                self.element_message = ui.markdown("", extras=['latex'])
