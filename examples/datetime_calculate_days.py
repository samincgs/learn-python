import datetime
import calendar

# write a script to calculate the number of days, weeks or months to reach specific goals

# pay off a credit card
balance = 5000
interest_rate = 13 * 0.01
monthly_payment = 500

today = datetime.date.today() # todays date
days_in_current_month = calendar.monthrange(today.year, today.month)[1] # first day of the next month

days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
