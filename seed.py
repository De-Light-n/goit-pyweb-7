import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from database import session
from models import Teacher, Grade, Group, Student, Subject

faker = Faker("uk-UA")

def add_groups():
    group_names = ["Group A", "Group B", "Group C"]
    for group_name in group_names:
        group = Group(name=group_name)
        session.add(group)
        
def add_teachers():
    for i in range(5):
        teacher = Teacher(full_name=faker.name())
        session.add(teacher)
        
def add_subjects():
    subject_names = ["Mathematics", "Physics", "History", "Literature", "Biology", "Chemistry", "Computer Science", "Art"]
    teachers = session.query(Teacher).all()
    for sub in subject_names:
        subject = Subject(name=sub, teacher_id=random.choice(teachers).id)
        session.add(subject)

def add_students():
    groups = session.query(Group).all()
    for i in range(30):
        student = Student(full_name=faker.name(), group_id = random.choice(groups).id)
        session.add(student)
        
def add_grades():
    subjects = session.query(Subject).all()
    students = session.query(Student).all()
    for student in students:
        for i in range(random.randint(15,20)):
            grade = Grade(grade=random.randint(2,10),
                          grade_dete=faker.date_this_month(),
                          student_id=student.id,
                          subject_id=random.choice(subjects).id)
            session.add(grade)

if __name__=="__main__":
    try:
        add_groups()
        add_teachers()
        session.commit()
        add_subjects()
        add_students()
        session.commit()
        add_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
        
    
            
