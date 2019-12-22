# GUI.py
# There are two classes in this program
# Grid and Cube
# Grid holds 9 Cubes
import pygame


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.selected = None
        self.model = None
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.model = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def sketch(self, value):
        row, col = self.selected
        self.cubes[row][col].set_temp(value)

    def draw(self, screen):
        # draw 9 grids to hold the cubes
        thick, thin = 4, 3
        unit = self.width / 9

        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                # draw thick lines
                pygame.draw.line(screen, (0, 0, 0), (0, i * unit), (self.width, i * unit), thick)
                pygame.draw.line(screen, (0, 0, 0), (i * unit, 0), (i * unit, self.height), thick)

            else:
                # draw thin lines
                pygame.draw.line(screen, (0, 0, 0), (0, i), (self.width, i), thin)
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, self.height), thin)


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 50)

        gap = self.width
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            screen.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)

    def set_value(self, value):
        self.value = value

    def set_temp(self, temp):
        self.temp = temp


def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    while True:
        pass


main()
