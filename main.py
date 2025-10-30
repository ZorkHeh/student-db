from peewee import SqliteDatabase

from menu.cli import cmd_start
from domain.models import *

if __name__ == "__main__":

    cmd_start()
    db.close()
