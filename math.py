class Math:

    @classmethod
    def one_based_mod(cls, num, offset, mod):
        return ((num + offset - 1) % mod) + 1
