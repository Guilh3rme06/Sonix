# pip install pygame
# Importa a biblioteca pygame que será usada para tocar a música e para manipular ficheiros
import pygame
import os

# Lista todos os arquivos MP3 no diretório especificado
def list_mp3_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.mp3')]

# Função para tocar a música especificada pelo caminho do ficheiro
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Função principal para listar os arquivos MP3 e permitir que o utilizador escolha uma música para tocar
def main():
    directory = 'musics'  # Diretório "musics"
    mp3_files = list_mp3_files(directory)

    if not mp3_files:
        print("Nenhum arquivo MP3 encontrado na pasta 'musics'.")
        return

    print("Escolha uma música para tocar:")
    for idx, file in enumerate(mp3_files):
        print(f"{idx + 1}. {file}")

    choice = int(input("Digite o número da música: ")) - 1

    if 0 <= choice < len(mp3_files):
        play_music(os.path.join(directory, mp3_files[choice]))
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()