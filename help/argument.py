from typing import List


class Argument:

    def __init__(self, name: str, description: str, values: List[str] = None, required: bool = True,
            repeated: bool = False) -> None:
        self._name: str = name
        self._description: str = description
        self._values: List[str] = values
        self._required: bool = required
        self._repeated: bool = repeated

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def values(self) -> List[str]:
        return self._values

    @property
    def required(self) -> bool:
        return self._required

    @property
    def repeated(self) -> bool:
        return self._repeated
