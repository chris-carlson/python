from configparser import RawConfigParser

from cac.io.config.config_file import ConfigFile

class ConfigReader:

    def __init__(self, file_name: str) -> None:
        self._file_name: str = file_name

    def read_config(self) -> ConfigFile:
        parser: RawConfigParser = RawConfigParser()
        parser.read(self._file_name)
        return ConfigFile(dict(parser))
