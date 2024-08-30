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

# my birthday
bday = datetime.date(2024, 4, 23)

till_bday = today - bday

# day seven days forward
# print(today + tdelta)

# day seven days before
# print(today - tdelta)

# print(till_bday.days)
# print(d)
# print(today)
# print(today.month)
# print(today.year)
# print(weekday)

#  work with time hours, minutes, seconds
t = datetime.time(9, 30, 45, 100000)
# print(t)

# combine date and time
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

tdelta = datetime.timedelta(days=7)

# # print the date
# print(dt.date())

# # print the time
# print(dt.time())

# # print the year
# print(dt.year)

# # add on timedelta
# print(dt + tdelta)

# different ways of calling datetime for todays date
dt_today = datetime.datetime.today() # current local datetime with a timezone of none
dt_now = datetime.datetime.now() # gives us an option to pass the timezone
dt_utcnow = datetime.datetime.utcnow()


print(dt_today)
print(dt_now)
print(dt_utcnow)

# strftime - Convert Datetime to a String
# strptime - Convert string to a Datetime