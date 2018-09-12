import pandas as pd
import numpy as np

# Create a DataFrame
d = {
    'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
             'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
    'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],
    'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]}

df = pd.DataFrame(d, columns=['Name', 'Age', 'Score'])

print(df)

print("\n==== Drop a row by condition ====")
df2 = df[df.Name != 'Alisa']
print(df2)

print("\n==== Drop an observation or row ====")
df2 = df.drop([1,3,5])
print(df2)

print("\n==== Drop a row by index ====")
df2 = df.drop(df.index[2])
print(df2)

print("\n==== Drop bottom 3 rows ====")
df2 = df[:-3]
print(df2)
