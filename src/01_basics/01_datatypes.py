"""
Welcome to python learning
"""


print('\n===== String Data Type =====')
var1 = "DD Sharma"
print(type(var1))
print(var1)


print('\n===== Integer Data Type =====')
var2 = 1
print(type(var2))
print(var2)


print('\n===== Float Data Type =====')
var3 = 1.0
print(type(var3))
print(var3)


print('\n===== Boolean Data Type =====')
# a special type of variable stores just True/False values. This is called a boolean variable.
var4 = True
var5 = False
print(type(var4))
print(var4)
print(type(var5))
print(var5)


# List of Other Data types
print('\n===== Data Types =====')
print('string', type(''))
print('string', type('DD Sharma'))
print('0', type(1))
print('1.0', type(1.0))
print('True', type(True))
print('[]', type([]))
print('{}', type({}))
print('{0}', type({0}))
print('()', type(()))
print('lambda', type(lambda a: 1))
print(None, type(None))


def func():
    pass


class Sample:
    pass


print('func', type(func))
print('Class()', type(Sample()))