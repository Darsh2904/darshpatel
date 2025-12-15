import pickle
import os

FILE = "library.dat"

def load_books():
    if os.path.exists(FILE):
        f = open(FILE, "rb")
        books = pickle.load(f)
        f.close()
        return books
    return []

def save_books(books):
    f = open(FILE, "wb")
    pickle.dump(books, f)
    f.close()

def login():
    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")

        if username == "Darsh" and password == "@Darsh2014":
            print("Login successful")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print("Invalid login. Attempts left:", attempts)

    print("Too many failed attempts. Program terminated.")
    return False

def add_book():
    books = load_books()
    bid = int(input("Book ID: "))

    for b in books:
        if b["id"] == bid and b["active"] == True:
            print("Duplicate Book ID not allowed")
            return

    book = {
        "id": bid,
        "title": input("Title: "),
        "author": input("Author: "),
        "qty": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "active": True
    }

    books.append(book)
    save_books(books)
    print("Book added successfully")

def display_books():
    books = load_books()
    print("\nID  Title  Author  Qty  Price")

    for b in books:
        if b["active"] == True:
            print(b["id"], b["title"], b["author"], b["qty"], b["price"])

def search_book():
    books = load_books()
    print("1. Search by ID")
    print("2. Search by Title")
    ch = int(input("Choice: "))

    if ch == 1:
        bid = int(input("Enter Book ID: "))
        for b in books:
            if b["id"] == bid and b["active"] == True:
                print("Found:", b)
                return

    elif ch == 2:
        title = input("Enter Title: ")
        for b in books:
            if b["title"] == title and b["active"] == True:
                print("Found:", b)
                return

    print("Book not found")

def delete_book():
    books = load_books()
    print("1. Delete by ID")
    print("2. Delete by Title")
    ch = int(input("Choice: "))

    if ch == 1:
        bid = int(input("Enter Book ID: "))
        for b in books:
            if b["id"] == bid and b["active"] == True:
                b["active"] = False
                save_books(books)
                print("Book deleted")
                return

    elif ch == 2:
        title = input("Enter Title: ")
        for b in books:
            if b["title"] == title and b["active"] == True:
                b["active"] = False
                save_books(books)
                print("Book deleted")
                return

    print("Book not found")

def main():
    if not login():
        return

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            add_book()
        elif ch == 2:
            display_books()
        elif ch == 3:
            search_book()
        elif ch == 4:
            delete_book()
        elif ch == 5:
            print("Program exited safely")
            break
        else:
            print("Invalid choice")

main()