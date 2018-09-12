import pandas as pd

# Assign spreadsheet filename to `file`
inpath = '../../inputs/excel_multi_header.xlsx'
outpath = '../../outputs/excel_multi_header.csv'

pd_df = pd.read_excel(inpath, header=None, skiprows=2, sheetname='Production Losses Breakdown')
print(type(pd_df))
print(pd_df.index.name)
print(pd_df.columns.values)
print(pd_df)

print("==== January DataFrame ====")
df = pd.DataFrame(pd_df[0:11], columns=[0,1,2,3,4,5,6])
print(df)

print("==== February DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[8,9,10,11,12,13,14])
print(df)

print("==== March DataFrame ====")
df = pd.DataFrame(pd_df[0:7], columns=[16,17,18,19,20,21,22])
print(df)

print("==== April DataFrame ====")
df = pd.DataFrame(pd_df[0:6], columns=[24,25,26,27,28,29,30])
print(df)

print("==== May DataFrame ====")
df = pd.DataFrame(pd_df[0:6], columns=[32,33,34,35,36,37,38])
print(df)

print("==== June DataFrame ====")
df = pd.DataFrame(pd_df[0:5], columns=[40,41,42,43,44,45,46])
print(df)

print("==== July DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[48,49,50,51,52,53,54])
print(df)

print("==== Aug DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[56,57,58,59,60,61,62])
print(df)

print("==== Sep DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[64,65,66,67,68,69,70])
print(df)

print("==== Oct DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[72,73,74,75,76,77,78])
print(df)

print("==== Nov DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[80,81,82,83,84,85,86])
print(df)

print("==== Dec DataFrame ====")
df = pd.DataFrame(pd_df[0:9], columns=[88,89,90,91,92,93,94])
print(df)

print("==== YTD DataFrame ====")
df = pd.DataFrame(pd_df[0:21], columns=[96,97,98,99,100,101,102])
print(df)

#df.to_csv(outpath)
