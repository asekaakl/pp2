import pygame
from ball import Ball

def main():
    pygame.init()
    app = Ball()
    app.run()
    pygame.quit()

if __name__ == "__main__":
    main()