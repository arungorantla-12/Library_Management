import random


def generate_member_id(first_name, last_name):
    return first_name[:2].upper() + last_name[:2].upper()


class Member:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.member_id = generate_member_id(self.first_name, self.last_name)
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)
