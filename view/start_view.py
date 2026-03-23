from nicegui import ui


class MainScreen:
    def __init__(self):
        self.setup_page()

    def setup_page(self):

        with ui.column().classes('w-full h-screen items-center justify-center -mt-32'):
            ui.label('Kemidle').classes('text-8xl')

            with ui.row().classes('gap-4'):
                ui.button('Quiz', on_click=lambda: ui.navigate.to('/quiz')).classes('text-xl py-4 w-64')
                ui.button('Periodisk System', on_click=lambda: ui.navigate.to('/table')).classes('text-xl py-4 w-64')



