from controller.quiz_layout_controller import QuizLayoutController

class QuizPackController(QuizLayoutController):
    """ This class is responsible for quiz packs and inherits from the daily quiz controller """
    def __init__(self, model):
        super().__init__(model)
        self.current_question = 0

    def get_question(self):
        self.pack = self.model.get_quiz_pack()
        self.next_question()

    def select_next_question(self):
        self.current_question += 1

    def next_question(self):
        self.question = self.pack[f"{self.current_question}"]
        answer_options = self.question['answers']
        question_text = self.question['question']
        image_path = self.question['image']
        self.view.place_question_text(question_text, answer_options, image_path)
        self.view.buttons_enabled(True)
        
    def check_answer(self, answer):
        """ This checks if the answer selected is correct or not, it varies from the parent in that it also enables/disables the next button """
        super().check_answer(answer)
        self.current_question += 1
        self.view.next_button.set_enabled(True)
        self.view.buttons_enabled(False)
