"""
Welcome to python learning
"""

error_code = -1

try:
    # try some code
    dicts = dict(blue=0, green=1, red=2)
    error_code = dicts['red1']
except Exception as e:
    # handle exception
    print('error accessing dictionary, key does not exist:', e)
else:
    print('colorCode', dicts)
finally:
    # run code which needs to execute regardless of error or not
    print('grace full shutdown')
