from datetime import date
from datetime import time
from datetime import datetime

def main():
    print("==== Date & Time Format ====")
    #Times and dates can be formatted using a set of predefined string Control codes
    now = datetime.now()

    print(" Date & Time Now Is: ", now)

    #[(%y/%Y – Year), (%a/%A- weekday), (%b/%B- month), (%d - day of month)]
    print("Use of y = ",now.strftime("%y"))
    print("Use of Y = ",now.strftime("%Y"))
    print("Use of a = ",now.strftime("%a"))
    print("Use of A = ",now.strftime("%A"))
    print("Use of b = ",now.strftime("%b"))
    print("Use of B = ",now.strftime("%B"))

    print("Use of m = ",now.strftime("%m"))
    #print("Use of M = ",now.strftime("%M"))
    print("Use of d = ",now.strftime("%d"))
    # MM/DD/YY
    print("Use of D = ",now.strftime("%D"))

    #%c - local date and time, %x-local's date, %X- local's time
    print("\n==== %c - local date and time, %x-local's date, %X- local's time ====")
    print("%c - local date and time = ", now.strftime("%c"))
    print("%x-local's date          = ", now.strftime("%x"))
    print("%X- local's time         = ", now.strftime("%X"))

    ##### Time Formatting ####
    print("\n==== %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM ====")
    print("12-Hour:Minute:Second:AM = ",now.strftime("%I:%M:%S %p"))
    print("12-Hour:Minute AM/PM     = ", now.strftime("%I:%M %p"))
    print("24-Hour:Minute           = ", now.strftime("%H:%M"))


if __name__ == "__main__":
    main()
