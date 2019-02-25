class Math:

    @staticmethod
    def one_based_mod(num: int, offset: int, mod: int) -> int:
        return ((num + offset - 1) % mod) + 1
