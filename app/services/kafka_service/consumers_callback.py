import os
import toolz as t
from kafka import KafkaConsumer
import app.db.postgres.repositories.students_repository as students_repo
import app.db.postgres.repositories.students_lifestyle_repository as students_lifestyle_repo
import app.db.postgres.repositories.students_course_performance_repository as students_course_performance_repo
import app.db.postgres.repositories.students_reviews_repository as students_reviews_repo
import app.db.postgres.repositories.courses_repository as courses_repo
import app.db.postgres.repositories.departments_repository as departments_repo
import app.db.postgres.repositories.teachers_repository as teachers_repo
import app.db.postgres.repositories.course_classes_repository as course_classes_repo
from app.db.postgres.models import Student, StudentLifestyle, StudentCoursePerformance, StudentAppReview, Course, \
    Teacher, Department, CourseClass, StudentTeacherClass

students_topic = os.environ["STUDENTS_TOPIC"]


def new_students(messages: KafkaConsumer):
    for message in messages:
        try:
            students = [Student(**s) for s in message.value]
            students_repo.insert_range(students)
        except Exception as e:
            print(e)
    print("complete insert students")


def new_students_lifestyle(messages: KafkaConsumer):
    for message in messages:
        try:
            students_lifestyle = [StudentLifestyle(
                study_Hours_Per_Day=s['Study_Hours_Per_Day'],
                extracurricular_Hours_Per_Day=s['Extracurricular_Hours_Per_Day'],
                sleep_Hours_Per_Day=s['Sleep_Hours_Per_Day'],
                social_Hours_Per_Day=s['Social_Hours_Per_Day'],
                physical_Activity_Hours_Per_Day=s['Physical_Activity_Hours_Per_Day'],
                GPA=s['GPA'],
                stress_Level=s['Stress_Level'],
                student_id=s['Student_ID'],
            ) for s in message.value]
            students_lifestyle_repo.insert_range(students_lifestyle)
        except Exception as e:
            print(e)
    print("complete insert students_lifestyle")


def new_students_course_performance(messages: KafkaConsumer):
    for message in messages:
        try:
            students_course_performance = [
                StudentCoursePerformance(
                    current_grade=s['current_grade'],
                    attendance_rate=s['attendance_rate'],
                    assignments_completed=s['assignments_completed'],
                    missed_deadlines=s['missed_deadlines'],
                    participation_score=s['participation_score'],
                    midterm_grade=s['midterm_grade'],
                    study_group_attendance=s['study_group_attendance'],
                    office_hours_visits=s['office_hours_visits'],
                    extra_credit_completed=s['extra_credit_completed'],
                    student_id=s['student_id'],
                    course_id=courses_repo.get_or_insert(Course(name=s['course_name'])).id
                ) for s in message.value]
            students_course_performance_repo.insert_range(students_course_performance)
        except Exception as e:
            print(e)
    print("complete insert students_course_performance")


def new_students_reviews(messages: KafkaConsumer):
    for message in messages:
        try:
            students_reviews = [StudentAppReview(
                uuid=s['review_id'],
                content=s['content'],
                score=s['score'],
                thumbs_up_count=s['thumbs_up_count'],
                review_created_version=s['review_created_version'],
                date_time=s['date_time'],
                app_version=s['app_version'],
                student_id=s['student_id'],
            ) for s in message.value]
            students_reviews_repo.insert_range(students_reviews)
        except Exception as e:
            print(e)
    print("complete insert students_reviews")


def new_teachers(messages: KafkaConsumer):
    for message in messages:
        try:
            teachers = [
                Teacher(
                    teacher_code=t['id'],
                    name=t['name'],
                    title=t['title'],
                    office=t['office'],
                    email=t['email'],
                    department_id=departments_repo.get_or_insert(Department(name=t['department'])).id
                ) for t in message.value]
            teachers_repo.insert_range(teachers)
        except Exception as e:
            print(e)
    print("complete insert students_course_performance")


def new_course_classes(messages: KafkaConsumer):
    for message in messages:
        try:
            course_classes = [
                CourseClass(
                    class_code=c['id'],
                    section=c['section'],
                    semester=c['semester'],
                    room=c['room'],
                    schedule=c['schedule'],
                    course_id=courses_repo.get_or_insert(Course(name=c['course_name'])).id
                ) for c in message.value]
            course_classes_repo.insert_range(course_classes)
        except Exception as e:
            print(e)
    print("complete insert students_course_performance")


def new_relations(messages: KafkaConsumer):
    for message in messages:
        try:
            student_teacher_class = [
                StudentTeacherClass(
                    enrollment_date=r['enrollment_date'],
                    relationship_type=r['relationship_type'],
                    student_id=students_repo.find_by_id(r['student_id']).id,
                    course_class_id=course_classes_repo.find_by_code(r['class_id']).id,
                    teacher_id=teachers_repo.find_by_code(r['teacher_id']).id
                ) for r in message.value]
            course_classes_repo.insert_range(student_teacher_class)
        except Exception as e:
            print(e)
    print("complete insert students_course_performance")
