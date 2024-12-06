from sentence_transformers import SentenceTransformer, util
import pandas as pd
from string import punctuation


class AnswerEngine:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        data = pd.read_csv("data/Intents.csv")
        self.questions = self.model.encode(
            self.clean_text(data["Questions"].values.tolist()), convert_to_tensor=True
        )
        self.answers = data["Answers"].values.tolist()

    def get_answer(self, question):
        question = self.clean_text(question)
        question_embedding = self.model.encode(question, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(question_embedding, self.questions)[0]
        max_score = cos_scores.max()
        if max_score > 0.2:
            index = cos_scores.argmax()
            return self.answers[index]
        else:
            return "Sorry, I don't know the answer to that question."

    def clean_text(self, text):
        if isinstance(text, list):
            return [self.clean_text(t) for t in text]
        else:
            text = "".join([c for c in text if c not in punctuation])
            return text.lower()
