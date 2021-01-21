import sys
from typing import Dict, List

from cac.cli.argument import Argument
from cac.cli.command import Command
from cac.cli.flag import Flag
from cac.cli.printer import Printer
from cac.finder import Finder
from cac.regex import Regex

FLAG_REGEX: Regex = Regex(r'--?(\w+)')


class Data:

    def __init__(self, command: Command) -> None:
        self._flags: Dict[str, str] = {}
        self._arguments: Dict[str, str] = {}
        user_inputs: List[str] = sys.argv[1:][:]
        if '-h' in user_inputs or '--help' in user_inputs:
            printer: Printer = Printer(command)
            printer.print_help()
            sys.exit()
        self._parse_flags(user_inputs, command.flags[:])
        self._parse_arguments(user_inputs, command.arguments[:])

    @property
    def flags(self) -> Dict[str, str]:
        return self._flags

    @property
    def arguments(self) -> Dict[str, str]:
        return self._arguments

    def has_flag_parameter(self, flag: str) -> bool:
        if flag not in self._flags:
            raise ValueError('Flag \'' + flag + '\' is not defined')
        return len(self._flags[flag]) > 0

    def _parse_flags(self, user_inputs: List[str], flags: List[Flag]) -> None:
        user_input_flags: List[str] = [FLAG_REGEX.find_group(user_input) for user_input in user_inputs if
                user_input.startswith('-')]
        parameter_flags: List[str] = [flag.names[0] for flag in flags if flag.parameter is not None] + [flag.names[1]
                for flag in flags if len(flag.names[1]) > 0 and flag.parameter is not None]
        for flag in flags:
            self._flags[flag.names[0]] = ''
            self._flags[flag.names[1]] = ''
        for user_input_flag in user_input_flags:
            try:
                flag_index: int = user_inputs.index(
                        '-' + user_input_flag if len(user_input_flag) == 1 else '--' + user_input_flag)
            except ValueError:
                raise ValueError('Unknown flag \'' + user_input_flag + '\' provided')
            if user_input_flag in parameter_flags:
                try:
                    parameter: str = user_inputs[flag_index + 1]
                    if parameter.startswith('-'):
                        raise ValueError('No parameter provided for flag \'' + user_input_flag + '\'')
                    matching_flag: Flag = Finder.find_only([flag for flag in flags if
                            user_input_flag == flag.names[0] or user_input_flag == flag.names[1]])
                    if matching_flag.values is not None and len(
                            matching_flag.values) > 0 and parameter not in matching_flag.values:
                        raise ValueError(
                                'Input \'{0}\' provided for flag \'{1}\' does not match one of the expected values '
                                '{2}'.format(parameter, user_input_flag, str(matching_flag.values)))
                    if matching_flag.regex is not None and not matching_flag.regex.matches(parameter):
                        raise ValueError('Input \'{0}\' provided for flag \'{1}\' does not match the expected format '
                                         '{2}'.format(parameter, user_input_flag, str(matching_flag.regex)))
                    self._flags[matching_flag.names[0]] = parameter
                    self._flags[matching_flag.names[1]] = parameter
                    user_inputs.pop(flag_index + 1)
                except IndexError:
                    raise ValueError('No parameter provided for flag \'' + user_input_flag + '\'')
            else:
                self._flags[user_input_flag] = ''
            user_inputs.pop(flag_index)

    def _parse_arguments(self, user_inputs: List[str], arguments: List[Argument]) -> None:
        while len(user_inputs) > 0:
            user_input: str = user_inputs.pop(0)
            try:
                argument: Argument = arguments.pop(0)
            except IndexError:
                raise ValueError('Extra argument \'' + user_input + '\' provided')
            if argument.values is not None and len(argument.values) > 0 and user_input not in argument.values:
                raise ValueError(
                        'Input \'{0}\' provided for argument \'{1}\' does not match one of the expected values '
                        '{2}'.format(user_input, argument.name, str(argument.values)))
            if argument.regex is not None and not argument.regex.matches(user_input):
                raise ValueError('Input \'{0}\' provided for argument \'{1}\' does not match the expected format '
                                 '{2}'.format(user_input, argument.name, str(argument.regex)))
            if argument.repeated:
                user_input += ',' + ','.join(user_inputs)
                user_inputs = []
            self._arguments[argument.name] = user_input
        required_arguments: List[Argument] = [argument for argument in arguments if argument.required]
        if len(required_arguments) > 0:
            required_argument: Argument = required_arguments[0]
            raise ValueError('Missing required argument \'' + required_argument.name + '\'')
