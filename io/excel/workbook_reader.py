from typing import List

from cac.io.excel.row import Row
from cac.io.excel.worksheet import Worksheet
from openpyxl import Workbook as OpenpyxlWorkbook, load_workbook

def row_is_blank(row_data: List[object]) -> bool:
    return len([cell for cell in row_data if cell is not None]) == 0

class WorkbookReader:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_worksheets(self) -> List[Worksheet]:
        worksheets: List[Worksheet] = []
        openpyxl_workbook: OpenpyxlWorkbook = load_workbook(filename=self._file_name)
        for openpyxl_worksheet in openpyxl_workbook:
            rows: List[Row] = []
            for openpyxl_row in openpyxl_worksheet:
                row_data: List[object] = [openpyxl_cell.value for openpyxl_cell in openpyxl_row]
                if not row_is_blank(row_data):
                    rows.append(Row.raw_data(row_data))
            worksheets.append(Worksheet(openpyxl_worksheet.title, rows))
        openpyxl_workbook.close()
        return worksheets

    def read_worksheet(self, title: str = None) -> Worksheet:
        worksheets: List[Worksheet] = self.read_worksheets()
        if title is None:
            if len(worksheets) > 1:
                raise ValueError('Found \'' + str(len(worksheets)) + '\' worksheets')
            return worksheets[0]
        else:
            matching_worksheets: List[Worksheet] = [worksheet for worksheet in worksheets if worksheet.title == title]
            if len(matching_worksheets) == 0:
                raise ValueError('Could not find any worksheets with title \'' + title + '\'')
            return matching_worksheets[0]
