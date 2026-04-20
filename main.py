from librian import *
import sys


def main():
    library = Library()
    while True:
        print(
            f"===== LIBRARY MENU =====\n1. Add Book\n2. Register Member\n3. Issue Book\n4. Return Book\n5. Show All Books\n6. Show Available Books\n7. Show Members\n8. Exit"
        )
        option = str(input("Select option: "))
        if option == "1":
            library.add_book()
        elif option == "2":
            library.register_member()
        elif option == "3":
            library.issue_book()
        elif option == "4":
            library.return_book()
        elif option == "5":
            library.show_all_books()
        elif option == "6":
            library.show_available_books()
        elif option == "7":
            library.show_members()
        elif option == "8":
            print("Exit")
            break
        else:
            print("Select a valid option")


main()
