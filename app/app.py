from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

##################### CHỖ NÀY TẠO DATABASE 
def get_db_connection():
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row
    return conn
with get_db_connection() as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            message TEXT
        )
    ''')
    conn.commit()
#####################
@app.route('/')
def home():
    return render_template('home.html')
####################
@app.route('/next')
def next_page():
    return render_template('next.html')

@app.route('/get_messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT name, message FROM messages').fetchall()
    conn.close()
    return jsonify([{'name': msg['name'], 'message': msg['message']} for msg in messages])

@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    name = data.get('name', 'Ẩn danh')
    message = data.get('message', '')
    if message:
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Message cannot be empty'}), 400

if __name__ == '__main__':
    app.run(debug=True)
