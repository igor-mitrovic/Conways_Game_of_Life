#Convays Game of Life in Python implemented in pygame
import pygame
import numpy as np
import time
import sys

#Defining colors 

COLOR_BACKGROUND = (10,10,10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (170,170,170)
COLOR_ALIVE_NEXT = (255,255,255)


pygame.init() 
#Initialize all of the imported pygame moduels

root = pygame.display.set_mode((800,600))
pygame.display.set_caption("Conways Game of Life v1.0")

clock = pygame.time.Clock(60) #The game will run in 60 frames per second

flag = True
while flag: #Set the main windows loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

#Need to create conway logic
#Split the screen into squares
