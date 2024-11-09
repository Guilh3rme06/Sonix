from venv import create

import musics
import users
from musics import insert_music, find_music
from users import find_user, change_user_favorite_song, print_all_users, create_user


def ask_user_prompt(_user):
    while True:
        name = _user[1]
        print(f'\nOlá {name}!')
        choice = input(
            f"\n(1) Adicionar Música"
            f"\n(2) Alterar Música Favorita"
            f"\n(3) Ver utilizadores"
            f"\n(4) Sair"
            f"\nEscolha uma opção: "
        )
        match choice:
            case '1':
                insert_music(
                    input('Titulo -> '),
                    input('Artista -> '),
                    input('Ano -> '),
                    input('Álbum -> '),
                    _user[0])
            case '2':
                title = input('Qual é o título da música? ')
                change_favorite_song(_user[0], title)
            case '3':
                print_all_users()
                break
            case '4':
                quit(f'\nAté logo!\n')
            case _:
                print("Opção inválida. Tente novamente.")


def change_favorite_song(user_id, title):
    song = find_music(title)
    if song:
        change_user_favorite_song(user_id, song[0])
        print(f"A música favorita foi alterada para '{title}'.")
    else:
        print("Não foi possível alterar a música favorita.")


def login():
    user_name = input("Qual é o seu nome? ")
    user = find_user(user_name)

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
                users.create_user_with_name(user_name)
                login()
            case _:
                quit('Até logo!')

print("\n-------------------Bem-vind@ ao Sonix!-------------------")
login()