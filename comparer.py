class Comparer:

    def __init__(self, list1, list2):
        self._list1 = list1
        self._list2 = list2

    def find_common_items(self):
        return [item for item in self._list1 if item in self._list2]

    def find_unique_items(self):
        return ([item for item in self._list1 if item not in self._list2], [item for item in self._list2 if item not in self._list1])
