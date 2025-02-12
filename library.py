from member import Member
from book import Book
class Library:
    def __init__(self):
        self.books = {}     
        self.members = {} 

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Added book: '{book.title}'.")

    def register_member(self, member):
        self.members[member.member_id] = member
        print(f"Registered member: {member.name}.")

    def lend_book(self, isbn, member_id):
        if isbn not in self.books:
            print("Book not found in the library.")
            return
        if member_id not in self.members:
            print("Member not registered.")
            return

        book = self.books[isbn]
        member = self.members[member_id]

        if book.is_checked_out:
            print(f"'{book.title}' is already checked out.")
        else:
            member.borrow_book(book)

    def return_book(self, isbn, member_id):
        if isbn not in self.books:
            print("Book not found in the library.")
            return
        if member_id not in self.members:
            print("Member not registered.")
            return

        book = self.books[isbn]
        member = self.members[member_id]

        if book in member.borrowed_books:
            member.return_book(book)
        else:
            print(f"{member.name} does not have '{book.title}'.")


if __name__ == "__main__":
    library = Library()

    book1 = Book("Animal Farm", "George Orwell", "000000")
    book2 = Book("Harry Potter", "J.K.Rowling", "0000123")
    library.add_book(book1)
    library.add_book(book2)

    member1 = Member(1, "Enkhzul")
    member2 = Member(2, "Enkhbat")
    library.register_member(member1)
    library.register_member(member2)

    library.lend_book("000000", 1)  
    library.lend_book("0000123", 2)  

    library.return_book("000000", 1) 