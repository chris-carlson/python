class Comparer:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common_items(self):
        common_items = []
        for item in self.list1:
            if item in self.list2:
                common_items.append(item)
        return common_items

    def find_unique_items(self):
        unique_items = ([], [])
        for item in self.list1:
            if item not in self.list2:
                unique_items[0].append(item)
        for item in self.list2:
            if item not in self.list1:
                unique_items[1].append(item)
        return unique_items
