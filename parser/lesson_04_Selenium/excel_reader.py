import pandas as panda

excel_data = panda.read_excel(
    'mashina_kg.xlsx',
    sheet_name='Sheet1',
    usecols=['Title', 'Price', 'Add. info']
)
print(excel_data)
print(excel_data['Title'])
