from app.db.postgres.models import Student
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(students: list[Student]):
    return generic_repo.insert_range(students)
