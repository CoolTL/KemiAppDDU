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
        i = 0
        for button in self.view.answer_buttons:
            button.set_text(question['answers'][i])
            i += 1
