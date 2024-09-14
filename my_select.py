from ast import Sub
from sqlalchemy import and_, func, desc, select
from pprint import pprint

from database import session
from models import Teacher, Grade, Group, Student, Subject



def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = session.query(Student.id, Student.full_name, func.round(func.avg(Grade.grade), 2).label("avarage"))\
        .select_from(Grade).join(Student)\
        .group_by(Student.id)\
        .order_by(desc("avarage")).limit(5).all()
    return result

def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = session.query(Student.id, Student.full_name, func.round(func.avg(Grade.grade), 2).label("avarage"))\
        .select_from(Student).join(Grade)\
        .group_by(Student.id).where(Grade.subject_id == 1)\
        .order_by(desc("avarage")).first()
    return result


def select_3():
    # Знайти середній бал у групах з певного предмета.
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avarage"), func.count(Grade.grade), Subject.name, Group.name)\
        .select_from(Student).join(Grade).join(Group).join(Subject)\
        .group_by(Group.name, Subject.name).filter(Grade.subject_id==1).all()
    return result 

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avarage")).select_from(Grade).all()
    return result

def select_5():
    # Знайти які курси читає певний викладач.
    result = session.query(Teacher.full_name, Subject.name)\
        .select_from(Subject).join(Teacher).filter(Teacher.id == 2).all()
    return result

def select_6():
    # Знайти список студентів у певній групі.
    return session.query(Student.full_name, Group.name)\
        .select_from(Student).join(Group).filter(Group.id==1).all()

def select_7():
    # Знайти оцінки студентів у окремій групі з певного предмета.
    return session.query(Grade.grade, Subject.name, Student.full_name, Group.name)\
        .select_from(Student).join(Grade).join(Group).join(Subject)\
        .filter(and_(Subject.id==1, Group.id==1)).all()
        
def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    return session.query(func.round(func.avg(Grade.grade), 2).label("avarage"), Teacher.full_name)\
        .select_from(Grade).join(Subject).join(Teacher)\
        .filter(Teacher.id==2).group_by(Teacher.full_name).all()
        
def select_9():
    # Знайти список курсів, які відвідує певний студент
    return session.query(Subject.name, Student.full_name)\
        .select_from(Student).join(Grade).join(Subject).filter(Student.id==1)\
        .group_by(Subject.name, Student.full_name).all()
        
def select_10():
    # Список курсів, які певному студенту читає певний викладач
    return session.query(Subject.name, Student.full_name, Teacher.full_name).select_from(Student).join(Grade).join(Subject).join(Teacher)\
        .filter(and_(Student.id==1, Teacher.id==2))\
        .group_by(Subject.name, Student.full_name, Teacher.full_name).all()
    
def select_11():
    # Середній бал, який певний викладач ставить певному студентові.
    return session.query(func.round(func.avg(Grade.grade), 2).label("avarage"), Student.full_name, Teacher.full_name)\
        .select_from(Student).join(Grade).join(Subject).join(Teacher)\
        .filter(and_(Student.id==1, Teacher.id==2))\
        .group_by(Student.full_name, Teacher.full_name).all()

def select_12():
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    return session.query(Grade.grade, Student.full_name, Group.name, Subject.name, Grade.grade_dete)\
        .select_from(Student).join(Grade).join(Subject).join(Group)\
        .filter(and_(Group.id==1, Subject.id==1, Grade.grade_dete == (
            select(func.max(Grade.grade_dete)).join(Student)\
            .filter(and_(Group.id==1, Subject.id==1)).scalar_subquery()
        ))).all()

if __name__=="__main__":
    pprint(select_12())
    

