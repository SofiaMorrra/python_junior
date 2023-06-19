import datetime

d = datetime.date(2023, 6, 10)
print(d)
print(type(d))

today = datetime.date.today()
print(today)
print(today - d)
print(type(today - d))

print(today.year)

print(today.weekday())  # ot 0 do 6 den nedeli
print(today.isoweekday())  # ot 1 do 7 dninedeli

tdelta = datetime.timedelta(days=7)
print(today + tdelta)

bday = datetime.date(2024, 3, 16)
till_bday = bday - today
print(till_bday.days)
print(till_bday.total_seconds())

print(datetime.datetime.now().timestamp())

