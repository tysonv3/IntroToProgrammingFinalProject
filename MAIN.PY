# my final main file

'''
my final project is...
'''

'''
sources:
picked block colors: https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp

'''

''' imported libraries '''
import pygame
import random

''' built in libraries '''

''' created libraries '''

''' global variables '''
# this creates the colors options for the blocks + the background
colors = [
    (0, 0, 0),
    (0, 240, 240),
    (0, 240, 0),
    (16, 0, 240),
    (160, 0, 241),
    (240, 160, 1),
    (240, 0, 0),
    (240, 240, 2),
    (255, 255, 255),
    (128, 128, 128)
         ]

# block + rotations
o_block = [
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
          [[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]],
          [[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ],
 
i_block = [
          [[0,0,0,0], [0,0,2,0], [0,0,0,0], [0,0,2,0]],
          [[2,2,2,2], [0,0,2,0], [2,2,2,2], [0,0,2,0]],
          [[0,0,0,0], [0,0,2,0], [0,0,0,0], [0,0,2,0]],
          [[0,0,0,0], [0,0,2,0], [0,0,0,0], [0,0,2,0]]
          ],

s_block = [
          [[0,0,0,0], [0,0,3,0], [0,0,0,0], [0,0,3,0]],
          [[0,0,3,3], [0,0,3,3], [0,0,3,3], [0,0,3,3]],
          [[0,3,3,0], [0,0,0,3], [0,3,3,0], [0,0,0,3]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ],

z_block = [
          [[0,0,0,0], [0,0,0,4], [0,0,0,0], [0,0,0,4]],
          [[0,4,4,0], [0,0,4,4], [0,4,4,0], [0,0,4,4]],
          [[0,0,4,4], [0,0,4,0], [0,0,4,4], [0,0,4,0]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ],

l_block = [
          [[0,0,0,0], [0,0,5,0], [0,0,0,5], [0,5,5,0]],
          [[0,5,5,5], [0,0,5,0], [0,5,5,5], [0,0,5,0]],
          [[0,5,0,0], [0,0,5,5], [0,0,0,0], [0,0,5,0]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ],

j_block = [
          [[0,0,0,0], [0,0,6,6], [0,6,0,0], [0,0,6,0]],
          [[0,6,6,6], [0,0,6,0], [0,6,6,6], [0,0,6,0]],
          [[0,0,0,6], [0,0,6,0], [0,0,0,0], [0,6,6,0]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ],

t_block = [
          [[0,0,0,0], [0,0,7,0], [0,0,7,0], [0,0,7,0]],
          [[0,7,7,7], [0,0,7,7], [0,7,7,7], [0,7,7,0]],
          [[0,0,7,0], [0,0,7,0], [0,0,0,0], [0,0,7,0]],
          [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
          ]

''' utility functions '''

''' classes '''
# this creates a class for the tetris block + it holds the matrix that contains the information for the block + its rotation
class Block:

    # possible block representation + its possible rotations
    blocks = [[i_block, z_block, s_block, j_block, l_block, t_block, o_block]]
    
    # randomly picks a block + color
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.block = random.randint(0, len(self.blocks) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    # rotate + get the current location
    def image(self):
        return self.blocks[self.type][self.rotation]
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.blocks[self.type])

class Tetris:
    
    # variables
    level = 2
    score = 0
    state = "start"
    # field of the game that contains zeros where it is empty + colors where there are blocks
    field = []
    height = 0 
    width = 0 
    x = 100
    y = 60
    zoom = 20
    block = None 

    # creates a field with size based on the height and width
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # creates a new block + position with a coordinate at (3,0)
    def new_block(self):
        self.block = Block(3, 0)

    # check if a block is out of bounds or touching another block on the bottom
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                        j + self.block.x > self.width - 1 or \
                        j + self.block.x < 0 or \
                        self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

    # checks if it reaches the bottom to stop the block from continuing to move
    def stop(self):
        for i in range (4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] > 0
                intersection = True
        return intersection

    # checks if full lines are completed 
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width) == 0:
                zeros += 1
        if zeros == 0:
            lines += 1
            for i1 in range(i1, 1, -1):
                for j in range(self.width):
                    self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

# initialize game + create a window
pygame.init()

# displaying the window with set size
pygame.display.set_mode((400, 500))
pygame.display.set_caption('Walmart Tetris')

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False