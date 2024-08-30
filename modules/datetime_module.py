import datetime

# naive datetimes -> dont have enough information for stuff like timezones or daylight savings but way easier to work with
# aware datetimes -> have enough information for timezones and daylight savings and leapyears, harder to work with

# naive datetimes
d = datetime.date(2016, 7, 24)

# todays date
today = datetime.date.today()

# get the day of the week
weekday = today.weekday() # Monday 0 Sunday 6
weekday = today.isoweekday() # Monday 1 Sunday 7

# timedeltas the difference between two dates and times
tdelta = datetime.timedelta(days=7)

# day seven days forward
print(today + tdelta)

# day seven days before
print(today - tdelta)


# print(d)
# print(today)
# print(today.month)
# print(today.year)
# print(weekday)