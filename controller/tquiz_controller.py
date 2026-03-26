import random as rng
class TQuizController:
    def __init__(self, model):
        self.model = model
        self.tquiz_view = None

        # Keeps track of the selected element so that it can be unselected
        self.selected_element =  None
        self.order = self.model.atoms
        rng.shuffle(self.order)
        self.num = 0

    def set_view(self, tquiz_view):
        """ We set the view here, this gets set by app.py """
        self.tquiz_view = tquiz_view
        self.setup()

        
    def generate_element_text(self):
        self.tquiz_view.set_element_text(f"Current element: {self.order[self.num].name}")



    def compare_elements(self, element):
        if element == self.order[self.num]:
            self.num += 1
            self.generate_element_text()
            return True
        else:
            return False

    def setup(self):
        self.generate_element_text()
