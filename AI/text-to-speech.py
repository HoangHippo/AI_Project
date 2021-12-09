import os
import speech_recognition as sr
import time
import playsound
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    
    tts.save(filename)
    playsound.playsound(filename)

speak("Xin chào bạn tên gì?")    