import getpass


class Credentials:

    def __init__(self, username=''):
        self._username = username
        self._password = ''

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def prompt_username(self):
        self._username = input('Username: ')

    def prompt_password(self):
        self._password = getpass.getpass()
