
# Library Management System

## Overview

The **Library Management System** is a Python-based application designed to manage and automate the basic functions of a library. The system handles book inventory, member management, book borrowing, and returning processes. It also includes unit tests to ensure the robustness and reliability of the codebase.

## Project Structure

The project is organized as follows:

```
.github/
└── workflows/
    └── test_lms.yaml            # GitHub Actions workflow for running tests

library/
├── book.py                      # Book class definition
├── library.py                   # Library class definition
├── member.py                    # Member class definition
└── specialized_members.py       # Specialized member classes (StudentMember, TeacherMember)

test/
├── test_book.py                 # Unit tests for the Book class
├── test_library.py              # Unit tests for the Library class
├── test_member.py               # Unit tests for the Member class
└── test_specialized_member.py   # Unit tests for specialized members

.coverage                        # Coverage report for unit tests
README.md                        # Project documentation
main.py                          # Entry point for running the Library Management System
```

## Features

- **Book Management:** Add, remove, search, and list books in the library's inventory.
- **Member Management:** Add, remove, search, and list members.
- **Borrowing and Returning:** Members can borrow and return books, with borrowing limits enforced for different member types.
- **Specialized Members:** Two types of members, `StudentMember` and `TeacherMember`, with different borrowing limits.

## Getting Started

### Prerequisites

- Python 3.9.18 or later
- Git (for version control)
- A code editor (e.g., VS Code)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RezwanHassanKhan/LibraryManagementSystem.git
   cd LibraryManagementSystem
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scriptsctivate`
   ```

3. **Install dependencies:**
   This project has no external dependencies. All required modules are part of the Python standard library.

4. **Run the application:**
   ```bash
   python main.py
   ```

### Running Tests

The project includes unit tests to ensure the code functions as expected. Tests are located in the `test/` directory and can be run using the following command:

```bash
python -m unittest discover -s test -p "*.py"
```

### Continuous Integration

The project uses **GitHub Actions** for continuous integration. The workflow configuration is located in `.github/workflows/test_lms.yaml`. This workflow automatically runs the unit tests on every push or pull request to the `main` branch.

### Coverage Report

The coverage report for the unit tests can be generated using the `coverage` tool:

```bash
coverage run -m unittest discover -s test -p "*.py"
coverage report -m
```

This will provide a detailed report showing which lines of code are covered by the tests.

## Usage

- **Add Books:** You can add books to the library by specifying the title, author, ISBN, and whether the book is currently borrowed.
- **Manage Members:** You can add new members (either students or teachers) and manage their borrowing activities.
- **Borrow and Return Books:** Members can borrow books if they haven't exceeded their borrowing limit. The system will update the status of the book accordingly.

### Example

Here is a basic usage example to demonstrate how the system works:

```python
from library.book import Book
from library.library import Library
from library.specialized_members import StudentMember, TeacherMember

library_manager = Library()

# Adding Books
book1 = Book("1984", "George Orwell", "9780451524935", False)
library_manager.add_book(book1)

# Adding Members
student = StudentMember("Alice", 1)
teacher = TeacherMember("Bob", 2)
library_manager.add_member(student)
library_manager.add_member(teacher)

# Borrowing Books
library_manager.borrow_book(1, "9780451524935")

# Listing Books
library_manager.list_books()

# Returning Books
library_manager.return_book(1, "9780451524935")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/RezwanHassanKhan/LibraryManagementSystem/issues) if you want to contribute.
