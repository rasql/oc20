import pygame
from pygame.locals import *

# Tools > Install packages...
# Find pygame
# Install

# définition de couleurs (RGB red, green, blue) un tuple
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# definition de variables
background = GRAY
key_dict = {K_k:BLACK, K_w:WHITE,
            K_r:RED, K_g:GREEN, K_b:BLUE,
            K_y:YELLOW, K_c:CYAN, K_m:MAGENTA}

# initialiser le module pygame
pygame.init()

# créer une nouvelle fenêtre
screen = pygame.display.set_mode((640, 480))
screen.fill(background)
pygame.display.update() # est nécessaire pour afficher les changement

# boucle principale (event loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT: # cliquer sur le bouton rouge (x)
            running = False
            
        elif event.type == KEYDOWN: # une touche du clavier est appuye
            print(event)
            if event.key in key_dict: # la touche appuyé est une des 8 dans le dictionnaire
                background = key_dict[event.key]
                
                caption = 'backround color = ' + str(background)
                pygame.display.set_caption(caption)
                
            screen.fill(background)
            pygame.display.update()

pygame.quit()