import subprocess

from subprocess import CompletedProcess
from typing import List

class Command:

    @staticmethod
    def run(arguments: List[str], cwd: str = None, run_cmd: bool = True) -> str:
        if run_cmd:
            arguments.insert(0, '/c')
            arguments.insert(0, 'cmd')
        completed_process: CompletedProcess = subprocess.run(arguments, capture_output = True, cwd = cwd)
        return completed_process.stdout.decode('utf-8')
