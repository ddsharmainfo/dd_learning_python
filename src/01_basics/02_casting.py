"""
Welcome to python learning

Type Conversion/casting: The process of converting one data type to another data type is called type conversion/casting.

In Python, we can perform two types of type conversion.
1. Implicit Type Conversion - Here, Python automatically converts one data type to another in order to avoid data loss.
2. Explicit Type Conversion - Here, the user can convert the data type of variable to the required data type by using
the in-built functions like int(), float(), str(), etc.
"""


print('\n===== Implicit type casting')
price = 100
discount = price * 0.25
print('The data type of variable price is', type(price))
print('The data type of variable discount is', type(discount))
"""
As we can see, the data type of 'discount' is float as Python is
implicitly converting the lower data type to a higher data type to avoid data loss.
"""

discounted_price = price - discount

# Running below line will give TypeError: can only concatenate str (not "float") to str
# print('The discounted price is ' + discounted_price)
print('\n===== Explicit type casting')
print('The data type of variable discounted_price is', type(discounted_price))
print('The discounted price is ' + str(discounted_price))


# casting with int
a = int(10)
b = int('10')
# c = int('10.10') # error, invalid literal for int() with base 10: '1.0', use float
d = int(10.10)
print('\ncasting with int()')
print(a, b, d)


# casting with float
a = float(10)
b = float('10')
c = float('10.10')
d = float(10.10)
print('\ncasting with float()')
print(a, b, c, d)


# casting with str
a = str(10)
b = str(10.10)
c = str("10.10")
d = str(True)
e = str([1, 2, 3])
f = str({'1': 'green', '2': 'blue', '3': 'green'})
print('\ncasting with str()')
print(a, b, c, d, e, f)


# Returns the boolean value of the specified object
print('\ncasting with bool()')
print('bool', bool(False))  # False
print('bool', bool(0))      # False
print('bool', bool(None))   # False
print('bool', bool(True))   # True
print('bool', bool(1))      # True
print('bool', bool('0'))    # True