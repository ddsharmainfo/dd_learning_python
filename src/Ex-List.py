print("\n==== Python list examples ====")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

# Accessing Values in Lists
print("list: ", list)          # Prints complete list
print("list[0]: ", list[0])       # Prints first element of the list
print("list[1:3]:", list[1:3])     # Prints elements starting from 2nd till 4th
print("list[2:]: ", list[2:])      # Prints elements starting from 3rd element
print("print list twice: ", tinylist * 2)  # Prints list two times
print("concatenated lists: ", list + tinylist) # Prints concatenated lists

# Updating Lists
print("\nUpdating Lists: ")
list1 = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ")
print(list1[2])
list1[2] = 2001;
print("New value available at index 2 : ")
print(list1[2])

# Delete List Elements
print("\nDelete List Elements:")
list2 = ['physics', 'chemistry', 1997, 2000];
print("befire delete list is: ", list2)
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

# Iteration
print("\nIteration of list: ")
for x in [1, 2, 3]: print(x)

# Indexing, Slicing, and Matrixes
print("\nIndexing, Slicing, and Matrixes:")
L = ['spam0', 'Spam1', 'SPAM2']
print("Actual List is: ", L)
print("Offsets start at zero, so L[2] is: ", L[2])
print("Negative: count from the right, so L[-2] is: ", L[-2])
print("Slicing fetches sections, L[1:]: ", L[1:])

# Built-in List Functions & Methods
print("\nBuilt-in List Functions & Methods: ")
#list3, list4 = [123, 'xyz'], [456, 'abc']
#print(cmp(list1, list2))
#print(cmp(list2, list1))
#list3 = list2 + [786];
#print(cmp(list2, list3))
#print("Compare list: ", cmp(list3, list4))

# Methods with Description
print("\nMethods with Description:")
list5 = [123, 'xyz', 'zara', 'abc', 123];
print("Actual List: ", list5)
list5.append(2009);
list5.append("test");
print("List after append: ", list5)

print("Count for 123 : ", list5.count(123))
print("Count for zara : ", list5.count('zara'))

bList = [2009, 'manni'];
list5.extend(bList)
print("Extended List : ", list5)














