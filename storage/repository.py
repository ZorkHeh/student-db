from peewee import IntegrityError

from core.config import DATABASE

from domain.models import Student
from domain.errors import DataBaseError


from storage.json_repository import get_all_students as js_get_all_students
from storage.json_repository import add_student as js_add_student
from storage.json_repository import search_student_by_last as js_search_student_by_last
from storage.json_repository import search_student_by_pesel as js_search_student_by_pesel
from storage.json_repository import delete_user_by_student_id as js_delete_user_by_student_id

from storage.sql_repository import get_all_students as db_get_all_students
from storage.sql_repository import add_student as db_add_student
from storage.sql_repository import get_student_by_last as db_get_student_by_last
from storage.sql_repository import get_student_by_pesel as db_get_student_by_pesel
from storage.sql_repository import delete_student_by_id as db_delete_student_by_id



def get_all_students() -> list[Student]:
    if DATABASE == "json":
        return js_get_all_students()
    elif DATABASE == "sqlite":
        students: list[Student] = []
        query = db_get_all_students()
        for row in query:
            students.append(Student(
                last_name=row.last_name,
                first_name=row.first_name,
                address=row.address,
                student_id=row.student_id,
                pesel=row.pesel,
                gender=row.gender,
            ))
        return students
    else:
        raise Exception(f"Database {DATABASE} is not supported.")


def add_student(student: Student) -> bool:

    if DATABASE == "json":
        return js_add_student(student)
    elif DATABASE == "sqlite":
        try:
            return db_add_student(
                first=student.first_name,
                last=student.last_name,
                address=student.address,
                student_id=student.student_id,
                pesel=student.pesel,
                gender=student.gender,
            )

        except IntegrityError:
            return False
    else:
        raise DataBaseError()

def search_student_by_last(last_name: str) -> list[Student] | None:
    if DATABASE == "json":
        return js_search_student_by_last(last_name)
    elif DATABASE == 'sqlite':
        query = db_get_student_by_last(last_name)
        students: list[Student] = []
        for student in query:
            students.append(Student(
                first_name=student.first_name,
                last_name=student.last_name,
                address=student.address,
                student_id=student.student_id,
                pesel=student.pesel,
                gender=student.gender,
            ))
        if students:
            return students
        else:
            return None
    else:
        raise DataBaseError()

def search_student_by_pesel(pesel: str) -> Student | None:
    if DATABASE == "json":
        return js_search_student_by_pesel(pesel)
    elif DATABASE == 'sqlite':
        query = db_get_student_by_pesel(pesel)
        if query:
            return Student(
                first_name=query.first_name,
                last_name=query.last_name,
                address=query.address,
                student_id=query.student_id,
                pesel=query.pesel,
                gender=query.gender,
            )
        else:
            return None
    else:
        raise DataBaseError()

def delete_user_by_student_id(student_id: str) -> bool:
    if DATABASE == "json":
        return js_delete_user_by_student_id(student_id)
    elif DATABASE == "sqlite":
        return db_delete_student_by_id(student_id)
    else:
        raise DataBaseError()
