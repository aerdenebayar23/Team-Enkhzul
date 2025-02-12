class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            book.is_checked_out = True
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already checked out.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_checked_out = False
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
