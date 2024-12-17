import os
from threading import Thread
from app.db.postgres.database_config import init_postgres_db
from app.services.kafka_service.admin import init_topics
from app.services.kafka_service.consumer import main_consumer
import app.services.kafka_service.consumers_callback as consumers_callback
from app.services.handle_data_service import load_source_files

teachers_topic = os.environ["TEACHERS_TOPIC"]
course_classes_topic = os.environ["COURSE_CLASSES_TOPIC"]
student_teacher_class_topic = os.environ["STUDENT_TEACHER_CLASS_TOPIC"]
students_topic = os.environ["STUDENTS_TOPIC"]
students_lifestyle_topic = os.environ["STUDENTS_LIFESTYLE_TOPIC"]
students_course_performance_topic = os.environ["STUDENTS_COURSE_PERFORMANCE_TOPIC"]
students_reviews_topic = os.environ["STUDENTS_REVIEWS_TOPIC"]


if __name__ == '__main__':
    init_topics()
    init_postgres_db()
    Thread(
        name="Consume_teachers",
        target=lambda: main_consumer(teachers_topic, consumers_callback.new_teachers)
    ).start()
    Thread(
        name="Consume_course_classes",
        target=lambda: main_consumer(course_classes_topic, consumers_callback.new_course_classes)
    ).start()
    Thread(
        name="Consume_student_teacher_class",
        target=lambda: main_consumer(student_teacher_class_topic, consumers_callback.new_relations)
    ).start()
    Thread(
        name="Consume_students",
        target=lambda: main_consumer(students_topic, consumers_callback.new_students)
    ).start()
    Thread(
        name="Consume_students_lifestyle",
        target=lambda: main_consumer(students_lifestyle_topic, consumers_callback.new_students_lifestyle)
    ).start()
    Thread(
        name="Consume_students_course_performance",
        target=lambda: main_consumer(students_course_performance_topic, consumers_callback.new_students_course_performance)
    ).start()
    Thread(
        name="Consume_students_reviews",
        target=lambda: main_consumer(students_reviews_topic, consumers_callback.new_students_reviews)
    ).start()
    load_source_files()
