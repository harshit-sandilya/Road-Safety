from utils.speech_to_text import SpeechToText
from utils.text_to_speech import TextToSpeech
from core.Handler import Handler
import os

print("Welcome to the Question Answering System")

language = input("Enter the language you want to use (en/hi): ")
handler = Handler(language)
stt = SpeechToText(language)
tts = TextToSpeech(language)

os.system("cls" if os.name == "nt" else "clear")

while True:
    tts.speak("Please ask your question")
    print("Please ask your question")
    question = stt.start_listening()
    print(f"Question: {question}")
    answer = handler.process_question(question)
    print(f"Answer: {answer}")
    tts.speak(answer)
    tts.speak("Do you have any more questions?")
    print("Do you have any more questions?")
    more_questions = stt.start_listening()
    if more_questions.lower() == "no":
        break
