class TableController:
    def __init__(self, model):
        self.model = model
        self.table_view = None

        # Keeps track of the selected element so that it can be unselected
        self.selected_element =  None

    def set_view(self, table_view):
        """ We set the view here, this gets set by app.py """
        self.table_view = table_view
        # Show the start message
        self.unselect_element()
        
    def unselect_element(self):
        """ This is also run at the start and everytime an element is unselected """
        self.selected_element = None
        start_message = """### Selected element: **None**
        Each element in the system is represented by its symbol and its atomic number in the top left corner."""
        self.table_view.set_element_text(start_message)
        


    def generate_element_text(self, element):
        """ This gets called by the table view, and then we use it to update the description of the element """
        if element != self.selected_element:
            el = self.model.get_info(element)
            el2 = el[1:]
            self.table_view.set_element_text(f"### Selected element: **{ el[0]}** <br> {'<br>'.join(el2)}")
            self.selected_element = element
        else:
            self.unselect_element()

    def update_search(self, text):
        """ This gets called by the view when the search changes, we use this to show/hide elements """
        self.hide_unsearched(self.model.search(text))

    def hide_unsearched(self, search):
        """ This hides the elements that don't fit the search """
        for button in self.table_view.buttons:
            if button.name in search:
                self.table_view.buttons[button].classes(remove='opacity-0 pointer-events-none')
            else:
                self.table_view.buttons[button].classes('opacity-0 pointer-events-none')
