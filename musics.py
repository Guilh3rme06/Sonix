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
    print('Música inserida com sucesso!')

def get_all_songs():
    cursor.execute('SELECT * FROM musics')
    connection.commit()
    return cursor.fetchall()

def delete_song(title):
    cursor.execute('DELETE FROM musics WHERE title = ?', title)
    connection.commit()
    print('Música removida com sucesso!')

cursor.execute('DROP TABLE musics')
connection.commit()
connection.close()