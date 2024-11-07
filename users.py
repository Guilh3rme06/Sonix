import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song integer,
    FOREIGN KEY (favorite_song) REFERENCES musics(id)
        )
    ''')

connection.commit()

def insert_user(username, age, favorite_song):
    cursor.execute('INSERT INTO users (username, age, favorite_song) VALUES (?, ?, ?)', (username, age, favorite_song))
    connection.commit()
    print('Utilizador registado com sucesso!')
def find_user(username):
    cursor.execute('SELECT * from users WHERE username = ?', username)
    connection.commit()
    return cursor.fetchall()
def delete_user(username):
    cursor.execute('DELETE FROM users WHERE username = ?', username)
    connection.commit()
def get_all_users():
    cursor.execute('SELECT * FROM users')
    connection.commit()
    return cursor.fetchall()

cursor.execute('DROP TABLE users')
connection.commit()
connection.close()