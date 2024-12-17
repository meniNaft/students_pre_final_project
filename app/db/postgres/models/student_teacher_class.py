from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.postgres.models import Base


class StudentTeacherClass(Base):
    __tablename__ = 'student_teacher_class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship("Student", uselist=False, back_populates="student_teacher_class_list")
    course_class_id = Column(Integer, ForeignKey('course_classes.id', ondelete='CASCADE'))
    course_class = relationship("CourseClass", uselist=False, back_populates="student_teacher_class_list")
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship("Teacher", uselist=False, back_populates="student_teacher_class_list")



    enrollment_date = Column(DateTime, nullable=False)
    relationship_type = Column(String(100), nullable=False)
    # teachers = relationship("Teacher", back_populates="department")



