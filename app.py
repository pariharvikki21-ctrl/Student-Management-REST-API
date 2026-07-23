import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Database Create
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        branch TEXT NOT NULL,
        semester INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()


# Home Route
@app.route('/')
def home():
    return "Student Management API"


# GET All Students
@app.route('/students', methods=['GET'])
def get_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "branch": row[2],
            "semester": row[3]
        })

    conn.close()

    return jsonify(students)


# POST Student
@app.route('/students', methods=['POST'])
def add_student():

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, branch, semester) VALUES (?, ?, ?, ?)",
        (
            data["id"],
            data["name"],
            data["branch"],
            data["semester"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student Added Successfully"
    })


# PUT Update Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (data["name"], id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        message = "Student Updated Successfully"
    else:
        message = "Student Not Found"

    conn.close()

    return jsonify({
        "message": message
    })


# DELETE Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        message = "Student Deleted Successfully"
    else:
        message = "Student Not Found"

    conn.close()

    return jsonify({
        "message": message
    })


if __name__ == "__main__":
    app.run(debug=True)