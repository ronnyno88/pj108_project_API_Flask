from ..models import course_model
from api import db

def create_course(course):
    course_db = course_model.Course(name=course.name,
                                    workload=course.workload,
                                    discipline=course.discipline)

    db.session.add(course_db)
    db.session.commit()
    return course_db


def list_courses():
    courses = course_model.Course.query.all()
    return courses


def list_course(id_course):
    course = course_model.Course.query.filter_by(id_course=id_course).first()
    return course


def update_course(previous_course, new_course):
    previous_course.name_course = new_course.name_course
    previous_course.desc_course = new_course.desc_course
    previous_course.workload = new_course.workload
    previous_course.discipline = new_course.discipline
    db.session.commit()


def delete_course(course):
    db.session.delete(course)
    db.session.commit()
