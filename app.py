from nicegui import ui

from model.model import Model
from model.quiz_model import QuizModel
from view.table import TablePage
from view.quiz_layout import QuizLayout
import view.start_view as start
import view.quiz_menu as qm
import view.table_quiz as qt
from controller.table_controller import TableController
from controller.quiz_layout_controller import QuizLayoutController
from controller.tquiz_controller import TQuizController

# Make buttons not all caps
ui.button.default_props('no-caps')
# Make latex fields use the same font as everything else
ui.add_head_html('''
<style>
math {
    font-family: inherit;
}
</style>
''', shared=True)


model = Model()
quiz_model = QuizModel()
# Each view will have its own controller for example the quiz page and the periodic table geoguessr
table_controller = TableController(model)
quiz_layout_controller = QuizLayoutController(quiz_model)
tquiz_controller = TQuizController(model)
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
@ui.page('/quiz/daily')
def quiz_layout_page():
    quiz_layout = QuizLayout()
    quiz_layout_controller.set_view(quiz_layout)
@ui.page('/tquiz')
def tquiz_page():
    tquiz = qt.TableQuiz(model.layout, tquiz_controller)
    tquiz_controller.set_view(tquiz)

ui.run()
