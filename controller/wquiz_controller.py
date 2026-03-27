import random as rng
class WQuizController:
    def __init__(self, model):
        self.model = model
        self.wquiz_view = None

        # Keeps track of the selected element so that it can be unselected
        self.order = self.model.atoms.copy()
        self.found = set()
        self.element_names = {el.name.lower(): el for el in self.order}
        self.score = 0
        self.total = 118

    def set_view(self, wquiz_view):
        """ We set the view here, this gets set by app.py """
        self.wquiz_view = wquiz_view
        self.setup()

        
    def generate_element_text(self):
        self.wquiz_view.set_element_text(f"{self.score}/{self.total}")


    def compare_elements(self, element):
        typed = element.strip().lower()
        if typed in self.element_names and typed not in self.found:
            self.found.add(typed)
            el = self.element_names[typed]
            return el


    def setup(self):
        self.generate_element_text()
