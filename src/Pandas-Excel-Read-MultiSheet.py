import pandas as pd

#pd_df = pd.read_excel('C:/Local_Petrofac/media/pf-spark-shared/pf-data-model/ranking_and_risk_score_inputs/LPC_Train_A_Threshold.xlsx')
#print(pd_df)

# Assign spreadsheet filename to `file`
inpath = '../inputs/excel_multi_sheet.xlsx'

# Load spreadsheet
pd_excel = pd.ExcelFile(inpath)

# Print the sheet names
print(pd_excel.sheet_names)

# Load a sheet into a DataFrame by name:
df_s1 = pd_excel.parse('Sheet1')
df_s2 = pd_excel.parse('Sheet2')
df_s3 = pd_excel.parse('Sheet3')

print("\n==== Data from sheet 1 ====")
#print("Length of DF:", len(df_s1))
#print("", df_s1)
print("\n==== Data from sheet 2 ====")
#print("Length of DF:", len(df_s2))
#print("", df_s2)
print("\n==== Data from sheet 3 ====")
#print("Length of DF:", len(df_s3))
#print("", df_s3)


#df = pd.DataFrame(df_s3.set_index('Name'), columns = ['name'])
#df = pd.DataFrame(df_s3.set_index('Name'), columns = ['Name', 'Total', 'As Of', '5 + 7'])
#df = pd.DataFrame(df_s3.set_index('Name of Months'), columns = ['Jan', 'Feb'])
#df = pd.DataFrame(df_s3, index=range(4), columns=['Name','Total'])
#print(df)

#df2 = pd.DataFrame(df_s3, header=[0, 6], index=range(16), columns=['Name','Total', '']) #shift(4)
#print(df2)

#for index, row in df_s2.iterrows():
 #   print(index, row['transactionId'], row['customerId'], row['itemValue'])

#for index, row in df_s3.iterrows():
 #   print(index, row['Name'], row['Total'], row['As of'])

#for key, value in df_s3.iteritems():
 #   print(key,value[0])
"""
print("\n==== Column selection From iLocation ====")
#print(df_s3.iloc[:, 0:4])
print('\n')
print(df_s3.iloc[0:4, 0:2])
print('\n')
print(df_s3.iloc[5:17, 0:4])

print('\n')
df_s3.set_index('Name', inplace=True)
df_s3.index.name = None
print(df_s3.head(17))
"""

print("==== Create DF from for loop ====")
print("Length of sheets is:", len(pd_excel.sheet_names))
for i in range (1, len(pd_excel.sheet_names)+1):
    #print(i)
    #print(pd_excel.sheet_names)
    df1 = pd_excel.parse(pd_excel.sheet_names[0])
    df2 = pd_excel.parse(pd_excel.sheet_names[1])
    df3 = pd_excel.parse(pd_excel.sheet_names[2])

#print(df1)
print("\n")
#print(df2)
print("\n")
print(df3)