#from library.member import Member
class Library:
    def __init__(self):
        self.members_list = []
        self.books_list = []
        # self.borrowed_book_list = []

    def add_book(self, book_to_add):
        for book in self.books_list:
            if book.isbn == book_to_add.isbn:
                print(f"****{book_to_add.author} with an ID {book_to_add.isbn} is already added****")
                break
        else:
            self.books_list.append(book_to_add)
            # print(f"{book_to_add.author} with an ID {book_to_add.isbn} added as new book")

    # def update_book(self, book):
    #     #pass

    def remove_book(self, isbn_to_chk):
        for book in self.books_list:
            if book.isbn == isbn_to_chk:
                self.books_list.remove(book)
                print(f"{book.title} with an {isbn_to_chk} "
                      f"removed from the list")
                break
        else:
            print(f'No book found with this  {isbn_to_chk}')

    def search_book(self, isbn_to_chk):
        for book in self.books_list:
            if book.isbn == isbn_to_chk:
                return book
        return None

    def list_books(self):
        for book in self.books_list:
            print(f"{book.title} by {book.author}")

    def add_member(self, member_to_add):
        for member in self.members_list:
            if member.member_id == member_to_add.member_id:
                print(f'****{member.name} with ID {member_to_add.member_id} is already an existing member****')
                break
        else:
            self.members_list.append(member_to_add)
            # print(f"{member_to_add.name} with an {member_to_add.member_id} added as new member")

    # def update_member(self):
    #     pass

    def delete_member(self, member_id_to_chk):
        for member in self.members_list:
            if member.member_id == member_id_to_chk:
                self.members_list.remove(member)
                print(f"{member.name} with an {member_id_to_chk} "
                      f"removed from the list")
                break
        else:
            print(f'No member found with this  {member_id_to_chk}')

    def search_member(self, member_id_to_chk):
        for member in self.members_list:
            if member.member_id == member_id_to_chk:
                return member
        return None

    def list_members(self):
        for member in self.members_list:
            print(f"Member name : {member.name} and ID: {member.member_id}")

    def borrow_book(self, member_id, isbn):
        member = self.search_member(member_id)
        print('member', member)

        book = self.search_book(isbn)
        print('book', book)

        if member and book:
            return member.borrow_book(book)
        else:
            print(f'No book or member found with id {isbn}')

    def return_book(self, member_id, isbn):
        member = self.search_member(member_id)
        book = self.search_book(isbn)
        if member and book:
            return member.return_book(book)
        else:
            print(f'No book or member found with id {isbn}')
