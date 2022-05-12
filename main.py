from pacman import Pacman
from pacman import Case

import pygame
pygame.init()
clock = pygame.time.Clock()

i = 0
pac = Pacman()

while(pac.running):
    pac.resolution_events()
    
    pac.affiche_pacman()
    
    pac.avance_pacman()

    # Animation ouverture porte sans mettre en pause le programme (déplacement possible)
    pac.animation_ouverture_porte()

    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()