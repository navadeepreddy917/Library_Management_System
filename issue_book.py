from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------- Issue Book ----------------

def issue_book():

    book_id = id_entry.get()
    student = student_entry.get()

    if book_id == "" or student == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    conn = sqlite3.connect("database/library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book is None:
        messagebox.showerror("Error", "Book ID not found.")
    elif book[0] <= 0:
        messagebox.showwarning("Unavailable", "Book is not available.")
    else:
        cursor.execute(
            "UPDATE books SET quantity = quantity - 1 WHERE id=?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            f"Book Issued Successfully to {student}"
        )

        id_entry.delete(0, END)
        student_entry.delete(0, END)

    conn.close()

# ---------------- Window ----------------

window = Tk()
window.title("Issue Book")
window.geometry("450x300")
window.configure(bg="#E8F8F5")

Label(
    window,
    text="Issue Book",
    font=("Arial",20,"bold"),
    bg="#E8F8F5",
    fg="green"
).pack(pady=20)

Label(window,text="Book ID",bg="#E8F8F5").pack()

id_entry = Entry(window,width=30)
id_entry.pack(pady=5)

Label(window,text="Student Name",bg="#E8F8F5").pack()

student_entry = Entry(window,width=30)
student_entry.pack(pady=5)

Button(
    window,
    text="Issue Book",
    command=issue_book,
    bg="green",
    fg="white",
    font=("Arial",12,"bold"),
    width=20
).pack(pady=20)

window.mainloop()