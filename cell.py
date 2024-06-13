import pygame


class Cell:
    def __init__(self, r, c, state, size, win):
        self.r = r
        self.c = c
        self.size = size
        self.state = state
        self.win = win
        self.gaps = 1

    def draw(self):
        win = self.win
        g = self.gaps

        sx = self.c * self.size + g
        sy = self.r * self.size + g

        fx = self.size - g * 2
        fy = self.size - g * 2

        color = pygame.Color("darkorange") if self.state == 1 else pygame.Color("black")
        pygame.draw.rect(win, color, (sx, sy, fx, fy))
