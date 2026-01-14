import questionary
from rich.console import Console
from rich.table import Table
from services import StudentService

# Create console instance
console = Console()


def run_cli():
    """
    Main CLI interface for the student database.
    Displays menu and handles user choices.
    """
    service = StudentService()

    console.print("=" * 50, style="bold cyan")
    console.print("STUDENT DATABASE SYSTEM", style="bold cyan", justify="center")
    console.print("=" * 50, style="bold cyan")
    console.print()

    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "Add new student",
                "Display all students",
                "Search for student",
                "Sort students",
                "Delete student",
                "Edit student",
                "Exit"
            ]
        ).ask()

        if choice == "Add new student":
            add_student_menu(service)
        elif choice == "Display all students":
            display_all_students(service)
        elif choice == "Search for student":
            search_student_menu(service)
        elif choice == "Sort students":
            sort_students_menu(service)
        elif choice == "Delete student":
            delete_student_menu(service)
        elif choice == "Edit student":
            edit_student_menu(service)
        elif choice == "Exit":
            console.print("\n[bold green]Thank you for using the Student Database System![/bold green]")
            break


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_students_table(students):
    """
    Create a Rich table from a list of students.
    Returns a formatted table ready to display.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Student ID")
    table.add_column("First Name")
    table.add_column("Last Name")
    table.add_column("PESEL")
    table.add_column("Gender")
    table.add_column("Address")

    for student in students:
        table.add_row(
            student.student_id,
            student.first_name,
            student.last_name,
            student.pesel,
            student.gender,
            student.address
        )

    return table


def display_students_with_title(students, title):
    """
    Display students with a title and count.
    Handles empty list case.
    """
    console.print(f"\n[bold cyan]--- {title} ---[/bold cyan]")

    if not students:
        console.print("[yellow]No students found.[/yellow]")
    else:
        console.print(f"\n[green]Total students: {len(students)}[/green]\n")
        table = create_students_table(students)
        console.print(table)


def print_section_header(title):
    """Print a formatted section header."""
    console.print(f"\n[bold cyan]--- {title} ---[/bold cyan]")


def print_success(message):
    """Print a success message."""
    console.print(f"\n[green]✓ {message}[/green]")


def print_error(message):
    """Print an error message."""
    console.print(f"\n[red]✗ {message}[/red]")


def print_warning(message):
    """Print a warning message."""
    console.print(f"\n[yellow]{message}[/yellow]")


def pause():
    """Pause and wait for user to press Enter."""
    input("\nPress Enter to continue...")


# ============================================================================
# MENU FUNCTIONS
# ============================================================================

def add_student_menu(service):
    """Handle adding a new student."""
    print_section_header("Add New Student")

    first_name = questionary.text("First name:").ask()
    last_name = questionary.text("Last name:").ask()
    address = questionary.text("Address:").ask()
    student_id = questionary.text("Student ID number:").ask()
    pesel = questionary.text("PESEL:").ask()
    gender = questionary.select(
        "Gender:",
        choices=["Male", "Female", "Other"]
    ).ask()

    try:
        student = service.add_student(
            first_name=first_name,
            last_name=last_name,
            address=address,
            student_id=student_id,
            pesel=pesel,
            gender=gender
        )
        print_success(f"Student {student.first_name} {student.last_name} added successfully!")
    except Exception as e:
        print_error(f"Error: {e}")

    pause()


def display_all_students(service):
    """Display all students in the database."""
    students = service.get_all_students()
    display_students_with_title(students, "All Students")
    pause()


def search_student_menu(service):
    """Handle searching for students."""
    search_type = questionary.select(
        "Search by:",
        choices=["Last name", "PESEL", "Back to main menu"]
    ).ask()

    if search_type == "Back to main menu":
        return

    if search_type == "Last name":
        last_name = questionary.text("Enter last name (or part of it):").ask()
        students = service.search_by_last_name(last_name)
        display_students_with_title(students, f"Search Results for last name '{last_name}'")

    elif search_type == "PESEL":
        pesel = questionary.text("Enter PESEL:").ask()
        student = service.search_by_pesel(pesel)
        students = [student] if student else []
        display_students_with_title(students, f"Search Results for PESEL '{pesel}'")

    pause()


def sort_students_menu(service):
    """Handle sorting students."""
    sort_by = questionary.select(
        "Sort by:",
        choices=["PESEL", "Last name", "Back to main menu"]
    ).ask()

    if sort_by == "Back to main menu":
        return

    if sort_by == "PESEL":
        students = service.get_students_sorted_by_pesel()
        title = "Students Sorted by PESEL"
    elif sort_by == "Last name":
        students = service.get_students_sorted_by_last_name()
        title = "Students Sorted by Last Name"

    display_students_with_title(students, title)
    pause()


def delete_student_menu(service):
    """Handle deleting a student."""
    print_section_header("Delete Student")

    student_id = questionary.text("Enter student ID to delete:").ask()

    confirm = questionary.confirm(
        f"Are you sure you want to delete student with ID {student_id}?"
    ).ask()

    if confirm:
        try:
            service.delete_student(student_id)
            print_success(f"Student with ID {student_id} deleted successfully!")
        except Exception as e:
            print_error(f"Error: {e}")
    else:
        print_warning("Deletion cancelled.")

    pause()


def edit_student_menu(service):
    """Handle editing an existing student."""
    print_section_header("Edit Student")

    student_id = questionary.text("Enter student ID to edit:").ask()

    # Check if student exists
    student = service.get_student_by_id(student_id)
    if not student:
        print_error(f"Student with ID {student_id} not found.")
        pause()
        return

    # Display current information
    console.print(f"\n[green]Current information for student {student_id}:[/green]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Field")
    table.add_column("Current Value")

    table.add_row("Student ID", student.student_id)
    table.add_row("First Name", student.first_name)
    table.add_row("Last Name", student.last_name)
    table.add_row("PESEL", student.pesel)
    table.add_row("Gender", student.gender)
    table.add_row("Address", student.address)

    console.print(table)
    console.print()

    # Ask what to edit
    fields_to_edit = questionary.checkbox(
        "Select fields to edit (use Space to select, Enter to confirm):",
        choices=[
            "First name",
            "Last name",
            "Address",
            "Student ID",
            "PESEL",
            "Gender"
        ]
    ).ask()

    if not fields_to_edit:
        print_warning("No fields selected. Edit cancelled.")
        pause()
        return

    # Collect new values
    updates = {}

    if "First name" in fields_to_edit:
        updates['first_name'] = questionary.text(
            "New first name:",
            default=student.first_name
        ).ask()

    if "Last name" in fields_to_edit:
        updates['last_name'] = questionary.text(
            "New last name:",
            default=student.last_name
        ).ask()

    if "Address" in fields_to_edit:
        updates['address'] = questionary.text(
            "New address:",
            default=student.address
        ).ask()

    if "Student ID" in fields_to_edit:
        updates['student_id'] = questionary.text(
            "New student ID:",
            default=student.student_id
        ).ask()

    if "PESEL" in fields_to_edit:
        updates['pesel'] = questionary.text(
            "New PESEL:",
            default=student.pesel
        ).ask()

    if "Gender" in fields_to_edit:
        updates['gender'] = questionary.select(
            "New gender:",
            choices=["Male", "Female", "Other"],
            default=student.gender
        ).ask()

    # Confirm changes
    confirm = questionary.confirm(
        f"Confirm updating {len(updates)} field(s)?"
    ).ask()

    if confirm:
        try:
            updated_student = service.update_student(student_id, **updates)
            print_success(f"Student {updated_student.first_name} {updated_student.last_name} updated successfully!")
        except Exception as e:
            print_error(f"Error: {e}")
    else:
        print_warning("Update cancelled.")

    pause()
