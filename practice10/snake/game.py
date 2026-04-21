import pygame
import random

# Цвета
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
GREEN  = (0,   200, 0)
DGREEN = (0,   140, 0)
RED    = (220, 0,   0)
YELLOW = (255, 215, 0)
GRAY   = (40,  40,  40)

# Размер клетки
CELL = 20

class Snake:
    def __init__(self):
        self.COLS = 30  # количество клеток по горизонтали
        self.ROWS = 30  # количество клеток по вертикали
        self.W = self.COLS * CELL
        self.H = self.ROWS * CELL

        self.screen = pygame.display.set_mode((self.W, self.H + 60))  # +60 для HUD
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

        self.reset()

    def reset(self):
        # Змейка начинает по центру
        self.snake = [
            (self.COLS // 2,     self.ROWS // 2),
            (self.COLS // 2 - 1, self.ROWS // 2),
            (self.COLS // 2 - 2, self.ROWS // 2),
        ]
        self.direction = (1, 0)   # движение вправо
        self.next_dir  = (1, 0)

        self.score = 0
        self.level = 1
        self.speed = 6            # кадров в секунду

        self.food = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        # Генерируем еду не на стене и не на змейке
        while True:
            x = random.randint(1, self.COLS - 2)
            y = random.randint(1, self.ROWS - 2)
            if (x, y) not in self.snake:
                return (x, y)

    def check_level(self):
        
        new_level = self.score // 4 + 1
        if new_level > self.level:
            self.level = new_level
            self.speed += 2   

    def draw_grid(self):
        # Фон
        self.screen.fill(GRAY)
        # Сетка
        for x in range(self.COLS):
            for y in range(self.ROWS):
                rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw_walls(self):
        # Стены по краям
        for x in range(self.COLS):
            pygame.draw.rect(self.screen, WHITE, (x * CELL, 0, CELL, CELL))
            pygame.draw.rect(self.screen, WHITE, (x * CELL, (self.ROWS - 1) * CELL, CELL, CELL))
        for y in range(self.ROWS):
            pygame.draw.rect(self.screen, WHITE, (0, y * CELL, CELL, CELL))
            pygame.draw.rect(self.screen, WHITE, ((self.COLS - 1) * CELL, y * CELL, CELL, CELL))

    def draw_snake(self):
        for i, (x, y) in enumerate(self.snake):
            color = GREEN if i == 0 else DGREEN  # голова светлее
            pygame.draw.rect(self.screen, color, (x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2), border_radius=4)

    def draw_food(self):
        fx, fy = self.food
        pygame.draw.circle(self.screen, RED,
                           (fx * CELL + CELL // 2, fy * CELL + CELL // 2), CELL // 2 - 2)

    def draw_hud(self):
        # Панель внизу
        hud_y = self.ROWS * CELL
        pygame.draw.rect(self.screen, BLACK, (0, hud_y, self.W, 60))

        score_text = self.font.render(f"Score: {self.score}", True, YELLOW)
        level_text = self.font.render(f"Level: {self.level}", True, GREEN)
        speed_text = self.font.render(f"Speed: {self.speed}", True, WHITE)

        self.screen.blit(score_text, (20,          hud_y + 15))
        self.screen.blit(level_text, (self.W // 2 - 50, hud_y + 15))
        self.screen.blit(speed_text, (self.W - 150, hud_y + 15))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    # Управление змейкой (нельзя повернуть назад)
                    if event.key == pygame.K_UP    and self.direction != (0, 1):
                        self.next_dir = (0, -1)
                    if event.key == pygame.K_DOWN  and self.direction != (0, -1):
                        self.next_dir = (0, 1)
                    if event.key == pygame.K_LEFT  and self.direction != (1, 0):
                        self.next_dir = (-1, 0)
                    if event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.next_dir = (1, 0)

                    # Рестарт
                    if event.key == pygame.K_r and self.game_over:
                        self.reset()

            if not self.game_over:
                self.direction = self.next_dir

                # Новая голова
                hx = self.snake[0][0] + self.direction[0]
                hy = self.snake[0][1] + self.direction[1]
                new_head = (hx, hy)

                # Проверка столкновения со стеной
                if hx <= 0 or hx >= self.COLS - 1 or hy <= 0 or hy >= self.ROWS - 1:
                    self.game_over = True

                # Проверка столкновения с собой
                elif new_head in self.snake:
                    self.game_over = True

                else:
                    self.snake.insert(0, new_head)

                    # Съели еду
                    if new_head == self.food:
                        self.score += 1
                        self.food = self.spawn_food()
                        self.check_level()  # проверяем уровень
                    else:
                        self.snake.pop()  # убираем хвост если еду не съели

                # Рисуем
                self.draw_grid()
                self.draw_walls()
                self.draw_food()
                self.draw_snake()
                self.draw_hud()

            else:
                # Экран game over
                self.screen.fill(BLACK)
                over    = self.font.render("GAME OVER", True, RED)
                score   = self.font.render(f"Score: {self.score}  Level: {self.level}", True, YELLOW)
                restart = self.font.render("Press R to restart", True, WHITE)
                self.screen.blit(over,    (self.W // 2 - over.get_width() // 2,    220))
                self.screen.blit(score,   (self.W // 2 - score.get_width() // 2,   280))
                self.screen.blit(restart, (self.W // 2 - restart.get_width() // 2, 340))

            pygame.display.flip()
            self.clock.tick(self.speed)