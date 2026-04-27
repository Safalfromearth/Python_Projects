from model.library import Library
from model.books import Book
from datetime import timedelta

library = Library()

def print_menu():
    print("\n\nLibrary Management System\n1. Add Book\n2. View Available Books\n3. Issue Book\n4. Return Book\n5. View Issued Books\n6. Exit")


while True:
    print_menu()
    choice = input("Enter your choice:")
    
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)
        print("Book added successfully!")
    
    elif choice == '2':
        print("\nAvailable Books:")
        if library.books:
            library.view_books()
        else:
            print("No books available.")
    
    elif choice == '3':
        isbn = input("Enter ISBN of the book to issue: ")
        issued_book, message = library.issue_book(isbn)
        if issued_book:
            print(f"  Book: '{issued_book.title}' by {issued_book.author}")
            print(f"{message}")
            print("Return it in 14 days to avoid fines.")
        else:
            print(f"{message}")
    
    elif choice == '4':
        isbn = input("Enter ISBN of the book to return: ")
        returned_book, message = library.return_book(isbn)
        if returned_book:
            print(f"{message}")
            print(f"  Book: '{returned_book.title}' by {returned_book.author}")
        else:
            print(f"{message}")
    
    elif choice == '5':
        library.view_issued_books()
    
    elif choice == '6':
        print("\nThanks for using Library Management System. Goodbye!")
        break
    
    else:
        print("✗ Invalid choice. Please try again.")