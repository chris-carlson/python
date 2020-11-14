from typing import List

from math import floor


class LetterConverter:
    LETTERS: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    @staticmethod
    def convert_letter(letter: str) -> int:
        column_index: int = 0
        letter = letter[::-1]
        for position_index in range(0, len(letter)):
            character: str = letter[position_index].upper()
            letter_index: int = LetterConverter.LETTERS.index(character) + 1
            column_index += letter_index * (26 ** position_index)
        return column_index - 1

    @staticmethod
    def convert_number(number: int) -> str:
        prefix: str = ''
        if number >= len(LetterConverter.LETTERS):
            multiplier: int = floor(number / len(LetterConverter.LETTERS))
            prefix = LetterConverter.convert_number(multiplier - 1)
        suffix: str = LetterConverter.LETTERS[number % len(LetterConverter.LETTERS)]
        return prefix + suffix
