from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.postgres.models import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(200), nullable=False)
    student_teacher_class_list = relationship("StudentTeacherClass", back_populates="student")
    student_lifestyle = relationship("StudentLifestyle", uselist=False, back_populates="student")
    students_course_performance = relationship("StudentCoursePerformance", back_populates="student")
    students_app_review = relationship("StudentAppReview", back_populates="student")
