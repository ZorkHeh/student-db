from core.config import DATABASE

from domain.models import Student
from domain.errors import DataBaseError


from storage.json_repository import get_all_students as js_get_all_students
from storage.json_repository import add_student as js_add_student
from storage.json_repository import search_student_by_last as js_search_student_by_last
from storage.json_repository import search_student_by_pesel as js_search_student_by_pesel
from storage.json_repository import delete_user_by_student_id as js_delete_user_by_student_id


def get_all_students() -> list[Student]:
    if DATABASE == "json":
        return js_get_all_students()
    else:
        raise Exception(f"Database {DATABASE} is not supported.")


def add_student(student: Student) -> bool | DataBaseError:

    if DATABASE == "json":
        return js_add_student(student)
    else:
        raise DataBaseError()

def search_student_by_last(last_name: str) -> list[Student] | list[None]:
    if DATABASE == "json":
        return js_search_student_by_last(last_name)
    else:
        raise DataBaseError()

def search_student_by_pesel(pesel: str) -> Student | None:
    if DATABASE == "json":
        return js_search_student_by_pesel(pesel)
    else:
        raise DataBaseError()

def delete_user_by_student_id(student_id: str) -> bool:
    if DATABASE == "json":
        return js_delete_user_by_student_id(student_id)
    else:
        raise DataBaseError()
