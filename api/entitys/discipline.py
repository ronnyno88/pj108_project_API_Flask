#this classe is a entity used in methodos of services in API
class Discipline:
    def __init__(self, name_discipline, desc_discipline, ):
        self.__name_discipline = name_discipline
        self.__desc_discipline = desc_discipline

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
