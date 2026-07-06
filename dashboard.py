from tkinter import *
import subprocess

# ---------------- Functions ----------------

def open_add_book():
    subprocess.Popen(["python", "add_book.py"])

def open_view_books():
    subprocess.Popen(["python", "view_books.py"])

def open_search_book():
    subprocess.Popen(["python", "search_book.py"])

def open_update_book():
    subprocess.Popen(["python", "update_book.py"])

def open_delete_book():
    subprocess.Popen(["python", "delete_book.py"])

def open_issue_book():
    subprocess.Popen(["python", "issue_book.py"])

def open_return_book():
    subprocess.Popen(["python", "return_book.py"])

# ---------------- Dashboard ----------------

dashboard = Tk()
dashboard.title("Library Management System")
dashboard.geometry("1000x600")
dashboard.configure(bg="#EAF6F6")

heading = Label(
    dashboard,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial",24,"bold"),
    bg="#EAF6F6",
    fg="navy"
)
heading.pack(pady=20)

welcome = Label(
    dashboard,
    text="Welcome Admin",
    font=("Arial",16),
    bg="#EAF6F6",
    fg="green"
)
welcome.pack(pady=10)

button_frame = Frame(dashboard, bg="#EAF6F6")
button_frame.pack(pady=30)

Button(button_frame, text="Add Book", width=20, height=2,
       bg="#3498DB", fg="white",
       font=("Arial",12,"bold"),
       command=open_add_book).grid(row=0, column=0, padx=20, pady=15)

Button(button_frame, text="View Books", width=20, height=2,
       bg="#2ECC71", fg="white",
       font=("Arial",12,"bold"),
       command=open_view_books).grid(row=0, column=1, padx=20, pady=15)

Button(button_frame, text="Search Book", width=20, height=2,
       bg="#F39C12", fg="white",
       font=("Arial",12,"bold"),
       command=open_search_book).grid(row=1, column=0, padx=20, pady=15)

Button(button_frame, text="Update Book", width=20, height=2,
       bg="#9B59B6", fg="white",
       font=("Arial",12,"bold"),
       command=open_update_book).grid(row=1, column=1, padx=20, pady=15)

Button(button_frame, text="Delete Book", width=20, height=2,
       bg="#E74C3C", fg="white",
       font=("Arial",12,"bold"),
       command=open_delete_book).grid(row=2, column=0, padx=20, pady=15)

Button(button_frame, text="Issue Book", width=20, height=2,
       bg="#16A085", fg="white",
       font=("Arial",12,"bold"),
       command=open_issue_book).grid(row=2, column=1, padx=20, pady=15)

Button(button_frame, text="Return Book", width=20, height=2,
       bg="#D35400", fg="white",
       font=("Arial",12,"bold"),
       command=open_return_book).grid(row=3, column=0, padx=20, pady=15)

Button(button_frame, text="Exit", width=20, height=2,
       bg="black", fg="white",
       font=("Arial",12,"bold"),
       command=dashboard.destroy).grid(row=3, column=1, padx=20, pady=15)

dashboard.mainloop()