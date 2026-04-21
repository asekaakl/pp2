import pygame
import datetime
import math
import os

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (239, 228, 176)

class MickeyClock:
    def __init__(self):
        self.W, self.H = 600, 600
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Mickey Clock")
        self.clock = pygame.time.Clock()

        self.cx = self.W // 2
        self.cy = self.H // 2

        base = os.path.dirname(__file__)
        img_path = os.path.join(base, "images")
        face = pygame.image.load(os.path.join(img_path, "mickeyclock.jpeg")).convert()
        self.face = pygame.transform.scale(face, (self.W, self.H))

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

    def draw_hand(self, angle_deg, length, color, width):
        angle_rad = math.radians(angle_deg - 90)
        x = self.cx + length * math.cos(angle_rad)
        y = self.cy + length * math.sin(angle_rad)
        pygame.draw.line(self.screen, color, (self.cx, self.cy), (int(x), int(y)), width)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            now = datetime.datetime.now()
            h = now.hour % 12
            m = now.minute
            s = now.second

            # Углы стрелок
            hour_angle   = h * 30 + m * 0.5   # 360/12 = 30 градусов на час
            minute_angle = m * 6 + s * 0.1     # 360/60 = 6 градусов на минуту
            second_angle = s * 6               # 360/60 = 6 градусов на секунду

            # Фон
            self.screen.blit(self.face, (0, 0))

            # Часовая стрелка - самая толстая, короткая
            self.draw_hand(hour_angle, 120, BLACK, 8)

            # Минутная стрелка - средняя
            self.draw_hand(minute_angle, 180, BLACK, 6)

            # Секундная стрелка - тонкая красная
            self.draw_hand(second_angle, 200, RED, 2)

            # Центральная точка
            pygame.draw.circle(self.screen, BLACK, (self.cx, self.cy), 8)

            # Время текстом - чёрный фон, белый текст
            text = self.font.render(now.strftime("%H:%M:%S"), True, WHITE, BLACK)
            self.screen.blit(text, (self.W - 140, self.H - 50))

            pygame.display.flip()
            self.clock.tick(60)