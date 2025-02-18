import gTTS

text_convert = "Ola mundo em maquina de aprendizagem"

def speak(text_convert):
    tts = gTTS(text=text_convert, lang='pt-br')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")
