import gTTS
import speech_recognition as sr
import os
import wikipedia
import webbrowser

text_convert = "Ola mundo em maquina de aprendizagem"
def speak(text_convert):
    tts = gTTS(text=text_convert, lang='pt-br')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

r = sr.Recognizer()
def listening():
     with sr.Microphone() as source:
        print("speak now...")
        audio = r.listen(source)
    try:
         text_convert = r.recognize_google(audio, lang='pt-br')
        print("Você disse: " + text_convert)
        return text_convert
    except sr.UnknownValueError:
        print("I don´t understand what you say.")
        return ""
    except sr.RequestError as e:
        print("Unable to connect to speech recognition service: " + str(e))
        return ""

text_open_wikipedia = "Alexa open wikipedia please"
def open_wikipedia(text_open_wikipedia):
    try:
        result = wikipedia.summary(text_open_wikipedia)
        speak(result)
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything about this on Wikipedia.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("I found several pages about this. Be more specific.")

text_open_wikipedia = "Alexa open youtube please"
def open_youtube():
    webbrowser.open("https://www.youtube.com/")
