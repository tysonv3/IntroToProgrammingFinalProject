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
         ]

''' utility functions '''

''' classes '''
# this creates a class for the tetris blocks + it holds the matrix that contains the information for the block + its rotation
class Block:

    # possible block representation + its possible rotations
    blocks = [
        # i-block + rotation
        [[1, 5, 9, 13]], [[4, 5, 6, 7]],
        # z-block + rotation
        [[4, 5, 9, 10]], [[2, 6, 5, 9]],
        # s-block + rotation
        [[6, 7, 9, 10]], [[1, 5, 6, 10]],
        # j-block + rotations
        [[1, 2, 5, 9]], [[0, 4, 5, 6]], [[1, 5, 9, 8]], [[4, 5, 6, 10]],
        # l-block + rotations
        [[1, 2, 6, 10]], [[5, 6, 7, 9]], [[2, 6, 10, 11]], [3, 5, 6, 7],
        # t-block + rotations
        [[1, 4, 5, 6]], [[1, 4, 5, 9]], [[4, 5, 6, 9]], [[1, 5, 6, 9]],
        # o-block
        [[1, 2, 5, 6]]
             ]
    
    # randomly picks a block + color
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.block = random.randint(0, len(self.blocks) - 1)
        self.color = random.random(1, len(colors) - 1)
        self.rotation = 0

    # rotate + get the current location
    def image(self):
        return self.blocks[self.type][self.rotation]
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.blocks[self.type])

class Tetris:
    
    # global variables
    level = 2
    score = 0
    state = "start"
    # field of the game that contains zeros where it is empty + colors where there are figures
    field = []
    height = 0 
    width = 0 
    x = 100
    y = 60
    zoom = 20
    block = None 

    # initialize the game + creates a field with size based on the height and width
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # creates a new block + position with a coordinate at (3,0)
    def new_block(self):
        self.block = Block(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                        j + self.figure.x > self.width - 1 or \
                        j + self.figure.x < 0 or \
                        self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection