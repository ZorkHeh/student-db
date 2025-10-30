from domain.errors import ValidationError, DataBaseError
from domain.models import Student

from storage.repository import (get_all_students,
                                add_student,
                                search_student_by_last,
                                search_student_by_pesel,
                                delete_user_by_student_id)

from validators.validator import validate_pesel, validate_student_id, validate_gender

def services_get_all_students() -> list[list[str]]:
    students_cl: list[Student] = get_all_students()
    students_str: list[list[str]] = []
    for student in students_cl:
        students_str.append([
            student.first_name,
            student.last_name,
            student.address,
            student.student_id,
            student.pesel,
            student.gender
        ])

    return students_str

def services_search_student_by_last(last: str) -> list[list[str]]:
    students: list[Student] = search_student_by_last(last)
    students_str: list[list[str]] = []
    if students:
        for student in students:
            students_str.append([
                student.first_name,
                student.last_name,
                student.address,
                student.student_id,
                student.pesel,
                student.gender
            ])
        return students_str
    else:
        return []


def services_search_student_by_pesel(pesel: str) -> list[str] | None:
    student: Student = search_student_by_pesel(pesel)
    if student:
        return [
            student.first_name,
            student.last_name,
            student.address,
            student.student_id,
            student.pesel,
            student.gender
        ]
    else:
        return None

def services_delete_user_by_student_id(student_id: str) -> bool:
    return delete_user_by_student_id(student_id)

def services_add_student(first_name: str, last_name: str, address: str,
                         student_id: str, pesel: str, gender: str) -> list[ValidationError] | list[None]:
    flag: bool = False

    errors: list[ValidationError | DataBaseError] = []


    if validate_pesel(pesel):
        errors.append(ValidationError("pesel"))
    if validate_gender(gender):
        errors.append(ValidationError("gender"))
    if validate_student_id(student_id):
        errors.append(ValidationError("student_id"))

    if not errors:
        student: Student = Student(first_name=first_name, last_name=last_name, address=address,
                          student_id=student_id, pesel=pesel, gender=gender)
        is_added: bool = add_student(student)

    return errors
