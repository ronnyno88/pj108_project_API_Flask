class Discipline:
    def __init__(self, description, teachers):
        self.__description = description
        self.__teachers = teachers

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        self.__teachers = teachers
