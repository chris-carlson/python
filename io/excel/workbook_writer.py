from typing import List

from cac.io.excel.letter_converter import LetterConverter
from cac.io.excel.row import Row
from cac.io.excel.worksheet import Worksheet
from openpyxl import Workbook as OpenpyxlWorkbook
from openpyxl.styles import Font
from openpyxl.worksheet.worksheet import Worksheet as OpenpyxlWorksheet


class WorkbookWriter:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name
        self._openpyxl_workbook: OpenpyxlWorkbook = OpenpyxlWorkbook()
        self._openpyxl_workbook.remove(self._openpyxl_workbook.worksheets[0])

    def write_worksheets(self, worksheets: List[Worksheet]) -> None:
        for worksheet in worksheets:
            self.write_worksheet(worksheet)

    # noinspection PyDunderSlots,PyUnresolvedReferences
    def write_worksheet(self, worksheet: Worksheet) -> None:
        openpyxl_worksheet: OpenpyxlWorksheet = self._openpyxl_workbook.create_sheet(worksheet.title)
        for row_index in range(0, len(worksheet)):
            row: Row[object] = worksheet[row_index]
            for column_index in range(0, len(row)):
                openpyxl_worksheet.cell(row=row_index + 1, column=column_index + 1, value=row[column_index])
                if row.bold:
                    openpyxl_worksheet.cell(row=row_index + 1, column=column_index + 1).font = Font(bold=True)
                letter: str = LetterConverter.convert_number(column_index)
                if letter in row.number_formats:
                    openpyxl_worksheet.cell(row=row_index + 1, column=column_index + 1).number_format = \
                        row.number_formats[letter]
        self._openpyxl_workbook.save(self._file_name)

    def close(self) -> None:
        self._openpyxl_workbook.close()
