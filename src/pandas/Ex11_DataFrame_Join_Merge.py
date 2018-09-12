import pandas as pd
import numpy as np

# data frame 1
d1 = {'Customer_id': pd.Series([1, 2, 3, 4, 5, 6]),
      'Product': pd.Series(['Oven', 'Oven', 'Oven', 'Television', 'Television', 'Television'])}
df1 = pd.DataFrame(d1)

# data frame 2
d2 = {'Customer_id': pd.Series([2, 4, 6]),
      'State': pd.Series(['California', 'California', 'Texas'])}
df2 = pd.DataFrame(d2)

print(df1)
print(df2)

print("\n==== Inner join pandas ====")
# Return only the rows in which the left table have matching keys in the right table
print(pd.merge(df1, df2, on='Customer_id', how='inner'))

print("\n==== Outer join pandas ====")
# Returns all rows from both tables, join records from the left which have matching keys in the right table.
print(pd.merge(df1, df2, on='Customer_id', how='outer'))

print("\n==== Left outer join pandas ====")
# Return all rows from the left table, and any rows with matching keys from the right table.
print(pd.merge(df1, df2, on='Customer_id', how='left'))

print("\n==== Right outer join pandas ====")
#  Return all rows from the right table, and any rows with matching keys from the left table.
print(pd.merge(df1, df2, on='Customer_id', how='right'))

