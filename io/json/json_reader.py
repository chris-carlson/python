import json
from typing import Dict, List

from cac.io.text.text_reader import TextReader


class JsonReader:

    @staticmethod
    def read_text(text: str) -> object:
        return json.loads(text)

    def __init__(self, file_name: str) -> None:
        self._file: TextReader = TextReader(file_name)

    def read_object(self) -> Dict[str, object]:
        value: object = self._get_value()
        if not isinstance(value, dict):
            raise ValueError('Could not read JSON: invalid object')
        return value

    def read_array(self) -> List[object]:
        value: object = self._get_value()
        if not isinstance(value, list):
            raise ValueError('Could not read JSON: invalid array')
        return value

    def _get_value(self) -> object:
        lines: List[str] = self._file.read_lines()
        self._file.close()
        return json.loads(''.join(lines))
