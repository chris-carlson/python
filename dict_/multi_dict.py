from list_.pair_list import PairList
from set_.ordered_set import OrderedSet

class MultiDict(PairList):

    def add(self, key, value):
        if key in self:
            set_ = self.get(key)
            set_.add(value)
        else:
            set_ = OrderedSet()
            set_.add(value)
            self._rep.append((key, set_))
