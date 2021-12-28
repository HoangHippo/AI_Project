from text_to_speak import speak

import os


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
