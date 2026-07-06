from tkinter import *
from tkinter import messagebox

# ---------------- Login Function ----------------
def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":

        messagebox.showinfo("Success", "Login Successful!")

        root.destroy()

        import dashboard

    else:

        messagebox.showerror("Error", "Invalid Username or Password")


# ---------------- Window ----------------
root = Tk()

root.title("Library Management System")
root.geometry("700x500")
root.configure(bg="#D6EAF8")

heading = Label(
    root,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial",20,"bold"),
    bg="#D6EAF8",
    fg="navy"
)
heading.pack(pady=20)

Label(root, text="Username", font=("Arial",14), bg="#D6EAF8").pack()

username_entry = Entry(root, font=("Arial",14), width=30)
username_entry.pack(pady=10)

Label(root, text="Password", font=("Arial",14), bg="#D6EAF8").pack()

password_entry = Entry(root, font=("Arial",14), width=30, show="*")
password_entry.pack(pady=10)

Button(
    root,
    text="Login",
    command=login,
    bg="green",
    fg="white",
    font=("Arial",14,"bold"),
    width=15
).pack(pady=30)

root.mainloop()