from rich.console import Console
from rich.table import Table

from services.student_services import *


START_TEXT = """
Welcome to the student DB
Print 
[add] to add student
[all] to get all student
[search] to search for a student
[delete] to delete a student
"""

columns: list[str] = ['name', 'surname', 'address', 'student_id', 'pesel', 'gender']

def print_table(students: list[list[str]]) -> None:
    my_console = Console()

    table = Table(title="Students")
    for column in columns:
        table.add_column(column)
    for student in students:
        table.add_row(*student)

    my_console.print(table)


def main_loop() -> None:
    while True:
        choice = input(">>> ").lower()

        if choice == "q":
            break

        if choice == "add":
            cmd_add_student()
            continue
        if choice == "all":
            cmd_list_students()
            continue
        if choice == "delete":
            cmd_delete_by_student_id()
            continue
        if choice == "search":
            cmd_search()
            continue
        if choice == "sort":
            cmd_sort()
            continue

def cmd_start() -> None:
    print(START_TEXT)
    main_loop()


def cmd_add_student() -> None:
    first_name: str = input("first name: ")
    last_name: str = input("last name: ")
    address: str = input("address: ")
    student_id: str = input("student id: ")
    pesel: str = input("pesel: ")
    gender: str = input("gender: ")


    errors: list[ValidationError] | list[None] = services_add_student(first_name, last_name, address, student_id,
                                                         pesel, gender)

    if not errors:
        print("Student added successfully")
    else:
        print(*errors)



def cmd_list_students() -> None:
    students: list[list[str]] = services_get_all_students()

    print_table(students)


def cmd_delete_by_student_id() -> None:
    student_id: str = input("student id: ")

    is_deleted: bool = services_delete_user_by_student_id(student_id)
    if is_deleted:
        print("Student deleted successfully")
    else:
        print("Student not found")

def cmd_search() -> None:
    print("Enter 'pesel' to search by pesel or enter 'last' to search by lst name")
    while True:
        choice = input(">>> ").lower()
        if choice == "pesel":
            cmd_search_by_pesel()
            break
        if choice == "last":
            cmd_search_by_last_name()
            break

def cmd_search_by_last_name() -> None:
    last_name: str = input("last name: ")
    students = services_search_student_by_last(last_name)
    print_table(students)

def cmd_search_by_pesel() -> None:
    pesel: str = input("pesel: ")
    student = services_search_student_by_pesel(pesel)
    if student:
        print_table([student])
    else:
        print("Student is not found")

def cmd_sort() -> None:
    print("Enter 'pesel to sort by pesel")
    while True:
        choice = input(">>> ").lower()
        if choice == "last":
            cmd_sort_by_last_name()
            break
        if choice == "pesel":
            cmd_sort_by_pesel()

def cmd_sort_by_last_name() -> None:
    ...

def cmd_sort_by_pesel() -> None:
    ...