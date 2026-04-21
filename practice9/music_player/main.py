import pygame
from player import MusicPlayer

def main():
    pygame.init()
    app = MusicPlayer()
    app.run()
    pygame.quit()

if __name__ == "__main__":
    main()