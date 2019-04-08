import os
import os.path
import xlrd
import xlsxwriter
import sys
file_name = sys.argv[2]
merged_file_name = file_name + ".xlsx"
dest_book = xlsxwriter.Workbook(merged_file_name)
dest_sheet_1 = dest_book.add_worksheet()
dest_row = 1
temp = 0
path = sys.argv[1]
for root,dirs,files in os.walk(path):
    files = [ _ for _ in files if _.endswith('.xlsx') ]
    files.sort()
    for xlsfile in files:
        print ("File in mentioned folder is: " + xlsfile)
        temp_book = xlrd.open_workbook(os.path.join(root,xlsfile))
        temp_sheet = temp_book.sheet_by_index(0)
        if temp == 0:
            for col_index in range(temp_sheet.ncols):
                str = temp_sheet.cell_value(0, col_index)
                dest_sheet_1.write(0, col_index, str)
            temp = temp + 1
        for row_index in range(1, temp_sheet.nrows):
            for col_index in range(temp_sheet.ncols):
                str = temp_sheet.cell_value(row_index, col_index)
                dest_sheet_1.write(dest_row, col_index, str)
            dest_row = dest_row + 1
dest_book.close()
book = xlrd.open_workbook(merged_file_name)
sheet = book.sheet_by_index(0)
print ("number of rows in destination file are: ", sheet.nrows)
print ("number of columns in destination file are: ", sheet.ncols)
