import sqlite3

# Conecta ao banco de dados 'musics.db'
connection = sqlite3.connect('musics.db')
cursor = connection.cursor()
uid = 0

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
    cursor.execute('INSERT INTO musics (title, artist, year, album, added_by) VALUES (?,?,?,?,?)',
                   (title, artist, int(year), album, added_by))
    connection.commit()
    print('Música inserida com sucesso!')


def find_music_by_id(id):
    cursor.execute('SELECT * FROM musics WHERE id = ?', (id,))
    result = cursor.fetchall()
    return result[0] if result else None

# Função para encontrar uma música na tabela 'musics' e retornar seu ID
def find_music(title):
    cursor.execute('SELECT * FROM musics WHERE title = ?', (title,))
    song = cursor.fetchall()
    if song:
        return song[0]

    opcao = input(f'Essa música não existe. Pretende adicionar?'
                  f'\n(1) Sim'
                  f'\n(2) Não')
    match opcao:
        case '1':
            insert_music(title,
                         input('Artista da música -> '),
                         input('Ano da música -> '),
                         input('Álbum da música -> '),
                         uid)
            return find_music(title)
        case '2':
            return None
        case _:
            return None


def get_all_songs():
    cursor.execute('SELECT * FROM musics')
    return cursor.fetchall()


# Função para remover uma música da tabela 'musics' com base no title
def delete_song(title):
    cursor.execute('DELETE FROM musics WHERE title = ?', (title,))
    connection.commit()
    print('Música removida com sucesso!')
