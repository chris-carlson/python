from typing import Dict
from typing import List

from cac.consumer import Consumer
from cac.regex import Regex


class Value:
    NUMBER_REGEX: Regex = Regex('-|[0-9]')
    BOOLEAN_REGEX: Regex = Regex('t|f')

    def __init__(self) -> None:
        self._object: Dict[str, Value] = None
        self._array: List[Value] = None
        self._string: str = None
        self._integer_number: int = None
        self._float_number: float = None
        self._boolean: bool = None

    @property
    def object(self) -> Dict[str, 'Value']:
        if self._object is None:
            raise ValueError('Expected type \'object\' but got type \'' + self._get_type() + '\'')
        return self._object

    @property
    def array(self) -> List['Value']:
        if self._array is None:
            raise ValueError('Expected type \'array\' but got type \'' + self._get_type() + '\'')
        return self._array

    @property
    def string(self) -> str:
        if self._string is None:
            raise ValueError('Expected type \'string\' but got type \'' + self._get_type() + '\'')
        return self._string

    @property
    def integer_number(self) -> int:
        if self._integer_number is None:
            raise ValueError('Expected type \'number (int)\' but got type \'' + self._get_type() + '\'')
        return self._integer_number

    @property
    def float_number(self) -> float:
        if self._float_number is None:
            raise ValueError('Expected type \'number (float)\' but got type \'' + self._get_type() + '\'')
        return self._float_number

    @property
    def boolean(self) -> bool:
        if self._boolean is None:
            raise ValueError('Expected type \'boolean\' but got type \'' + self._get_type() + '\'')
        return self._boolean

    def parse(self, consumer: Consumer) -> None:
        if consumer.peek() == '{':
            self._parse_object(consumer)
        elif consumer.peek() == '[':
            self._parse_array(consumer)
        elif consumer.peek() == '\"':
            self._parse_string(consumer)
        elif self.NUMBER_REGEX.matches(consumer.peek()):
            self._parse_number(consumer)
        elif self.BOOLEAN_REGEX.matches(consumer.peek()):
            self._parse_boolean(consumer)

    def _parse_object(self, consumer: Consumer) -> None:
        self._object = {}
        consumer.consume_char('{')
        consumer.consume_whitespace()
        while consumer.peek() != '}':
            consumer.consume_char('\"')
            key: str = consumer.consume_to('\"')
            consumer.consume_char('\"')
            consumer.consume_whitespace()
            consumer.consume_char(':')
            consumer.consume_whitespace()
            value: Value = Value()
            value.parse(consumer)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
            self._object[key] = value
        consumer.consume_char('}')

    def _parse_array(self, consumer: Consumer) -> None:
        self._array = []
        consumer.consume_char('[')
        consumer.consume_whitespace()
        while consumer.peek() != ']':
            value: Value = Value()
            value.parse(consumer)
            consumer.consume_whitespace()
            if consumer.peek() == ',':
                consumer.consume_char(',')
                consumer.consume_whitespace()
            self._array.append(value)
        consumer.consume_char(']')

    def _parse_string(self, consumer: Consumer) -> None:
        consumer.consume_char('\"')
        self._string = consumer.consume_to('\"')
        consumer.consume_char('\"')

    def _parse_number(self, consumer: Consumer):
        value: str = consumer.consume_to_one_of([',', '}', ']']).strip()
        if '.' in value or 'e' in value or 'E' in value:
            self._float_number = float(value)
        else:
            self._integer_number = int(value)

    def _parse_boolean(self, consumer: Consumer) -> None:
        value: str = consumer.consume_to_one_of([',', '}', ']']).strip()
        self._boolean = value == 'true'

    def _get_type(self) -> str:
        if self._object is not None:
            return 'object'
        elif self._array is not None:
            return 'array'
        elif self._string is not None:
            return 'string'
        elif self._integer_number is not None:
            return 'number (int)'
        elif self._float_number is not None:
            return 'number (float)'
        elif self._boolean is not None:
            return 'boolean'
