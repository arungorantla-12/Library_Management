def generate_book_id(title, author):
    return title[:2].upper() + author[:2].upper()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_id = generate_book_id(self.title, self.author)
        self.isAvailable = True
