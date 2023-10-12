#this classe is a entity used in methodos of services in API

class Course:
    def __init__(self, name, workload, discipline):
        self.__name = name
        self.__workload = workload
        self.__discipline = discipline

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def workload(self):
        return self.__workload

    @workload.setter
    def workload(self, workload):
        self.__workload = workload

    @property
    def discipline(self):
        return self.__discipline

    @discipline.setter
    def discipline(self, discipline):
        self.__discipline = discipline
