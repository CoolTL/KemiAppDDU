from nicegui import ui
from view.quiz_layout import QuizLayout

class QuizPackView(QuizLayout):
    def __init__(self, controller):
        super().__init__(controller)

    def setup_page(self):
        # Back button
        with ui.row().classes('w-full items-center relative'):
            ui.button(icon='arrow_back', on_click=lambda: ui.navigate.back())
            ui.label('Quiz pakke: Navngivning af molekyler').classes('text-2xl absolute left-1/2 -translate-x-1/2')

        with ui.column().classes('w-full h-screen items-center'):
            # Question text
            self.question = ui.label("Question goes here").classes('text-3xl mt-16')
            # Question image
            self.image = ui.image('Picture goes here').classes('object-contain').style('width: 25vw; max-width: 400px; min-width: 200px; height: auto;')
            # Answer options
            with ui.grid(columns=2):
                for i in range(len(self.answer_buttons)):
                    self.answer_buttons[i] = ui.button("Test").classes('w-64 text-xl')
            # Now we seperately set the on_click
            for i in range(len(self.answer_buttons)):
                self.answer_buttons[i].on_click(lambda val=self.answer_buttons[i]: self.answer_pressed(val))
            # Explanation text
            self.explanation_label = ui.label("Vælg et svar for at fortsætte.").classes('text-2xl')
            self.next_button = ui.button("Næste spørgsmål").on_click(self.next_button_pressed)
        self.next_button.set_enabled(False)

    def next_button_pressed(self):
        self.next_button.set_enabled(False)
        self.controller.next_question()
    def completed(self):
        with ui.dialog() as dialog, ui.card():
            ui.markdown(f"**Quiz Completed**")
            ui.button("Go Back", on_click=lambda: ui.navigate.back())
        dialog.open()
