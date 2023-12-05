import pandas as pd

# Creating a dictionary to store data
data = {'Name': ['Tony', 'Steve', 'Bruce', 'Peter'],
        'Age': [35, 70, 45, 20]}

# Creating DataFrame
df = pd.DataFrame(data)

# Print the dataframe
print(df)

# Pandas to list
print('\n', df.values.tolist())

# Pandas to list
print('\n', df['Name'].values.tolist())

