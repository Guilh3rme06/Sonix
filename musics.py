import sqlite3

# Conecta ao banco de dados 'musics.db'
connection = sqlite3.connect('musics.db')
cursor = connection.cursor()

# Cria a tabela 'musics' se ela não existir
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

# Função para inserir uma nova música na tabela 'musics'
def insert_music(title, artist, year, album, added_by):
    cursor.execute('INSERT INTO musics (title, artist, year, album, added_by) VALUES (?,?,?,?,?)', (title, artist, year, album, added_by))
    connection.commit()
    print('Música inserida com sucesso!')

# Função para obter todas as músicas da tabela 'musics'
def get_all_songs():
    cursor.execute('SELECT * FROM musics')
    connection.commit()
    return cursor.fetchall()

# Função para remover uma música da tabela 'musics' com base no title
def delete_song(title):
    cursor.execute('DELETE FROM musics WHERE title = ?', title)
    connection.commit()
    print('Música removida com sucesso!')

# Exclui a tabela 'musics'
cursor.execute('DROP TABLE musics')
connection.commit()

# Fecha a conexão com o banco de dados
connection.close()