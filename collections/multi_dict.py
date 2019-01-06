from cac.collections.ordered_set import OrderedSet
from cac.collections.pair_list import PairList


class MultiDict(PairList):

    def add(self, key, value):
        if key in self:
            set_ = self.get(key)
            set_.add(value)
        else:
            set_ = OrderedSet()
            set_.add(value)
            self._rep.append((key, set_))
