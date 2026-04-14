import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Тест Pygame")

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 128, 255))  # Синий фон
    pygame.display.flip()

pygame.quit()
sys.exit()