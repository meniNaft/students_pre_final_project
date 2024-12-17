from sqlalchemy.orm import declarative_base

Base = declarative_base()
from .teacher import Teacher
from .course import Course
from .course_class import CourseClass
from .department import Department
from .student import Student
from .student_app_review import StudentAppReview
from .student_course_performance import StudentCoursePerformance
from .student_lifestyle import StudentLifestyle
from .student_teacher_class import StudentTeacherClass
