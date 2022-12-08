from typing import List

from cac.regex import Regex


class Ignore:
    DIRECTORIES: List[Regex] = [Regex(r'.ebextensions'), Regex(r'.git'), Regex(r'.idea'), Regex(r'.settings'),
            Regex(r'.vscode'), Regex(r'My Music'), Regex(r'My Pictures'), Regex(r'My Videos'), Regex(r'__pycache__'),
            Regex(r'bin'), Regex(r'build'), Regex(r'bundle'), Regex(r'dist'), Regex(r'node_modules'), Regex(r'out'),
            Regex(r'out-tsc'), Regex(r'target'), Regex(r'venv')]
    FILES: List[Regex] = [Regex(r'\.class$'), Regex(r'\.classpath$'), Regex(r'\.d.ts$'), Regex(r'\.DS_Store$'), Regex(r'\.factorypath$'),
            Regex(r'\.ico$'), Regex(r'\.ini$'), Regex(r'\.jpeg$'), Regex(r'\.jpg$'), Regex(r'\.lock$'), Regex(r'\.min.js$'),
            Regex(r'^package-lock.json$'), Regex(r'\.png$'), Regex(r'\.project$'), Regex(r'\.pyc$'), Regex(r'\.pyo$'),
            Regex(r'\.pyd$'), Regex(r'\.xlsx$')]
