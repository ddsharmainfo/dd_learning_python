"""
Welcome to python learning
"""


list1 = ['A', 'B', 'C', 'D', 'E']

# for in loop
print('\nfor in loop:')
for item in list1:
    print(item)

# classical range based for loop
print('\n===== range(n) =====')
for i in range(5):
    # range with single param n: starts from 0 to n-1, incrementing 1
    print(i)

print('\n===== range(m,n) =====')
for i in range(3, 5):
    # range with param m,n: starts from m to n-1, incrementing 1
    print(i)

print('\n===== range(m,n,o) =====')
for i in range(3, 5, 2):
    # range with param m,n,o: starts from m to n-1, incrementing o
    print(i)
