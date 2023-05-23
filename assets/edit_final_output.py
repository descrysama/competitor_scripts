import openpyxl
import os
from dotenv import load_dotenv
load_dotenv()

def editFinalOutput(final_checked_prices):
    xlsx_file_path = os.getenv('EDITFILE_PATH')
    workbook = openpyxl.load_workbook(xlsx_file_path)
    sheet = workbook.active

    price_dict = {price[0]: price for price in final_checked_prices}

    for row_index in range(1, sheet.max_row + 1):
        cell1 = sheet.cell(row=row_index, column=1)
        key = cell1.value
        price = price_dict.get(key)
        if price:
            cell2 = sheet.cell(row=row_index, column=2)
            cell2.value = price[1]
            cell3 = sheet.cell(row=row_index, column=3)
            cell3.value = price[2] if len(price) == 3 else ""

    workbook.save(xlsx_file_path)