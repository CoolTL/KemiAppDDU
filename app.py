from nicegui import ui

from model.model import Model
from model.quiz_model import QuizModel
from view.table import TablePage
from view.quiz_layout import QuizLayout
from view.quiz_pack_view import QuizPackView
import view.start_view as start
import view.quiz_menu as qm
import view.table_quiz as qt
import view.colour_quiz as ct
import view.writing_quiz as wt
from controller.table_controller import TableController
from controller.quiz_layout_controller import QuizLayoutController
from controller.quiz_pack_controller import QuizPackController
from controller.tquiz_controller import TQuizController
from controller.cquiz_controller import CQuizController
from controller.wquiz_controller import WQuizController

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
daily_quiz_controller = QuizLayoutController(quiz_model)
molecule_quiz_controller = QuizPackController(quiz_model)
tquiz_controller = TQuizController(model)
cquiz_controller = CQuizController(model)
wquiz_controller = WQuizController(model)
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
@ui.page('/daily')
def daily_quiz_page():
    daily_quiz = QuizLayout(daily_quiz_controller)
    daily_quiz_controller.set_view(daily_quiz)
@ui.page('/molecule')
def molecule_quiz_page():
    molecule_quiz = QuizPackView(molecule_quiz_controller)
    molecule_quiz_controller.set_view(molecule_quiz)
@ui.page('/tquiz')
def tquiz_page():
    tquiz = qt.TableQuiz(model.layout, tquiz_controller)
    tquiz_controller.set_view(tquiz)
@ui.page('/cquiz')
def cquiz_page():
    cquiz = ct.ColourQuiz(model.layout, cquiz_controller)
    cquiz_controller.set_view(cquiz)
@ui.page('/wquiz')
def wquiz_page():
    wquiz = wt.WritingQuiz(model.layout, wquiz_controller)
    wquiz_controller.set_view(wquiz)

ui.run()
