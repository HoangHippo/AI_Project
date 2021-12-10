import os
import speech_recognition as sr
import time
import playsound
from gtts import gTTS
import datetime
import webbrowser as wb
import re
import requests
import json
r = sr.Recognizer()


def speak(text):
    print("Thằng đệ: " + text)

    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'

    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def command():
    with sr.Microphone() as source:
        # Lay giong noi
        audio_data = r.record(source, duration=5)

        print("Đang nghe...", end="\r")
        time.sleep(1)

        # Chuyen doi giong noi sang text
        try:
            text = r.recognize_google(audio_data, language="vi")
        except:
            text = "...        "
        print("Tôi: " + text)
    return text


def welcome():
    # Chao hoi
    speak("Chào bạn, tôi có thể giúp gì cho bạn?")


def get_time():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("Bây giờ là " + Time)


def get_day():
    Day = datetime.datetime.now().strftime("%d/%m/%Y")
    speak("Hôm nay là ngày " + Day)


def open_app(text):
    if "chrome" in text:
        speak("Mở google chrome")
        # Hà
        # os.system("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.exe")

        # Đạt
        os.system(
            "C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
        # mở ứng dụng dẽ ko tắt chương tr, tắt ứng dụng thì mới tát ct

    elif "zalo" in text:
        speak("Đang mở ứng dụng zalo")
        # Hà
        # os.system("C:\\Users\\admin\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")
        # Đạt
        os.system("C:\\Users\\Admin\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")
    else:
        speak("Ứng dụng của bạn có vẻ chưa được cài đặt!")


def open_web(text):
    text = text.replace("trang", "")
    print(text)
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        wb.open(url)
        speak("Trang web bạn yêu cầu đã được mở")
        # sau khi mở web thì chương trình sẽ dừng lại đến khi bạn nhập "a"
        if input("Hãy nhập a để tiếp tục: ") == "a":
            pass
        return True
    else:
        return False


def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = command()   # lưu tên thành phố vào biến city
    if not city:    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
        pass
    # api_key lấy trên open weather map
    api_key = "540c4efbf623055574abfc7d8772cab4"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + \
        "&units=metric"    # tìm kiếm thông tin thời thời tiết của thành phố
    # truy cập đường dẫn lấy dữ liệu thời tiết
    response = requests.get(call_url)  # gửi yêu cầu lấy dữ liệu
    data = response.json()    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    if data["cod"] != "404":     # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
        # lấy dữ liệu của key main
        city_res = data["main"]
        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        speak("Không tìm thấy địa chỉ của bạn")


if __name__ == "__main__":
    welcome()

    while True:
        text = command().lower()

        if text == "":
            bot_brain = "Tôi đang nghe đây"
            speak(bot_brain)

        elif "xin chào" in text:
            bot_brain = "Chào bạn, bạn khỏe không"
            speak(bot_brain)

        elif"mấy giờ" in text:
            get_time()

        elif"ngày" in text:
            get_day()

        elif "phim" in text:
            meme = r"E:\AI_Project\meme.mp4"
            os.startfile(meme)

        elif "google" in text:
            speak("Bạn muốn tìm kiếm gì?")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả {search} trên google')

        elif "youtube" in text:
            speak("Bạn muốn tìm kiếm gì?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả {search} trên youtube')

        elif "mở" in text:
            open_app(text)

        elif "thời tiết" in text:
            current_weather()


# Thêm chức năng ở trên đây
        elif "tạm biệt" in text:
            bot_brain = "Tạm biệt bạn!"
            speak(bot_brain)
            break

        else:
            bot_brain = "Bạn muốn nói gì với tôi?"
            speak(bot_brain)
