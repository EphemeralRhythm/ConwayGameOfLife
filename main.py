import pygame
from cell import Cell

WIDTH = 1000
HEIGHT = 600
SQUARE_SIZE = 5
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Conway's Game Of Life")

# initial_state = [(2, 0), (0, 0), (0, 1), (-1, 1), (0, 2)]


def main():
    rows = HEIGHT // SQUARE_SIZE
    cols = WIDTH // SQUARE_SIZE

    grid = [[Cell(r, c, 0, SQUARE_SIZE, win) for c in range(cols)] for r in range(rows)]
    started = False

    while True:
        win.fill(pygame.Color("darkslategray"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = not started

            elif pygame.mouse.get_pressed()[0]:
                if started:
                    continue
                x, y = pygame.mouse.get_pos()
                r = y // SQUARE_SIZE
                c = x // SQUARE_SIZE
                grid[r][c].state = not grid[r][c].state

        for r in range(rows):
            for c in range(cols):
                grid[r][c].draw()

        pygame.display.update()
        if started:
            cur = [[cell.state for cell in row] for row in grid]
            next = [[0 for _ in row] for row in grid]

            for r in range(rows):
                for c in range(cols):
                    neighbors = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and cur[nr][nc]:
                                neighbors += 1

                    if cur[r][c] == 0 and neighbors == 3:
                        next[r][c] = 1
                    elif cur[r][c] == 1 and 2 <= neighbors <= 3:
                        next[r][c] = 1
                    else:
                        next[r][c] = 0

            for r in range(rows):
                for c in range(cols):
                    grid[r][c].state = next[r][c]

        clock.tick(12 if not started else 5)


if __name__ == "__main__":
    main()
