from nicegui import ui
from view.quiz_layout import QuizLayout

class QuizPackView(QuizLayout):
    def __init__(self, controller):
        super().__init__(controller)

    def setup_page(self):
        super().setup_page()
        self.next_button = ui.button("Næste spørgsmål").on_click(self.next_button_pressed)
        self.next_button.set_enabled(False)

    def next_button_pressed(self):
        self.next_button.set_enabled(False)
        self.controller.next_question()
