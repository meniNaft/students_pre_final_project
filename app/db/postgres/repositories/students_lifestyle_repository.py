from app.db.postgres.models import StudentLifestyle
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(students_lifestyle: list[StudentLifestyle]):
    return generic_repo.insert_range(students_lifestyle)
