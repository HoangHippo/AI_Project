from speak_to_text import command
from text_to_speak import speak

import smtplib


def email():
    speak('Bạn gửi email cho ai nhỉ')
    recipient = command()
    if 'Peter Parker' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = command()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('1fast0mail1@gmail.com', 'asdfghjkl123456@')
        mail.sendmail('1fast0mail1@gmail.com',
                      'alexnguyen123229@gmail.com', content.encode('utf-8'))
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
