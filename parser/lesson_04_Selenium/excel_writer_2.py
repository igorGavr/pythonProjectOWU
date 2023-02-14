import xlrd

file = xlrd.open_workbook_xls('mashina_kg_2.xls', formatting_info=True)
sheet = file.sheet_by_index(0)
#        (індекс колонки, індекс комірки з якої починаємо читати)
column = sheet.col_values(1, 1)
print(column)
print(len(column))