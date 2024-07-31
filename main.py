from library.book import Book
from library.member import Member
from library.library import Library
from library.specialized_members import StudentMember, TeacherMember

if __name__ == "__main__":
    library_manager = Library()  # creating a library class

    # Add Book
    # List of books to add

    books = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", False),
        ("1984", "George Orwell", "9780451524935", False),
        ("1984", "George Orwell", "9780451524935", False),
        ("To Kill a Mockingbird", "Harper Lee", "9780061120084", False),
        ("Pride and Prejudice", "Jane Austen", "9781503290563", False),
        ("Harry Potter", "J.K. Rowling", "9780439136365", False)
    ]
    # Loop to add members
    for title, author, isbn, is_borrowed in books:
        book = Book(title, author, isbn, is_borrowed)
        library_manager.add_book(book)

    # Add Member
    # List of members to add
    # Add Members
    members = [
        ("Alice", 1, "student"),
        ("Bob", 2, "teacher"),
        ("Charlie", 3, "student"),
        ("Diana", 4, "teacher"),
        ("Edward", 5, "student"),
        ("Mamia " , 6 , 'Student')
    ]

    # Loop to add members
    for name, member_id, member_type in members:
        if member_type == 'student':
            member = StudentMember(name, member_id)

        else:
            member = TeacherMember(name, member_id)

        library_manager.add_member(member)

    library_manager.borrow_book(2, '9780743273565')
    library_manager.borrow_book(6, '9780439136365')



    # #print(library_manager.list_books())
    # # # delete_book
    # # library_manager.remove_book("9780451524935")
    # # # print(library_manager.list_books())
    # #
    # # print(library_manager.list_members())
    # # # delete member
    # # library_manager.delete_member(3)
    # library_manager.list_members()
    # #
    # # # search book
    # print(library_manager.search_book('9780743273565'))
    # # # search member
    # print(library_manager.search_member(6))
    # #

    #print(library_manager.search_member(6))
