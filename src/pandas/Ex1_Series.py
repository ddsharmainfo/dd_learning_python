import pandas as pd
import numpy as np

print("==== Example Create an Empty Series ====")
s = pd.Series()
print(s)

print("\n==== Create a series from array without index ====")
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data)
print(s)

print("\n==== Create a series from array with index ====")
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data,index=[1000,1001,1002,1003,1004,1005])
print(s)

print("\n==== Create a series from Dictionary ====")
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

print("\n==== Create a series from Scalar value ====")
s = pd.Series(7, index=[0, 1, 2, 3])
print(s)

print("\n==================== Accessing data from series with position ====================")
data = np.array(['a','b','c','d','e','f'])
s = pd.Series(data)

print("\n==== retrieve the first element ====")
print(s[0])

print("\n==== retrieve first three elements ====")
print(s[:3])

print("\n==== retrieve last three elements ====")
print(s[-3:])

print("\n==================== Accessing data from series with Labels or index ====================")
data = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
s = pd.Series(data, index=[100, 101, 102, 103, 104, 105])

print("\n==== Retrieve a single element using index label ====")
print(s[102])

print("\n==== Retrieve multiple elements using index labels ====")
print(s[[102,103,104]])



