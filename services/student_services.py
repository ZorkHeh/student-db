from domain.models import Student

from storage.repository import (get_all_students,
                                add_student,
                                search_student_by_last,
                                search_student_by_pesel,
                                delete_user_by_student_id)

from validators.pesel import validate_pesel

def services_get_all_students() -> list[Student]:
    return get_all_students()

def services_search_student_by_last(last: str) -> list[Student] | list[None]:
    return search_student_by_last(last)

def services_search_student_by_pesel(pesel: str) -> Student | None:
    return search_student_by_pesel(pesel)

def services_delete_user_by_student_id(student_id: str) -> bool:
    return delete_user_by_student_id(student_id)

def services_add_student(first_name: str, last_name: str, address: str,
                         student_id: str, pesel: str, gender: str) -> bool:
    flag: bool = False
    is_valid_pesel = validate_pesel(pesel)
    if is_valid_pesel:
        student = Student(first_name=first_name,
                          last_name=last_name,
                          address=address,
                          student_id=student_id,
                          pesel=pesel,
                          gender=gender
                          )

        flag = add_student(student)

    return flag