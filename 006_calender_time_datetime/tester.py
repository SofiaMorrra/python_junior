import calendar

# print(calendar.month(2023, 6, w=5, l=2))

# print(calendar.calendar(2023, c=5, m=4))

# print(calendar.weekday(2023, 6, 16))

print(calendar.isleap(2021))
print(calendar.leapdays(2020, 2029))

x = calendar.HTMLCalendar()
print(x.formatyear(2023))

