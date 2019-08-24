import json

from typing import Dict, List

from cac.io.text.text_reader import TextReader


class JsonReader:

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

    def read_string(self) -> str:
        value: object = self._get_value()
        if not isinstance(value, str):
            raise ValueError('Could not read JSON: invalid string')
        return value

    def read_integer_number(self) -> int:
        value: object = self._get_value()
        if not isinstance(value, int):
            raise ValueError('Could not read JSON: invalid integer')
        return value

    def read_float_number(self) -> float:
        value: object = self._get_value()
        if not isinstance(value, float):
            raise ValueError('Could not read JSON: invalid float')
        return value

    def read_boolean(self) -> bool:
        value: object = self._get_value()
        if not isinstance(value, bool):
            raise ValueError('Could not read JSON: invalid boolean')
        return value

    def _get_value(self) -> object:
        lines: List[str] = self._file.read_lines()
        self._file.close()
        return json.loads(''.join(lines))
