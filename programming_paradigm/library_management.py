class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False  # private attribute

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []  # private list of Book objects

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.check_out():
                    return True
                return False  # Already checked out
        return False  # Not found

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book.return_book():
                    return True

