#Convays Game of Life in Python implemented in pygame
import pygame
import sys


pygame.init() 
#Initialize all of the imported pygame moduels

root = pygame.display.set_mode((800,600))
pygame.display.set_caption("Conways Game of Life v1.0")

flag = True
while flag: #Set the main windows loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
