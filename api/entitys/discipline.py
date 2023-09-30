#this classe is a entity used in methodos of services in API
#describe classes of business model of API
class Discipline:
    #not necessary get id because will be automatic inserted
    def __init__(self, name_discipline, desc_discipline, teachers):
        self.__name_discipline = name_discipline
        self.__desc_discipline = desc_discipline
        self.__teachers = teachers

    #this methodos are getters e setters, retuns and modify the parameters
    @property
    def name_discipline(self):
        return self.__name_discipline

    @name_discipline.setter
    def name_discipline(self, name_discipline):
        self.__name_discipline = name_discipline

    @property
    def desc_discipline(self):
        return self.__desc_discipline

    @desc_discipline.setter
    def desc_discipline(self, desc_discipline):
        self.__desc_discipline = desc_discipline

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        self.__teachers = teachers
