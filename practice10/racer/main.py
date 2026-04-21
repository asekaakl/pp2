import pygame
from game import Racer

def main():
    pygame.init()
    app = Racer()
    app.run()
    pygame.quit()

if __name__ == "__main__":
    main()