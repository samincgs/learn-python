# PYTZ MODULE
# use when timezones are needed
import pytz, datetime


dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

# timezone aware
dt_now = datetime.datetime.now(tz=pytz.UTC)

print(dt_now)

# convert to a different timezone
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))

print(dt_mtn)