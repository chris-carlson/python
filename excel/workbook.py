from custom.excel.worksheet import Worksheet
from openpyxl import Workbook as OpenpyxlWorkbook, load_workbook

class Workbook:

    def __init__(self, file_name=None):
        self._file_name = file_name
        self._worksheets = []
        self._rep = OpenpyxlWorkbook()

    def __str__(self):
        return '[' + ', '.join(self._worksheets) + ']'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._worksheets)

    def __iter__(self):
        for worksheet in self._worksheets:
            yield worksheet

    def __getitem__(self, index):
        return self._worksheets[index]

    def load_data(self):
        if self._file_name == None:
            raise ValueError('No file name given')
        self._rep = load_workbook(filename=self._file_name)
        for worksheet in self._rep:
            self._worksheets.append(Worksheet(worksheet))

    def get_worksheet(self, title):
        for worksheet in self._worksheets:
            if worksheet.get_title() == title:
                return worksheet
        return None

    def create_worksheet(self, title, position=None):
        if position == None:
            position = len(self._worksheets)
        openpyxl_worksheet = self._rep.create_sheet(title, position)
        self._worksheets.insert(position, Worksheet(openpyxl_worksheet))
        return self._worksheets[position]

    def save(self):
        self._rep.save(self._file_name)

    def save_as(self, file_name):
        self._rep.save(file_name)
