from datetime import date, datetime

todaysdate = date.today()
todaysdatetime = datetime.today()
# we print the date and run the code. default format is YYYY-MM-DD
print("Default Formated Date is: ", todaysdate)
print("Default Formated Date Time is: ", todaysdatetime)

# Print individual day/month/year
print("Today's Year is: ", todaysdate.year)
print("Today's Month is: ", todaysdate.month)
print("Today's Date is: ", todaysdate.day)
print("Formated Date is: ", f'{date.today():%Y-%m-%d}')
print("Formated Date Time is: ", f'{datetime.today():%Y-%m-%d}')

today = todaysdate.replace(day=1)
print(today)

today = todaysdate.replace(year=2020, month=6, day=1)
print(today)

today = todaysdatetime.replace(minute=59, hour=23, second=59, year=2020, month=6, day=1)
print(today)