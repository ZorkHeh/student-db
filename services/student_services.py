from domain.models import Student

from storage.repository import (get_all_students,
                                add_student,
                                search_student_by_last,
                                search_student_by_pesel,
                                delete_user_by_student_id)


def services_get_all_students() -> list[Student]:
    return get_all_students()

def services_search_student_by_last(last: str) -> list[Student] | list[None]:
    return search_student_by_last(last)

def services_search_student_by_pesel(pesel: str) -> Student | None:
    return search_student_by_pesel(pesel)

def services_delete_user_by_student_id(student_id: str) -> bool:
    return delete_user_by_student_id(student_id)
