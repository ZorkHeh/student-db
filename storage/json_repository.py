import json

from domain.models import Student
from core.config import JSON_PATH



def get_all_students() -> list[Student]:
    students: list[Student] = []
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)

    for student in data:
        students.append(Student(
            first_name=student[0],
            last_name=student[1],
            address=student[2],
            student_id=student[3],
            pesel=student[4],
            gender=student[5]
        ))
    return students

def add_student(student: Student) -> None:
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)

    data.append([
        student.first_name,
        student.last_name,
        student.address,
        student.student_id,
        student.pesel,
        student.gender
    ])

    with open(JSON_PATH, 'w') as file:
        json.dump(data, file)

def search_student_by_last(last_name: str) -> list[Student] | list[None]:
    with open(JSON_PATH, 'r') as file:
        data = json.load(file)

    matches: list[Student] = []
    for student in data:
        if last_name.lower() in student[1].lower():
            matches.append(Student(
                first_name=student[0],
                last_name=student[1],
                address=student[2],
                student_id=student[3],
                pesel=student[4],
                gender=student[5]
            ))

    return matches

