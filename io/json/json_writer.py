import json

from cac.io.text.text_writer import TextWriter


class JsonWriter:

    def __init__(self, file_name: str) -> None:
        self._file: TextWriter = TextWriter(file_name)

    def write(self, data: object) -> None:
        self._file.write_line(json.dumps(data, indent=2))

    def close(self) -> None:
        self._file.close()
