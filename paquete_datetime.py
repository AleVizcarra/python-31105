from datetime import datetime

dt = datetime.now()

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)


dt2 = datetime(2021, 9, 8, 22, 13)
print(dt2)

dt2 = dt2.replace(2033)
print(dt2)

print(dt2.strftime('%A %d %B %Y %I:%M'))