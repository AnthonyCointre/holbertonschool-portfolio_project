import sqlite3


def view_users():
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    for user in users:
        print(f"Username: {user[0]}, Password: {user[1]}")

    conn.close()


view_users()
