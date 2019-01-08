from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init


class Color:

    FORE = {'Black': Fore.BLACK, 'Red': Fore.RED, 'Green': Fore.GREEN, 'Yellow': Fore.YELLOW, 'Blue': Fore.BLUE, 'Magenta': Fore.MAGENTA, 'Cyan': Fore.CYAN, 'White': Fore.WHITE}
    BACK = {'Black': Back.BLACK, 'Red': Back.RED, 'Green': Back.GREEN, 'Yellow': Back.YELLOW, 'Blue': Back.BLUE, 'Magenta': Back.MAGENTA, 'Cyan': Back.CYAN, 'White': Back.WHITE}
    STYLE = {'Bright': Style.BRIGHT, 'Dim': Style.DIM, 'Normal': Style.NORMAL}

    @classmethod
    def highlight_text(cls, text, color, style):
        init()
        return color + style + text + Style.RESET_ALL

    @classmethod
    def highlight_matches(cls, text, match_indexes, color, style):
        init()
        highlighted_text = ''
        start_index = 0
        for match, index in match_indexes:
            highlighted_text += text[start_index:index] + color + style + match + Style.RESET_ALL
            start_index = index + len(match)
        highlighted_text += text[start_index:]
        return highlighted_text
