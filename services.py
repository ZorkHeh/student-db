from peewee import fn

from models import Student
from utils.validators import validate_pesel  


class ValidationError(Exception):
    pass


class UniquenessError(Exception):
    pass


class StudentNotFound(Exception):
    pass


class StudentService:
    """
    Business logic layer for student operations.
    Handles all CRUD operations and validation.
    """

    def _check_pesel_exists(self, pesel, exclude_student_id=None):
        """Helper to check if PESEL is already taken by another student."""
        existing = Student.get_or_none(Student.pesel == pesel)
        if existing and existing.student_id != exclude_student_id:
            return True
        return False

    def _check_student_id_exists(self, student_id):
        """Helper to check if student ID already exists."""
        return Student.get_or_none(Student.student_id == student_id) is not None

    def add_student(self, first_name, last_name, address, student_id, pesel, gender):
        """
        Add a new student to the database.
        Returns created instance.
        """
        is_pesel_valid = validate_pesel(pesel)
        if not is_pesel_valid:
            raise ValidationError(f"Pesel {pesel} is not valid")

        if self._check_student_id_exists(student_id):
            raise UniquenessError(f"Student Id {student_id} exists")

        if self._check_pesel_exists(pesel):
            raise UniquenessError(f"Pesel {pesel} exists")
        student = Student.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            student_id=student_id,
            pesel=pesel,
            gender=gender
        )
        return student

    def get_all_students(self):
        students = Student.select()
        return list(students)

    def search_by_last_name(self, last_name: str):
        """
        Search students by last name (can return multiple).
        """

        students = Student.select().where(fn.LOWER(Student.last_name).contains(last_name.lower()))
        return list(students)

    def search_by_pesel(self, pesel: str):
        """
        Search student by PESEL (returns one or None).
        """
        student = Student.get_or_none(Student.pesel == pesel)
        return student

    def get_students_sorted_by_pesel(self):
        return list(Student.select().order_by(Student.pesel))

    def get_students_sorted_by_last_name(self):
        return list(Student.select().order_by(Student.last_name))

    def delete_student(self, student_id):
        """
        Delete a student by student ID.
        """
        student = Student.get_or_none(Student.student_id == student_id)
        if student:
            student.delete_instance()
            return True
        else:
            raise StudentNotFound("Student not found")

    def get_student_by_id(self, student_id):
        """
        Get a single student by student ID.
        Returns the student object or None if not found.
        """
        return Student.get_or_none(Student.student_id == student_id)

    def update_student(self, student_id, **kwargs):
        """
        Update student information by student ID.
        """
        # Find the student
        student = self.get_student_by_id(student_id)
        if not student:
            raise StudentNotFound(f"Student with ID {student_id} not found")

        # If updating PESEL, validate it first
        if 'pesel' in kwargs:
            new_pesel = kwargs['pesel']

            # Validate PESEL
            if not validate_pesel(new_pesel):
                raise ValidationError(f"PESEL {new_pesel} is not valid")

            # Check if another student already has this PESEL
            if self._check_pesel_exists(pesel=new_pesel, exclude_student_id=student_id):
                raise UniquenessError(f"PESEL {new_pesel} already exists")

        # If updating student_id, check if new ID is available
        if 'student_id' in kwargs:
            new_student_id = kwargs['student_id']

            # Check if another student already has this ID
            existing = Student.get_or_none(Student.student_id == new_student_id)
            if existing and existing.student_id != student_id:
                raise UniquenessError(f"Student Id {new_student_id} already exists")

        # Update all fields that were passed
        for key, value in kwargs.items():
            setattr(student, key, value)

        student.save()

        return student
