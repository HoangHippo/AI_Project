import os
import ctypes
import speech_recognition as sr
import time
import playsound
from gtts import gTTS
import datetime
import webbrowser as wb
import re
import requests
import json
import wikipedia
import smtplib
import urllib.request as urllib2
from time import strftime
from youtube_search import YoutubeSearch
r = sr.Recognizer()


from speak_to_text import command
from text_to_speak import speak
import getdatetime
import openvideo
import search
import weather
import openapp
import sendmail
import wallpaper
import translate


def welcome():
    # Chao hoi
    speak("Tôi có thể giúp gì cho bạn?")


def help_me():
    speak("""Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:""")
    print(""" 
    1. Chào hỏi
    2. Hiển thị ngày, giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở video 
    8. Định nghĩa từ điển trên Wikipedia
    9. Đọc báo hôm nay
    10. Nghe nhạc trên Youtube
    11. Thay đổi hình nền """)


def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))

if __name__ == "__main__":
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = command()
    if name:
        speak("Chào bạn {}".format(name))
        welcome()

    while True:
        text = command().lower()

        if text == "":
            bot_brain = "Tôi đang nghe đây"
            speak(bot_brain)

        elif "chào" in text:
            hello(name)

        elif "giúp" in text:
            help_me()

        elif"mấy giờ" in text:
            result = getdatetime.get_time()
            speak("Bây giờ là " + result)

        elif"ngày" in text:
            result = getdatetime.get_day()
            speak("Hôm nay là ngày " + result)

        elif"thứ mấy" in text:
            result = getdatetime.getDayOfWeek()
            speak("Hôm nay là "+result)    

        elif "phim" in text:
            openvideo.open_video();

        elif "google" in text:
            speak("Bạn muốn tìm kiếm gì?")
            find = command().lower()
            search.google(find);
            speak(f'Đây là kết quả {find} trên google')

        elif "youtube" in text:
            speak("Bạn muốn tìm kiếm gì?")
            find = command().lower()
            search.youtube(find);
            speak(f'Đây là kết quả {find} trên youtube')

        elif 'tin tức' in text:
            news = wb.open_new_tab("https://vnexpress.net/")
            speak('Hãy cập nhật tin tức mỗi ngày nhé!')
            time.sleep(6)

        elif 'wikipedia' in text:
            search.wikipedia()

        elif 'tìm bài báo' in text:
            search.news()

        elif "mở" in text:
            openapp.open_app(text)

        elif "thời tiết" in text:
            weather.current_weather()

        elif "gửi mail" in text:
            sendmail.email()

        elif "nghe nhạc" in text:
            search.play_song()

        elif "thay đổi hình nền" in text:
            wallpaper.change_wallpaper()

        elif "trang Web" in text:
            search.open_web(text)

        elif "dịch" in text:
            speak("Bạn muốn dịch từ gì?")
            a = command().lower()
            speak("Bạn chọn ngôn ngữ gì?")
            lang = command().lower()
            result = translate.lang_translate(a, lang)
            if result=="None": speak("Ngôn ngữ này không có!")
            else:             speak(result)



# Thêm chức năng ở trên đây
        elif "tạm biệt" in text:
            bot_brain = "Tạm biệt bạn!"
            speak(bot_brain)
            break

        else:
            bot_brain = "Bạn muốn nói gì với tôi?"
            speak(bot_brain)
