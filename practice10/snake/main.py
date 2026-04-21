import pygame
from game import Snake

def main():
    pygame.init()
    app = Snake()
    app.run()
    pygame.quit()

if __name__ == "__main__":
    main()