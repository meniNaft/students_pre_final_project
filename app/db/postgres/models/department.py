from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.db.postgres.models import Base


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    teachers = relationship("Teacher", back_populates="department")
