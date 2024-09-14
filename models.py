
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Date, ForeignKey, Integer, String

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column("id", Integer, primary_key=True)
    full_name = Column("fullname", String(150), nullable=False)
    
    
class Group(Base):
    __tablename__ = "groups"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(150), nullable=False)
    
class Student(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    full_name = Column("fullname", String(150), nullable=False)
    group_id = Column("group_id", ForeignKey("groups.id", ondelete="CASCADE", onupdate="CASCADE"))
    group = relationship('Group', backref='students')
    
class Subject(Base):
    __tablename__ = "subjects"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(150), nullable=False)
    teacher_id = Column("teacher_id", ForeignKey("teachers.id", ondelete='CASCADE', onupdate='CASCADE'))
    teacher = relationship('Teacher', backref='subject')
    
class Grade(Base):
    __tablename__ = "grades"
    id = Column("id", Integer, primary_key=True)
    grade = Column("grade", Integer, nullable=False)
    grade_dete = Column("date", Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    student = relationship('Student', backref='grade')
    subject = relationship('Subject', backref='grade')
    
    
    
    
