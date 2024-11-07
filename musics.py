import sqlite3

conexao = sqlite3.connect('musics.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS musics(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    artist TEXT,
    year INTEGER,
    album TEXT,
    added_by INTEGER,
    FOREIGN KEY (added_by) REFERENCES users(username)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song INTEGER,
    FOREIGN KEY (favorite_song) REFERENCES musics(title)
    )
''')

conexao.commit()

def insert_music(title, artist, year, album, added_by):
    cursor.execute('INSERT INTO musics (title, artist, year, album, added_by) VALUES (?,?,?,?,?)', (title, artist, year, album, added_by))
    conexao.commit()

insert_music("Thriller", "Michael Jackson", 1983, "X", "Pedro")
insert_music("Smooth Criminal", "Michael Jackson", 1987, "Y", "Gustavo")
insert_music("Beat It", "Michael Jackson", 1982, "Z", "Gui")

def get_all_songs(title, artist, year, album, added_by):
    cursor.execute('SELECT * FROM musics')

get_all_songs('?', '?', '?', '?', '?')

resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conexao.close()