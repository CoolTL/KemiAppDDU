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
        answer_options = self.model.prepare_question()['answers']
        self.view.place_question_text(answer_options)

    def get_explanation(self):
        """ This gets run after you press an answer, either we display a correct message, or an explanation """
        explanation_text = self.model.prepare_question()['explanation']
        self.view.write_explanation(explanation_text)
