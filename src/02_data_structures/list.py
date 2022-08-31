"""
Welcome to python learning
"""


# List is iterable
print("\n===== Iterate Lists =====")
for x in [1, 2, 3]:
    print(x)


tiny_list = [123, 'john']
for item in tiny_list:
    print(item)


list1 = ['abcd', 786, 2.23, 'john', 70.2]

# Accessing Values in Lists
print("\n===== Accessing Lists =====")
print("list: ", list1)          # Prints complete list
print("list[0]: ", list1[0])       # Prints first element of the list
print("list[1:3]:", list1[1:3])     # Prints elements starting from 2nd till 4th
print("list[2:]: ", list1[2:])      # Prints elements starting from 3rd element
print("print list twice: ", tiny_list * 2)  # Prints list two times
print("concatenated lists: ", list1 + tiny_list)  # Prints concatenated lists


# Updating Lists
print("\n===== Updating List ===== ")
list2 = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ", list2[2])
list2[2] = 2001;
print("New value available at index 2 : ", list2[2])


# Delete List Elements
print("\n===== Delete elements from list  =====")
print("before delete list is: ", list2)

del list2[2];
print("After deleting value at index 2 : ", list2)

# Basic List Operations
print("\nLength of the list is: ", len([1, 2, 3]))

# Concatenation
print("\nConcatenation of list: ", [1, 2, 3] + [4, 5, 6])

# Repetition
print("\nRepetition of list:", ['Hi!'] * 4)

# Membership
print("\nMembership in list: ", 3 in [1, 2, 3])
print("\nMembership in list: ", 5 in [1, 2, 3])


# Indexing, Slicing, and Matrices
print("\n===== Indexing, Slicing, and Matrices =====")
list3 = ['item0', 'item1', 'item2']
print("Actual List is: ", list3)
print("Offsets start at zero, so list3[2] is: ", list3[2])
print("Negative: count from the right, so list3[-2] is: ", list3[-2])
print("Slicing fetches sections, list3[1:]: ", list3[1:])