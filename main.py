import musics
import users
# Listar todas as músicas na biblioteca, incluindo título, artista e ano.
all_songs = musics.get_all_songs()

# Consultar todas as músicas adicionadas por um utilizador específico.
musics.get_user_songs('miguel')

# Listar todos os utilizadores e as respetivas músicas favoritas.
all_users = users.get_all_users()
all_users.foreach((user) =>{
    users.get_fav_song(user.id)
})
# Listar as músicas mais recentes (filtrar por ano).
