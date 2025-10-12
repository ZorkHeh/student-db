def validate_pesel(pesel: str) -> bool:

    if len(pesel) != 11 or not pesel.isdigit():
        return False

    digits = list(map(int, pesel))
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    s = sum(w * d for w, d in zip(weights, digits[:10]))
    control = (10 - (s % 10)) % 10

    return control == digits[10]