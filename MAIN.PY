''' TYSON'S FINAL PROJECT IS...TETRIS '''

'''
SOURCES:
previous game attempt
https://www.youtube.com/watch?v=7kGNs5R-AM8
https://www.youtube.com/watch?v=zfvxp7PgQ6c
https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318

'''

''' IMPORTED LIBRARIES '''
import pygame
import random

''' GLOBAL VARIABLES '''
CYAN   = (0, 255, 255  )
GREEN  = (0, 128, 0    )
RED    = (255, 0, 0    )
YELLOW = (255, 255, 0  )
PURPLE = (128, 0, 128  )
ORANGE = (255, 165, 0  )
BLUE   = (0, 0, 255    )
BLACK  = (0, 0, 0      )
WHITE  = (255, 255, 255)
GRAY   = (128, 128, 128)
COLORS = (CYAN, GREEN, RED, YELLOW, PURPLE, ORANGE, BLUE)


''' CLASSES '''
# this sets up the tetris blocks class through matrices
class Tetromino:
    x = 0
    y = 0

    tetrominoes = [
                  # I-block
                  [[1, 5, 9, 13], [4, 5, 6, 7]],
                  # Z-block
                  [[4, 5, 9, 10], [2, 6, 5, 9]],
                  # S-block
                  [[6, 7, 9, 10], [1, 5, 6, 10]],
                  # J-block
                  [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
                  # L-block
                  [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
                  # T-block
                  [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
                  # O-block
                  [[1, 2, 5, 6]],
                  ]

    # initiate the class to randomly pick color and the type
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.tetrominoes) - 1)
        self.color = random.randint(1, len(COLORS) - 1)
        self.rotation = 0

    # rotates and gets the current rotation of a tetromino
    def image(self):
        return self.tetrominoes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.tetrominoes[self.type])

class Tetris:
    # variables
    # starts at 2 since it would get divided by 2 at line 200
    level = 2
    score = 0
    # tells if it is being played or not
    state = "start"
    # contains zeroes to represent that it is empty, and the colors where there are tetrominoes
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    tetromino = None
    
    # initialize the game
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        # creates a field with the height and width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # create a new tetromino and position
    def new_tetromino(self):
        self.tetromino = Tetromino(3, 0)

    # check if the floating tetromino is touching something on the field
    # line 113 checks if we can move or rotate since 0 represents empty space
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tetromino.image():
                    if i + self.tetromino.y > self.height - 1 or \
                            j + self.tetromino.x > self.width - 1 or \
                            j + self.tetromino.x < 0 or \
                            self.field[i + self.tetromino.y][j + self.tetromino.x] > 0:
                        intersection = True
        return intersection

    # checking for full lines
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i][j] = self.field[i - 1][j]
        self.score += lines ** 2

    # moving method, duplicates go_down until it touches something or the bottom
    def go_space(self):
        while not self.intersects():
            self.tetromino.y += 1
        self.tetromino.y -= 1
        self.freeze()

    # moving method
    def go_down(self):
        self.tetromino.y += 1
        if self.intersects():
            self.tetromino.y -= 1
            self.freeze()

    # freezes the tetromino once it reaches the bottom
    # checks if there are full lines to remove and if it goes all the way up, then it is game over
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tetromino.image():
                    self.field[i + self.tetromino.y][j + self.tetromino.x] = self.tetromino.color
        self.break_lines()
        self.new_tetromino()
        if self.intersects():
            self.state = "gameover"

    # moving method
    def go_side(self, dx):
        old_x = self.tetromino.x
        self.tetromino.x += dx
        if self.intersects():
            self.tetromino.x = old_x

    # moving method
    def rotate(self):
        old_rotation = self.tetromino.rotation
        self.tetromino.rotate()
        if self.intersects():
            self.tetromino.rotation = old_rotation

''' GAME LOOP '''
# initialize the game
pygame.init()

# window size
size = (400, 500)
screen = pygame.display.set_mode(size)

# game window title
pygame.display.set_caption('Walmart Tetris')

# game loop until no longer playing
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

# keeps the game going onto it surpasses 100,000
while not done:
    if game.tetromino is None:
        game.new_tetromino()
    counter += 1
    if counter > 100000:
        counter = 0

    # this divides the initial level of 2 as the variable above
    if counter % (fps // game.level // 2) == 0:
        if game.state == "start":
            game.go_down()

    # controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_DOWN:
                game.go_space()
            # allows the game to restart and initializes when the previous game is over
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    # makes the background white
    screen.fill(WHITE)

    # draws the grid 
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, COLORS[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    # this check if it is true and continues running the game until it out of the ranges, and loops when it is in range of the boundaries
    if game.tetromino is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.tetromino.image():
                    pygame.draw.rect(screen, COLORS[game.tetromino.color],
                                     [game.x + game.zoom * (j + game.tetromino.x) + 1,
                                      game.y + game.zoom * (i + game.tetromino.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    # displays text for the score, escape button, and when you finish the game
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (0, 0, 0))
    text_game_over1 = font1.render("Press ESC", True, (0, 0, 0))

    # allows for gameover to be displayed on the screen
    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()