import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# Constants
BG_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 800
FPS = 60
PLAYER_SPD = 5


pygame.init() #initiliazes pygame
pygame.display.set_caption("Platformer") #sets the title at the top of the game window



window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):

    clock = pygame.time.Clock()


    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit
    quit()

if __name__ == "__main__": # game code is only executed inside game.py
    main(window)