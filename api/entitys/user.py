#this classe is a entity used in methodos of services in API

class User:
    def __init__(self, login, email, password, is_adm):
        self.__login = login
        self.__email = email
        self.__password = password
        self.is_adm = is_adm

    #this methodos are getters e setters, retuns and modify the parameters
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_adm(self):
        return self.__is_adm

    @is_adm.setter
    def is_adm(self, is_adm):
        self.__is_adm = is_adm