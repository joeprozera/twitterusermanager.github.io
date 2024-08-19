from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Fetch the list of followed usernames to display on the page
    conn = get_db_connection()
    followed_users = conn.execute('SELECT username FROM followed_users').fetchall()
    conn.close()
    return render_template('index.html', followed_users=followed_users)

@app.route('/submit-username', methods=['POST'])
def submit_username():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify(message="Username is required"), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO followed_users (username) VALUES (?)', (username,))
        conn.commit()
        conn.close()
        return jsonify(message="Followed successfully"), 200
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify(message="Already followed"), 400

if __name__ == '__main__':
    app.run(debug=True)
