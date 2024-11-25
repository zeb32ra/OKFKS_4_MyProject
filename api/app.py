from flask import Flask, jsonify
import mysql.connector
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password=os.environ.get("MYSQL_ROOT_PASSWORD", "password"),
        database=os.environ.get("MYSQL_DATABASE", "my_database")
    )

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
