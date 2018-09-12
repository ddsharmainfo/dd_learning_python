import pandas as pd

d = {'Quarters': ['Quarter1','Quarter2','Quarter3','Quarter4'],
     'Revenue':[23400344.567,54363744.678,56789117.456,4132454.987]}

df = pd.DataFrame(d)
print(df)

print("\n==== Round off the column values to two decimal places in python pandas ====")
pd.options.display.float_format = '{:.2f}'.format
print(df)

print("\n==== Format with commas and round off to two decimal places in python pandas: ====")
pd.options.display.float_format = '{:,.2f}'.format
print(df)

print("\n==== Format with commas and Dollar sign with two decimal places in python pandas ====")
pd.options.display.float_format = '${:,.2f}'.format
print(df)

print("\n==== Format with Scientific notation in python pandas ====")
pd.options.display.float_format = '{:.2E}'.format
print(df)
