from nicegui import ui

class QuizLayout:
    """ This class is the actual quiz screen for daily quizzes """
    def __init__(self, controller):
        # List of answer buttons
        self.controller = controller
        self.answer_buttons = [None, None, None, None]
        self.setup_page()

    def setup_page(self):
        # Back button
        ui.button(icon='arrow_back', on_click=lambda: ui.navigate.back())
        # Question text
        self.question = ui.label("Question goes here")
        # Question image
        # TODO implement later
        # Answer options
        with ui.grid(columns=2):
            for i in range(len(self.answer_buttons)):
                self.answer_buttons[i] = ui.button("Test")
        # Now we seperately set the on_click
        for i in range(len(self.answer_buttons)):
            self.answer_buttons[i].on_click(lambda val=self.answer_buttons[i]: self.answer_pressed(val))
        # Explanation text
        self.explanation_label = ui.label("Choose an answer")

    def place_question_text(self, question, options):
        """ This gets called by the controller and gives the options for answers, plus the question """
        self.question.set_text(question)
        i = 0
        for button in self.answer_buttons:
            button.set_text(options[i])
            i += 1

    def write_explanation(self, explanation):
        """ This puts a string into the explanation label after you've answered something """
        self.explanation_label.set_text(explanation)

    def answer_pressed(self, button):
        """ This calls the controller to check if it was correct or not """
        answer_picked = button.text
        self.controller.check_answer(answer_picked)

    def buttons_enabled(self, state):
        """ Enable or disable answers """
        if state:
            for button in self.answer_buttons:
                button.enable()
        else:
            for button in self.answer_buttons:
                button.disable()
