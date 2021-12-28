from text_to_speak import speak

import urllib.request as urllib2
import json
import os
import ctypes

def change_wallpaper():
    api_key = 'K2yC2smNNshFB1cAMgsQu_O1LyDiWmZ9sVBg9LhpEEY'
    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.

    #Hoang#
    # urllib2.urlretrieve(photo, "D:/EPU/Images/a.png")
    # image=os.path.join("D:/EPU/Images/a.png")

    #Ha#
    urllib2.urlretrieve(photo, "D:/Pictures/ThayAnhNen/a.png")
    image=os.path.join("D:/Pictures/ThayAnhNen/a.png")

    #Dat#

    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')