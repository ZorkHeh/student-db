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
db.connect()


class DbStudent(Model):
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    album_number = IntegerField()
    pesel = CharField()
    gender = CharField()

    def __repr__(self):
        return f'<{self.first_name}, {self.last_name}, {self.address}, {self.pesel}, {self.gender}>'

    class Meta:
        database = db

db.create_tables([DbStudent])
