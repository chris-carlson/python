import sys
from typing import Dict, List, Set

from cac.cli.argument import Argument
from cac.cli.flag import Flag
from cac.cli.printer import Printer
from cac.finder import Finder
from cac.regex import Regex

HELP_FLAGS: List[str] = ['--help', '-h']
FLAG_REGEX: Regex = Regex(r'^--?(\w+)$')


def validate_parameter(parameter: str, input_flag: str, flag: Flag) -> None:
    if flag.values is not None and len(flag.values) > 0 and parameter not in flag.values:
        raise ValueError('Input \'{0}\' provided for flag \'{1}\' does not match one of the expected values '
                         '{2}'.format(parameter, input_flag, str(flag.values)))
    if flag.regex is not None and not flag.regex.matches(parameter):
        raise ValueError('Input \'{0}\' provided for flag \'{1}\' does not match the expected format '
                         '{2}'.format(parameter, input_flag, str(flag.regex)))


def validate_argument(input_argument: str, argument: Argument) -> None:
    if argument.values is not None and len(argument.values) > 0 and input_argument not in argument.values:
        raise ValueError('Input \'{0}\' provided for argument \'{1}\' does not match one of the expected values '
                         '{2}'.format(input_argument, argument.name, str(argument.values)))
    if argument.regex is not None and not argument.regex.matches(input_argument):
        raise ValueError('Input \'{0}\' provided for argument \'{1}\' does not match the expected format '
                         '{2}'.format(input_argument, argument.name, str(argument.regex)))


class Command:

    def __init__(self, name: str, arguments: List[Argument] = None, flags: List[Flag] = None, description: str = None,
            user_inputs: List[str] = None) -> None:
        self._name: str = name
        self._arguments: List[Argument] = arguments if arguments is not None else []
        self._flags: List[Flag] = flags if flags is not None else []
        self._user_inputs: List[str] = user_inputs if user_inputs is not None else sys.argv[1:][:]
        self._description: str = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def arguments(self) -> List[Argument]:
        return self._arguments

    @property
    def flags(self) -> List[Flag]:
        return self._flags

    @property
    def description(self) -> str:
        return self._description

    def _validate(self) -> None:
        flag_names: List[str] = [flag.names[0] for flag in self._flags] + [flag.names[1] for flag in self._flags]
        if '--help' in sys.argv or '-h' in sys.argv:
            self.print_help()
            sys.exit()
        duplicate_flag_names: Set[str] = Finder.find_duplicates(flag_names)
        if len(duplicate_flag_names) > 0:
            raise ValueError('Duplicate flag definitions found: ' + str(duplicate_flag_names))
        argument_names: List[str] = [argument.name for argument in self._arguments]
        duplicate_argument_names: Set[str] = Finder.find_duplicates(argument_names)
        if len(duplicate_argument_names) > 0:
            raise ValueError('Duplicate argument definitions found: ' + str(duplicate_argument_names))

    def parse_flags(self) -> Dict[str, str]:
        self._validate()
        user_flags: Dict[str, str] = {}
        input_flags: List[str] = [FLAG_REGEX.find_group(user_input) for user_input in self._user_inputs if
                user_input.startswith('-')]
        parameter_flags: List[str] = self._find_parameter_flags()
        for input_flag in input_flags:
            if input_flag in parameter_flags:
                flag_index: int = self._find_flag_index(input_flag)
                parameter: str = self._find_parameter(flag_index, input_flag)
                flag_definition: Flag = self._find_flag(input_flag)
                validate_parameter(parameter, input_flag, flag_definition)
                user_flags[flag_definition.names[0]] = parameter
            else:
                flag_definition: Flag = self._find_flag(input_flag)
                user_flags[flag_definition.names[0]] = ''
        return user_flags

    def _find_parameter_flags(self) -> List[str]:
        return [flag.names[0] for flag in self._flags if flag.parameter is not None] + [flag.names[1] for flag in
                self._flags if len(flag.names[1]) > 0 and flag.parameter is not None]

    def _find_flag_index(self, input_flag) -> int:
        try:
            return self._user_inputs.index('-' + input_flag if len(input_flag) == 1 else '--' + input_flag)
        except ValueError:
            raise ValueError('Unknown flag \'' + input_flag + '\' provided')

    def _find_parameter(self, flag_index: int, input_flag: str) -> str:
        try:
            parameter: str = self._user_inputs[flag_index + 1]
            if parameter.startswith('-'):
                raise ValueError('No parameter provided for flag \'' + input_flag + '\'')
        except IndexError:
            raise ValueError('No parameter provided for flag \'' + input_flag + '\'')
        return parameter

    def _find_flag(self, user_input_flag) -> Flag:
        return Finder.find_only(
                [flag for flag in self._flags if user_input_flag == flag.names[0] or user_input_flag == flag.names[1]])

    def parse_arguments(self) -> Dict[str, str]:
        self._validate()
        user_arguments: Dict[str, str] = {}
        input_arguments: List[str] = self._find_input_arguments()
        for index in range(0, len(input_arguments)):
            input_argument: str = input_arguments[index]
            argument_definition: Argument = self._get_argument(index, input_argument)
            validate_argument(input_argument, argument_definition)
            if argument_definition.repeated:
                user_arguments[argument_definition.name] = ','.join(input_arguments[index:])
                break
            user_arguments[argument_definition.name] = input_argument
        self._validate_required_arguments(user_arguments)
        return user_arguments

    def _find_input_arguments(self) -> List[str]:
        input_arguments: List[str] = []
        parameter_flags: List[str] = self._find_parameter_flags()
        for index in range(0, len(self._user_inputs)):
            user_input: str = self._user_inputs[index]
            previous_input: str = self._user_inputs[index - 1].replace('-', '') if index > 0 else ''
            if not FLAG_REGEX.matches(user_input) and previous_input not in parameter_flags:
                input_arguments.append(user_input)
        return input_arguments

    def _get_argument(self, index: int, input_argument: str) -> Argument:
        try:
            return self._arguments[index]
        except IndexError:
            raise ValueError('Extra argument \'' + input_argument + '\' provided')

    def _validate_required_arguments(self, user_arguments: Dict[str, str]) -> None:
        required_arguments: List[str] = [argument.name for argument in self._arguments if argument.required]
        for required_argument in required_arguments:
            if required_argument not in user_arguments:
                raise ValueError('Missing required argument \'' + required_argument + '\'')

    def print_help(self) -> None:
        printer: Printer = Printer(self._name, self._arguments, self._flags)
        printer.print_help()
