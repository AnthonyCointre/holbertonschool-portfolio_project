import sqlite3
import bcrypt


def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (username, hashed_password))

    conn.commit()
    print(f"User '{username}' created.")

    conn.close()


create_user('testuser', 'testuser')
