class QuizLayoutController:
    def __init__(self, model):
        self.model = model
        self.view = None
        # The question
        self.question = None

    def set_view(self, view):
        """ Set the view variable """
        self.view = view
        self.setup_question()

    def get_question(self):
        """ Gets the question from model """
        self.question = self.model.prepare_daily_question()

    def setup_question(self):
        """ Put question text into the view """
        self.get_question()
        answer_options = self.question['answers']
        question_text = self.question['question']
        image_path = self.question['image']
        self.view.place_question_text(question_text, answer_options, image_path)

    def get_explanation(self):
        """ This gets run if you picked the wrong answer """
        explanation_text = self.question['explanation']
        self.view.write_explanation(explanation_text)

    def check_answer(self, answer):
        """ This checks if the answer selected is correct or not """
        correct_answer = self.question['answers'][self.question['correct']]
        if answer == correct_answer:
            self.view.write_explanation("Korrekt!")
        else:
            self.get_explanation()
        self.view.buttons_enabled(False)
