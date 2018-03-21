from custom.io.text.write_file import WriteFile as TextWriteFile

class WriteFile:

    def __init__(self, file_name):
        self._file = TextWriteFile(file_name)

    def write_row(self, values):
        self._file.write_line(','.join(['\"' + value + '\"' for value in values]))
