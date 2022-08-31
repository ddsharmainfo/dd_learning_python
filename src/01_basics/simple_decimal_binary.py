"""
Welcome to python learning
"""


def decimal_to_binary(d):
    binary = []
    while d/2 != 0:
        d, r = divmod(d, 2)
        binary.append(str(r))
    binary.reverse()
    return int(''.join(binary))
    

def binary_to_decimal(b):
    a = [s for s in str(b)]
    a.reverse()
    d = 0
    for i in range(len(a)):
        d += 2**i * int(a[i])
    return d


print(decimal_to_binary(49))      # 110001
print(binary_to_decimal(110001))  # 49
print(binary_to_decimal(decimal_to_binary(49)) == 49)   # True