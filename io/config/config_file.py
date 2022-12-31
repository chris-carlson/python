from typing import Dict


# noinspection PyUnresolvedReferences
class ConfigFile:

    def __init__(self, rep: Dict[str, object]) -> None:
        self._rep: Dict[str, object] = rep

    def get_default_value(self, name: str) -> str:
        return self._rep['DEFAULT'][name]

    def get_section_value(self, section: str, key: str) -> str:
        return self._rep[section][key]
