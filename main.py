import musics
import users
from users import *
from musics import *

users_data = []
for i in range(1, 5):
    username = input("Qual é o nome de utilizador?")
    age = int(input("Qual é a idade?"))
    fav_song = input("Música favorita?")
    song_id = getattr(musics.find_music(fav_song), 'id', i)
    create_user(username, age, song_id)

musics_data = []
for i in range(1, 5):
    title = input("Música -> ")
    artist = input("Artista -> ")
    year = int(input("Ano -> "))
    album = input("Álbum -> ")
    insert_music(title, artist, year, album, i)

# Listar todas as músicas na biblioteca, incluindo título, artista e ano.
all_songs = musics.get_all_songs()
print('Todas as músicas:')
for song in all_songs:
    print(song[1] + ' - ' + song[2])

# Consultar todas as músicas adicionadas por um utilizador específico.
# musics.get_user_songs('miguel')

# Listar todos os utilizadores e as respetivas músicas favoritas.
all_users = users.get_all_users()
for user in all_users:
    print(f"{user[1]} tem {user[2]} - música favorita -> {user[3]}")

# Listar as músicas mais recentes (filtrar por ano).


# Exclui a tabela 'musics'
musics.cursor.execute('DROP TABLE musics')
musics.connection.commit()
musics.connection.close()

# Exclui a tabela 'users'
users.cursor.execute('DROP TABLE users')
users.connection.commit()
users.connection.close()