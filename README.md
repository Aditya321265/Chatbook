# 💬 ChatBook

ChatBook is a beginner-friendly **Python Object-Oriented Programming (OOP)** project that simulates a simple social messaging platform.

The project is designed to understand and implement important Python OOP concepts such as **classes, objects, instance methods, magic/dunder methods, `self`, encapsulation, getters, setters, and static methods**.

---

## 📌 Project Overview

ChatBook allows users to create profiles and perform basic operations such as:

* Create a user account
* Store user information
* Display user profiles
* Send messages
* Manage passwords using encapsulation
* Validate passwords
* Validate email addresses
* Use getters and setters for controlled access to private data

The main purpose of this project is to understand how **Object-Oriented Programming** can be used to structure a real-world application.

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Covered

### 1. Class

A class acts as a blueprint for creating users.

```python
class User:
    pass
```

### 2. Object

Objects are individual instances created from the `User` class.

```python
user1 = User(...)
user2 = User(...)
```

### 3. `__init__()` — Constructor

The `__init__()` method initializes the attributes of each user object.

```python
def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.__password = password
```

### 4. `self`

`self` refers to the current object and allows us to access its attributes and methods.

```python
self.name
self.email
```

### 5. Instance Methods

Methods that operate on a particular user object.

```python
def send_message(self, message):
    print(self.name, "sent:", message)
```

### 6. Magic / Dunder Methods

Special methods surrounded by double underscores.

Example:

```python
def __str__(self):
    return f"User: {self.name}"
```

This controls how a user object is represented when using:

```python
print(user1)
```

### 7. Encapsulation

Sensitive information such as passwords is protected using a private attribute.

```python
self.__password = password
```

### 8. Getter

A getter is used to retrieve a private attribute.

```python
def get_password(self):
    return self.__password
```

### 9. Setter

A setter is used to update a private attribute while allowing validation.

```python
def set_password(self, new_password):
    if len(new_password) >= 8:
        self.__password = new_password
```

### 10. Static Method

A static method performs functionality that does not depend on a particular user object.

```python
@staticmethod
def validate_email(email):
    return "@" in email
```

---

## 📂 Project Structure

```text
ChatBook/
│
├── chatbook.py
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ChatBook.git
```

### 2. Navigate to the project

```bash
cd ChatBook
```

### 3. Run the Python file

```bash
python chatbook.py
```

---

## 💻 Example Usage

```python
user1 = User(
    "Aditya",
    "aditya@example.com",
    "password123"
)

user1.get_profile()

user1.send_message("Hello everyone!")

user1.set_password("newpassword123")

print(User.validate_email("aditya@example.com"))

print(user1)
```

Example output:

```text
Name: Aditya
Email: aditya@example.com

Aditya sent: Hello everyone!

Password updated

True

User: Aditya
```

---

## 🎯 Learning Objectives

Through this project, I am learning how to:

* Build classes and objects in Python
* Understand the use of `self`
* Create constructors using `__init__()`
* Differentiate between functions and methods
* Understand magic/dunder methods
* Implement encapsulation
* Use getters and setters
* Implement static methods
* Structure a small real-world application using OOP
* Use Git and GitHub for project version control

---

## 🚀 Future Improvements

Possible improvements for the project include:

* User login and authentication
* Friend requests
* Multiple-user messaging
* Message history
* Profile updates
* Password hashing
* Database integration
* User search
* GUI or web interface
* REST API integration

---

## 👨‍💻 Author

**Aditya Pattnaik**

This project was created as part of my Python and Object-Oriented Programming learning journey.

---

## 📄 License

This project is created for educational and learning purposes.
