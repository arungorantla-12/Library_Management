from book import *
from member import *


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        while True:
            book_title = str(input("Enter book title: "))
            book_author = str(input("Enter books author: "))

            if len(book_title) < 2:
                print(
                    "Book Title is too short.Please add atleast 2 characters to add the book"
                )

            elif len(book_author) < 2:
                print(
                    "Book Author is too short.Please add atleast 2 characters to add the book"
                )

            else:
                break

        if len(self.books) != 0:
            for b in self.books:
                if b.author == book_author and b.title == book_title:
                    print("Book already in the Library")
                    return

        book = Book(book_title, book_author)
        self.books.append(book)
        print("Book added successfully")
        print(f"The book ID is {book.book_id}.Please note this for future use")

    def register_member(self):
        while True:
            member_first_name = str(input("Enter your first name: "))
            member_last_name = str(input("Enter your last name: "))

            if len(member_first_name) < 2:
                print(
                    "First Name is too short.Please add atleast 2 characters to get registered"
                )

            elif len(member_last_name) < 2:
                print(
                    "Last Name is too short.Please add atleast 2 characters to get registered"
                )

            else:
                break

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
        print(f"The memeber ID is {member.member_id}.Please note this for future use")

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
        temp_borrowed_books = mem_object.borrowed_books.copy()

        for b in temp_borrowed_books:
            if b.book_id == book_id:
                mem_object.borrowed_books.remove(b)
                book_obj.isAvailable = True
                found = True
                print("Book return successful")
                break

        if not found:
            print("Book not found in borrowed books")

        del temp_borrowed_books

    def show_all_books(self):
        print("Showing All Books:")
        for b in self.books:
            print(f"Book Title is {b.title} and Book Author is {b.author}")

    def show_members(self):
        print("Showing All Members:")
        for m in self.members:
            print(f"FirstName is {m.first_name} and LastName is {m.last_name}")

    def show_available_books(self):
        print("Showing Available Books:")
        for b in self.books:
            if b.isAvailable:
                print(f"{b.title}")

    def show_borrowed_books(self):
        member_id = str(input("Enter your Member ID: "))
        for m in self.members:
            if m.member_id == member_id and m.borrowed_books:
                print(f"List of Borrowed books for {m.first_name} are:")
                for b in m.borrowed_books:
                    print(b.title)
                break
            elif m.member_id == member_id and not m.borrowed_books:
                print("No books have been borrowed")
                break

            else:
                print(
                    "Member not found. If you are new user, please select option 2 for registration"
                )
