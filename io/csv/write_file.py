from typing import List

from cac.io.text.write_file import WriteFile as TextWriteFile


class WriteFile:

    def __init__(self, file_name: str, append: bool = False) -> None:
        self._file: TextWriteFile = TextWriteFile(file_name, append)

    def write_row(self, values: List[str]) -> None:
        self._file.write_line(','.join(['\"' + value + '\"' for value in values]))
        row_values: List[str] = []
        for value in values:
            if ',' in values:
                row_values.append('\"' + value + '\"')
            else:
                row_values.append(value)
        self._file.write_line(','.join(row_values))

    def close(self) -> None:
        self._file.close()
