class Teacher:
    def __init__(self, name, graduate_level):
        self.__name = name
        self.__graduate_level = graduate_level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__nameteacher = name

    @property
    def graduate_level(self):
        return self.__graduate_level

    @graduate_level.setter
    def graduate_level(self, graduate_level):
        self.__graduate_level = graduate_level
