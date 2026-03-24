class TableController:
    def __init__(self, model):
        self.model = model

    def generate_element_text(self, table_view, element):
        """ This gets called by the table view, and then we use it to update the description of the element """
        table_view.set_element_text(f"Test: {element.name}")
