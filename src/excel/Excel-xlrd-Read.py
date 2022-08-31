import xlrd as xl

inpath = '../inputs/sales_multisheet_excel.xlsx'

# Load in the workbook
wb = xl.open_workbook(inpath)
sheet3 = wb.sheet_by_name('Sheet3')

#print(sheet3.nrows)
#print(sheet3.ncols)
print(sheet3.cell_value(0, 0), sheet3.cell_value(0, 1))
print(sheet3.cell_value(1, 0), sheet3.cell_value(1, 1))

#for col in range(sheet3.ncols):
 #   print(sheet3.cell_value(0, col))

print("==== Name and Total from header ====")
for row in range(1, 5):  #sheet3.nrows
    print("Name = ", sheet3.cell_value(row, 0), "|| Total is =", sheet3.cell_value(row, 1))

print("\n==== Values from month ====")
for row in range(7, 17):  #sheet3.nrows
    print("Name = ", sheet3.cell_value(row, 0), "|| Total is =", sheet3.cell_value(row, 1))