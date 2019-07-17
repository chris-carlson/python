from typing import Dict
from typing import List

from cac.consumer import Consumer
from cac.io.text.text_reader import TextReader
from cac.json.json_value import JsonValue


class JsonDocument:

    def __init__(self, file_name) -> None:
        self._file: TextReader = TextReader(file_name)

    def parse_object(self) -> Dict[str, JsonValue]:
        value: JsonValue = self._get_value()
        return value.object

    def parse_array(self) -> List[JsonValue]:
        value: JsonValue = self._get_value()
        return value.array

    def parse_string(self) -> str:
        value: JsonValue = self._get_value()
        return value.string

    def parse_integer_number(self) -> int:
        value: JsonValue = self._get_value()
        return value.integer_number

    def parse_float_number(self) -> float:
        value: JsonValue = self._get_value()
        return value.float_number

    def parse_boolean(self) -> bool:
        value: JsonValue = self._get_value()
        return value.boolean

    def _get_value(self) -> JsonValue:
        self._file.read_lines()
        parse_line: str = self._file.get_parse_line()
        consumer: Consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        value: JsonValue = JsonValue()
        value.parse(consumer)
        return value
