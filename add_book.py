from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------- Save Book ----------------
def save_book():
    title = title_entry.get()
    author = author_entry.get()
    category = category_entry.get()
    quantity = quantity_entry.get()

    if title == "" or author == "" or quantity == "":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books(title, author, category, quantity)
    VALUES (?, ?, ?, ?)
    """, (title, author, category, quantity))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Book Added Successfully!")

    title_entry.delete(0, END)
    author_entry.delete(0, END)
    category_entry.delete(0, END)
    quantity_entry.delete(0, END)

# ---------------- Window ----------------
window = Tk()
window.title("Add Book")
window.geometry("500x450")
window.configure(bg="#F4F6F6")

Label(window, text="Add New Book",
      font=("Arial", 20, "bold"),
      bg="#F4F6F6").pack(pady=20)

Label(window, text="Book Title", bg="#F4F6F6").pack()
title_entry = Entry(window, width=35)
title_entry.pack(pady=5)

Label(window, text="Author", bg="#F4F6F6").pack()
author_entry = Entry(window, width=35)
author_entry.pack(pady=5)

Label(window, text="Category", bg="#F4F6F6").pack()
category_entry = Entry(window, width=35)
category_entry.pack(pady=5)

Label(window, text="Quantity", bg="#F4F6F6").pack()
quantity_entry = Entry(window, width=35)
quantity_entry.pack(pady=5)

Button(window,
       text="Save Book",
       command=save_book,
       bg="green",
       fg="white",
       font=("Arial", 12, "bold"),
       width=20).pack(pady=20)

window.mainloop()