START_TEXT = """Welcome to the student DB"""

def main_loop() -> None:
    while True:
        choice = input(">>> ").lower()

        if choice == "q":
            break

        if choice == "add":
            cmd_get_new_user_student()
            continue
        if choice == "all":
            cmd_list_students()
            continue
        if choice == "delete":
            cmd_delete_by_student_id()
            continue
        if choice == "searchl":
            cmd_search_by_last_name()
            continue
        if choice == "searchp":
            cmd_search_by_pesel()
            continue
        if choice == "sbnamel":
            cmd_sort_by_last_name()
            continue
        if choice == "sbpesel":
            cmd_sort_by_pesel()
            continue


def cmd_start() -> None:
    print(START_TEXT)
    main_loop()


def cmd_get_new_user_student():
    first_name = input("first name: ")
    last_name = input("last name: ")
    address = input("address: ")
    student_id = input("student id: ")
    pesel = input("pesel: ")
    gender = input("gender: ")




def cmd_list_students() -> None:
    ...

def cmd_delete_by_student_id() -> None:
    ...

def cmd_search_by_last_name() -> None:
    ...

def cmd_search_by_pesel() -> None:
    ...

def cmd_sort_by_last_name() -> None:
    ...

def cmd_sort_by_pesel() -> None:
    ...