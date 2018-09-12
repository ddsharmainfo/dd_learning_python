from datetime import date
from datetime import time
from datetime import datetime

def parser(x):
	return datetime.strptime(x, '%d/%m/%Y %H:%M')

#print("Date From parser method is: ", parser('30/07/18 17:05'))

now = datetime.now()
print("Date & Time Now Is: ", now)

# 2000-11-30 00:00:00
struct_time = datetime.strptime("30-Nov-18 11:25", "%d-%b-%y %H:%M")
print("returned tuple 1: %s " % struct_time)

struct_time2 = datetime.strptime("30 11 18 11:25", "%d %m %y %H:%M")
print("returned tuple 2: %s " % struct_time2)

struct_time3 = datetime.strptime("30/11/18 11:25", "%d/%m/%y %H:%M")
print("returned tuple 3: %s " % struct_time3)

# 28-11-2017 11:00
struct_time4 = datetime.strptime("30/11/2018 11:25", "%d/%m/%Y %H:%M")
print("returned tuple 4: %s " % struct_time4)

