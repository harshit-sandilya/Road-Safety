from piper import PiperVoice
import sys
import simpleaudio as sa


class TextToSpeech:
    def __init__(self, language="en"):
        self.model = PiperVoice.load("data/en_US-amy-low.onnx")

    def speak(self, text):
        audio_stream = self.model.synthesize_stream_raw(text)
        audio_data = b"".join(audio_stream)
        wave_obj = sa.WaveObject(
            audio_data, num_channels=1, bytes_per_sample=2, sample_rate=22050
        )
        play_obj = wave_obj.play()
        play_obj.wait_done()
