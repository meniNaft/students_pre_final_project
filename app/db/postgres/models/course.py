from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.db.postgres.models import Base


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    classes = relationship("CourseClass", back_populates="course")
    students_course_performance = relationship("StudentCoursePerformance", back_populates="course")
