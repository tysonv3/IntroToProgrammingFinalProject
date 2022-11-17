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
# this creates the colors options for the blocks and the background
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
# this creates a class for the tetris blocks and it holds the matrix that contains the information for the shape of the block
class BlockShapes:
    
    shapes = [
        [[1, 5, 9, 13]], [[4, 5, 6, 7]],
        [[4, 5, 9, 10]], [[2, 6, 5, 9]],
        [[6, 7, 9, 10]], [[1, 5, 6, 10]],
        [[1, 2, 5, 9]], [[0, 4, 5, 6]], [[1, 5, 9, 8]], [[4, 5, 6, 10]],
        [[1, 2, 6, 10]], [[5, 6, 7, 9]], [[2, 6, 10, 11]], [3, 5, 6, 7],
        [[1, 4, 5, 6]], [[1, 4, 5, 9]], [[4, 5, 6, 9]], [[1, 5, 6, 9]],
        [[1, 2, 5, 6]]
             ]
    
