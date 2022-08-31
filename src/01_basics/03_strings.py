"""
Welcome to python learning
"""

# string concatenation
first_name = 'DD'
last_name = 'Sharma'
print('Hi ' + first_name + ' ' + last_name)

# string and other data type variable concatenation
# print(first_name + ' is ' + 30 + ' years old') # error, TypeError: cannot concatenate 'str' and 'int' objects
print(first_name + ' is ' + str(30) + ' years old')

# string format
user = 'Hi, I am {0} {1} and I am {2} years old'
# int to string casting is not needed when passing argument to format
print(user.format(first_name, last_name, 28))

# char at index
print('Hello World'[4])

# substring
print('Hello World'[2:4])

# len
print(len('Hello World'))

# upper case
print('Hello World'.upper())

# lower case
print('Hello World'.lower())

# strip
print('   Hello World   '.strip())

# split
tokens = 'Hello:world'.split(':')
print(tokens)