from typing import List

from openpyxl import Workbook as OpenpyxlWorkbook, load_workbook

from cac.excel.worksheet import Worksheet

class WorkbookReader:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_worksheets(self) -> List[Worksheet]:
        worksheets: List[Worksheet] = []
        openpyxl_workbook: OpenpyxlWorkbook = load_workbook(filename=self._file_name)
        for openpyxl_worksheet in openpyxl_workbook:
            rows: List[List[object]] = []
            for openpyxl_row in openpyxl_worksheet:
                row: List[object] = []
                for openpyxl_cell in openpyxl_row:
                    row.append(openpyxl_cell.value)
                rows.append(row)
            worksheets.append(Worksheet(openpyxl_worksheet.title, rows))
        openpyxl_workbook.close()
        return worksheets
