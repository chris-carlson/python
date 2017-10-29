import getpass

class Credentials:
    def __init__(self):
        self._username = ''
        self._password = ''

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def prompt_user(self, first_prompt='Username'):
        self._username = input(first_prompt + ': ')
        self._password = getpass.getpass()
