class Student:
    def __init__(self, first_name: str, last_name: str, address: str, student_id: str, pesel: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.student_id = student_id
        self.pesel = pesel
        self.gender = gender

    def __repr__(self):
        return f'<{self.first_name} {self.last_name} {self.address} {self.student_id} {self.pesel} {self.gender}>'