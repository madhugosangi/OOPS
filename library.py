import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# -----------------------
# Core Classes (OOP)
# -----------------------

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def borrow_book(self, book):
        pass

class Student(User):
    def borrow_book(self, book):
        return f"Student {self.name} borrowed '{book}'"

class Teacher(User):
    def borrow_book(self, book):
        return f"Teacher {self.name} borrowed '{book}'"

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        return self.__books.copy()

    def issue_book(self, book, user: User):
        if book in self.__books:
            self.__books.remove(book)
            return user.borrow_book(book)
        else:
            return f"'{book}' is not available."

    def return_book(self, book):
        self.__books.append(book)
        return f"'{book}' returned to library."


# -----------------------
# GUI
# -----------------------

class LibraryApp:
    def __init__(self, root):
        self.lib = Library()
        self.root = root
        self.root.title("Library Management System")

        self.create_widgets()

    def create_widgets(self):
        # --- Book Entry ---
        tk.Label(self.root, text="Book Name:").grid(row=0, column=0)
        self.book_entry = tk.Entry(self.root)
        self.book_entry.grid(row=0, column=1)

        # --- User Name ---
        tk.Label(self.root, text="User Name:").grid(row=1, column=0)
        self.user_entry = tk.Entry(self.root)
        self.user_entry.grid(row=1, column=1)

        # --- User Type ---
        tk.Label(self.root, text="User Type:").grid(row=2, column=0)
        self.user_type = tk.StringVar()
        self.user_type.set("Student")
        tk.OptionMenu(self.root, self.user_type, "Student", "Teacher").grid(row=2, column=1)

        # --- Buttons ---
        tk.Button(self.root, text="Add Book", command=self.add_book).grid(row=3, column=0)
        tk.Button(self.root, text="View Books", command=self.view_books).grid(row=3, column=1)
        tk.Button(self.root, text="Borrow Book", command=self.borrow_book).grid(row=4, column=0)
        tk.Button(self.root, text="Return Book", command=self.return_book).grid(row=4, column=1)

        # --- Output Area ---
        self.output = tk.Text(self.root, height=10, width=50)
        self.output.grid(row=5, column=0, columnspan=2, pady=10)

    def get_user(self):
        name = self.user_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Enter User Name")
            return None
        return Student(name) if self.user_type.get() == "Student" else Teacher(name)

    def add_book(self):
        book = self.book_entry.get().strip()
        if not book:
            messagebox.showwarning("Input Error", "Enter Book Name")
            return
        self.lib.add_book(book)
        self.output.insert(tk.END, f"'{book}' added to library.\n")

    def view_books(self):
        books = self.lib.show_books()
        self.output.insert(tk.END, "Available Books:\n" + "\n".join(f"- {b}" for b in books) + "\n")

    def borrow_book(self):
        user = self.get_user()
        book = self.book_entry.get().strip()
        if user and book:
            result = self.lib.issue_book(book, user)
            self.output.insert(tk.END, result + "\n")

    def return_book(self):
        book = self.book_entry.get().strip()
        if not book:
            messagebox.showwarning("Input Error", "Enter Book Name")
            return
        result = self.lib.return_book(book)
        self.output.insert(tk.END, result + "\n")


# -----------------------
# Run the App
# -----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
