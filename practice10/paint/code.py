import pygame

# Цвета палитры
COLORS = [
    (0,   0,   0),    # чёрный
    (255, 255, 255),  # белый
    (220, 0,   0),    # красный
    (0,   200, 0),    # зелёный
    (0,   0,   220),  # синий
    (255, 215, 0),    # жёлтый
    (255, 140, 0),    # оранжевый
    (150, 0,   200),  # фиолетовый
    (0,   200, 200),  # голубой
    (139, 69,  19),   # коричневый
]

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GRAY  = (200, 200, 200)
DGRAY = (150, 150, 150)

TOOLBAR_H = 60  # высота панели инструментов

class Paint:
    def __init__(self):
        self.W, self.H = 800, 600
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Paint")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 16, bold=True)

        # Холст — белый
        self.canvas = pygame.Surface((self.W, self.H - TOOLBAR_H))
        self.canvas.fill(WHITE)

        self.color     = BLACK   # текущий цвет
        self.tool      = "pen"   # текущий инструмент
        self.brush_size = 5      # размер кисти

        # Для прямоугольника и круга — начальная точка
        self.start_pos = None
        self.drawing   = False

    def draw_toolbar(self):
        # Фон панели
        pygame.draw.rect(self.screen, GRAY, (0, 0, self.W, TOOLBAR_H))
        pygame.draw.line(self.screen, DGRAY, (0, TOOLBAR_H), (self.W, TOOLBAR_H), 2)

        # Инструменты
        tools = ["pen", "rect", "circle", "eraser"]
        labels = ["Pen", "Rect", "Circle", "Eraser"]
        for i, (t, label) in enumerate(zip(tools, labels)):
            x = 10 + i * 80
            color = DGRAY if self.tool == t else WHITE
            pygame.draw.rect(self.screen, color, (x, 10, 70, 40), border_radius=6)
            pygame.draw.rect(self.screen, BLACK, (x, 10, 70, 40), 2, border_radius=6)
            text = self.font.render(label, True, BLACK)
            self.screen.blit(text, (x + 35 - text.get_width() // 2, 22))

        # Палитра цветов
        for i, c in enumerate(COLORS):
            x = 350 + i * 35
            pygame.draw.rect(self.screen, c, (x, 12, 30, 30), border_radius=4)
            # Рамка вокруг выбранного цвета
            if c == self.color:
                pygame.draw.rect(self.screen, BLACK, (x - 2, 10, 34, 34), 3, border_radius=4)

        # Текущий цвет
        pygame.draw.rect(self.screen, self.color, (710, 12, 30, 30), border_radius=4)
        pygame.draw.rect(self.screen, BLACK, (710, 12, 30, 30), 2, border_radius=4)

        # Размер кисти
        size_text = self.font.render(f"Size: {self.brush_size}", True, BLACK)
        self.screen.blit(size_text, (750, 22))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Выбор цвета и инструмента мышкой
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos

                    # Клик по панели инструментов
                    if my < TOOLBAR_H:
                        # Инструменты
                        tools = ["pen", "rect", "circle", "eraser"]
                        for i, t in enumerate(tools):
                            x = 10 + i * 80
                            if x <= mx <= x + 70:
                                self.tool = t

                        # Палитра
                        for i, c in enumerate(COLORS):
                            x = 350 + i * 35
                            if x <= mx <= x + 30:
                                self.color = c

                    # Клик по холсту
                    else:
                        self.drawing = True
                        self.start_pos = (mx, my - TOOLBAR_H)

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.drawing and self.start_pos:
                        mx, my = event.pos
                        end_pos = (mx, my - TOOLBAR_H)

                        # Рисуем прямоугольник
                        if self.tool == "rect":
                            x = min(self.start_pos[0], end_pos[0])
                            y = min(self.start_pos[1], end_pos[1])
                            w = abs(end_pos[0] - self.start_pos[0])
                            h = abs(end_pos[1] - self.start_pos[1])
                            pygame.draw.rect(self.canvas, self.color, (x, y, w, h), 2)

                        # Рисуем круг
                        if self.tool == "circle":
                            cx = (self.start_pos[0] + end_pos[0]) // 2
                            cy = (self.start_pos[1] + end_pos[1]) // 2
                            r  = int(((end_pos[0] - self.start_pos[0])**2 + (end_pos[1] - self.start_pos[1])**2) ** 0.5 // 2)
                            pygame.draw.circle(self.canvas, self.color, (cx, cy), r, 2)

                    self.drawing   = False
                    self.start_pos = None

                # Размер кисти колёсиком
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_PLUS:
                        self.brush_size = min(30, self.brush_size + 1)
                    if event.key == pygame.K_KP_MINUS:
                        self.brush_size = max(1, self.brush_size - 1)
                # Клавиши
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.canvas.fill(WHITE)  # очистить холст
                    if event.key == pygame.K_1:
                        self.tool = "pen"
                    if event.key == pygame.K_2:
                        self.tool = "rect"
                    if event.key == pygame.K_3:
                        self.tool = "circle"
                    if event.key == pygame.K_4:
                        self.tool = "eraser"

            # Рисование пером и ластиком (зажатая кнопка мыши)
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                if my > TOOLBAR_H:
                    canvas_y = my - TOOLBAR_H
                    if self.tool == "pen":
                        pygame.draw.circle(self.canvas, self.color, (mx, canvas_y), self.brush_size)
                    elif self.tool == "eraser":
                        pygame.draw.circle(self.canvas, WHITE, (mx, canvas_y), self.brush_size * 3)

            # Отрисовка
            self.screen.blit(self.canvas, (0, TOOLBAR_H))
            self.draw_toolbar()
            pygame.display.flip()
            self.clock.tick(60)