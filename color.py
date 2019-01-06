from colorama import init
from colorama import Style

# Fore/Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
# Style: BRIGHT, DIM, NORMAL

class Color:

    @classmethod
    def highlight_text(cls, color, style, text):
        init()
        return color + style + text + Style.RESET_ALL

    @classmethod
    def highlight_matches(cls, color, style, text, match_indexes):
        init()
        highlighted_text = ''
        start_index = 0
        for match, index in match_indexes:
            highlighted_text += text[start_index:index] + color + style + match + Style.RESET_ALL
            start_index = index + len(match)
        highlighted_text += text[start_index:]
        return highlighted_text
