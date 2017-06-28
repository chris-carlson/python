from list_.pair_list import PairList

class OrderedDict(PairList):

    def __setitem__(self, key, value):
        if key in self:
            for item_index in range(0, len(self._rep)):
                if self._rep[item_index][0] == key:
                    self._rep[item_index] = (key, value)
        else:
            self.add(key, value)

    def add(self, key, value):
        if not key in self:
            self._rep.append((key, value))
