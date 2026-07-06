from tkinter import *
from tkinter import ttk
import sqlite3

# ---------------- Search Function ----------------

def search_book():

    title = search_entry.get()

    # Remove old search results
    for row in tree.get_children():
        tree.delete(row)

    # Connect to database
    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    # Search by title
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ?",
        ('%' + title + '%',)
    )

    books = cursor.fetchall()

    # Display search results
    for book in books:
        tree.insert("", END, values=book)

    conn.close()


# ---------------- Window ----------------

window = Tk()
window.title("Search Book")
window.geometry("900x500")
window.configure(bg="#EAF6F6")

# Heading
Label(
    window,
    text="Search Book",
    font=("Arial",20,"bold"),
    bg="#EAF6F6",
    fg="navy"
).pack(pady=10)

# Search Label
Label(
    window,
    text="Enter Book Title",
    font=("Arial",12),
    bg="#EAF6F6"
).pack()

# Search Box
search_entry = Entry(window, width=40, font=("Arial",12))
search_entry.pack(pady=5)

# Search Button
Button(
    window,
    text="Search",
    command=search_book,
    bg="green",
    fg="white",
    font=("Arial",12,"bold"),
    width=15
).pack(pady=10)

# Table
tree = ttk.Treeview(
    window,
    columns=("ID","Title","Author","Category","Quantity"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Title", text="Book Title")
tree.heading("Author", text="Author")
tree.heading("Category", text="Category")
tree.heading("Quantity", text="Quantity")

tree.column("ID", width=50)
tree.column("Title", width=250)
tree.column("Author", width=180)
tree.column("Category", width=150)
tree.column("Quantity", width=100)

tree.pack(fill=BOTH, expand=True)

window.mainloop()