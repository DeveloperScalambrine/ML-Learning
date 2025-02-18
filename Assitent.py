import gTTS
import speech_recognition as sr
import os

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
