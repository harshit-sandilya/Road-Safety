from vosk import Model, KaldiRecognizer
import queue
import sys
import sounddevice as sd


class SpeechToText:
    def __init__(self, language="en"):
        language = language + "-in"
        self.model = Model(lang=language)
        self.q = queue.Queue()
        self.samplerate = 16000

    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def start_listening(self):
        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._audio_callback,
            device=None,
        ):
            rec = KaldiRecognizer(self.model, self.samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    return result
