from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------- Return Book ----------------

def return_book():

    book_id = id_entry.get()

    if book_id == "":
        messagebox.showerror("Error", "Please enter Book ID.")
        return

    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book is None:
        messagebox.showerror("Error", "Book ID not found.")
    else:
        cursor.execute(
            "UPDATE books SET quantity = quantity + 1 WHERE id=?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Book Returned Successfully!"
        )

        id_entry.delete(0, END)

    conn.close()

# ---------------- Window ----------------

window = Tk()

window.title("Return Book")
window.geometry("450x250")
window.configure(bg="#FCF3CF")

Label(
    window,
    text="Return Book",
    font=("Arial",20,"bold"),
    bg="#FCF3CF",
    fg="#B9770E"
).pack(pady=20)

Label(
    window,
    text="Enter Book ID",
    bg="#FCF3CF",
    font=("Arial",12)
).pack()

id_entry = Entry(window, width=30)
id_entry.pack(pady=10)

Button(
    window,
    text="Return Book",
    command=return_book,
    bg="#B9770E",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
).pack(pady=20)

window.mainloop()