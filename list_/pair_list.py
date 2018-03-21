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
            yield item

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def get(self, key):
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in the list')
        for item in self._rep:
            if item[0] == key:
                return item[1]

    def keys(self):
        return [item[0] for item in self._rep]

    def values(self):
        return [item[1] for item in self._rep]

    def add(self, key, value):
        self._rep.append((key, value))

    def remove(self, key):
        if key not in self:
            raise AssertionError('Key \'' + str(key) + '\' is not in the list')
        for item in self._rep:
            if item[0] == key:
                item_to_remove = item
                break
        self._rep.remove(item_to_remove)

    def sort_keys(self):
        if len(self._rep) > 0:
            if type(self._rep[0][0]) == str:
                self._rep.sort(key=lambda pair: pair[0].lower())
            else:
                self._rep.sort(key=lambda pair: pair[0])

    def sort_values(self):
        if len(self._rep) > 0:
            if type(self._rep[0][1]) == str:
                self._rep.sort(key=lambda pair: pair[1].lower())
            else:
                self._rep.sort(key=lambda pair: pair[1])

    def reverse(self):
        self._rep.reverse()
