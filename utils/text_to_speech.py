import piper


class TextToSpeech:
    def __init__(self, language="en"):
        self.model = piper.load_model(language)

    def speak(self, text):
        audio = self.model.synthesize(text)
        audio.play()
