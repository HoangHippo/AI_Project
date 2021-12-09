import os
import speech_recognition as sr
import time
import playsound
from gtts import gTTS
import datetime


r = sr.Recognizer()


def speak(text):
    print('Thằng đệ: ' + text)

    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def welcome():
        #Chao hoi
        speak("Chào bạn, tôi có thể giúp gì cho bạn?") 

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M")
    Hour = datetime.datetime.now().hour
    if Hour >= 6 and Hour<12:
        Session = "sáng"
    elif Hour>=12 and Hour<18:
        Session = "chiều"
    elif Hour>=18 and Hour<24:
        Session = "tối"
    speak("Bây giờ là " + Time + " " + Session)

def get_day():
    Day = datetime.datetime.now().strftime("%d/%m/%Y")
    speak("Hôm nay là ngày " + Day)

if __name__  =="__main__":
    welcome()      

    while True:
        with sr.Microphone() as source:
            # Lay giong noi
            audio_data = r.record(source, duration=5)
            print("Đang xử lý...", end= "\r")
            time.sleep (2)
            # Chuyen doi giong noi sang text
            try:
                text = r.recognize_google(audio_data, language="vi")
            except:
                text = ""
            print("Tôi: " + text)

            if text == "":
                bot_brain = "Tôi đang nghe đây"
                speak(bot_brain)

            elif "Xin chào" in text:
                bot_brain = "Chào bạn, bạn khỏe không"
                speak(bot_brain)

            elif"mấy giờ" in text:
                get_time()

            elif"ngày bao nhiêu" in text:
                get_day()

            elif "tạm biệt" in text:
                bot_brain = "Tạm biệt bạn!"
                speak(bot_brain)
                break

            else:
                bot_brain = "Bạn muốn nói gì với tôi?"
                speak(bot_brain)

  