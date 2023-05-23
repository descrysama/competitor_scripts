import openpyxl
import os
from dotenv import load_dotenv
load_dotenv()

def fetchFinalOutput(): 
    array_to_return = []
    xlsx_file_path = os.getenv('EDITFILE_PATH')
    workbook = openpyxl.load_workbook(xlsx_file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(values_only=True):
        sku = row[0]  # Assuming SKU is in the first column
        value = row[1]  # Assuming value is in the second column
        array_to_return.append([sku, value])

    return array_to_return