from models import initialize_database, close_database
from cli import run_cli


def main():
    initialize_database()
    run_cli()
    close_database()


if __name__ == "__main__":
    main()
