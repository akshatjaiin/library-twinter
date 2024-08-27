import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def get_books(self):
        return [(book.title, book.author, "Borrowed" if book.is_borrowed else "Available") for book in self.books]

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    return True
                else:
                    return False
        return None

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    return True
                else:
                    return False
        return None

class LibraryApp:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")

        # Frames
        self.add_book_frame = tk.Frame(root)
        self.add_book_frame.pack(pady=10)

        self.view_books_frame = tk.Frame(root)
        self.view_books_frame.pack(pady=10)

        # Add Book Frame
        tk.Label(self.add_book_frame, text="Add Book").grid(row=0, column=0, columnspan=2)
        tk.Label(self.add_book_frame, text="Title:").grid(row=1, column=0)
        self.title_entry = tk.Entry(self.add_book_frame)
        self.title_entry.grid(row=1, column=1)

        tk.Label(self.add_book_frame, text="Author:").grid(row=2, column=0)
        self.author_entry = tk.Entry(self.add_book_frame)
        self.author_entry.grid(row=2, column=1)

        tk.Button(self.add_book_frame, text="Add Book", command=self.add_book).grid(row=3, column=0, columnspan=2)

        # View Books Frame
        tk.Label(self.view_books_frame, text="View Books").grid(row=0, column=0, columnspan=3)

        tk.Button(self.view_books_frame, text="View Books", command=self.view_books).grid(row=1, column=0, columnspan=3)

        self.books_listbox = tk.Listbox(self.view_books_frame, width=50)
        self.books_listbox.grid(row=2, column=0, columnspan=3)

        tk.Label(self.view_books_frame, text="Borrow/Return Book").grid(row=3, column=0, columnspan=3)

        tk.Label(self.view_books_frame, text="Title:").grid(row=4, column=0)
        self.borrow_title_entry = tk.Entry(self.view_books_frame)
        self.borrow_title_entry.grid(row=4, column=1)

        tk.Button(self.view_books_frame, text="Borrow Book", command=self.borrow_book).grid(row=5, column=0)
        tk.Button(self.view_books_frame, text="Return Book", command=self.return_book).grid(row=5, column=1)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.library.add_book(title, author)
            messagebox.showinfo("Success", f'Book "{title}" by {author} added.')
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both title and author.")

    def view_books(self):
        self.books_listbox.delete(0, tk.END)
        books = self.library.get_books()
        for book in books:
            self.books_listbox.insert(tk.END, f'"{book[0]}" by {book[1]} - {book[2]}')

    def borrow_book(self):
        title = self.borrow_title_entry.get()
        if title:
            result = self.library.borrow_book(title)
            if result is True:
                messagebox.showinfo("Success", f'You have borrowed "{title}".')
            elif result is False:
                messagebox.showwarning("Borrow Error", f'"{title}" is already borrowed.')
            else:
                messagebox.showwarning("Borrow Error", f'"{title}" is not available in the library.')
            self.borrow_title_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a book title.")

    def return_book(self):
        title = self.borrow_title_entry.get()
        if title:
            result = self.library.return_book(title)
            if result is True:
                messagebox.showinfo("Success", f'Thank you for returning "{title}".')
            elif result is False:
                messagebox.showwarning("Return Error", f'"{title}" was not borrowed.')
            else:
                messagebox.showwarning("Return Error", f'"{title}" is not a library book.')
            self.borrow_title_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a book title.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
