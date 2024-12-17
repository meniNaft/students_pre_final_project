from app.db.postgres.models import Teacher
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(teachers: list[Teacher]):
    return generic_repo.insert_range(teachers)
