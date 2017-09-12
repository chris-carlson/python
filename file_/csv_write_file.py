from custom.file_.write_file import WriteFile

class CsvWriteFile:

    def __init__(self, file_name):
        self._file = WriteFile(file_name)

    def write_row(self, values):
        self._file.write_line(','.join(values))
