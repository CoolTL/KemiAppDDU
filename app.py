from nicegui import ui

from model.model import Model
from view.table import MainPage
from controller.controller import Controller

model = Model()
@ui.page('/table')
def table():
    table = MainPage(model.layout)
# Well implement controller later
#controller = Controller(model, view)

ui.run()
