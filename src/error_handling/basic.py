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
    print("Error From Specific Exception: Division by zero")
except FileNotFoundError as fnf_error:
    # Handle specific exception
    print('File Not Found Error: ', fnf_error)
except RuntimeError as runtime_error:
    # Handle specific exception
    print('Run Time Error: ', runtime_error)
except Exception as e:
    # Handle generic exception
    print("An error occurred:", e)
else:
    # No exception? Run this code
    print('No exception? Run this code!')
finally:
    # Finally block typically used for cleanup
    # run code which needs to execute regardless of error or not
    print('Application Gracefully Shutdown!')