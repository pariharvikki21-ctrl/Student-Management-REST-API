# 🎓 Student Management REST API

A REST API built using **Python, Flask, and SQLite** for managing student records.

## 🚀 Features

- Add Student
- View Students
- Update Student
- Delete Student
- SQLite Database
- JSON Response
- REST API
- CRUD Operations

## 🛠️ Technologies Used

- Python 3
- Flask
- SQLite
- Postman

## 📂 Project Structure

Student_Api/
│── app.py
│── students.db
│── requirements.txt
│── README.md
│── .gitignore

## 📌 API Endpoints

### GET

```http
GET /students
```

Returns all students.

### POST

```http
POST /students
```

Adds a new student.

### PUT

```http
PUT /students/<id>
```

Updates student details.

### DELETE

```http
DELETE /students/<id>
```

Deletes a student.

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/pariharvikki21-ctrl/Student-Management-REST-API.git
```

Go to project folder

```bash
cd Student-Management-REST-API
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Server

```
http://127.0.0.1:5000
```

---

## 👨‍💻 Author

**Vikram Singh**

GitHub:
https://github.com/pariharvikki21-ctrl
