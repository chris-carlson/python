from typing import List

class Ignore:
    DIRECTORIES: List[str] = ['.git', '.svn', '__pycache__', 'node_modules', 'target', 'dist', 'build', 'bin', 'bundle', 'out', 'out-tsc', '.idea', '.settings', '.vscode', 'venv', 'My Music', 'My Pictures', 'My Videos']
    FILES: List[str] = ['.classpath', '.project', '.factorypath', '.xlsx', '.png', '.ini', '.ico', '.jpg', '.jpeg', '.lock']
