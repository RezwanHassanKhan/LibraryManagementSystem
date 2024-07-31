import unittest
from unittest.mock import MagicMock, patch

import library.book
from library.member import Member


class TestMember(unittest.TestCase):
    def setUp(self):
        self.members = []
        member_lists = [
            ("Alice", 1, "student"),
            ("Bob", 2, "teacher")
        ]
        for name, id, member_type in member_lists:
            self.members.append(Member(name, id))
        self.member1, self.member2 = self.members

    def test_member_creation(self):
        self.assertEqual(self.member1.name, 'Alice')
        self.assertEqual(self.member1.member_id, 1)

        self.assertEqual(self.member2.name, 'Bob')
        self.assertEqual(self.member2.member_id, 2)

    @patch('library.book.Book', autospec=True)
    def test_borrow_success(self, Mock_Book):
        # arrange
        mock_book = Mock_Book.return_value
        mock_book.is_borrowed = False
        mock_book.title = 'Harry Potter'

        with patch('builtins.print') as mocked_print:
            # action
            self.member1.borrow_book(mock_book)
            mock_book.is_borrowed = True

            # assert for printing output
            mocked_print.assert_called_with(f"The book 'Harry Potter'"
                                            f" has been borrowed by {self.member1.name}.")
            # assert
            self.assertTrue(mock_book.is_borrowed)
            self.assertEqual(len(self.member1.borrowed_books), 1)
            self.assertIn(mock_book, self.member1.borrowed_books)

    @patch('library.book.Book', autospec=True)
    def test_borrow_book_already_borrowed(self, Mock_Book):
        # arrange
        mock_book = Mock_Book.return_value
        mock_book.is_borrowed = True
        mock_book.title = 'Harry Potter'

        # assert
        with patch('builtins.print') as mocked_print:
            # action
            self.member1.borrow_book(mock_book)
            # assert for printing
            mocked_print.assert_called_with(f"The book 'Harry Potter' is already borrowed.")

            # assert
            self.assertEqual(len(self.member1.borrowed_books), 0)
            self.assertNotIn(mock_book, self.member1.borrowed_books)

    @patch('library.book.Book', autospec=True)
    def test_return_book_success(self, Mock_Book):
        mock_book = Mock_Book.return_value
        mock_book.title = "Harry Potter"

        # action
        with patch('builtins.print') as mocked_print:
            # action
            self.member1.borrowed_books.append(mock_book)
            self.member1.return_book(mock_book)
            mock_book.is_borrowed = False

            # assert for printing
            mocked_print.assert_called_with(
                f"The book '{mock_book.title}' has been returned by "
                f"{self.member1.name}.")
            # assert
            self.assertFalse(mock_book.is_borrowed)
            self.assertEqual(len(self.member1.borrowed_books), 0)
            self.assertNotIn(mock_book, self.member1.borrowed_books)

    @patch('library.book.Book', autospec=True)
    def test_return_book_not_borrowed(self, Mock_Book):
        mock_book = Mock_Book.return_value
        mock_book.title = "Harry Potter"

        # action
        with patch('builtins.print') as mocked_print:
            self.member1.clear_borrowed_books
            self.member1.return_book(mock_book)

            # assert for printing
            mocked_print.assert_called_with(f"The book '{mock_book.title}' was not borrowed by {self.member1.name}.")

            # assert
            self.assertEqual(len(self.member1.borrowed_books), 0)
            self.assertNotIn(mock_book, self.member1.borrowed_books)

    @patch('library.book.Book', autospec=True)
    def test__str__(self, Mock_Book):
        mock_book = Mock_Book.return_value
        mock_book.title = 'Harry Potter'
        mock_book.is_borrowed = False

        # action
        self.member2.borrow_book(mock_book)

        # assert
        print(str(self.member2))
        expected_str = f"Member ID: {self.member2.member_id}, " \
                       f"Name: {self.member2.name}, " \
                       f"Borrowed Books: {mock_book.title}"
        self.assertEqual(str(self.member2), expected_str)
