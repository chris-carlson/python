import subprocess

from typing import List

class Command:

    @staticmethod
    def run(arguments: List[str]) -> None:
        arguments.insert(0, '/c')
        arguments.insert(0, 'cmd')
        subprocess.run(arguments)
