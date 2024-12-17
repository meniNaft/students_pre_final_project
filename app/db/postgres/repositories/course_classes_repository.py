from app.db.postgres.database_config import session_maker
from app.db.postgres.models import CourseClass
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(course_classes: list[CourseClass]):
    return generic_repo.insert_range(course_classes)


def find_by_code(code: str):
    with session_maker() as session:
        return session.query(CourseClass).filter(CourseClass.class_code == code).first()
