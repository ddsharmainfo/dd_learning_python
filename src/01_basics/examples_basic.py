#!/usr/bin/python

"""
Welcome to python learning
"""

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
# raw_input("\n\nPress the enter key to exit.")

# Multiple Statements on a Single Line
import sys; x = 'foo'; sys.stdout.write(x + '\n')

print("\n==== Python Strings ====")
var_str = 'Hello World!'
print(var_str)          # Prints complete string
print(var_str[0])       # Prints first character of the string
print(var_str[2:5])     # Prints characters starting from 3rd to 5th
print(var_str[2:])      # Prints string starting from 3rd character
print(var_str * 2)      # Prints string two times
print(var_str + "TEST")  # Prints concatenated string


print("\n==== Python Tuples ====")
tuples = ('abcd', 786 , 2.23, 'john', 70.2)
tiny_tuples = (123, 'john')
print (tuples)           # Prints complete list
print (tuples[0])        # Prints first element of the list
print (tuples[1:3])      # Prints elements starting from 2nd till 3rd
print (tuples[2:])       # Prints elements starting from 3rd element
print (tiny_tuples * 2)   # Prints list two times
print (tuples + tinytuple) # Prints concatenated lists

print("\n==== Python Dictionary ====")
dicts = {}
dicts['one'] = "This is one"
dicts[2] = "This is two"
tiny_dict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dicts['one'])       # Prints value for 'one' key
print(dicts[2])           # Prints value for 2 key
print(tiny_dict)          # Prints complete dictionary
print(tiny_dict.keys())   # Prints all the keys
print(tiny_dict.values()) # Prints all the values





