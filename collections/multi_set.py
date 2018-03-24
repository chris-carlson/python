from custom.collections.pair_list import PairList

class MultiSet(PairList):

    def add(self, key):
        if key in self:
            for item in self._rep:
                if item[0] == key:
                    index = self._rep.index(item)
                    count = item[1]
                    self._rep.remove(item)
                    self._rep.insert(index, (key, count + 1))
                    break
        else:
            self._rep.append((key, 1))
