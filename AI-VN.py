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
import wikipedia
from time import strftime
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
    speak("Tôi có thể giúp gì cho bạn?")


def help_me():
    speak("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị ngày, giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở video 
    8. Định nghĩa từ điển trên Wikipedia
    9. Đọc báo hôm nay """)


def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))


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

        # Hoang
        #  os.system(
        #     "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe")

        # mở ứng dụng dẽ ko tắt chương tr, tắt ứng dụng thì mới tát ct

    elif "zalo" in text:
        speak("Đang mở ứng dụng zalo")
        # Hà
        # os.system("C:\\Users\\admin\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")

        # Đạt
        os.system("C:\\Users\\Admin\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")

        # Hoàng
        # os.system("C:\\Users\\Admin\\AppData\\Local\\Programs\\Zalo\\Zalo.exe")
    else:
        speak("Ứng dụng của bạn có vẻ chưa được cài đặt!")


def open_web(text):
    speak("Bạn muốn tìm kiếm trang web nào?")
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        wb.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
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


def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = command()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = command()
            if "có" not in ans:
                break
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")


def read_news():
    speak("Bạn muốn đọc báo về gì")

    queue = command()
    params = {
        'apiKey': '6ede27befd2e4a2cb187b4e55a4a43c9',
        "q": queue,
    }
    api_result = requests.get(
        'https://newsapi.org/v2/top-headlines?country=us&apiKey=6ede27befd2e4a2cb187b4e55a4a43c9', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            wb.open(result['url'])


if __name__ == "__main__":
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = command()
    if name:
        speak("Chào bạn {}".format(name))
        welcome()
        help_me()

    while True:
        text = command().lower()

        if text == "":
            bot_brain = "Tôi đang nghe đây"
            speak(bot_brain)

        elif "chào trợ lý ảo" in text:
            hello(name)

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

        elif 'news' in text:
            speak("Bạn muốn đọc tin gì?")
            news = wb.open_new_tab("https://vnexpress.net/")
            speak('Hãy cập nhật tin tức mỗi ngày nhé!')
            time.sleep(6)

        elif 'wikipedia' in text:
            tell_me_about()

        elif 'tin tức' in text:
            read_news()

        elif "mở" in text:
            open_app(text)

        elif "thời tiết" in text:
            current_weather()

        elif "trang Web" in text:
            open_web(text)


# Thêm chức năng ở trên đây
        elif "tạm biệt" in text:
            bot_brain = "Tạm biệt bạn!"
            speak(bot_brain)
            break

        else:
            bot_brain = "Bạn muốn nói gì với tôi?"
            speak(bot_brain)
