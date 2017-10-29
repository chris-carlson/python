class Str(str):

    def __init__(self, str_):
        self._rep = str_

    def find_between(self, char):
        index1 = self._rep.find(char)
        index2 = self._rep.find(char, index1 + 1)
        if index1 == -1 or index2 == -1:
            return ''
        return Str(self._rep[index1 + 1 : index2].strip())

    def find_after(self, find_str, after_str):
        after_index = self._rep.find(after_str)
        return Str(self._rep.find(find_str, after_index + 1))

    def substring_to(self, substring):
        index = self._rep.find(substring)
        return Str(self._rep[:index])

    def substring_from(self, substring):
        index = self._rep.find(substring)
        return Str(self._rep[index:])

    def substring_after(self, substring):
        index = self._rep.find(substring)
        return Str(self._rep[index + len(substring):])

    def is_capitalized(self):
        return Str(self._rep[0] == self._rep[0].upper())

    def capitalize_first(self):
        return Str(self._rep[0].upper() + self._rep[1:])

    def remove(self, char):
        str_ = self._rep
        while contains(char):
            index = self._rep.find(char)
            str_ = str_[:index] + str_[index + 1:]
        return Str(str_)

    def remove_whitespace(self):
        str_ = self._rep
        str_ = str_.replace(' ', '')
        str_ = str_.replace('\t', '')
        str_ = str_.replace('\r', '')
        str_ = str_.replace('\n', '')
        return Str(str_)

    def insert_text(self, index, text):
        return Str(self._rep[:index] + text + self._rep[index:])

    def insert_text_before(self, char, text):
        index = self._rep.find(char)
        return self.insert_text(index, text)

    def insert_text_after(self, char, text):
        index = self._rep.find(char) + 1
        return self.insert_text(index, text)
