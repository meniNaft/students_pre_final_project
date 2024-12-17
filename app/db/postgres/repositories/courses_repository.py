from app.db.postgres.database_config import session_maker
from app.db.postgres.models import Student, Course
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(courses: list[Course]):
    return generic_repo.insert_range(courses)


def get_or_insert(course: Course) -> Course:
    with session_maker() as session:
        found = session.query(Course).filter(Course.name == course.name).one_or_none()
        if found:
            return found
        else:
            session.add(course)
            session.commit()
            session.refresh(course)
            return course
