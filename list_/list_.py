from regex import Regex
from set_.multi_set import MultiSet
from set_.ordered_set import OrderedSet

class List(list):

    def count_items(self):
        counted_items = MultiSet()
        for item in self:
            counted_items.add(item)
        return counted_items

    def filter_duplicates(self):
        unique_items = OrderedSet()
        for item in self:
            unique_items.add(item)
        return unique_items

    def filter_text(self, regex_str):
        regex = Regex(regex_str)
        filtered_list = List()
        for item in self:
            if regex.matches(item):
                filtered_list.append(item)
        return filtered_list

    def replace(self, old_item, new_item):
        index = self.index(old_item)
        self.remove(old_item)
        self.insert(index, new_item)

    def write(self, file_):
        for item in self:
            file_.write(str(item) + '\n')

    def to_string(self):
        str_ = ''
        for itemIndex in range(0, len(self)):
            item = self[itemIndex]
            str_ += str(item)
            if itemIndex < len(self) - 1:
                str_ += ','
        return str_
