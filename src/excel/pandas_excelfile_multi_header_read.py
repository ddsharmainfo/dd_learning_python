import pandas as pd

# Assign spreadsheet filename to `file`
inpath = '../../inputs/excel_multi_header.xlsx'

# Load spreadsheet
pd_excel = pd.ExcelFile(inpath)
print(type(pd_excel))

# Print the sheet names
print(pd_excel.sheet_names)

print("==== Load a sheet into a DataFrame by name:")
pd_df = pd_excel.parse('Sheet1', skiprows=1, header=0)
print(type(pd_df))
print(pd_df.index.name)
print("Length of DF:", len(pd_df))
print(pd_df.columns.values)
#print(pd_df)

pd_df = pd.DataFrame(pd_df[0:12], columns=['Type', 'Oil Loss (bbls)', 'Gas Loss (MMscf)', 'Oil Loss (boe)', 'Gas Loss (boe)', 'Total Loss (boe)', 'Loss %'])



print(pd_df)



"""
pd_df2 = pd.DataFrame(pd_df, columns=[('February', 'Type'),('February', 'Oil Loss (bbls)')])
print(type(pd_df2))
print("Length of DF:", len(pd_df2))
print(pd_df2)


print("==== Parse 2 ====")
pd_df_p2 = pd_excel.parse('Production Losses Breakdown', header=[0,1], skiprows=2)
print(pd_df_p2)


#pd_df_p2 = pd.DataFrame(pd_df_p2, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], columns=[0,1,2,3,4,5,6])
#print(pd_df_p2)

#

#pd_df = pd.DataFrame(pd_df[0:4], columns=[0, 1])
#df = pd.DataFrame(df_s3.set_index('Name'), columns = ['name'])
#df = pd.DataFrame(df_s3.set_index('Name'), columns = ['Name', 'Total', 'As Of', '5 + 7'])
#df = pd.DataFrame(df_s3.set_index('Name of Months'), columns = ['Jan', 'Feb'])
#df = pd.DataFrame(df_s3, index=range(4), columns=['Name','Total'])
#print(df)

"""




# Find the month value based on "As of" available in sheet
def find_as_of_month(df_sheet):
    month = df_sheet.iloc[5, 14]
    print("==== Month value based on As of available in sheet is:", month)
    if (month == 'Jan' or month == 'January'):
        month = 1
    if (month == 'Feb' or month == 'February'):
        month = 2
    if (month == 'Mar' or month == 'March'):
        month = 3
    if (month == 'Apr' or month == 'April'):
        month = 4
    if (month == 'May' or month == 'May'):
        month = 5
    if (month == 'Jun' or month == 'June'):
        month = 6
    if (month == 'Jul' or month == 'July'):
        month = 7
    if (month == 'Aug' or month == 'Augest'):
        month = 8
    if (month == 'Sep' or month == 'Septenber'):
        month = 9
    if (month == 'Oct' or month == 'October'):
        month = 10
    if (month == 'Nov' or month == 'November'):
        month = 11
    if (month == 'Dec' or month == 'December'):
        month = 12
    return month