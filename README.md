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
