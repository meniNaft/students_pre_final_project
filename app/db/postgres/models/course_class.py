from turtle import ondrag

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.postgres.models import Base


class CourseClass(Base):
    __tablename__ = 'course_classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    section = Column(Integer, nullable=False)
    semester = Column(String(200), nullable=False)
    room = Column(String(200), nullable=False)
    schedule = Column(String(200), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    course = relationship("Course", uselist=False, back_populates="classes")
    student_teacher_class_list = relationship("StudentTeacherClass", back_populates="course_class")
