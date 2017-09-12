from custom.list_.list_ import List

_HEADER = '***'

def _find_common_items(list1, list2):
    common_items = List()
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

def _find_unique_items(list1, list2):
    unique_items = (List(), List())
    for item in list1:
        if item not in list2:
            unique_items[0].append(item)
    for item in list2:
        if item not in list1:
            unique_items[1].append(item)
    return unique_items

def _write_items(list_, output_file):
    if len(list_) == 0:
        output_file.write('No results\n')
    else:
        list_.write(output_file)
    output_file.write('\n')

class Comparer:

    def __init__(self, list1, list2):
        self._common_items = _find_common_items(list1, list2)
        self._unique_items = _find_unique_items(list1, list2)

    @property
    def common_items(self):
        return self._common_items

    @property
    def unique_items(self):
        return self._unique_items

    def write_common_items(self, output_file):
        output_file.write(_HEADER + ' Common Items ' + _HEADER + '\n')
        _write_items(self._common_items, output_file)

    def write_unique_items(self, output_file):
        output_file.write(_HEADER + ' In first list but not second ' + _HEADER + '\n')
        _write_items(self._unique_items[0], output_file)
        output_file.write(_HEADER + ' In second list but not first ' + _HEADER + '\n')
        _write_items(self._unique_items[1], output_file)

    def write_all_items(self, output_file):
        self.write_common_items(output_file)
        self.write_diffs(output_file)
