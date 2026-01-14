# Student Database System

## Installation

Create and activate a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The SQLite database will be created automatically on first run.


### PESEL Validation

The application validates PESEL numbers according to Polish standards, checking length (11 digits), format (numeric only), and checksum correctness using the official algorithm.

## Description

A command-line application for managing student records. The application provides full CRUD operations (Create, Read, Update, Delete) with PESEL validation and persistent SQLite storage. Use arrow keys to navigate and Enter to select options.

## Features

The application meets all assignment requirements including adding students, displaying records, searching by last name or PESEL, sorting by PESEL or last name, deleting records, and validating PESEL numbers. Additional features include editing existing student records and a modern interactive CLI interface with formatted table output.

## Technology Stack

- Python 3.8+
- SQLite database with Peewee ORM
- Questionary for interactive CLI
- Rich for formatted output

## Project Structure

```
student_database/
├── main.py                 # Application entry point
├── models.py               # Database models and initialization
├── services.py             # Business logic layer
├── cli.py                  # CLI interface layer
├── utils/
│   ├── __init__.py
│   └── validators.py       # PESEL validation
├── requirements.txt        # Dependencies
└── README.md
```

## Database Schema

The application uses a single Student table with the following fields:
- student_id (primary key, unique)
- first_name
- last_name
- pesel (unique, 11 characters)
- gender
- address


## Troubleshooting

**Arrow keys not working:**  
If running from PyCharm's integrated terminal, the interactive menu may not work properly. Please run the application from your system terminal (Command Prompt, PowerShell, or Terminal) instead.

