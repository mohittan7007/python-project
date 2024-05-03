class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = 'Available'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added successfully!")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.status == 'Available':
                    book.status = 'Issued'
                    print(f"Book with ID {book_id} issued successfully!")
                else:
                    print(f"Book with ID {book_id} is already issued.")
                return
        print(f"Book with ID {book_id} not found.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} removed successfully!")
                return
        print(f" Book with ID {book_id} not found.")

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {book.status}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Remove Book")
        print("4. Display Books")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)
        elif choice == 2:
            book_id = int(input("Enter book ID to issue: "))
            library.issue_book(book_id)
        elif choice == 3:
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
        elif choice == 4:
            library.display_books()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
