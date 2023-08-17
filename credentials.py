import getpass

class Credentials:

    def __init__(self, username: str = '') -> None:
        self._username: str = username
        self._password: str = ''

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    def prompt_username(self) -> None:
        self._username = input('Username: ')

    def prompt_password(self) -> None:
        self._password = getpass.getpass()
