"""
Welcome to python learning
"""


def divide(x, y):
    return x/y


a = 10
b = 0

try:
    # Code that may raise an exception
    result = divide(a, b)
except ZeroDivisionError:
    # Handle specific exception
    print("Error: Division by zero")
except Exception as e:
    # Handle generic exception
    print("An error occurred:", e)
finally:
    # Finally block typically used for cleanup
    # run code which needs to execute regardless of error or not
    print('Application Gracefully Shutdown!')