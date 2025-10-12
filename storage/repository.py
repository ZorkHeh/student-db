from domain.models import Student

from json_repository import get_all_students as js_get_all_students


def get_all_students() -> list[Student]:

    return js_get_all_students()