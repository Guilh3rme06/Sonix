import sqlite3

from musics import find_music, find_music_by_id

# Conecta ao banco de dados 'users.db'
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Cria a tabela 'users' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song INTEGER,
    FOREIGN KEY (favorite_song) REFERENCES musics(id)
    )
''')
connection.commit()


# Função para criar um utilizador na tabela 'users'
def create_user():
    username = input("Qual é o nome de utilizador? ")
    age = int(input("Qual é a idade? "))
    cursor.execute('INSERT INTO users (username, age, favorite_song) VALUES (?, ?, 0)', (username, age))
    print("Utilizador criado com sucesso!")
    connection.commit()

def create_user_with_name(username):
    age = int(input("Qual é a idade? "))
    cursor.execute('INSERT INTO users (username, age, favorite_song) VALUES (?, ?, 0)', (username, age))
    print("Utilizador criado com sucesso!")
    connection.commit()

# Função para encontrar um utilizador na tabela 'users'
def find_user(username):
    cursor.execute('SELECT * from users WHERE username = ?', (username,))
    result = cursor.fetchall()
    if result:
        return result[0]
    return None


# Função para remover um utilizador da tabela 'users' com base no username
def delete_user(username):
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    connection.commit()


def change_user_favorite_song(uid, sid):
    cursor.execute('UPDATE users SET favorite_song = ? WHERE id = ?', (sid, uid))
    connection.commit()
    print(f'\nMúsica favorita alterada com sucesso!\n')


# Função para obter todos os utilizadores da tabela 'users'
def print_all_users():
    cursor.execute('SELECT * FROM users')
    resultado = cursor.fetchall()
    if not resultado:
        print('Não há utilizadores.')

    else:
        print(f'\nUtilizadores:')
        for user in resultado:
            song = find_music_by_id(user[3])

            if not song or user[3] == 0:
                song_msg = 'Sem música favorita.'
            else:
                song_msg = f'Música favorita - {song[1]}'

            print(f'{user[0]} - {user[1]} - {user[2]} anos\n'
                  f'{song_msg}\n')

