from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.postgres.models import Base


class StudentLifestyle(Base):
    __tablename__ = 'students_lifestyle'
    id = Column(Integer, primary_key=True, autoincrement=True)
    study_Hours_Per_Day = Column(Float, nullable=False)
    extracurricular_Hours_Per_Day = Column(Float, nullable=False)
    sleep_Hours_Per_Day = Column(Float, nullable=False)
    social_Hours_Per_Day = Column(Float, nullable=False)
    physical_Activity_Hours_Per_Day = Column(Float, nullable=False)
    GPA = Column(Float, nullable=False)
    stress_Level = Column(String(100), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship("Student", uselist=False, back_populates="student_lifestyle")
