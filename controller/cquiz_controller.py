import random as rng
from collections import Counter
class CQuizController:
    def __init__(self, model):
        self.model = model
        self.cquiz_view = None

        # Keeps track of the selected element so that it can be unselected
        self.selected_element =  None
        self.series_total = Counter(el.series for el in self.model.atoms)
        self.series_progress = {series: 0 for series in self.series_total}
        self.current_series = None
        self.score = 0
        self.clicked = set()
        self.completed = False

    def set_view(self, cquiz_view):
        """ We set the view here, this gets set by app.py """
        self.cquiz_view = cquiz_view
        self.setup()

        
    def generate_element_text(self):
        if self.current_series is None:
            self.completed = True
            self.cquiz_view.set_element_text(f"***Quiz Completed, final score: *** {self.score}")
        else:
            series = self.current_series
            self.cquiz_view.set_element_text(f"Current series: {self.current_series} <br> Amount pressed: {self.series_progress[series]}/{self.series_total[series]} ***Score:*** {self.score}")



    def compare_series(self, element):
        if element in self.clicked:
            return
        if self.current_series is None:
            return

        if element.series == self.current_series:
            self.series_progress[self.current_series] += 1
            self.score += 100
            self.clicked.add(element)
            if self.series_progress[self.current_series] == self.series_total[self.current_series]:
                self.next_series()
                return True
            self.generate_element_text()
            return True
        else:
            self.score -= 50
        self.generate_element_text()

    def next_series(self):
        if self.series_index is None and self.completed == False:
            rng.shuffle(self.series_list)
        if self.series_index >= len(self.series_list):
            self.current_series = None
            self.generate_element_text()
            return
        self.current_series = self.series_list[self.series_index]
        self.series_index += 1
        self.series_progress[self.current_series] = 0
        self.generate_element_text()



    def setup(self):
        self.series_list = list(self.series_total.keys())
        rng.shuffle(self.series_list)
        self.score = 0
        self.series_index = 0
        self.next_series()
