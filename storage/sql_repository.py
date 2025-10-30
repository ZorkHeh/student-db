from domain.models import DbStudent


def get_all_students():
    query = DbStudent.select()
    return query

def get_student_by_pesel(pesel: str):
    query = DbStudent.get(pesel=pesel)
    return query

def get_student_by_last(last: str):
    query = DbStudent.select().where(DbStudent.last_name == last)
    return query

def add_student(first: str, last: str, address: str, album_number: int, pesel: str, gender: str):
    DbStudent.create(first_name=first, last_name=last, address=address,
                            album_number=album_number, pesel=pesel, gender=gender)
    return True

def delete_student_by_id(album_number: int) -> bool:
    student = DbStudent.get(album_number=album_number)
    return student.delete_instance()


