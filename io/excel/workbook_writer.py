from typing import List

from openpyxl import Workbook as OpenpyxlWorkbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet as OpenpyxlWorksheet

from cac.io.excel.worksheet import Worksheet

class WorkbookWriter:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name
        self._openpyxl_workbook: OpenpyxlWorkbook = OpenpyxlWorkbook()
        self._openpyxl_workbook.remove(self._openpyxl_workbook.worksheets[0])

    def write_worksheets(self, worksheets: List[Worksheet]) -> None:
        for worksheet in worksheets:
            self.write_worksheet(worksheet)

    def write_worksheet(self, worksheet: Worksheet) -> None:
        openpyxl_worksheet: OpenpyxlWorksheet = self._openpyxl_workbook.create_sheet(worksheet.title)
        for row_index in range(0, len(worksheet)):
            row: List[List[object]] = worksheet[row_index]
            for column_index in range(0, len(row)):
                openpyxl_worksheet.cell(row=row_index + 1, column=column_index + 1, value=row[column_index])
        self._openpyxl_workbook.save(self._file_name)

    def close(self) -> None:
        self._openpyxl_workbook.close()
