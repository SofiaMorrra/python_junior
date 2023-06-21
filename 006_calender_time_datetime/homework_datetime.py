import datetime


# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
new_sample1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
print(new_sample1)

sample2 = '14:20 10/12/22'  # YY/MM/DD
new_sample2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(new_sample2)

sample3 = 'Tuesday, September 24, 2019'
new_sample3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(new_sample3)

sample4 = '01.01.1970 - 00:00:01'
new_sample4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(new_sample4)


# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
print(today - datetime.timedelta(days=1))
print(today)

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
new_date = datetime.datetime.fromtimestamp(some_day)
print(new_date.strftime('%d.%m.%Y'))


def date_from_timestamp(timestamp):
    new_date = datetime.datetime.fromtimestamp(timestamp)
    return new_date.strftime('%d.%m.%Y')


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)


def two_weeks_before(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    date -= datetime.timedelta(weeks=2)
    return datetime.datetime.timestamp(date)


print(two_weeks_before(some_day))
