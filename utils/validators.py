def validate_pesel(pesel):
    """
    Validate PESEL number according to Polish rules.
    Returns:
        bool: True if valid, False otherwise
    """
    # Length must be 11
    if len(pesel) != 11:
        return False

    # Must contain only digits
    if not pesel.isdigit():
        return False

    # Checksum validation
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    # Calculate checksum
    checksum = 0
    for i in range(10):
        checksum += int(pesel[i]) * weights[i]

    checksum = checksum % 10
    checksum = (10 - checksum) % 10

    # Compare with the 11th digit (control digit)
    control_digit = int(pesel[10])

    if checksum != control_digit:
        return False


    return True
