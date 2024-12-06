from .AnsweringEngine import AnswerEngine
from .Translator import Translator


class Handler:
    def __init__(self, language):
        self.answer_engine = AnswerEngine()
        if language == "hi":
            self.translator = Translator()

    def process_question(self, question):
        if hasattr(self, "translator"):
            question = self.translator.translate_hi(question)
        answer = self.answer_engine.get_answer(question)
        if hasattr(self, "translator"):
            answer = self.translator.translate_en(answer)
        return answer
