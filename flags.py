class Flags:

    def __init__(self, args):
        self._flags = []
        for index in range(1, len(args)):
            arg = args[index]
            if arg.startswith('--'):
                self._flags.append(arg[2:])
            elif arg.startswith('-'):
                self._flags.append(arg[1:])

    def has_flag(self, flag):
        return flag in self._flags

    def get_flags(self):
        return self._flags

    def add_flag(self, flag):
        self._flags.append(flag)
