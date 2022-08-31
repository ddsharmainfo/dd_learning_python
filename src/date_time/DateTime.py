from datetime import date
from datetime import time
from datetime import datetime
from datetime import *


def main():
    print("==== DATE OBJECTS ====")
    # create an instance of the date object
    today = date.today()
    # we print the date and run the code. default format is YYYY-MM-DD
    print("Default Formated Date is: ", today)

    # Print individual day/month/year
    print("Today's date is: ", today.year,today.month,today.day)
    print("Today's date is: ", today.year,"/", today.month,"/", today.day)
    print("Today's date is: ", today.year,"_",today.month,"_",today.day)

    # weekday number - Monday tp Sunday is 0 to 6
    print("Today's weekday is: ", today.weekday())

    print("======================")
    test = "TEST"
    today1 = date.today()
    #print(test+today1)

    print("==== DATETIME OBJECTS ====")
    #It gives date along with time in hours, minutes, seconds and milliseconds.
    todayNow = datetime.now()
    print("Time date and time now is: ", todayNow)

    #With "DATETIME OBJECT", you can also call time class
    time = datetime.time(datetime.now())
    print("Current time is: ", time)

    #We will apply our weekday indexer to our weekday's arrayList to know which day is today
    wd = date.weekday(today)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Today is day",wd, "which is", days[wd])


    print("\n==== Time Delta or previous date and convert date into string ====")
    todaydate = today + timedelta(days=0)
    print("Today's Date is:", todaydate)
    prevdate = today+ timedelta(days = -1)
    print("Yesterday's Date was:", prevdate)

    date_string1 = f'{today:%Y-%m-%d}'
    date_string2 = f'{todaydate:%Y-%m-%d}'
    date_string3 = f'{prevdate:%Y-%m-%d}'

    print("test1_" + date_string1)
    print("test2_" + date_string2)
    print("test3_" + date_string3)

if __name__ == "__main__":
    main()
