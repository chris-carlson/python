import sys
from typing import Dict, List, Set

from cac.cli.argument import Argument
from cac.cli.flag import Flag
from cac.cli.printer import Printer
from cac.finder import Finder
from cac.regex import Regex

FLAG_REGEX: Regex = Regex(r'^--?(\w+)$')


def validate_parameter(parameter: str, input_flag: str, flag_definition: Flag) -> None:
    if flag_definition.values is not None and len(
            flag_definition.values) > 0 and parameter not in flag_definition.values:
        raise ValueError('Input \'{0}\' provided for flag \'{1}\' does not match one of the expected values '
                         '{2}'.format(parameter, input_flag, str(flag_definition.values)))
    if flag_definition.regex is not None and not flag_definition.regex.matches(parameter):
        raise ValueError('Input \'{0}\' provided for flag \'{1}\' does not match the expected format '
                         '{2}'.format(parameter, input_flag, str(flag_definition.regex)))


def validate_argument(input_argument: str, argument_definition: Argument) -> None:
    if argument_definition.values is not None and len(
            argument_definition.values) > 0 and input_argument not in argument_definition.values:
        raise ValueError('Input \'{0}\' provided for argument \'{1}\' does not match one of the expected values '
                         '{2}'.format(input_argument, argument_definition.name, str(argument_definition.values)))
    if argument_definition.regex is not None and not argument_definition.regex.matches(input_argument):
        raise ValueError('Input \'{0}\' provided for argument \'{1}\' does not match the expected format '
                         '{2}'.format(input_argument, argument_definition.name, str(argument_definition.regex)))


class Command:

    def __init__(self, name: str, argument_definitions: List[Argument] = None,
            flag_definitions: List[Flag] = None) -> None:
        self._name: str = name
        self._argument_definitions: List[Argument] = argument_definitions if flag_definitions is not None else []
        self._flag_definitions: List[Flag] = flag_definitions if flag_definitions is not None else []
        self._user_inputs: List[str] = sys.argv[1:][:]
        if '-h' in self._user_inputs or '--help' in self._user_inputs:
            printer: Printer = Printer(name, argument_definitions, flag_definitions)
            printer.print_help()
            sys.exit()

    @property
    def name(self) -> str:
        return self._name

    def set_user_inputs(self, user_inputs: List[str]) -> None:
        self._user_inputs = user_inputs

    def _validate(self) -> None:
        flag_names: List[str] = [flag.names[0] for flag in self._flag_definitions] + [flag.names[1] for flag in
                self._flag_definitions]
        duplicate_flag_names: Set[str] = Finder.find_duplicates(flag_names)
        if len(duplicate_flag_names) > 0:
            raise ValueError('Duplicate flag definitions found: ' + str(duplicate_flag_names))
        argument_names: List[str] = [argument.name for argument in self._argument_definitions]
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
                flag_definition: Flag = self._find_flag_definition(input_flag)
                validate_parameter(parameter, input_flag, flag_definition)
                user_flags[flag_definition.names[0]] = parameter
            else:
                flag_definition: Flag = self._find_flag_definition(input_flag)
                user_flags[flag_definition.names[0]] = ''
        return user_flags

    def _find_parameter_flags(self) -> List[str]:
        return [flag.names[0] for flag in self._flag_definitions if flag.parameter is not None] + [flag.names[1] for
                flag in self._flag_definitions if len(flag.names[1]) > 0 and flag.parameter is not None]

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

    def _find_flag_definition(self, user_input_flag) -> Flag:
        return Finder.find_only([flag for flag in self._flag_definitions if
                user_input_flag == flag.names[0] or user_input_flag == flag.names[1]])

    def parse_arguments(self) -> Dict[str, str]:
        self._validate()
        user_arguments: Dict[str, str] = {}
        input_arguments: List[str] = self._find_input_arguments()
        for index in range(0, len(input_arguments)):
            input_argument: str = input_arguments[index]
            argument_definition: Argument = self._get_argument_definition(index, input_argument)
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

    def _get_argument_definition(self, index: int, input_argument: str) -> Argument:
        try:
            return self._argument_definitions[index]
        except IndexError:
            raise ValueError('Extra argument \'' + input_argument + '\' provided')

    def _validate_required_arguments(self, user_arguments: Dict[str, str]) -> None:
        required_arguments: List[str] = [argument.name for argument in self._argument_definitions if argument.required]
        for required_argument in required_arguments:
            if required_argument not in user_arguments:
                raise ValueError('Missing required argument \'' + required_argument + '\'')
