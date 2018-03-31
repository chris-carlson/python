from custom.collections.pair_list import PairList


class MultiSet:

    def __init__(self):
        self._rep = PairList()

    def __str__(self):
        return self._rep.__str__()

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

    def get(self, key):
        return self._rep.get(key)

    def keys(self):
        return self._rep.keys()

    def values(self):
        return self._rep.values()

    def add(self, key):
        if key in self:
            for item in self._rep:
                if item[0] == key:
                    count = item[1]
                    self._rep.remove(item)
                    self._rep.add(key, count)
                    break
        else:
            self._rep.add(key, 1)

    def remove(self, key):
        self._rep.remove(key)

    def sort_keys(self):
        self._rep.sort_keys()

    def sort_values(self):
        self._rep.sort_values()

    def reverse(self):
        self._rep.reverse()
