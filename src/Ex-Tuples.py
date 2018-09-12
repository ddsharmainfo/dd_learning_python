#A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 'a', 'b' );
tup3 = "a", "b", "c", "d";
tup4 = ();
tup5 = (50);
tup6 = (50,);

print("Tuples 1:", tup1)
print("Tuples 2:", tup2)
print("Tuples 3:", tup3)
print("Tuples 4:", tup4)
print("Tuples 5:", tup5)
print("Tuples 6:", tup6)


#Accessing Values in Tuples
print("\n==== Accessing Values in Tuples ====")
print("tup1[0]: ", tup1[0]);
print("tup3[1:3]: ", tup3[1:3]);


#Updating Tuples
print("\n==== Updating Tuples ====")
#tup1[0] = 100;     #Following action is not valid for tuples

# So let's create a new tuple as follows
tupnew3 = tup1 + tup2;
print(tupnew3);


# Delete Tuple Elements
print("==== Delete Tuple Elements ====")
print("Before deleting tup : ", tup1);
del tup1;
#print("After deleting tup : ", tup1);




