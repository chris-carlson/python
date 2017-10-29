PAIR_CHARS = ['(', '{', '[']
SAME_CHARS = ['\"', '\'']

def find_match(rep):
    start_char = rep[0]
    if start_char in PAIR_CHARS:
        return _find_pair_match(rep)
    if start_char in SAME_CHARS:
        return _find_same_match(rep)
    raise ValueError('Invalid starting character')

def _find_pair_match(rep):
    matched_area = ''
    index = 1
    level = 0
    start_char = rep[0]
    match_char = _get_match_char(start_char)
    matched_area += rep[0]
    while rep[index] != match_char or level > 0:
        if rep[index] == start_char:
            level += 1
        elif rep[index] == match_char:
            level -= 1
        matched_area += rep[index]
        index += 1
        assert index < len(rep)
    matched_area += rep[index]
    return matched_area

def _find_same_match(rep):
    matched_area = ''
    index = 1
    preceding_backslash = False
    start_char = rep[0]
    match_char = _get_match_char(start_char)
    matched_area += rep[0]
    while rep[index] != match_char or preceding_backslash:
        preceding_backslash = rep[index] == '\\'
        matched_area += rep[index]
        index += 1
        assert index < len(rep)
    matched_area += rep[index]
    return matched_area

def _get_match_char(char):
    if char == '(':
        return ')'
    elif char == '{':
        return '}'
    elif char == '[':
        return ']'
    elif char == '\"':
        return '\"'
    elif char == '\'':
        return '\''
