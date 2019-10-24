import openpyxl 
import os

os.chdir('C:\\Users\\52038474\\AppData\\Local\\Programs\\Python\\Python37\\Excel')
wb=openpyxl.load_workbook('AmitY.xlsx')
a=type(wb) ##type of workbook

sheet=wb.get_sheet_names()
print(sheet) ## get sheet names in workbook
sheet['A1'].value