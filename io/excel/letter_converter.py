from math import floor
from typing import List

class LetterConverter:

    LETTERS: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    @staticmethod
    def convert_letter(letter: str) -> int:
        column_index: int = 0
        for letter_index in range(0, len(letter)):
            character: str = letter[letter_index].upper()
            column_index += (ord(character) - 65) + (letter_index * 26)
        return column_index

    @staticmethod
    def convert_number(number: int) -> str:
        prefix: str = ''
        if number >= len(LetterConverter.LETTERS):
            multiplier: int = floor(number / len(LetterConverter.LETTERS))
            prefix = LetterConverter.convert_number(multiplier - 1)
        suffix: str = LetterConverter.LETTERS[number % len(LetterConverter.LETTERS)]
        return prefix + suffix
