import re


class Regex:

    def __init__(self, regex):
        self._rep = re.compile(regex)

    def matches(self, str_):
        matches = self.find_matches(str_)
        return len(matches) > 0

    def find_match(self, str_):
        matches = self.find_matches(str_)
        if len(matches) == 0:
            raise ValueError('Found no matches for str \'' + str_ + '\'')
        return matches[0]

    def find_matches(self, str_):
        return [match.group() for match in self._rep.finditer(str_)]

    def find_match_indexes(self, str_):
        return [(match.group(), match.start()) for match in self._rep.finditer(str_)]
