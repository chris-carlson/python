class PairList:

    def __init__(self):
        self._rep = []

    def __str__(self):
        str_ = '{'
        for i in range(0, len(self._rep)):
            item = self._rep[i]
            str_ += str(item[0]) + ': ' + str(item[1])
            if i < len(self._rep) - 1:
                str_ += ', '
        str_ += '}'
        return str_

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._rep)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        for item in self._rep:
            yield item[0]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def get(self, key):
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in here')
        for item in self._rep:
            if item[0] == key:
                return item[1]

    def keys(self):
        keys = []
        for item in self._rep:
            keys.append(item[0])
        return keys

    def values(self):
        values = []
        for item in self._rep:
            values.append(item[1])
        return values

    def add(self, key, value):
        self._rep.append((key, value))

    def remove(self, key):
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in here')
        for item in self._rep:
            if item[0] == key:
                item_to_remove = item
        self._rep.remove(item_to_remove)

    def sort_keys(self):
        self._rep.sort(key=lambda pair: pair[0])

    def sort_values(self):
        self._rep.sort(key=lambda pair: pair[1])

    def reverse(self):
        self._rep.reverse()

    def write(self, file_):
        for pair in self._rep:
            file_.write(str(pair[0]) + ': ' + str(pair[1]) + '\n')
