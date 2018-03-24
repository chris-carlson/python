class Flags:

    def __init__(self, args):
        self._flags = []
        for arg in args[1:]:
            if arg.startswith('--'):
                self._flags.append(arg[2:])
            elif arg.startswith('-'):
                self._flags.append(arg[1:])

    def has_flag(self, flag):
        return flag in self._flags

    def get_flags(self):
        return self._flags
