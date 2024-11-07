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

insert_music("Thriller", "Michael Jackson", 1983, "X", 1)
insert_music("Smooth Criminal", "Michael Jackson", 1987, "Y", 2)
insert_music("Beat It", "Michael Jackson", 1982, "Z", 3)

def get_all_songs(title, artist, year, album, added_by):
    cursor.execute('SELECT * FROM musics')

get_all_songs('?', '?', '?', '?', '?')

results = cursor.fetchall()

for line in results:
    print(line)

cursor.execute('DROP TABLE musics')
connection.commit()
connection.close()