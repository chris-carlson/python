class String(str):

    def __init__(self, str_=''):
        super().__init__()
        self._rep = str_

    def __getitem__(self, key):
        return String(self._rep[key])

    def find(self, find_str, num=1):
        count = 0
        index = 0
        while count < num:
            if count > 0:
                index += 1
            index = self._rep.find(find_str, index)
            if index < 0:
                raise ValueError('Could not find occurrence ' + str(num) + ' of \'' + find_str + '\'')
            count += 1
        return index

    def find_between(self, str1, str2, pair_num=1):
        indexes = ()
        current_pair = 0
        start_index = 0
        while current_pair < pair_num:
            indexes = self._find_pair_indexes(str1, str2, start_index)
            current_pair += 1
            start_index = indexes[1] + 1
        return String(self._rep[indexes[0] + len(str1): indexes[1]].strip())

    def find_after(self, find_str, after_str, num=1):
        after_index = -1
        current_num = 0
        start_index = 0
        while current_num < num:
            after_index = self._rep.find(after_str, start_index)
            if after_index == -1:
                raise ValueError('String \'' + after_str + '\' not found')
            current_num += 1
            start_index = after_index + 1
        return String(self._rep.find(find_str, after_index + 1))

    def find_indexes(self, char, invalid_preceding_char=''):
        indexes = []
        current_index = 0
        while current_index != -1:
            char_index = self._rep.find(char, current_index)
            if char_index != -1:
                if not self._preceded_by(invalid_preceding_char, char_index):
                    indexes.append(char_index)
                current_index = char_index + 1
            else:
                current_index = -1
        return indexes

    def substring_to(self, substring):
        index = self._rep.find(substring)
        return String(self._rep[:index])

    def substring_to_last(self, substring):
        index = self._rep.rfind(substring)
        return String(self._rep[:index])

    def substring_through(self, substring):
        index = self._rep.find(substring)
        return String(self._rep[:index + len(substring)])

    def substring_from(self, substring):
        index = self._rep.find(substring)
        return String(self._rep[index:])

    def substring_after(self, substring):
        index = self._rep.find(substring)
        return String(self._rep[index + len(substring):])

    def substring_after_last(self, substring):
        index = self._rep.rfind(substring)
        return String(self._rep[index + len(substring):])

    def is_capitalized(self):
        return String(self._rep[0] == self._rep[0].upper())

    def capitalize_first(self):
        return String(self._rep[0].upper() + self._rep[1:])

    def remove(self, sequence):
        str_ = self._rep
        while str_.find(sequence) != -1:
            index = self._rep.find(sequence)
            str_ = str_[:index] + str_[index + len(sequence):]
        return String(str_)

    def remove_whitespace(self):
        str_ = self._rep
        str_ = str_.replace(' ', '')
        str_ = str_.replace('\t', '')
        str_ = str_.replace('\r', '')
        str_ = str_.replace('\n', '')
        return String(str_)

    def insert_text(self, index, text):
        return String(self._rep[:index] + text + self._rep[index:])

    def insert_text_before(self, char, text):
        index = self._rep.find(char)
        return self.insert_text(index, text)

    def insert_text_after(self, char, text):
        index = self._rep.find(char) + 1
        return self.insert_text(index, text)

    def _find_pair_indexes(self, str1, str2, index=0):
        index1 = self._rep.find(str1, index + 1)
        index2 = self._rep.find(str2, index1 + 1)
        if index1 == -1 or index2 == -1:
            raise ValueError(
                'Could not find a pair of (\'' + str1 + '\', \'' + str2 + '\') in string starting at index ' + str(
                    index))
        return index1, index2

    def _preceded_by(self, char, index):
        if index == -1 or index == 0:
            return False
        return self._rep[index - 1] == char
