from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

DB_CONFIG = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER', 'admin'),
    'password': os.environ.get('DB_PASS'),
    'database': os.environ.get('DB_NAME', 'notesdb')
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY id DESC LIMIT 20")
    notes = cursor.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title')
    body = request.form.get('body')
    if title and body:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, body) VALUES (%s, %s)", (title, body))
        conn.commit()
        conn.close()
    return '<script>window.location="/"</script>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
