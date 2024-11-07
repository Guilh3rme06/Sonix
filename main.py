import musics
import users
from users import *

# Inserir utilizadores aqui
username1 = input('Qual é o nome de utilizador?')
age1 = input('Qual é a idade?')
fav_song1 = input('Música favorita?')
username2 = input('Qual é o nome de utilizador?')
age2 = input('Qual é a idade?')
fav_song2 = input('Música favorita?')
username3 = input('Qual é o nome de utilizador?')
age3 = input('Qual é a idade?')
fav_song3 = input('Música favorita?')

search_song1 = musics.find_song(fav_song1) # procurar música por nome "ex.: Thriller" e devolver o ID
search_song2 = musics.find_song(fav_song2) # procurar música por nome "ex.: Billie Jean" e devolver o ID
search_song3 = musics.find_song(fav_song3) # procurar música por nome "ex.: Smooth Criminal" e devolver o ID

create_user(username1, int(age1), int(search_song1))
create_user(username2, int(age2), int(search_song2))
create_user(username3, int(age3), int(search_song3))

# Inserir músicas aqui
song1 = input("Música nova -> ")
artist1 = input("Artista -> ")
year1 = input("Ano -> ")
album1 = input("Álbum -> ")

song2 = input("Música nova -> ")
artist2 = input("Artista -> ")
year2 = input("Ano -> ")
album2 = input("Álbum -> ")

song3 = input("Música nova -> ")
artist3 = input("Artista -> ")
year3 = input("Ano -> ")
album3 = input("Álbum -> ")

musics.insert_music(song1, artist1, year1, album1, 0)
musics.insert_music(song2, artist2, year2, album2, 0)
musics.insert_music(song3, artist3, year3, album3, 0)

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