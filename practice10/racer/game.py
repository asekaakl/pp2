import pygame
import random

# Цвета
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
RED    = (220, 0,   0)
GRAY   = (100, 100, 100)
YELLOW = (255, 215, 0)
GREEN  = (0,   200, 0)
ORANGE = (255, 140, 0)

class Racer:
    def __init__(self, best=0):  # best передаём чтобы рекорд не сбрасывался
        self.W, self.H = 500, 600
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Racer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

        # Машина игрока
        self.car_w, self.car_h = 50, 80
        self.car_x = self.W // 2 - self.car_w // 2
        self.car_y = self.H - 120
        self.car_speed = 6

        # Препятствия
        self.enemies = []
        self.enemy_speed = 5

        # Монеты
        self.coins = []
        self.coin_speed = 4
        self.score = 0

        # Рекорд — не сбрасывается между играми
        self.best = best

        # Дорога
        self.road_x = 100
        self.road_w = 300
        self.line_y = 0

        # Таймеры спавна
        self.enemy_timer = 0
        self.coin_timer  = 0

        self.game_over = False

    def spawn_enemy(self):
        x = random.randint(self.road_x, self.road_x + self.road_w - 50)
        self.enemies.append(pygame.Rect(x, -80, 50, 80))

    def spawn_coin(self):
        x = random.randint(self.road_x + 10, self.road_x + self.road_w - 30)
        self.coins.append(pygame.Rect(x, -30, 25, 25))

    def draw_road(self):
        self.screen.fill(GREEN)
        pygame.draw.rect(self.screen, GRAY, (self.road_x, 0, self.road_w, self.H))
        self.line_y += self.enemy_speed
        if self.line_y > 60:
            self.line_y = 0
        for y in range(-60 + self.line_y, self.H, 60):
            pygame.draw.rect(self.screen, WHITE, (self.W // 2 - 5, y, 10, 40))

    def draw_car(self):
        car_rect = pygame.Rect(self.car_x, self.car_y, self.car_w, self.car_h)
        pygame.draw.rect(self.screen, (0, 100, 255), car_rect, border_radius=8)
        pygame.draw.rect(self.screen, WHITE, (self.car_x + 8, self.car_y + 10, 34, 20), border_radius=4)

    def draw_enemies(self):
        for e in self.enemies:
            pygame.draw.rect(self.screen, RED, e, border_radius=8)
            pygame.draw.rect(self.screen, WHITE, (e.x + 8, e.y + 10, 34, 20), border_radius=4)

    def draw_coins(self):
        for c in self.coins:
            pygame.draw.circle(self.screen, YELLOW, c.center, 12)
            pygame.draw.circle(self.screen, (200, 160, 0), c.center, 12, 2)

    def draw_hud(self):
        # Монеты — правый верхний угол
        score_text = self.font.render(f"Coins: {self.score}", True, YELLOW)
        self.screen.blit(score_text, (self.W - 130, 10))

        # Рекорд — под монетами
        best_text = self.font.render(f"Best: {self.best}", True, ORANGE)
        self.screen.blit(best_text, (self.W - 130, 40))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        # Передаём рекорд в новую игру
                        self.__init__(best=self.best)

            if not self.game_over:
                # Управление
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and self.car_x > self.road_x:
                    self.car_x -= self.car_speed
                if keys[pygame.K_RIGHT] and self.car_x + self.car_w < self.road_x + self.road_w:
                    self.car_x += self.car_speed

                # Спавн врагов
                self.enemy_timer += 1
                if self.enemy_timer >= 90:
                    self.spawn_enemy()
                    self.enemy_timer = 0

                # Спавн монет
                self.coin_timer += 1
                if self.coin_timer >= 60:
                    self.spawn_coin()
                    self.coin_timer = 0

                # Движение врагов
                for e in self.enemies:
                    e.y += self.enemy_speed
                self.enemies = [e for e in self.enemies if e.y < self.H]

                # Движение монет
                for c in self.coins:
                    c.y += self.coin_speed
                self.coins = [c for c in self.coins if c.y < self.H]

                car_rect = pygame.Rect(self.car_x, self.car_y, self.car_w, self.car_h)

                # Столкновение с врагом
                for e in self.enemies:
                    if car_rect.colliderect(e):
                        # Обновляем рекорд если побили
                        if self.score > self.best:
                            self.best = self.score
                        self.game_over = True

                # Сбор монет
                for c in self.coins[:]:
                    if car_rect.colliderect(c):
                        self.score += 1
                        self.coins.remove(c)

                self.draw_road()
                self.draw_enemies()
                self.draw_coins()
                self.draw_car()
                self.draw_hud()

            else:
                # Экран game over
                self.screen.fill(BLACK)
                new_record = self.score >= self.best and self.score > 0

                over   = self.font.render("GAME OVER", True, RED)
                coins  = self.font.render(f"Coins collected: {self.score}", True, YELLOW)
                best   = self.font.render(f"Best: {self.best}", True, ORANGE)
                restart = self.font.render("Press R to restart", True, WHITE)

                self.screen.blit(over,    (self.W // 2 - over.get_width() // 2,    200))
                self.screen.blit(coins,   (self.W // 2 - coins.get_width() // 2,   260))
                self.screen.blit(best,    (self.W // 2 - best.get_width() // 2,    310))
                self.screen.blit(restart, (self.W // 2 - restart.get_width() // 2, 360))

                # Надпись NEW RECORD если побили рекорд
                if new_record:
                    rec = self.font.render(" NEW RECORD!", True, YELLOW)
                    self.screen.blit(rec, (self.W // 2 - rec.get_width() // 2, 150))

            pygame.display.flip()
            self.clock.tick(60)