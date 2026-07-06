from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------- Delete Function ----------------

def delete_book():

    book_id = id_entry.get()

    if book_id == "":
        messagebox.showerror("Error", "Please enter Book ID.")
        return

    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()

    if cursor.rowcount == 0:
        messagebox.showwarning("Not Found", "No book found with this ID.")
    else:
        messagebox.showinfo("Success", "Book Deleted Successfully!")

    conn.close()

    id_entry.delete(0, END)

# ---------------- Window ----------------

window = Tk()

window.title("Delete Book")
window.geometry("450x250")
window.configure(bg="#FDEDEC")

Label(
    window,
    text="Delete Book",
    font=("Arial",20,"bold"),
    bg="#FDEDEC",
    fg="red"
).pack(pady=20)

Label(
    window,
    text="Enter Book ID",
    font=("Arial",12),
    bg="#FDEDEC"
).pack()

id_entry = Entry(window, width=30, font=("Arial",12))
id_entry.pack(pady=10)

Button(
    window,
    text="Delete Book",
    command=delete_book,
    bg="red",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
).pack(pady=20)

window.mainloop()