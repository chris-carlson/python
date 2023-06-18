class Cell:

    def __init__(self, value: object, bold: bool = False, color: str = None, number_format: str = None) -> None:
        self._value: object = value
        self._bold: bool = bold
        self._color: str = color
        self._number_format: str = number_format

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def value(self) -> object:
        return self._value

    @property
    def bold(self) -> bool:
        return self._bold

    @property
    def color(self) -> str:
        return self._color

    @property
    def number_format(self) -> str:
        return self._number_format
