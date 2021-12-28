from speak_to_text import command
from text_to_speak import speak

import webbrowser as wb
import requests
import re
import time
from youtube_search import YoutubeSearch

def google(search):
    url = f"https://google.com/search?q={search}"
    wb.get().open(url)

def youtube(search):
    url = f"https://youtube.com/search?q={search}"
    wb.get().open(url)

def news():
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

def wikipedia():
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

def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    mysong = command()
    while True:
        result = YoutubeSearch(mysong, max_results=100).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    wb.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")        