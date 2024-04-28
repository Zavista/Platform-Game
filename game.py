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

def get_background(name): 
    image = pygame.image.load(join("assets", "Background", name)) 
    x, y, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height) # pos of the top-left corner of the background tile
            tiles.append(pos)

    return tiles, image

def draw(window, tiles, bg_image):
    for tile in tiles:
        window.blit(bg_image, tile)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    tiles, bg_image = get_background("Blue.png")
    # Blue
    # Brown
    # Gray
    # Green
    # Pink
    # Purple
    # Yellow

    run = True
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        
        draw(window, tiles, bg_image)
    
    pygame.quit
    quit()

if __name__ == "__main__": # game code is only executed inside game.py
    main(window)