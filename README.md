# 📚 Library Management System

A desktop-based **Library Management System** developed using **Python**, **Tkinter**, and **SQLite**. This application provides an easy-to-use graphical interface for managing library books, allowing administrators to perform all essential library operations efficiently.

---

## 📖 Project Overview

The Library Management System is designed to simplify the process of managing books in a library. It enables the administrator to add, search, update, delete, issue, and return books through a simple graphical user interface. The application uses SQLite as the backend database for storing book records.

---

## ✨ Features

- 🔐 Secure Admin Login
- ➕ Add New Books
- 📚 View All Books
- 🔍 Search Books by ID
- ✏️ Update Book Details
- 🗑️ Delete Books
- 📤 Issue Books
- 📥 Return Books
- 💾 SQLite Database Integration
- 🖥️ User-Friendly Graphical Interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Tkinter | Graphical User Interface |
| SQLite3 | Database Management |
| VS Code | Code Editor |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
Library_Management_System/
│
├── assets/
│
├── database/
│   └── library.db
│
├── main.py
├── database.py
├── login.py
├── dashboard.py
├── add_book.py
├── view_books.py
├── search_book.py
├── update_book.py
├── delete_book.py
├── issue_book.py
├── return_book.py
└── README.md
```

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/navadeepreddy917/Library_Management_System.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Library_Management_System
```

### Step 3: Create the Database

```bash
python database.py
```

### Step 4: Run the Application

```bash
python login.py
```

---

## 🔑 Default Login Credentials

**Username**

```
admin
```

**Password**

```
admin123
```

---

## 📸 Modules Included

- Login Module
- Dashboard
- Add Book
- View Books
- Search Book
- Update Book
- Delete Book
- Issue Book
- Return Book
- Database Management

---

## 🗄️ Database

The project uses **SQLite** as the backend database.

### Books Table

| Field | Type |
|-------|------|
| id | INTEGER (Primary Key) |
| title | TEXT |
| author | TEXT |
| category | TEXT |
| quantity | INTEGER |

---

## 📋 How It Works

1. Administrator logs in using valid credentials.
2. Dashboard opens after successful login.
3. Books can be added to the database.
4. All books can be viewed in a table.
5. Books can be searched using their ID.
6. Existing book information can be updated.
7. Books can be deleted from the database.
8. Books can be issued to students.
9. Returned books are added back to the available quantity.

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Python Programming
- GUI Development using Tkinter
- SQLite Database Operations
- CRUD Operations
- File Organization
- Event Handling
- Git and GitHub
- Desktop Application Development

---

## 🔮 Future Enhancements

- Student Registration
- Fine Calculation
- Barcode Integration
- Book Categories Filter
- Export Reports to PDF/Excel
- Email Notifications
- Multi-User Login
- Book Cover Images

---

## 👨‍💻 Author

**Navadeep Reddy**

B.Tech Third Year Student

Annamacharya Institute of Technology and Sciences

---

## 📄 License

This project is developed for educational and learning purposes.

---

# ⭐ Thank You

If you found this project useful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
