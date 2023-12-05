import pandas as pd

# Creating a dictionary to store data
data = {'Name': ['Tony', 'Steve', 'Bruce', 'Peter'],
        'Age': [35, 70, 45, 20]}

# Creating DataFrame
df = pd.DataFrame(data)

# Print the dataframe
print(df)

list_all = df.values.tolist()
list_name = df['Name'].values.tolist()

# Pandas to list
#print('\n', new_list)

# Pandas to list
#print('\n', df['Name'].values.tolist())

print('\n', tuple(list_all))

print('\n', list_name)

print('\n', tuple(list_name))