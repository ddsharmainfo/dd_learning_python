"""
Welcome to python learning
    
Following are the dictionary methods:
    all
    any
    append
    clear
    copy
    count
    extend
    index
    len
    remove
    reverse
    sort
"""

# Built-in List Functions & Methods

print('\n===== Initialize a list =====')
# Initialize a list of size 1
list_nums = [1]
print('\nList size 1\n', list_nums)

# Initialize a list of size 5 with each element as 2
list_nums = [2] * 5
print('\nList size 5\n', list_nums)

# Initialise a 2D list of 5, 5 size with each element as 3
list_nums2d = [[3] * 5] * 5
print('\n2D list size 5, 5: \n', list_nums2d)

# Initialise a 2D list 5, 5 size with numbers in each list from 0-4
list_nums2d = [[i for i in range(5)] for _ in range(5)]
print('\n\n2D list size 5, 5, 0-5\n', list_nums2d)

# Same as above
list_nums2d = [[i for i in range(5)]] * 5
print('\n\n2D Array size 5, 5, 0-4\n', list_nums2d)

# Generate a list with numbers from 0-4 repeating 5 times
list_nums2d = [i for i in range(5)] * 5
print('\n\nArray size 5 repeating 0-4\n', list_nums2d)


print('\n===== Append items in list =====')
list_items = ['red', 'green', 'blue']
print(list_items)

# Adds new item to the last of the colors
list_items.append('white')
print(list_items)

print('\n===== Concatenates items in list =====')
# Concatenates the list provided in argument
list_items.extend(['cyan', 'magenta', 'yellow'])
print(list_items)

# Returns the first index of the found item
print('\n===== Returns the first index of the found item =====')
print(list_items.index('cyan'))
# Scans the colors from index 4
print(list_items.index('cyan', 4))
# Scans the colors from index 0 to 4
print(list_items.index('cyan', 0, 5))
# print(colors.index('some color')) # ValueError: 'some color' is not in colors

# Removes item with by value
print('\n===== Removes item with by value =====')
list_items.remove('white')
print(list_items)

print('\n===== Make copy of list =====')
# Makes a copy of list
list_copy = list_items.copy()
print(list_items)
print(list_copy)

# Reverses the list
print('\n===== Reverses the list =====')
list_copy.reverse()
print(list_copy)

# Sorts the list
print('\n===== sort the list =====')
list_copy.sort()
print(list_copy)

# Empties the list
print('\n===== Empty the list =====')
print(list_copy)
list_copy.clear()
print(list_copy)

# Prints length of list
print('\nLength of the list is: ', len(list_items))

# Count the number of items in list
print('\n===== Count the number of items in list =====')
print(list_items.count('yellow'))

# Sorting with Key
print('\n===== Sort =====')
list_items = ['aa', 'a', 'aaaa', 'aaa']
list_items.sort(key=len)
print(list_items)

print('\n===== Sort reverse =====')
list_items.sort(key=len, reverse=True)   # reverse indicates to reverse the order decided by key
print(list_items)


# Pop, pops the element at given index
print('\n===== Pop elements =====')
list_items = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
print(list_items)
# Removes first item
list_items.pop(0)
print(list_items)
# Removes last item
list_items.pop(-1)
print(list_items)
list_items.pop()
# No index, removes last time
print(list_items)