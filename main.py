from pacman import PacmanJeu

import pygame
pygame.init()
clock = pygame.time.Clock()

i = 0
jeu = PacmanJeu()

while(jeu.running):
    jeu.resolution_events()
    
    jeu.affiche_jeu()
    
    jeu.pac.avance()
    jeu.pac.update_animation()

    # Animation ouverture porte sans mettre en pause le programme (déplacement possible)
    jeu.animation_ouverture_porte()

    clock.tick(120)
    pygame.display.flip()
    
pygame.quit()