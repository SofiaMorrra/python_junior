import datetime

t = datetime.time(14, 13, 43, 100)

print(t)

dt = datetime.datetime(2023, 6, 16, 14, 25, 17)
print(dt)

today = datetime.datetime.now()
print(today)
print(today.date())
print(today.time())

print(today - dt)
tdelta = datetime.timedelta(days=7, hours=10)
print(today - tdelta)

print(today.strftime('%a %p'))
someday = 'November 24, 2034 17:45'
newdt = datetime.datetime.strptime(someday, '%B %d, %Y %H:%M')
print(newdt)
