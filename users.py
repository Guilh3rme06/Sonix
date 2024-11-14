import sqlite3

import musics
from musics import *

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
uid = 0
username = ''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    favorite_song INTEGER,
    FOREIGN KEY (favorite_song) REFERENCES musics(id)
    CONSTRAINT username UNIQUE(username)
    )
''')
connection.commit()


def create_user_with_name(username, age=None):
    """
    When the user types their name and is met with the "Unknown user" message,
    they will be prompted to create a new user with the name they typed in.
    :param username: The name that was typed previously
    """
    try:
        if age is None:
            age = int(input("Qual é a idade? "))
        cursor.execute('INSERT INTO users (username, age, favorite_song) VALUES (?, ?, 0)', (username, age))
        connection.commit()
        print("Utilizador criado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este nome de utilizador já existe. Por favor escolha um nome diferente.")
    except ValueError:
        print("\n --------------------------- Erro ao inserir idade ---------------------------")


def find_user_by_name(username):
    """
    Function used to get a specific user by their username.
    :param username: parameter for SQL query.
    :return: The specific user if it exists, if not, returns None
    """
    cursor.execute('SELECT * from users WHERE username = ?', (username,))
    result = cursor.fetchall()
    if result:
        return result[0]
    return None


def find_user_by_id(user_id):
    """
    Function used to get a specific user by their ID.
    :param user_id: parameter for SQL query.
    :return: The specific user if it exists, if not, returns None
    """
    cursor.execute('SELECT * from users WHERE id = ?', (user_id,))
    result = cursor.fetchall()
    if result:
        return result[0]
    return None


def change_user_favorite_song(uid, sid):
    """
    Function used to change a specific user's favorite song.
    :param uid: User id for SQL query
    :param sid: Song id for SQL query
    """
    cursor.execute('UPDATE users SET favorite_song = ? WHERE id = ?', (sid, uid))
    connection.commit()
    print(f'\nMúsica favorita alterada com sucesso!\n')


def print_all_users():
    """
    Function to print all users with their respective ids, ages and favorite songs.
    """
    cursor.execute('SELECT * FROM users')
    resultado = cursor.fetchall()
    if not resultado:
        print('\nNão há utilizadores.')
    else:
        print(f'\nUtilizadores:')
        for user in resultado:
            song = musics.find_music_by_id(user[3])

            if not song or user[3] == 0:
                song_msg = 'Sem música favorita.'
            else:
                song_msg = f'Música favorita - {song[1]}'

            print(f'{user[0]} - {user[1]} - {user[2]} anos\n'
                  f'{song_msg}\n')