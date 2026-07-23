# 🎓 Student Management REST API

A simple and efficient **Student Management REST API** built using **Python, Flask, and SQLite**. This project performs CRUD (Create, Read, Update, Delete) operations on student records and returns responses in JSON format.

---

## 🚀 Features

- ➕ Add New Student
- 📋 View All Students
- ✏️ Update Student Details
- 🗑️ Delete Student
- 💾 SQLite Database Integration
- 🔄 RESTful API
- 📦 JSON Response
- 🧪 API Testing using Postman

---

## 🛠️ Technologies Used

- Python 3
- Flask
- SQLite
- Postman
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```text
Student-Management-REST-API/
│
├── app.py
├── students.db
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── home.png
    ├── terminal.png
    ├── get.png
    ├── post.png
    ├── put.png
    ├── delete.png
    └── project-structure.png
```

---

# 📸 Project Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

---

## 💻 Flask Server Running

![Terminal](screenshots/terminal.png)

---

## 📥 GET API Response

![GET](screenshots/get.png)

---

## ➕ POST API Response

![POST](screenshots/post.png)

---

## ✏️ PUT API Response

![PUT](screenshots/put.png)

---

## 🗑️ DELETE API Response

![DELETE](screenshots/delete.png)

---

## 📂 Project Structure

![Project Structure](screenshots/project-structure.png)

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| POST | `/students` | Add a new student |
| PUT | `/students/<id>` | Update student details |
| DELETE | `/students/<id>` | Delete student |

---

# 🧾 Sample JSON

### POST Request

```json
{
  "id": 1,
  "name": "Vikram Singh",
  "branch": "CSE",
  "semester": 5
}
```

### Response

```json
{
  "message": "Student Added Successfully"
}
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/pariharvikki21-ctrl/Student-Management-REST-API.git
```

### Go to Project Folder

```bash
cd Student-Management-REST-API
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Server will start on:

```text
http://127.0.0.1:5000
```

---

# 🧪 Testing

The API can be tested using:

- Postman
- Thunder Client
- Browser (GET Request)

---

# 💡 Learning Outcomes

During this project I learned:

- Python Programming
- Flask Framework
- SQLite Database
- REST API Development
- CRUD Operations
- JSON Handling
- API Testing using Postman
- Git & GitHub
- Backend Development Basics

---

# 🔮 Future Improvements

- User Authentication
- JWT Login
- Password Encryption
- Search Student
- Pagination
- Swagger API Documentation
- MySQL Database Support
- Docker Deployment

---

# 👨‍💻 Author

**Vikram Singh**

🎓 Diploma in Computer Science Engineering

📍 Uttarakhand, India

GitHub: https://github.com/pariharvikki21-ctrl

---

## ⭐ Support

If you like this project, don't forget to ⭐ Star this repository.
