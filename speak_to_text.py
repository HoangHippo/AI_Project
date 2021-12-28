import time
import speech_recognition as sr
r = sr.Recognizer()


def command():
    with sr.Microphone() as source:
        # Lay giong noi
        audio_data = r.record(source, duration=5)

        print("Nghe...", end="\r")
        time.sleep(3)

        # Chuyen doi giong noi sang text
        try:
            text = r.recognize_google(audio_data, language="vi")
        except:
            text = "...        "
        print("Tôi: " + text)
    return text
