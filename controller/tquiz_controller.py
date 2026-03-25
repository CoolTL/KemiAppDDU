import random as rng
class TQuizController:
    def __init__(self, model):
        self.model = model
        self.tquiz_view = None

        # Keeps track of the selected element so that it can be unselected
        self.selected_element =  None

    def set_view(self, tquiz_view):
        """ We set the view here, this gets set by app.py """
        self.tquiz_view = tquiz_view
        
    def generate_element_text(self, element):
        """ This gets called by the table view, and then we use it to update the description of the element """
        if element != self.selected_element:
            el = self.model.get_info(element)
            el2 = el[1:]
            self.tquiz_view.set_element_text(f"### Selected element: **{ el[0]}** <br> {'<br>'.join(el2)}")
            self.selected_element = element

    def random_element(self, element_list):
        return rng.shuffle(element_list)

    def compare_elements(self, element, current):
        if element == current:
            return True
        else:
            return False
