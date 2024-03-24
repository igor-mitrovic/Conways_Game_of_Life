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

def update(screen,cells,size,with_progress=False):
    update_cells = np.empty((cells.shape[0],cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2,col-1:col+2]) - cells[row,col]
        color = COLOR_BACKGROUND if cells[row,col] == 0 else COLOR_ALIVE_NEXT

        if cells[row,col] == 1:
            if alive < 2 or alive > 3 :
                if with_progress == True:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <=3:
                update_cells[row,col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT 
        else:
            if alive == 3:
                update_cells[row,col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        pygame.draw.rect(screen,color,(col*size,row*size,size-1,size-1))
    return update_cells


def main():
    pygame.init() 
    #Initialize all of the imported pygame moduels

    root = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Conways Game of Life v1.0")
    cells = np.zeros((60,80))
    root.fill(COLOR_GRID)
    update(root,cells,10)

    pygame.display.flip()
    pygame.display.update()
    running = False
    while True: #Set the main windows loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(root,cells,10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(root,cells,10)
                pygame.display.update()

        root.fill(COLOR_GRID)

        if running:
            cells = update(root,cells,10,with_progress=True)
            pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
