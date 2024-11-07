import musics
import users

# Inserir utilizadores aqui
users.insert_user('Gui', 19, 0)
users.insert_user('Gustavo', 19, 1)
users.insert_user('Cunha', 19, 2)

# Inserir músicas aqui
musics.insert_music('Thriller', 'Michael Jackson', 1984, 'Thriller', 0)
musics.insert_music('Beat it', 'Michael Jackson', 1980, 'Bad', 2)
musics.insert_music('Smooth Criminal', 'Michael Jackson', 1984, 'Thriller', 1)

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
    print(user[1] + ' tem ' + user[2] + ' - música favorita -> ' + user[3])

# Listar as músicas mais recentes (filtrar por ano).

