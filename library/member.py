class Member:
    def __init__(self, name: str, member_id: int):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def member_id(self):
        return self.__member_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def clear_borrowed_books(self):
        self.__borrowed_books.clear()  # Clear the borrowed books list

    def borrow_book(self,book_to_borrow):
        if book_to_borrow.is_borrowed:
            print(f"The book '{book_to_borrow.title}' is already borrowed.")
        else:
            book_to_borrow.is_borrowed = True
            self.__borrowed_books.append(book_to_borrow)
            print(f"The book '{book_to_borrow.title}' has been borrowed by {self.__name}.")

    def return_book(self, book_to_return):
        if book_to_return in self.__borrowed_books:
            book_to_return.is_borrowed = False
            self.__borrowed_books.remove(book_to_return)
            print(f"The book '{book_to_return.title}' has been returned by {self.__name}.")
        else:
            print(f"The book '{book_to_return.title}' was not borrowed by {self.__name}.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.__borrowed_books]
        borrowed_books_str = ", ".join(borrowed_titles) if borrowed_titles else "No books borrowed"
        return f"Member ID: {self.__member_id}, Name: {self.__name}, Borrowed Books: {borrowed_books_str}"