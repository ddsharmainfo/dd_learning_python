import pandas as pd
import numpy
from datetime import date

# Assign spreadsheet filename to `file`
inpath = '../inputs/excel_multi_sheet.xlsx'
outpath_dash1 = '../outputs/sales_dash1.csv'
outpath_dash2 = '../outputs/sales_dash2.csv'

"""
df = pd.read_excel(inpath)
print("\n==== Print DF ====")
print("\n", df)

print("\n==== Print Head ====")
print(df.head(2))

print("\n==== Row selection From Location ====")
#print(df.loc[0,:])
#print(df.loc[[0,1,2],:])
print(df.loc[0:2,:])

print("\n==== Column selection From Location ====")
print(df.loc[:, ['transactionId','itemValue']])
print('\n')
print(df.loc[0:2, 'transactionId':'itemId'])
print('\n')
print(df.head(3).drop(['itemValue', 'itemId'], axis=1))



print("\n==== Column selection From iLocation ====")
print(df.iloc[:, 0:4])
print('\n')
print(df.iloc[0:3, :])
print('\n')
print(df.iloc[0:2, 0:4])

"""

print("============================================================================")
df_sheet3 = pd.read_excel(inpath, header=None, skiprows=1, sheet_name='Sheet3')       #header=[0, 7]
#print("\n df_sheet3 dimention is = ", df_sheet3.shape)
#print(df_sheet3)

# Slice the DataFrame rows based on index
df_sheet3_1 = pd.DataFrame(df_sheet3, index=[0,1,2,3], columns=[0,1])
#print("\n df_sheet3_1 dimention is = ", df_sheet3_1.shape)
#print(df_sheet3_1)

# Slice the DataFrame rows and result will be DataFrame
df_sheet3_2 = pd.DataFrame(df_sheet3[6:16], columns=[0,1,2,3,4,5,6,7,8,9,10,11,12])
#print("\n df_sheet3_2 dimention is = ", df_sheet3_2.shape)
#print("\n df_sheet3_2 length is = ", len(df_sheet3_2))
#print(df_sheet3_2)

print("\n==== Print the location ====")
# Select column	df[col]	and result will be eries
#print(df_sheet3_1[0])
# Select row by label	df.loc[label] and result will be eries
#print(df_sheet3_1.loc[0])
# Select row by integer location	df.iloc[loc] and result will be eries
#print(df_sheet3_1.iloc[2])
#print(df_sheet3_1.iloc[2,1])

# Find the month value based on "As of" available in sheet
print("==== Month value based on As of available in sheet =", df_sheet3.iloc[5,14])
"""print("==== Find the value by if loop ====")
if(df_sheet3.iloc[5,14] == 'May'):
    print("Sheet is having data of May Month")
    YTD_budgeted_revenue = df_sheet3_2.iloc[0,5]
    YTD_budgeted_revenue_cumul = df_sheet3_2.iloc[1, 5]
    print(YTD_budgeted_revenue)
    print(YTD_budgeted_revenue_cumul)
else:
    print("No month value found in sheet")
"""

month = df_sheet3.iloc[5,14]
if(month == 'Jan'):
    month = 1
if(month == 'Feb'):
    month = 2
if(month == 'Mar'):
    month = 3
if(month == 'Apr'):
    month = 4
if(month == 'May'):
    month = 5
if(month == 'Jun'):
    month = 6
if(month == 'Jul'):
    month = 7
if(month == 'Aug'):
    month = 8
if(month == 'Sep'):
    month = 9
if(month == 'Oct'):
    month = 10
if(month == 'Nov'):
    month = 11
if(month == 'Dec'):
    month = 12

print("==== Find the value by for loop ====")
#print(len(df_sheet3_2))
#month = 5
for row in range (0, 1):
    print("==== From for loop and value of i is = ", row)
    row1 = df_sheet3_2.iloc[0, month]
    row2 = df_sheet3_2.iloc[1, month]
    row3 = df_sheet3_2.iloc[2, month]
    row4 = df_sheet3_2.iloc[3, month]
    row5 = df_sheet3_2.iloc[4, month]
    row6 = df_sheet3_2.iloc[5, month]
    row7 = df_sheet3_2.iloc[6, month]
    row8 = df_sheet3_2.iloc[7, month]
    row9 = df_sheet3_2.iloc[8, month]
    row10 = df_sheet3_2.iloc[9, month]
    df_sheet3_3 = pd.DataFrame(df_sheet3[6:16], columns=[0, month])

#print(row1*1000)
#print(row2)
#print(row3)
#print(row4)
#print(row5)
#print(row6)
#print(row7)
#print(row8)
#print(row9)
#print(row10)

df_sheet3_1['unit'] = pd.Series('£', index=df_sheet3_1.index)
df_sheet3_1['date'] = pd.Series(date.today(), index=df_sheet3_1.index)
df_sheet3_3['unit'] = pd.Series('£', index=df_sheet3_3.index)
df_sheet3_3['date'] = pd.Series(date.today(), index=df_sheet3_3.index)
df_sheet3_4 = df_sheet3_3.assign(new_month_value=lambda x:x[month]* 1000)

df_sheet3_4 = pd.DataFrame(df_sheet3_4, index=[7,9,11,13,15], columns=[0, 'new_month_value', 'unit', 'date'])

#print(df_sheet3_1)
#print(df_sheet3_3)
print(df_sheet3_4)

#df_final = df_sheet3_1.append(df_sheet3_3

#df_final = [df_sheet3_1, df_sheet3_3]
#print(df_final)

#df_merge = pd.concat([df_sheet3_1, df_sheet3_3])
#df_merge1 = pd.DataFrame(df_merge[0:15], columns=[0,1])
#df_merge2 = pd.DataFrame(df_merge[0:15], columns=[0,5])
#df_merge_final = pd.merge(df_merge1, df_merge2[[5]], on=0, how='right')
#result = result['currency'] = 'test'
#print(df_merge)
#print(df_merge1)
#print(df_merge2)
#print(df_merge_final)

#df_sheet3_1.to_csv(outpath_dash1)
df_sheet3_4.to_csv(outpath_dash2)
