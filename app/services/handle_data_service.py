import os
import toolz as t
from typing import List, Callable
import app.services.read_sourse_data_files_service as load_data_service
from app.services.kafka_service.producer import producer_send_message

course_classes_topic = os.environ["COURSE_CLASSES_TOPIC"]
teachers_topic = os.environ["TEACHERS_TOPIC"]
student_teacher_class_topic = os.environ["STUDENT_TEACHER_CLASS_TOPIC"]
students_topic = os.environ["STUDENTS_TOPIC"]
students_lifestyle_topic = os.environ["STUDENTS_LIFESTYLE_TOPIC"]
students_course_performance_topic = os.environ["STUDENTS_COURSE_PERFORMANCE_TOPIC"]
students_reviews_topic = os.environ["STUDENTS_REVIEWS_TOPIC"]


def load_source_files():
    students = load_data_service.read_csv('./data/students-profiles.csv')
    students_lifestyle = load_data_service.read_csv('./data/student_lifestyle.csv')
    students_course_performance = load_data_service.read_csv('./data/student_course_performance.csv')
    students_reviews = load_data_service.read_csv('./data/reviews_with_students.csv')
    academic_network = load_data_service.read_json_file('./data/academic_network.json')

    students = students.drop(columns=['id']).to_dict(orient='records')
    produce_chunks(students, t.partial(action_producer, key="student_list", topic=students_topic), 100)
    print("inserting students")

    teachers = academic_network['teachers']
    produce_chunks(teachers, t.partial(action_producer, key="teacher_list", topic=teachers_topic), 100)
    print("inserting teachers")

    course_classes = academic_network['classes']
    produce_chunks(course_classes, t.partial(action_producer, key="course_class_list", topic=course_classes_topic), 100)
    print("inserting classes")

    relationships = academic_network['relationships']
    produce_chunks(relationships, t.partial(action_producer, key="relations", topic=student_teacher_class_topic), 100)
    print("inserting relations")

    students_lifestyle = students_lifestyle.to_dict(orient='records')
    produce_chunks(students_lifestyle, t.partial(action_producer, key="student_list", topic=students_lifestyle_topic), 100)
    print("inserting student_lifestyle")

    students_course_performance = students_course_performance.to_dict(orient='records')
    produce_chunks(students_course_performance, t.partial(action_producer, key="student_list", topic=students_course_performance_topic), 100)
    print("inserting students_course_performance")

    students_reviews[['app_version', 'review_created_version', 'content']] = students_reviews[
        ['app_version', 'review_created_version', 'content']].fillna('')
    students_reviews = students_reviews.to_dict(orient='records')
    produce_chunks(students_reviews, t.partial(action_producer, key="student_list", topic=students_reviews_topic), 1000)
    print("inserting students_reviews")

def action_producer(new_value, key, topic):
    producer_send_message(topic, new_value, key)


def produce_chunks(data: List, produce: Callable, chunks_size: int):
    [produce(item) for item in list(t.partition_all(chunks_size, data))]
