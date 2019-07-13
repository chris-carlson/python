from typing import Dict
from typing import List

from cac.consumer import Consumer
from cac.io.text.text_reader import TextReader
from cac.json.value import Value


class Document:

    def __init__(self, file_name) -> None:
        self._file: TextReader = TextReader(file_name)

    def parse_object(self) -> Dict[str, Value]:
        value: Value = self._get_value()
        return value.object

    def parse_array(self) -> List[Value]:
        value: Value = self._get_value()
        return value.array

    def parse_string(self) -> str:
        value: Value = self._get_value()
        return value.string

    def parse_integer_number(self) -> int:
        value: Value = self._get_value()
        return value.integer_number

    def parse_float_number(self) -> float:
        value: Value = self._get_value()
        return value.float_number

    def parse_boolean(self) -> bool:
        value: Value = self._get_value()
        return value.boolean

    def _get_value(self) -> Value:
        self._file.read_lines()
        parse_line: str = self._file.get_parse_line()
        consumer: Consumer = Consumer(parse_line)
        consumer.consume_whitespace()
        value: Value = Value()
        value.parse(consumer)
        return value
