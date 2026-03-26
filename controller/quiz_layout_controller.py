class QuizLayoutController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        """ Set the view variable """
        self.view = view
        self.setup_question()

    def setup_question(self):
        """ Put question text into the view """
        question = self.model.prepare_question()
        answer_options = question['answers']
        question_text = question['question']
        self.view.place_question_text(question_text, answer_options)

    def get_explanation(self):
        """ This gets run if you picked the wrong answer """
        explanation_text = self.model.prepare_question()['explanation']
        self.view.write_explanation(explanation_text)

    def check_answer(self, answer):
        """ This checks if the answer selected is correct or not """
        correct_answer = self.model.correct_answer()
        if answer == correct_answer:
            self.view.write_explanation("Correct!")
        else:
            self.get_explanation()
        self.view.buttons_enabled(False)
