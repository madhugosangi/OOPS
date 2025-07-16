from abc import ABC, abstractmethod

# ------------------------
# Abstraction
# ------------------------
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def borrow_book(self, book):
        pass


# ------------------------
# Polymorphism
# ------------------------
class Student(User):
    def borrow_book(self, book):
        print(f"Student {self.name} borrowed {book}")


class Teacher(User):
    def borrow_book(self, book):
        print(f"Teacher {self.name} borrowed {book}")


# ------------------------
# Encapsulation
# ------------------------
class Library:
    def __init__(self):
        self.__books = []  # Private book list

    def add_book(self, book):
        self.__books.append(book)
        print(f"Book '{book}' added to the library.")

    def show_books(self):
        print("Available books:")
        for book in self.__books:
            print(f"- {book}")

    def issue_book(self, book, user: User):
        if book in self.__books:
            self.__books.remove(book)
            user.borrow_book(book)
        else:
            print(f"Sorry, '{book}' is not available.")

    def return_book(self, book):
        self.__books.append(book)
        print(f"Book '{book}' returned to the library.")


# ------------------------
# Class and Object
# ------------------------
library = Library()

# Add books (admin task)
library.add_book("Python Programming")
library.add_book("Machine Learning")
library.add_book("Data Science")

print()
library.show_books()
print()

# Create user objects
student = Student("Madhu")
teacher = Teacher("Mr.Satish Kumar")

# Users borrow books
library.issue_book("Python Programming", student)
library.issue_book("Data Science", teacher)

print()
library.show_books()
print()

# Book is returned
library.return_book("Python Programming")

print()
library.show_books()
