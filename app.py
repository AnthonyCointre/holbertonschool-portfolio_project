import sqlite3
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'therapist'


def get_user(username):
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


def save_user(username, hashed_password):
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (username, hashed_password))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form['username']
        password = request.form['password']

        if action == 'login':
            user = get_user(username)
            if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Invalid username or password.')

        elif action == 'sign-up':
            if get_user(username):
                return render_template('login.html', error='Username already exists.')
            hashed_password = bcrypt.hashpw(password.encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')
            save_user(username, hashed_password)
            session['username'] = username
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
