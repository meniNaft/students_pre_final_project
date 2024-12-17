from app.db.postgres.models import StudentCoursePerformance
import app.db.postgres.repositories.generic_repository as generic_repo


def insert_range(students_course_performance: list[StudentCoursePerformance]):
    return generic_repo.insert_range(students_course_performance)
