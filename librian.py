from book import *
from member import *


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_title = str(input("Enter book title: "))
        book_author = str(input("Enter books author: "))

        if len(self.books) != 0:
            for b in self.books:
                if b.author == book_author and b.title == book_title:
                    print("Book already in the Library")
                    return

        book = Book(book_title, book_author)
        self.books.append(book)
        print("Book added successfully")

    def register_member(self):
        member_first_name = str(input("Enter your first name: "))
        member_last_name = str(input("Enter your last name: "))

        if len(self.members) != 0:
            for m in self.members:
                if (
                    m.first_name == member_first_name
                    and m.last_name == member_last_name
                ):
                    print("Member already exists")
                    return

        member = Member(member_first_name, member_last_name)
        self.members.append(member)
        print("Member added successfully")

    def issue_book(self):
        member_id = str(input("Enter your id: "))
        book_id = str(input("Enter the book id that you want to take: "))

        mem_object = None
        for m in self.members:
            if m.member_id == member_id:
                mem_object = m
                break

        book_obj = None
        for b in self.books:
            if b.book_id == book_id:
                book_obj = b
                break

        if mem_object is None:
            print("Member not found")
            return

        if book_obj is None:
            print("Book not found")
            return

        if book_obj.isAvailable:
            book_obj.isAvailable = False
            mem_object.borrow_book(book_obj)
            print("Book issued successfully")
        else:
            print("Book is not available")

    def return_book(self):
        member_id = str(input("Enter your id: "))
        book_id = str(input("Enter the book id that you want to return: "))

        mem_object = None
        for m in self.members:
            if m.member_id == member_id:
                mem_object = m
                break

        book_obj = None
        for b in self.books:
            if b.book_id == book_id:
                book_obj = b
                break

        if mem_object is None:
            print("Member not found")
            return

        if book_obj is None:
            print("Book not found")
            return

        found = False
        for b in mem_object.borrowed_books:
            if b.book_id == book_id:
                mem_object.remove(b)
                book_obj.isAvailable = True
                found = True
                print("Book return successful")
                break

        if not found:
            print("Book not found in borrowed books")

    def show_all_books(self):
        for b in self.books:
            print(f"{b.title},{b.author}\n")

    def show_members(self):
        for m in self.members:
            print(f"{m.first_name},{m.last_name}\n")

    def show_available_books(self):
        print("Showing Available Books:")
        for b in self.books:
            if b.isAvailable:
                print(f"{b.title}\n")
