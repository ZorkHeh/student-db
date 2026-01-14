from peewee import *

# Database configuration
db = SqliteDatabase('students.db')


class BaseModel(Model):
    """Base model class that all models inherit from."""

    class Meta:
        database = db


class Student(BaseModel):
    """
    Student model representing a student record.
    """

    student_id = CharField(primary_key=True, unique=True)
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    pesel = CharField(unique=True, max_length=11)
    gender = CharField()

    class Meta:
        table_name = 'students'

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.student_id})"


def initialize_database():
    """
    Initialize the database connection and create tables if they don't exist.
    """

    db.connect()
    db.create_tables([Student], safe=True)
    print("Database initialized successfully.")


def close_database():
    """
    Close the database connection.
    """

    if not db.is_closed():
        db.close()
        print("Database connection closed.")
