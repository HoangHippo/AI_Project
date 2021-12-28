from gtts import gTTS
import playsound
import os

def speak(text):
    print("Thằng đệ: " + text)

    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'

    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)