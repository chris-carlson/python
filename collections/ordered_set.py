from typing import Generic, TypeVar, List

E = TypeVar('E')


class OrderedSet(Generic[E]):

    def __init__(self, existing_list: List[E] = None) -> None:
        self._rep: List[E] = []
        if existing_list is not None:
            for item in existing_list:
                self.add(item)

    def __str__(self) -> str:
        string = '{'
        for i in range(0, len(self._rep)):
            item = self._rep[i]
            string += str(item)
            if i < len(self._rep) - 1:
                string += ', '
        string += '}'
        return string

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._rep)

    def __contains__(self, item) -> bool:
        return item in self._rep

    def __iter__(self) -> E:
        for item in self._rep:
            yield item

    def items(self) -> List[E]:
        return self._rep

    def add(self, item) -> None:
        if item not in self._rep:
            self._rep.append(item)

    def remove(self, item) -> None:
        if item not in self:
            raise AssertionError('Item \'' + str(item) + '\' is not in here')
        self._rep.remove(item)

    def reverse(self) -> None:
        self._rep.reverse()

    def sort(self) -> None:
        self._rep.sort()
