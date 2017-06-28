from excel.worksheet import Worksheet
from openpyxl import load_workbook

class Workbook:

    def __init__(self, file_name):
        self._file_name = file_name
        self._rep = load_workbook(filename=file_name)
        self._worksheets = []
        for worksheet in self._rep:
            self._worksheets.append(Worksheet(worksheet))

    def __str__(self):
        str_ = '['
        for i in range(0, len(self._worksheets)):
            worksheet = self._worksheets[i]
            str_ += worksheet.title
            if i < len(self._worksheets) - 1:
                str_ += ', '
        str_ += ']'
        return str_

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._worksheets)

    def __iter__(self):
        for worksheet in self._worksheets:
            yield worksheet

    def __getitem__(self, index):
        return self._worksheets[index]

    def get_worksheet(self, title):
        for worksheet in self._worksheets:
            if worksheet.title == title:
                return worksheet

    def create_worksheet(self, title, position=None):
        worksheet = self._rep.create_sheet(title, position)
        self._worksheets.insert(position, Worksheet(worksheet))
        return self._worksheets[position]

    def save(self):
        self._rep.save(self._file_name)

    def save_as(self, file_name):
        self._rep.save(file_name)
