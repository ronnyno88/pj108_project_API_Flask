#this classe is a entity used in methodos of services in API
#describe classes of business model of API
class Teacher:
    #not necessary get id because will be automatic inserted
    def __init__(self, name_teacher, age_teacher):
        self.__name_teacher = name_teacher
        self.__age_teacher = age_teacher

    #this methodos are getters e setters, retuns and modify the parameters
    @property
    def name_teacher(self):
        return self.__name_teacher

    @name_teacher.setter
    def name_teacher(self, name_teacher):
        self.__nameteacher = name_teacher

    @property
    def age_teacher(self):
        return self.__age_teacher

    @age_teacher.setter
    def age_teacher(self, age_teacher):
        self.__age_teacher = age_teacher
