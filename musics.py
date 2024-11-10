from datetime import datetime
from users import *

# Conecta ao banco de dados 'musics.db'
connection = sqlite3.connect('musics.db')
cursor = connection.cursor()
uid = 0
username = ''

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
    """
    Function to insert a new song.
    :param title: song title
    :param artist: song author, singer or band
    :param year: the release year
    :param album: the songs album
    :param added_by: id of the user that is adding the song
    """
    cursor.execute('INSERT INTO musics (title, artist, year, album, added_by) VALUES (?,?,?,?,?)',
                   (title, artist, int(year), album, added_by))
    connection.commit()
    print('Música inserida com sucesso!')


def find_music_by_id(song_id):
    """
    Function to find a specific song by its id.
    :param song_id: the song id.
    :return: The song if it exists, if not, returns None.
    """
    cursor.execute('SELECT * FROM musics WHERE id = ?', (song_id,))
    result = cursor.fetchall()
    return result[0] if result else None


# Função para encontrar uma música na tabela 'musics' e retornar seu ID
def find_music(title):
    """
    Function to find a specific song by its title.
    :param title: the song title.
    :return: The song if it exists. If it doesn't and the user doesn't want to add the song, returns None.
    """
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


def print_all_songs():
    """
        Function to print all songs with their respective id, author, album, year and user.
    """
    cursor.execute('SELECT * FROM musics')
    resultado = cursor.fetchall()
    if not resultado:
        print('\nNão há Músicas.')
    else:
        print(f'\n---------Todas as Músicas---------')
        for song in resultado:
            user = find_user_by_id(song[5])
            if user:
                user_msg = f'Adicionado por {user[1]}'
            else:
                user_msg = f'Utilizador desconhecido.'
            print(f'{song[0]} - "{song[1]}" de {song[2]}'
                  f'\nDo Álbum "{song[4]}" ({song[3]})'
                  f'\n{user_msg}\n')
        print(f'---------Todas as Músicas---------\n')


def print_user_songs():
    """
    Prints all songs added by the current user.
    """
    cursor.execute('SELECT * FROM musics WHERE added_by = ?', (uid,))
    resultado = cursor.fetchall()
    if not resultado:
        print(f'\nVocê não adicionou músicas.')
    else:
        print(f'\n---------Músicas de {username}---------')
        for song in resultado:
            print(f'{song[0]} - "{song[1]}" de {song[2]}'
                  f'\nÁlbum - {song[4]} ({song[3]})')
        print(f'---------Músicas de {username}---------\n')


def print_recent_songs():
    """
    Prints all songs from the last 5 years, in order of most recent.
    """
    min_year = datetime.now().year - 5
    cursor.execute('SELECT * FROM musics WHERE year >= ? ORDER BY year DESC', (min_year,))
    resultado = cursor.fetchall()
    if not resultado:
        print('\nNão há Músicas.')
    else:
        print(f'\n---------Músicas Recentes---------')
        for song in resultado:
            user = find_user_by_id(song[5])
            if user:
                user_msg = f'Adicionado por {user[1]}'
            else:
                user_msg = f'Utilizador desconhecido.'

            print(f'({song[3]}){song[0]} - "{song[1]}" de {song[2]}'
                  f'\nDo Álbum "{song[4]}"'
                  f'\n{user_msg}\n')
        print(f'---------Músicas Recentes---------\n')