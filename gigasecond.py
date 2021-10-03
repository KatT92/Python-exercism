from datetime import datetime, time, date

y = datetime.now()
print(y)


def add(x):
    total_seconds = int(x) % 60
    total_minutes = int(x / 60) % 60
    total_hours = int(x / 3600) % 24
    total_days = int(x / 86400) % 30
    total_month = int(x / (86400*30)) % 12
    total_years = int(x / 31536000)
    year = y.year + total_years
    month = y.month + total_month
    day = y.day + total_days
    hour = y.hour + total_hours + 1
    minute = y.minute + total_minutes + 1 - 60
    second = y.second + total_seconds

    if second >= 60:
        second = second - 60
        minute = minute + 1
    if minute >= 60:
        minute = minute - 60
        hour = hour + 1
    if hour >= 24:
        hour = hour - 24
        month = month + 1
    if month >= 12:
        month = month - 12
        year = year + 1

    return datetime(year, month, day, hour, minute, second)

print(add(1000000000))







