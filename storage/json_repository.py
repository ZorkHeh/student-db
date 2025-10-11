import json

from domain.models import Student



def get_all_students() -> list[Student]:
    students: list[Student] = []
    with open('data.json', 'r') as file:
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
    with open('data.json', 'r') as file:
        data = json.load(file)

    data.append([
        student.first_name,
        student.last_name,
        student.address,
        student.student_id,
        student.pesel,
        student.gender
    ])

    with open('data.json', 'w') as file:
        json.dump(data, file)
