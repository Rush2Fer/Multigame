from pacman import PacmanJeu

import pygame
pygame.init()
clock = pygame.time.Clock()

jeu = PacmanJeu()

while(jeu.running):
    jeu.resolution_events()
    
    jeu.affiche_jeu()
    
    jeu.avance()
    jeu.update_animations()

    # Animation ouverture porte sans mettre en pause le programme (déplacement possible)
    jeu.animation_ouverture_porte()

    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()