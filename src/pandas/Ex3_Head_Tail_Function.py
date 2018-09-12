import pandas as pd
from sklearn import datasets

print("\n==== Loading the iris data set from sklearn ====")
iris = pd.DataFrame(datasets.load_iris().data)
print(iris)

print("\n==== head function in python ====")
print(iris.head())

print("\n==== head function in python with arguments ====")
print(iris.head(8))

print("\n==== Tail function in python ====")
print(iris.tail())

print("\n==== tail function in python with arguments ====")
print(iris.tail(8))

