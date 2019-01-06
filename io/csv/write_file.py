from cac.io.text.write_file import WriteFile as TextWriteFile


class WriteFile:

    def __init__(self, file_name, append=False):
        self._file = TextWriteFile(file_name, append)

    def write_row(self, values):
        self._file.write_line(','.join(['\"' + value + '\"' for value in values]))

    def close(self):
        self._file.close()
