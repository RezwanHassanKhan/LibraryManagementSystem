import builtins
from unittest import TestCase
from unittest.mock import patch, call
import library.book
from library.library import Library
from library.book import Book
from library.member import Member


class TestLibrary(TestCase):
    def setUp(self):
        self.library_m = Library()
        self.books = []
        book_list = [
            ("1984", "George Orwell", "9780451524935", False),
            ("Harry Potter", "J.K. Rowling", "9780439136365", False)
        ]
        for title, author, isbn, is_borrowed in book_list:
            self.books.append(Book(title, author, isbn, is_borrowed))
        self.book1, self.book2 = self.books

        self.members = []
        member_lists = [
            ("Alice", 1, "student"),
            ("Bob", 2, "teacher")
        ]
        for name, id, member_type in member_lists:
            self.members.append(Member(name, id))
        self.member1, self.member2 = self.members

    def test_library_creation(self):
        pass

    @patch('library.book.Book', autospec=True)
    def test_add_book_success(self, Mock_Book):
        # arrange
        mock_book = Mock_Book.return_value
        mock_book.isbn = self.book1.isbn
        mock_book.author = self.book1.author
        self.library_m.books_list = []
        # action
        self.library_m.add_book(mock_book)

        # assert
        self.assertEqual(len(self.library_m.books_list), 1)
        self.assertIn(mock_book, self.library_m.books_list)
        self.assertEqual(self.library_m.books_list[0].isbn, mock_book.isbn)
        self.assertEqual(self.library_m.books_list[0].author, mock_book.author)

    @patch('library.book.Book', autospec=True)
    def test_add_book_already_added(self, Mock_Book):
        mock_book = Mock_Book.return_value
        mock_book.isbn = self.book1.isbn
        mock_book.author = self.book1.author
        # arrange
        self.library_m.books_list = [self.book1, self.book2]

        with patch('builtins.print') as mocked_print:
            # action
            self.library_m.add_book(mock_book)
            # assert for printing
            # print(mocked_print)
            mocked_print.assert_called_with(f"****{mock_book.author} with an ID {mock_book.isbn} is already added****")
            # assert
            self.assertEqual(mock_book.isbn, self.book1.isbn)

    def test_remove_book_unsucessfull(self):
        # arrange
        self.library_m.books_list = []
        # action
        with patch('builtins.print') as mocked_print:
            # action
            self.library_m.remove_book(self.book2.isbn)
            # assert
            mocked_print(f'No book found with this '
                         f'{self.book2.isbn}')

    @patch('library.book.Book', autospec=True)
    def test_remove_book_sucess(self, Mock_Book):
        # arrange
        mock_book = Mock_Book.return_value
        mock_book.isbn = self.book2.isbn
        mock_book.title = self.book2.title
        self.library_m.books_list = [self.book1, self.book2]
        # action
        with patch('builtins.print') as mocked_print:
            # action
            self.library_m.remove_book(mock_book.isbn)
            # assert for printing
            mocked_print.assert_called_with(f"{mock_book.title} with an {mock_book.isbn} "
                                            f"removed from the list")
            # assert
            self.assertNotIn(mock_book, self.library_m.books_list)
            self.assertEqual(mock_book.isbn, self.book2.isbn)
            self.assertEqual(mock_book.title, self.book2.title)
            self.assertEqual(len(self.library_m.books_list), 1)
            self.assertEqual(self.library_m.books_list[0].isbn, self.book1.isbn)

    def test_search_book_success(self):
        # arrange
        self.library_m.books_list = [self.book1, self.book2]
        # action
        for expected_book in self.library_m.books_list:
            actual_book = self.library_m.search_book(expected_book.isbn)
            # assert
            self.assertEqual(actual_book, expected_book)

    def test_search_book_not_success(self):
        # arrange
        self.library_m.books_list = [self.book1, self.book2]
        # action
        actual_result = self.library_m.search_book('1234455')
        # assert
        self.assertIsNone(actual_result)

    @patch('builtins.print')
    def test_list_book(self, mocked_print):
        # arrange
        self.library_m.books_list = [self.book1, self.book2]
        # action
        self.library_m.list_books()
        expected_calls = [
            call('1984 by George Orwell'),
            call('Harry Potter by J.K. Rowling')
        ]

        # Verify that print was called with the expected output
        mocked_print.assert_has_calls(expected_calls, any_order=False)
        # Ensure print was called the exact number of times (2 books)
        self.assertEqual(mocked_print.call_count, len(expected_calls))

    @patch.object(Library, 'search_book')  # Mock the search_book method
    @patch.object(Member, 'borrow_book')
    def test_borrow_book_unsucessful(self, mock_search_member,
                                     mock_search_book):
        expected_member = self.member1
        expected_book = self.book1
        mock_search_member.return_value = None
        mock_search_book.return_value = None
        with patch('builtins.print') as mocked_print:
            self.library_m.borrow_book(expected_member.member_id,
                                       expected_book.isbn)

            mocked_print.assert_called_with(f"No book or member found with id {expected_book.isbn}")

    @patch.object(Library, 'search_member')  # Mock the search_member method
    @patch.object(Library, 'search_book')  # Mock the search_book method
    @patch.object(Member, 'borrow_book')  # Mock the borrow_book method
    def test_borrow_book_success(self, mock_borrow_book, mock_search_book, mock_search_member):
        # Arrange
        expected_member = self.member1
        expected_book = self.book1
        expected_str = "The book '1984' has been borrowed by Alice."

        # Mock return values
        mock_search_member.return_value = expected_member
        mock_search_book.return_value = expected_book
        mock_borrow_book.return_value = expected_str

        # Act: Call borrow_book from the Library class
        actual_result = self.library_m.borrow_book(expected_member.member_id, expected_book.isbn)
        print('actual', actual_result)

        # Assert
        self.assertEqual(actual_result, expected_str)
        mock_borrow_book.assert_called_once_with(expected_book)

    @patch.object(Library, 'search_member')  # Mock the search_member method
    @patch.object(Library, 'search_book')  # Mock the search_book method
    @patch.object(Member, 'return_book')  # Mock the return_book method
    def test_return_book_success(self, mock_return_book,
                                 mock_search_book,
                                 mock_search_member):
        # Arrange
        expected_member = self.member1
        expected_book = self.book1
        expected_str = "The book '1984' has been borrowed by Alice."

        # Mock return values
        mock_search_member.return_value = expected_member
        mock_search_book.return_value = expected_book
        mock_return_book.return_value = expected_str

        # Act: Call borrow_book from the Library class
        actual_result = self.library_m.return_book(expected_member.member_id, expected_book.isbn)
        print('actual', actual_result)

        # Assert
        self.assertEqual(actual_result, expected_str)
        mock_return_book.assert_called_once_with(expected_book)

    @patch.object(Library, 'search_book')  # Mock the search_book method
    @patch.object(Member, 'borrow_book')
    def test_return_book_unsucessful(self, mock_search_member,
                                     mock_search_book):
        expected_member = self.member1
        expected_book = self.book1
        mock_search_member.return_value = None
        mock_search_book.return_value = None
        with patch('builtins.print') as mocked_print:
            self.library_m.return_book(expected_member.member_id,
                                       expected_book.isbn)

            mocked_print.assert_called_with(f"No book or member found with id {expected_book.isbn}")
