import sqlite3


def delete_user(username):
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE username = ?", (username,))

    conn.commit()
    print(f"User '{username}' deleted.")

    conn.close()


delete_user('testuser')
