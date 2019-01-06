import sys

class Args:

    def __init__(self, num_args=-1, arg_flags=[]):
        self._args = []
        self._flags = {}
        args = sys.argv[1:][:]
        while len(args) > 0:
            arg = args.pop(0)
            if arg.startswith('-'):
                if arg.startswith('--'):
                    flag = arg[2:]
                else:
                    flag = arg[1:]
                value = ''
                if flag in arg_flags:
                    if len(args) == 0:
                        raise ValueError('Argument expected after flag \'' + flag + '\'')
                    value = args.pop(0)
                self._flags[flag] = value
            else:
                self._args.append(arg)
        if num_args != -1:
            assert len(self._args) == num_args

    def __len__(self):
        return len(self._args)

    def get_args(self):
        return self._args

    def get_arg(self, num):
        assert num >= 1
        return self._args[num - 1]

    def has_flag(self, flag):
        return flag in self._flags

    def get_flag(self, flag):
        return self._flags[flag]
