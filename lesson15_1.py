
import re

class Email:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        print('geter call')
        return self.__email

    @staticmethod
    def is_include_sobaka(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    @email.setter
    def email(self, value):
        print('seter call')
        if not isinstance(value, str):
            raise TypeError('емеил должен быть строкой ')
        if len(value) < 5:
            raise ValueError('что-то мутишь')
        if Email.is_include_sobaka(value):
            raise ValueError('собаку став) ) ')
        self.__email = value


c = Email('vfgfg@gmail.com')
print(c.email)
c.email = ('fdfdf@ferf.ds')
