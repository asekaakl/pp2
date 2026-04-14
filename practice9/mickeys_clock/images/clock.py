import pygame
import datetime
import math
import os
import sys

pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

font = pygame.font.SysFont("Arial", 28, bold=True)
clock = pygame.time.Clock()

base = os.path.dirname(__file__)
img_path = os.path.join(base, "images")

# Загружаем руку Микки
hand_img = pygame.image.load(os.path.join(img_path, "mickey_hand.jpeg")).convert_alpha()
hand_img = pygame.transform.scale(hand_img, (40, 80))

cx, cy = W // 2, H // 2


def draw_hand(angle_deg, length):
    # Поворачиваем руку Микки на нужный угол
    angle_rad = math.radians(angle_deg - 90)
    x = cx + length * math.cos(angle_rad)
    y = cy + length * math.sin(angle_rad)
    
    rotated = pygame.transform.rotate(hand_img, -angle_deg)
    rect = rotated.get_rect(center=(int(x), int(y)))
    screen.blit(rotated, rect)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    # Углы стрелок
    minute_angle = m * 6        # 360 / 60 = 6 градусов на минуту
    second_angle = s * 6        # 360 / 60 = 6 градусов на секунду

    screen.fill(WHITE)

    # Циферблат
    pygame.draw.circle(screen, BLACK, (cx, cy), 150, 3)

    # Правая рука = минуты
    draw_hand(minute_angle, 100)

    # Левая рука = секунды (зеркально)
    draw_hand(-second_angle, 100)

    # Центральная точка
    pygame.draw.circle(screen, BLACK, (cx, cy), 6)

    # Время текстом
    text = font.render(now.strftime("%M:%S"), True, RED, YELLOW)
    screen.blit(text, (430, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()