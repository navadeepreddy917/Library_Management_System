from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------- Update Function ----------------

def update_book():

    book_id = id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    category = category_entry.get()
    quantity = quantity_entry.get()

    if book_id == "" or title == "" or author == "" or quantity == "":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET title=?, author=?, category=?, quantity=?
        WHERE id=?
    """, (title, author, category, quantity, book_id))

    conn.commit()

    if cursor.rowcount == 0:
        messagebox.showwarning("Not Found", "No book found with this ID.")
    else:
        messagebox.showinfo("Success", "Book Updated Successfully!")

        id_entry.delete(0, END)
        title_entry.delete(0, END)
        author_entry.delete(0, END)
        category_entry.delete(0, END)
        quantity_entry.delete(0, END)

    conn.close()

# ---------------- Window ----------------

window = Tk()
window.title("Update Book")
window.geometry("500x500")
window.configure(bg="#F4F6F6")

Label(window,
      text="Update Book",
      font=("Arial",20,"bold"),
      bg="#F4F6F6").pack(pady=20)

Label(window,text="Book ID",bg="#F4F6F6").pack()
id_entry=Entry(window,width=35)
id_entry.pack(pady=5)

Label(window,text="Book Title",bg="#F4F6F6").pack()
title_entry=Entry(window,width=35)
title_entry.pack(pady=5)

Label(window,text="Author",bg="#F4F6F6").pack()
author_entry=Entry(window,width=35)
author_entry.pack(pady=5)

Label(window,text="Category",bg="#F4F6F6").pack()
category_entry=Entry(window,width=35)
category_entry.pack(pady=5)

Label(window,text="Quantity",bg="#F4F6F6").pack()
quantity_entry=Entry(window,width=35)
quantity_entry.pack(pady=5)

Button(
    window,
    text="Update Book",
    command=update_book,
    bg="blue",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
).pack(pady=20)

window.mainloop()