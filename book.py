import random


def generate_book_id(title):
    return title[:2].upper() + str(random.randint(1000, 9999))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = generate_book_id(self.title)
        self.isAvailable = True
