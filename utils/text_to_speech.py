import piper


class TextToSpeech:
    def __init__(self, language="en"):
        self.model = piper.Model(language)

    def speak(self, text):
        audio = self.model.synthesize(text)
        audio.play()
