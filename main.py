from pacman import PacmanJeu
from pacman import Pacman

import pygame
pygame.init()
clock = pygame.time.Clock()

jeu = PacmanJeu()

while(jeu.running):
    jeu.resolution_events()
    
    jeu.affiche_jeu()
    
    jeu.pac.avance()
    jeu.pac.update_animation()

    # Animation ouverture porte sans mettre en pause le programme (déplacement possible)
    jeu.animation_ouverture_porte()

    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()