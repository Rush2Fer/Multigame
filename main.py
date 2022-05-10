from pacman import Pacman
from pacman import Case

import pygame
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Multigame")
screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0]-100,pygame.display.get_desktop_sizes()[0][1]-100),pygame.RESIZABLE)

i = 0
running,doors_state = 1,0
pac = Pacman(screen)

# Récupère les portes pour plus tard
portes = pac.portes()
while(running):
    pac.affiche_pacman(screen)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                running = False
            if (event.key == pygame.K_f):
                pygame.display.toggle_fullscreen()

    # Animation ouverture porte sans mettre en pause le programme (déplacement possible)
    time = pygame.time.get_ticks()

    if (doors_state == 0) and time >=4000:
        for e in portes:
            e.update(0)
        doors_state = 1
        print("state update")

    elif (doors_state == 1) and time >= 4500:
        doors_state = 2
        for e in portes:
            e.update(9)
        print("state update")
    elif (doors_state==2) and time >= 5000:
        doors_state = 3
        for e in portes:
            e.update(0)
        print("state update")

    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()