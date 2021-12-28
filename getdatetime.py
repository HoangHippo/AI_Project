import datetime


def get_time():
    Time = datetime.datetime.now().strftime("%I:%M")
    return Time


def get_day():
    Day = datetime.datetime.now().strftime("%d/%m/%Y")
    return Day

dayOfWeek = ["Thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "chủ nhật"]

# print(dayOfWeek[today])

def getDayOfWeek():
    today = datetime.datetime.today().weekday()
    return dayOfWeek[today]