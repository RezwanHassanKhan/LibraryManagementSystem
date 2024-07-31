class Book:
    def __init__(self, title: str, author: str, isbn: str, is_borrowed: bool):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = is_borrowed

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, status: bool):
        self.__is_borrowed = status



    def __str__(self):
        borrowed_status = "Borrowed" if self.__is_borrowed else "Available"
        return f"'{self.__title}' by {self.__author} (ISBN: {self.__isbn}) - Status: {borrowed_status}"