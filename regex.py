import re

class Regex:

    def __init__(self, regex):
        self._rep = re.compile(regex)

    def matches(self, str_):
        matches = self.find_matches(str_)
        return len(matches) > 0

    def find_match(self, str_):
        matches = self.find_matches(str_)
        return matches[0]

    def find_matches(self, str_):
        matches = []
        for match in self._rep.finditer(str_):
            matches.append(match.group())
        return matches
