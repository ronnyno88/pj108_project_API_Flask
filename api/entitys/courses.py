#this classe is a entity used in methodos of services in API
class Course:
    def __init__(self, name_course, desc_course, publish_course):
        self.__name_course = name_course
        self.__desc_course = desc_course
        self.__publish_course = publish_course

    #this methodos are getters e setters, retuns and modify the parameters
    @property
    def name_course(self):
        return self.__name_course

    @name_course.setter
    def name_course(self, name_course):
        self.__name_course = name_course

    @property
    def desc_course(self):
        return self.__desc_course

    @desc_course.setter
    def desc_course(self, desc_course):
        self.__desc_course = desc_course

    @property
    def publish_course(self):
        return self.__publish_course

    @publish_course.setter
    def publish_course(self, publish_course):
        self.__publish_course = publish_course
