from ..models import course_model
from api import db

#methods for manipulate DB
def create_course(course):
    course_db = course_model.CourseModel(name_course=course.name_course, desc_course=course.desc_course,
                                      publish_course=course.publish_course)
    db.session.add(course_db)
    db.session.commit()
    return course_db

def list_courses():
    courses = course_model.CourseModel.query.all()
    return courses

def list_course(id_course):
    course = course_model.CourseModel.query.filter_by(id_course=id_course).first()
    return course

def update_course(previous_course, new_course):
    previous_course.name_course = new_course.name_course
    previous_course.desc_course = new_course.desc_course
    previous_course.publish_course = new_course.publish_course
    db.session.commit()

def delete_course(course):
    db.session.delete(course)
    db.session.commit()