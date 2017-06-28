class OrderedSet:

    def __init__(self):
        self._rep = []

    def __str__(self):
        str_ = '{'
        for i in range(0, len(self._rep)):
            item = self._rep[i]
            str_ += str(item)
            if i < len(self._rep) - 1:
                str_ += ', '
        str_ += '}'
        return str_

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._rep)

    def __contains__(self, item):
        return item in self._rep

    def __iter__(self):
        for item in self._rep:
            yield item

    def items(self):
        return self._rep

    def add(self, item):
        if item not in self:
            self._rep.append(item)

    def remove(self, item):
        if item not in self:
            raise AssertionError('Item \'' + str(item) + '\' is not in here')
        self._rep.remove(item)

    def reverse(self):
        self._rep.reverse()

    def sort(self):
        self._rep.sort()

    def write(file_):
        for item in self._rep:
            file_.write(str(item) + '\n')
