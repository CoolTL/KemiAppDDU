from nicegui import ui

from model.model import Model
from view.table import TablePage
import view.start_view as start
import view.quiz_menu as qm
import view.table_quiz as qt
from controller.table_controller import TableController


ui.button.default_props('no-caps')

ui.add_head_html('''
<style>
math {
    font-family: inherit;
}
</style>
''', shared=True)


model = Model()
# Each view will have its own controller for example the quiz page and the periodic table geoguessr
table_controller = TableController(model)
@ui.page('/table')
def table_page():
    table = TablePage(model.layout, table_controller)
    table_controller.set_view(table)
@ui.page('/')
def main_page():
    main = start.MainScreen()
@ui.page('/quiz')
def quiz():
    quiz = qm.QuizScreen()
@ui.page('/tquiz')
def tquiz():
    tqiz = qt.TableQuiz(model.layout, table_controller)

ui.run()
