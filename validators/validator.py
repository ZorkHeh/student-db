from domain.errors import ValidationError


def validate_pesel(pesel: str) -> None | ValidationError:

    if len(pesel) != 11 or not pesel.isdigit():
        return ValidationError("pesel")

    digits = list(map(int, pesel))
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    s = sum(w * d for w, d in zip(weights, digits[:10]))
    control = (10 - (s % 10)) % 10
    if control == digits[10]:
        return None
    else:
        return ValidationError("pesel")

def validate_student_id(student_id: str) -> None | ValidationError:
    if len(student_id) == 5 and student_id.isdigit():
        return None
    else:
        return ValidationError("student_id")

def validate_gender(gender: str) -> None | ValidationError:
    if len(gender) == 1:
        if gender == 'm' or gender == 'f':
            return None
        else:
            return ValidationError("gender")
    else:
        return ValidationError("gender")
