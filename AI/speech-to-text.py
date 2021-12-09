import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # Lay giong noi
    audio_data = r.record(source, duration=5)
    print("Đang nghe...")
    # Chuyen doi giong noi sang text
    try:
        text = r.recognize_google(audio_data, language="vi")
    except:
        text = "Không hiểu!"
    print(text)