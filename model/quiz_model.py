import json
import os

class QuizModel:
    """ This model gets the data from the quiz databases so it can be presented in the view """
    def __init__(self):
        # Here we need to make sure the path to the JSON is correct
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, 'quiz1.json')
        with open(json_path, 'r') as file:
            self.json_database = json.load(file)

    def prepare_question(self):
        """ This method returns a question to be used by the controller """
        return self.json_database['questions']['q1']
