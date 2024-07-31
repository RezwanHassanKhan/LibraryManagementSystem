from library.member import Member

class StudentMember(Member):
    def __init__(self, name: str, member_id: int):
        super().__init__(name, member_id) #call constructer of member class
        self.__borrow_limit = 3

    @property
    def borrow_limit(self):
        return self.__borrow_limit

    def borrow_book(self, book_to_borrow):
        if len(self.borrowed_books) >= self.__borrow_limit:
            print(f"{self.name} has reached the borrow limit of {self.__borrow_limit} books.")
        else:
            super().borrow_book(book_to_borrow)

class TeacherMember(Member):
    def __init__(self, name: str, member_id: int):
        super().__init__(name, member_id)
        self.__borrow_limit = 5

    @property
    def borrow_limit(self):
        return self.__borrow_limit

    def borrow_book(self, book_to_borrow):
        if len(self.borrowed_books) >= self.__borrow_limit:
            print(f"{self.name} has reached the borrow limit of {self.__borrow_limit} books.")
        else:
            super().borrow_book(book_to_borrow)