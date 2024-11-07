import sqlite3

connection = sqlite3.connect('musics.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS musics(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    year INTEGER,
    album TEXT,
    added_by INTEGER,
    FOREIGN KEY (added_by) REFERENCES users(id)
    )
''')

connection.commit()

def insert_music(title, artist, year, album, added_by):
    cursor.execute('INSERT INTO musics (title, artist, year, album, added_by) VALUES (?,?,?,?,?)', (title, artist, year, album, added_by))
    connection.commit()

def get_all_songs():
    cursor.execute('SELECT * FROM musics')
    return cursor.fetchall()

results = cursor.fetchall()

cursor.execute('DROP TABLE musics')
connection.commit()
connection.close()