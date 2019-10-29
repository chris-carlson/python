from typing import List

from openpyxl import Workbook as OpenpyxlWorkbook, load_workbook

from cac.io.excel.worksheet import Worksheet

class WorkbookReader:

    @staticmethod
    def _row_is_blank(row: List[object]) -> bool:
        return len([cell for cell in row if cell is not None]) == 0

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
                if not WorkbookReader._row_is_blank(row):
                    rows.append(row)
            worksheets.append(Worksheet(openpyxl_worksheet.title, rows))
        openpyxl_workbook.close()
        return worksheets
