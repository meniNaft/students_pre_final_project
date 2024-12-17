from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.postgres.models import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_code = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    office = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id', ondelete='CASCADE'))
    department = relationship("Department", uselist=False, back_populates="teachers")
    student_teacher_class_list = relationship("StudentTeacherClass", back_populates="teacher")
