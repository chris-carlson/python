import json

from cac.io.text.text_writer import TextWriter

class JsonWriter:

    def __init__(self, file_name) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, data: object) -> None:
        self._file.write_line(json.dumps(data))
