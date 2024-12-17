from app.db.postgres.database_config import session_maker
from app.db.postgres.models import Teacher
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(teachers: list[Teacher]):
    return generic_repo.insert_range(teachers)


def find_by_code(code: str):
    with session_maker() as session:
        return session.query(Teacher).filter(Teacher.teacher_code == code).first()

