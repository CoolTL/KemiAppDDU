from nicegui import ui

from model.model import Model
from view.table import MainPage
import view.start_view as start
from controller.controller import Controller

model = Model()
@ui.page('/table')
def table():
    table = MainPage(model.layout)
@ui.page('/')
def main_page():
    main = start.MainScreen()
# Well implement controller later
#controller = Controller(model, view)

ui.run()
