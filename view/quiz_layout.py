from nicegui import ui

class QuizLayout:
    """ This class is the actual quiz screen for daily quizzes """
    def __init__(self):
        # List of answer buttons
        self.answer_buttons = [None, None, None, None]
        self.setup_page()

    def setup_page(self):
        # Question text
        question = ui.label("Question goes here")
        # Question image
        # TODO implement later
        # Answer options
        with ui.grid(columns=2):
            for i in range(len(self.answer_buttons)):
                self.answer_buttons[i] = ui.button("Test")


