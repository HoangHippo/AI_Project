import os
import speech_recognition as sr
import time
import playsound
from gtts import gTTS
import datetime
import webbrowser as wb


r = sr.Recognizer()


def speak(text):
    print('Thằng đệ: ' + text)

    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def command():
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
    return text        

def welcome():
        #Chao hoi
        speak("Chào bạn, tôi có thể giúp gì cho bạn?") 

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M")
    Hour = datetime.datetime.now().hour
    if Hour >= 6 and Hour<10:
        Session = "sáng"
    elif Hour>=11 and Hour<12:
        Session = "trưa"
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
            text=command().lower()

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

            elif "phim" in text:
                meme =r"D:\A_BaiTap\AI\AI_Project\meme.mp4"
                os.startfile(meme)

            if "google" in text:
                speak("Bạn muốn tìm kiếm gì?")
                search=command().lower()
                url = f"https://google.com/search?q={search}"
                wb.get().open(url)
                speak(f'Here is your {search} on google')

            elif "youtube" in text:
                speak("Bạn muốn tìm kiếm gì?")
                search=command().lower()
                url = f"https://youtube.com/search?q={search}"
                wb.get().open(url)
                speak(f'Here is your {search} on youtube')                
                

                
########### Thêm chức năng ở trên đây 
            elif "tạm biệt"or"bye" in text:
                bot_brain = "Tạm biệt bạn!"
                speak(bot_brain)
                break

            else:
                bot_brain = "Bạn muốn nói gì với tôi?"
                speak(bot_brain)

  