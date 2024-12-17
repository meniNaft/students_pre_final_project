from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.db.postgres.models import Base


class StudentAppReview(Base):
    __tablename__ = 'students_app_review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String, unique=True, autoincrement=True)
    content = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    thumbs_up_count = Column(Integer, nullable=False)
    review_created_version = Column(String(200), nullable=False)
    date_time = Column(String, nullable=False)
    app_version = Column(String(200), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    student = relationship("Student", uselist=False, back_populates="students_app_review")
