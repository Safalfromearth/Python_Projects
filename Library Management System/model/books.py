from datetime import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issue_date = None
    
    def set_issue_date(self):
        self.issue_date = datetime.now()
    
    def clear_issue_date(self):
        self.issue_date = None
        