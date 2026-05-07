from nicegui import ui
from paths import resource_path

class QuizLayout:
    """ This class is the actual quiz screen for daily quizzes """
    def __init__(self, controller):
        # List of answer buttons
        self.controller = controller
        self.answer_buttons = [None, None, None, None]
        self.setup_page()

    def setup_page(self):
        # Back button
        with ui.row().classes('w-full items-center relative'):
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.back())
            ui.label('Dagens Kemi Spørgsmål').classes('text-2xl absolute left-1/2 -translate-x-1/2')

        with ui.column().classes('w-full h-screen items-center'):
            # Question text
            self.question = ui.label("Question goes here").classes('text-3xl mt-16')
            # Question image
            self.image = ui.image('Picture goes here').classes('w-32 h-32 object-contain').style('width: 25vw; max-width: 400px; min-width: 200px; height: auto;')
            # Answer options
            with ui.grid(columns=2):
                for i in range(len(self.answer_buttons)):
                    self.answer_buttons[i] = ui.button("Test").classes('w-64 text-xl')
            # Now we seperately set the on_click
            for i in range(len(self.answer_buttons)):
                self.answer_buttons[i].on_click(lambda val=self.answer_buttons[i]: self.answer_pressed(val))
            # Explanation text
            self.explanation_label = ui.label("Vælg et svar for at fortsætte.").classes('text-2xl')

    def place_question_text(self, question, options, image):
        """ This gets called by the controller and gives the options for answers, plus the question """
        self.question.set_text(question)
        self.image.set_source(resource_path(image))
        self.explanation_label.set_text("Vælg et svar for at fortsætte.")
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
    def completed(self):
        with ui.dialog() as dialog, ui.card():
            ui.markdown(f"**Quiz Completed**")
            ui.button("Go Back", on_click=lambda: ui.navigate.back())
        dialog.open()

