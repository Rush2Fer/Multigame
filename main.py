from random import randint

import pygame
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Multigame")
screen = pygame.display.set_mode((1080, 650))
r = v = b = 0

while(not (pygame.event.peek(pygame.QUIT))):
    screen.fill(pygame.Color(r, v, b))
    r = round(randint(0,255))
    v = round(randint(0,255))
    b = round(randint(0,255))
    
    pygame.display.flip()
    clock.tick(5)
    
pygame.quit()