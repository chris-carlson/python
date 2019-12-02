class LetterConverter:

    @staticmethod
    def convert_letter(letter: str) -> int:
        column_index: int = 0
        for letter_index in range(0, len(letter)):
            character: str = letters[letter_index].upper()
            column_index += (ord(character) - 65) + (letter_index * 26)
        return column_index
