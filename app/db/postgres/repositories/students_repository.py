from app.db.postgres.database_config import session_maker
from app.db.postgres.models import Student
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(students: list[Student]):
    return generic_repo.insert_range(students)


def find_by_id(student_id: str):
    with session_maker() as session:
        return session.query(Student).filter(Student.id == student_id).first()
