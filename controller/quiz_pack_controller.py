from controller.quiz_layout_controller import QuizLayoutController

class QuizPackController(QuizLayoutController):
    """ This class is responsible for quiz packs and inherits from the daily quiz controller """
    def __init__(self, model):
        super().__init__(model)

    def get_question(self):
        self.question = self.model.get_quiz_pack()
        self.next_question("1")

    def setup_question(self):
        self.get_question()

    def next_question(self, index):
        print(self.question[index])
