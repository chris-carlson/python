from typing import Dict, List, Tuple

from colorama import Back
from colorama import Fore
from colorama import Style
from colorama import init


class Color:
    FORE: Dict[str, int] = {'Black': Fore.BLACK, 'Red': Fore.RED, 'Green': Fore.GREEN, 'Yellow': Fore.YELLOW,
        'Blue': Fore.BLUE, 'Magenta': Fore.MAGENTA, 'Cyan': Fore.CYAN, 'White': Fore.WHITE}
    BACK: Dict[str, int] = {'Black': Back.BLACK, 'Red': Back.RED, 'Green': Back.GREEN, 'Yellow': Back.YELLOW,
        'Blue': Back.BLUE, 'Magenta': Back.MAGENTA, 'Cyan': Back.CYAN, 'White': Back.WHITE}
    STYLE: Dict[str, int] = {'Bright': Style.BRIGHT, 'Dim': Style.DIM, 'Normal': Style.NORMAL}

    @staticmethod
    def highlight_text(text: str, color: int, style: int) -> str:
        init()
        return color + style + text + Style.RESET_ALL

    @staticmethod
    def highlight_matches(text: str, match_indexes: List[Tuple[str, int]], color: int, style: int) -> str:
        init()
        highlighted_text = ''
        start_index = 0
        for match, index in match_indexes:
            highlighted_text += text[start_index:index] + color + style + match + Style.RESET_ALL
            start_index = index + len(match)
        highlighted_text += text[start_index:]
        return highlighted_text
