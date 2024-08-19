# Library Management System

## Overview

The **Library Management System** is a Python-based application designed to manage and automate the basic functions of a library. The system handles book inventory, member management, book borrowing, and returning processes. It also includes unit tests to ensure the robustness and reliability of the codebase.

## Project Structure

The project is organized as follows:
.github/
└── workflows/
└── test_lms.yaml        # GitHub Actions workflow for running tests

library/
├── book.py                  # Book class definition
├── library.py               # Library class definition
├── member.py                # Member class definition
└── specialized_members.py   # Specialized member classes (StudentMember, TeacherMember)

test/
├── test_book.py             # Unit tests for the Book class
├── test_library.py          # Unit tests for the Library class
├── test_member.py           # Unit tests for the Member class
└── test_specialized_member.py # Unit tests for specialized members

.coverage                    # Coverage report for unit tests
README.md                    # Project documentation
main.py                      # Entry point for running the Library Management System


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

   
