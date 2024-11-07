# pip install pygame
import pygame
import os

def list_mp3_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.mp3')]

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    directory = '.'  # Diretório atual
    mp3_files = list_mp3_files(directory)

    if not mp3_files:
        print("Nenhum arquivo MP3 encontrado.")
        return

    print("Escolha uma música para tocar:")
    for idx, file in enumerate(mp3_files):
        print(f"{idx + 1}. {file}")

    choice = int(input("Digite o número da música: ")) - 1

    if 0 <= choice < len(mp3_files):
        play_music(mp3_files[choice])
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()
