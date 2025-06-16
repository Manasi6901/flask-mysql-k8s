from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to ToDo API"

@app.route('/add', methods=['POST'])
def add():
    task = request.json['task']
    db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="rootpass",
        database="todo"
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    db.commit()
    return {"message": "Task added"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

