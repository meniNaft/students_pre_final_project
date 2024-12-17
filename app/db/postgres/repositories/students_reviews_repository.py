from app.db.postgres.models import Student, StudentAppReview
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(students_reviews: list[StudentAppReview]):
    res = generic_repo.insert_range(students_reviews)
    return res
