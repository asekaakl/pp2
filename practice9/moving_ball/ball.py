import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Ball:
    def __init__(self):
        self.W, self.H = 600, 600
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Moving Ball")
        self.clock = pygame.time.Clock()

        self.radius = 25
        self.step = 20  

        # Начальная позиция — центр экрана
        self.x = self.W // 2
        self.y = self.H // 2

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Двигаем вверх только если не выйдет за границу
                        if self.y - self.radius - self.step >= 0:
                            self.y -= self.step

                    if event.key == pygame.K_DOWN:
                        if self.y + self.radius + self.step <= self.H:
                            self.y += self.step

                    if event.key == pygame.K_LEFT:
                        if self.x - self.radius - self.step >= 0:
                            self.x -= self.step

                    if event.key == pygame.K_RIGHT:
                        if self.x + self.radius + self.step <= self.W:
                            self.x += self.step

            self.screen.fill(WHITE)

            # Рисуем шар
            pygame.draw.circle(self.screen, RED, (self.x, self.y), self.radius)

            pygame.display.flip()
            self.clock.tick(60)