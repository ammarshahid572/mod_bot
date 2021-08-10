from gtts import gTTS
import os

def Speak(text, filename='late.mp3'):
    speech=gTTS(text)
    speech.save(filename)
    #os.system('omxplayer -o local '+filename)

Speak('You have no questions, please ask me to sleep.')
