import openpyxl
import os
from dotenv import load_dotenv
load_dotenv()


def editFinalOutput(final_checked_prices):
    xlsx_file_path = os.getenv('EDITFILE_PATH')
    workbook = openpyxl.load_workbook(xlsx_file_path)
    sheet = workbook.active
    for price in final_checked_prices:
        key = price[0]
        value = price[1]
        for row_index, row in enumerate(sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=1, values_only=False), start=1):
            print(str(row[0].value).strip(),' : ',str(key).strip())
            if str(row[0].value).strip() == str(key).strip():
                cell = sheet.cell(row=row_index, column=3)  # Update the third column (column C)
                updateFile(value, cell, workbook, xlsx_file_path)
                break


def updateFile(value, cell, workbook, xlsx_file_path) :
    cell.value = value
    workbook.save(xlsx_file_path)
    return