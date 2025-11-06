from peewee import Model, CharField, IntegerField, SqliteDatabase


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

db = SqliteDatabase('data/students.db')

def initialize_db(database):

    database.connect()
    database.create_tables([DbStudent])

class DbStudent(Model):
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    student_id = CharField(unique=True)
    pesel = CharField(unique=True)
    gender = CharField()

    class Meta:
        database = db




