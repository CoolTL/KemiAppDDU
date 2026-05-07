import json
import os
from paths import resource_path

class QuizModel:
    """ This model gets the data from the quiz databases so it can be presented in the view """
    def __init__(self):
        pass

    def get_json(self, name):
        # Here we need to make sure the path to the JSON is correct
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, name)
        with open(json_path, 'r') as file:
            return json.load(file)

    def prepare_daily_question(self):
        """ This method returns a question to be used by the controller """
        return self.get_json(resource_path("model/quiz1.json"))['questions']["0"]

    def get_quiz_pack(self):
        return self.get_json(resource_path("model/molecule.json"))['molecule']
