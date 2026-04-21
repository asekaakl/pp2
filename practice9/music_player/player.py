import pygame
import os
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
BLUE = (100, 149, 237)

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((700, 400))
        pygame.display.set_caption("Music Player")
        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.SysFont("Arial", 32, bold=True)
        self.font2 = pygame.font.SysFont("Arial", 24)

        base = os.path.dirname(__file__)
        music_folder = os.path.join(base, "music")
        self.playlist = []
        for name in os.listdir(music_folder):
            if name.endswith(".mp3") or name.endswith(".wav"):
                self.playlist.append(name)
        self.playlist.sort()

        self.cur = 0
        self.playing = False
        self.paused = False
        self.msg = ""

    def textt(self, txt, font, color, x, y):
        img = font.render(txt, True, color)
        self.screen.blit(img, (x, y))

    def timm(self, sec):
        mm = sec // 60
        ss = sec % 60
        return f"{mm:02}:{ss:02}"

    def playy(self):
        if not self.playlist:
            self.msg = "No music files"
            return
        base = os.path.dirname(__file__)
        path = os.path.join(base, "music", self.playlist[self.cur])
        try:
            if self.paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self.msg = "Playing now"
        except pygame.error:
            self.playing = False
            self.paused = False
            self.msg = "Unsupported audio format"

    def pausee(self):
        pygame.mixer.music.pause()
        self.playing = False
        self.paused = True
        self.msg = "Paused"

    def stopp(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.msg = "Stopped"

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    ch = event.unicode.lower()
                    if ch in ("q", "й"):
                        running = False
                    elif ch in ("p", "з"):
                        if self.playing:
                            self.pausee()
                        else:
                            self.playy()
                    elif ch in ("s", "ы"):
                        self.stopp()
                    elif ch in ("n", "т"):
                        if self.playlist:
                            self.cur = (self.cur + 1) % len(self.playlist)
                            self.playy()
                    elif ch in ("b", "и"):
                        if self.playlist:
                            self.cur = (self.cur - 1) % len(self.playlist)
                            self.playy()

            self.screen.fill(WHITE)
            self.textt("Music Player", self.font1, BLUE, 240, 50)

            if self.playlist:
                self.textt("Track: " + self.playlist[self.cur], self.font2, BLACK, 60, 130)
            else:
                self.textt("Track: No music", self.font2, BLACK, 60, 130)

            if self.playing:
                status, color = "Playing", GREEN
            elif self.paused:
                status, color = "Paused", BLUE
            else:
                status, color = "Stopped", RED

            self.textt("Status: " + status, self.font2, color, 60, 180)

            pos = pygame.mixer.music.get_pos() // 1000
            if pos < 0:
                pos = 0
            self.textt("Position: " + self.timm(pos), self.font2, BLACK, 60, 230)
            self.textt("Message: " + self.msg, self.font2, RED, 60, 270)
            self.textt("P/З-play  S/Ы-stop  N/Т-next  B/И-back  Q/Й-quit", self.font2, BLACK, 60, 320)

            pygame.display.flip()
            self.clock.tick(30)