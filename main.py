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
    if language != "hi":
        tts.speak("Please ask your question")
        print("Please ask your question")
    else:
        print(handler.translator.translate_en("Please ask your question"))
    question = stt.start_listening()
    print(f"Question: {question}")
    answer = handler.process_question(question)
    print(f"Answer: {answer}")
    if language != "hi":
        tts.speak(answer)
        tts.speak("Do you have any more questions?")
        print("Do you have any more questions?")
    else:
        print(handler.translator.translate_en(("Do you have any more questions?"))
    more_questions = stt.start_listening()
    if language == "hi":
        more_questions = handler.translator.translate_hi(more_questions)
    if more_questions.lower() == "no":
        break
