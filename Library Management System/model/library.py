from datetime import datetime

class Library:
    def __init__(self, fine_per_day=10):
        self.books = []
        self.issued_books = {}
        self.fine_per_day = fine_per_day 
        self.due_days = 14  
    
    def add_book(self, book):
        self.books.append(book)
    
    def view_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")
    
    def is_book_issued(self, isbn):
        return isbn in self.issued_books
    
    def issue_book(self, isbn):
        if self.is_book_issued(isbn):
            return None, "Book is already issued"
        
        for book in self.books:
            if book.isbn == isbn:
                book.set_issue_date() 
                self.issued_books[isbn] = book
                self.books.remove(book)
                return book, "Book issued successfully"
        return None, "Book not found"
    
    def return_book(self, isbn):
        if isbn not in self.issued_books:
            return None, "Book not found in issued books"
        
        book = self.issued_books.pop(isbn)
        fine = self.calculate_fine(book)
        
        book.clear_issue_date()
        self.books.append(book)
        
        if fine > 0:
            return book, f"Book returned successfully. Fine: ₹{fine} (Late by {self.get_days_late(book)} days)"
        else:
            return book, "Book returned successfully. No fine."
    
    def calculate_fine(self, book):
        if book.issue_date is None:
            return 0
        
        days_late = self.get_days_late(book)
        if days_late > 0:
            return days_late * self.fine_per_day
        return 0
    
    def get_days_late(self, book):
        if book.issue_date is None:
            return 0
        
        days_issued = (datetime.now() - book.issue_date).days
        days_late = days_issued - self.due_days
        return max(0, days_late)
    
    def view_issued_books(self):
        if not self.issued_books:
            print("No books are currently issued.")
            return
        
        print("\nIssued Books:")
        for isbn, book in self.issued_books.items():
            days_issued = (datetime.now() - book.issue_date).days
            days_left = self.due_days - days_issued
            days_late = max(0, -days_left)
            fine = self.calculate_fine(book)
            
            status = "ON TIME" if days_left >= 0 else "OVERDUE"
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {isbn}")
            print(f"Issued on: {book.issue_date.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Days Issued: {days_issued}")
            print(f"Status: {status} ({abs(days_left)} days {'left' if days_left >= 0 else 'overdue'})")
            if fine > 0:
                print(f"Current Fine: ₹{fine}")
            print('\n\n')
    