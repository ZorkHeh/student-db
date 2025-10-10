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
        if choice == "search":
            cmd_search()
            continue
        if choice == "sort":
            cmd_sort()
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
    ...

def cmd_search_by_pesel() -> None:
    ...

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