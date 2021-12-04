import xlrd
workbook=xlrd.open_workbook("D:\\Selenium_Training\\TestData.xls")
sheet=workbook.sheet_by_name("Test")
rowcount=sheet.nrows
columncount=sheet.ncols
for curr_row in range(1,rowcount):
    uname=sheet.cell_value(curr_row,0)
    upass=sheet.cell_value(curr_row,1)
    print(uname + " " + upass)