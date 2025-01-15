from piper import PiperVoice
import sys


class TextToSpeech:
    def __init__(self, language="en"):
        self.model = PiperVoice.load("data/en_US-amy-low.onnx")

    def speak(self, text):
        audio_stream = self.model.synthesize_stream_raw(text)
        for audio_bytes in audio_stream:
            sys.stdout.buffer.write(audio_bytes)
            sys.stdout.buffer.flush()
