from nicegui import ui


class QuizScreen:
    def __init__(self):
        self.setup_page()

    def setup_page(self):
        ui.button(icon='arrow_back',on_click= ui.navigate.back)
        with ui.column().classes('w-full items-center'):
            ui.label('Vælg en quiz').classes('text-4xl')

            self.quiz('Daglig Quiz')
            self.quiz('Udfyld det periodiske system')
            self.quiz('Farv det periodiske system')
            self.quiz('Lær navngivning af molekyler')
            

    def quiz(self, text):
        return ui.button(text).classes('w-64 py-4 text-xl')

