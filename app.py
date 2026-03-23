from nicegui import ui

from model.model import Model
from view.table import TablePage
import view.start_view as start
import view.quiz_menu as qm
from controller.controller import Controller

ui.button.default_props('no-caps')

model = Model()
@ui.page('/table')
def table():
    table = TablePage(model.layout)
@ui.page('/')
def main_page():
    main = start.MainScreen()
@ui.page('/quiz')
def quiz():
    quiz = qm.QuizScreen()
# Well implement controller later
#controller = Controller(model, view)

ui.run()
