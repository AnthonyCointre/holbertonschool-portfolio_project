import json
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_users():
    with open('data/users.json', 'r') as f:
        return json.load(f)


def save_users(users):
    with open('data/users.json', 'w') as f:
        json.dump(users, f, indent=2)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = load_users()
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form['username']
        password = request.form['password']

        if action == 'login':
            if username in users['users'] and bcrypt.checkpw(password.encode('utf-8'), users['users'][username].encode('utf-8')):
                session['username'] = username
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Invalid username or password.')
        elif action == 'sign-up':
            if username in users['users']:
                return render_template('login.html', error='Username already exists.')
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())
            users['users'][username] = hashed_password.decode('utf-8')
            save_users(users)
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
