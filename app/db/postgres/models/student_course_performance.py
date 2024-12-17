from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.postgres.models import Base


class StudentCoursePerformance(Base):
    __tablename__ = 'students_course_performance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    current_grade = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    assignments_completed = Column(Integer, nullable=False)
    missed_deadlines = Column(Integer, nullable=False)
    participation_score = Column(Float, nullable=False)
    midterm_grade = Column(Float, nullable=False)
    study_group_attendance = Column(Integer, nullable=False)
    office_hours_visits = Column(Integer, nullable=False)
    extra_credit_completed = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship("Student", uselist=False, back_populates="students_course_performance")
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))
    course = relationship("Course", uselist=False, back_populates="students_course_performance")
