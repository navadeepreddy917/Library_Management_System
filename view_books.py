from tkinter import *
from tkinter import ttk
import sqlite3

# Create the main window
window = Tk()
window.title("View Books")
window.geometry("900x500")

# Heading
heading = Label(
    window,
    text="Library Books",
    font=("Arial", 20, "bold")
)
heading.pack(pady=10)

# Create Table
tree = ttk.Treeview(
    window,
    columns=("ID", "Title", "Author", "Category", "Quantity"),
    show="headings"
)

# Table Headings
tree.heading("ID", text="ID")
tree.heading("Title", text="Book Title")
tree.heading("Author", text="Author")
tree.heading("Category", text="Category")
tree.heading("Quantity", text="Quantity")

# Column Width
tree.column("ID", width=50)
tree.column("Title", width=250)
tree.column("Author", width=180)
tree.column("Category", width=150)
tree.column("Quantity", width=100)

tree.pack(fill=BOTH, expand=True)

# Connect to Database
conn = sqlite3.connect("database/library.db")

cursor = conn.cursor()

# Fetch all books
cursor.execute("SELECT * FROM books")

books = cursor.fetchall()

# Display books in the table
for book in books:
    tree.insert("", END, values=book)

# Close connection
conn.close()

# Keep window open
window.mainloop()