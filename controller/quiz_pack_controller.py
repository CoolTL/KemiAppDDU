from controller.quiz_layout_controller import QuizLayoutController
from paths import resource_path

class QuizPackController(QuizLayoutController):
    """ This class is responsible for quiz packs and inherits from the daily quiz controller """
    def __init__(self, model):
        super().__init__(model)
        self.current_question = 0

    def get_question(self):
        self.pack = self.model.get_quiz_pack()
        self.next_question()


    def next_question(self):
        self.question = self.pack[f"{self.current_question}"]
        answer_options = self.question['answers']
        question_text = self.question['question']
        image_path = resource_path(self.question['image'])
        self.view.place_question_text(question_text, answer_options, image_path)
        self.view.buttons_enabled(True)
        
    def check_answer(self, answer):
        """ This checks if the answer selected is correct or not """
        correct_answer = self.question['answers'][self.question['correct']]
        if answer == correct_answer:
            self.view.write_explanation("Korrekt!")
        else:
            self.get_explanation()
        self.view.buttons_enabled(False)
        self.current_question += 1
        if str(self.current_question) not in self.pack:
            self.view.completed()
            self.current_question = 0
        self.view.next_button.set_enabled(True)
        self.view.buttons_enabled(False)

