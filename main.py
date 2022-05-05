from pacman import Pacman

import pygame
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Multigame")
screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0]-100,pygame.display.get_desktop_sizes()[0][1]-100),pygame.RESIZABLE)

i = 0
running = 1
pac = Pacman(screen)

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
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()