#!/usr/bin/python

if True:
   print("True")
else:
    print("False")

if True:
   print("Answer")
   print("True")
else:
   print("Answer")
   print("False")

# Multi-Line Statements
item_one = 0
item_two = 1
item_three = 2
total = item_one +\
        item_two +\
        item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# Waiting for the User
#raw_input("\n\nPress the enter key to exit.")

# Multiple Statements on a Single Line
import sys; x = 'foo'; sys.stdout.write(x + '\n')



print("\n==== Python Strings ====")
str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string






print("\n==== Python Tuples ====")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

print("\n==== Python Dictionary ====")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values





