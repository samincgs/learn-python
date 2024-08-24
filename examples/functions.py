# number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 31, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''return True for leap years, False for non leap years'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    '''return number of days in that month in that year'''
    if not 1 <= month <= 12:
        return 'Invalid month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2020))
print(is_leap(2017))

print(days_in_month(2020, 3))
print(days_in_month(2017, 2))
print(days_in_month(2000, 2))