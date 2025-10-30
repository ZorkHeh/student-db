class AppError(Exception):
    pass


class ValidationError(AppError):
    def __init__(self, field: str) -> None:
        message = f"Validation error: {field}"
        super().__init__(message)


class DataBaseError(AppError):
    def __init__(self) -> None:
        message = f"Cant access the Data Base"
        super().__init__(message)



class UniquenessError(AppError):
    pass

