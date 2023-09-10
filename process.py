import subprocess

from subprocess import CompletedProcess
from typing import List

class Process:

    @staticmethod
    def run(arguments: List[str], cwd: str = None) -> str:
        completed_process: CompletedProcess = subprocess.run(arguments, capture_output=True, cwd=cwd)
        return completed_process.stdout.decode('utf-8')
