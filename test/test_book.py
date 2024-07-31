import unittest

from library.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.books = []
        book_data = [
            ("1984", "George Orwell", "9780451524935", False),
            ("Harry Potter", "J.K. Rowling", "9780439136365", False)
        ]
        for title, author, isbn, is_borrowed in book_data:
            self.books.append(Book(title, author, isbn, is_borrowed))
        self.book1, self.book2 = self.books


    def test_book_creation(self):
        self.assertEqual(self.book1.title, "1984")
        self.assertEqual(self.book1.author, "George Orwell")
        self.assertEqual(self.book1.isbn, "9780451524935")
        self.assertEqual(self.book1.is_borrowed, False)

        self.assertEqual(self.book2.title, "Harry Potter")
        self.assertEqual(self.book2.author, "J.K. Rowling")
        self.assertEqual(self.book2.isbn, "9780439136365")
        self.assertEqual(self.book2.is_borrowed, False)

    def test_is_borrowed(self):
        self.book1.is_borrowed = True
        self.assertTrue(self.book1.is_borrowed)
        self.book2.is_borrowed = True
        self.assertTrue(self.book2.is_borrowed)

    def test__str__(self):
        self.assertEqual(str(self.book1), "'1984' by George Orwell (ISBN: 9780451524935) - Status: Available")
        self.book1.is_borrowed = True
        self.assertEqual(str(self.book1), "'1984' by George Orwell (ISBN: 9780451524935) - Status: Borrowed")
        # Check string representation for book2 before borrowing
        expected_str2 = "'Harry Potter' by J.K. Rowling (ISBN: 9780439136365) - Status: Available"
        self.assertEqual(str(self.book2), expected_str2)

        # Change status to borrowed and check string representation again
        self.book2.is_borrowed = True
        expected_str2 = "'Harry Potter' by J.K. Rowling (ISBN: 9780439136365) - Status: Borrowed"
        self.assertEqual(str(self.book2), expected_str2)


if __name__ == '__main__':
    unittest.main()
