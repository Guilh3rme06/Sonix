import musics
import users
from musics import *
from users import *

create_user_with_name("Guilherme Alves", 18)
create_user_with_name("Gustavo Rodrigues", 18)
create_user_with_name("Pedro Cunha", 18)
create_user_with_name("Tiago Reis", 27)
create_user_with_name("Elieser dos Santos", 54)

insert_music("Tikiti", "Azhunky", 2024, "musicas azhunky", 4)
insert_music("sheets", "jhfly", 2016, "sounds and things",5)
insert_music("Demon", "imagine", 2013, "LOOM", 1)
insert_music("Mockingbird", "Eminem", 2010, "Bodied", 2)
insert_music("Thriller", "Michael Jackson", 2009, "Thriller", 3)

def ask_user_prompt(_user):
    """
    Main page of the program. Has all the main prompts to display/insert information or quit.
    :param _user: The current user's object (includes id and name)
    """
    name = _user[1]
    print(f'\nOlá {name}!')

    options = {
        '1': lambda: insert_music(input('Titulo -> '), input('Artista -> '), input('Ano -> '), input('Álbum -> '), _user[0]),
        '2': lambda: change_favorite_song(_user[0], input('Qual é o título da música? ')),
        '3': print_all_users,
        '4': print_all_songs,
        '5': print_user_songs,
        '6': print_recent_songs,
        '7': logout,
        '8': lambda: quit(f'\nAté logo!\n')
    }

    while True:
        choice = input(
            f"\nEscolha uma opção:"
            f"\n(1) Adicionar Música"
            f"\n(2) Alterar Música favorita"
            f"\n(3) Ver utilizadores"
            f"\n(4) Todas as Músicas"
            f"\n(5) As minhas Músicas"
            f"\n(6) Músicas mais recentes"
            f"\n(7) Mudar de Utilizador"
            f"\n(8) Sair"
            f"\nEscolha uma opção: "
        )
        action = options.get(choice)
        if action:
            action()
        else:
            print("Opção inválida. Tente novamente.")


def change_favorite_song(user_id, title):
    """
    Changes the current user's favorite song.
    :param user_id: Current user id.
    :param title: Song title.
    :return:
    """
    song = find_music(title)
    if song:
        change_user_favorite_song(user_id, song[0])
        print(f"A música favorita foi alterada para '{title}'.")
    else:
        print("Não foi possível alterar a música favorita.")

def logout():
    """
    Prints a goodbye message to the current user and points back to log in.
    :return:
    """
    print(f'\nAdeus, {users.username}')
    login()

def login():
    """
    The starting point of the app. Asks for the username and logs/registers the user.
    """
    user_name = input("\nQual é o seu nome? ")
    user = find_user_by_name(user_name)
    musics.username = user_name
    users.username = user_name

    if user:
        musics.uid = user[0]
        users.uid = user[0]
        ask_user_prompt(user)
    else:
        prompt_create_user = input(f"Utilizador '{user_name}' não encontrado."
              f"\nCriar novo utilizador?"
              f"\n(1) Sim"
              f"\n(2) Não\n")
        match prompt_create_user:
            case '1':
                create_user_with_name(user_name)
                login()
            case _:
                quit('Até logo!')

print("\n-------------------Bem-vind@ ao Sonix!-------------------")
login()