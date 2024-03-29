# GUI.py
# There are two classes in this program
# Grid and Cube
# Grid holds 9 Cubes
import pygame
from solver import checker, solver, print_board
pygame.font.init()

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

        # draw lines
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                # draw thick lines
                pygame.draw.line(screen, (0, 0, 0), (0, i * unit), (self.width, i * unit), thick)
                pygame.draw.line(screen, (0, 0, 0), (i * unit, 0), (i * unit, self.height), thick)

            else:
                # draw thin lines
                pygame.draw.line(screen, (0, 0, 0), (0, i * unit), (self.width, i * unit), thin)
                pygame.draw.line(screen, (0, 0, 0), (i * unit, 0), (i * unit, self.height), thin)

        # draw cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(screen)

    # clear selected box
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def put(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_value(val)
            self.update_model()

            if solver(self.model) and checker(self.model, val, row, col):
                return True
            else:
                self.cubes[row][col].set_value(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            gap = self.width / 9
            x = position[0] // gap
            y = position[1] // gap
            return (int(x), int(y))
        else:
            return None

    def sketch(self, key):
        row, col = self.selected
        self.cubes[row][col].set_temp(key)

    def select(self, col, row):

        # reset all cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def solve(self):
        solver(self.board)
        print_board(self.board)
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]





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
        self.temp = 0

    def draw(self, screen):
        font = pygame.font.SysFont("comicsans", 50)

        gap = self.width / 9
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


def redraw(screen, board):
    # background color
    screen.fill((255, 255, 255))
    board.draw(screen)


def main():
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    run = True

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        # if temp value is correct
                        if board.put(board.cubes[i][j].temp):
                            print("Correct")
                        else:
                            print("Wrong")
                        key = None

                    if board.is_finished():
                        print("Game Over")
                        run = False

                if event.key == pygame.K_SPACE:
                    board.solve()
                    print("space")

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                print(position)
                clicked = board.click(position)
                print(clicked)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw(screen, board)
        pygame.display.update()


main()
pygame.quit()
