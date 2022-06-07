import pygame

class Jeu:
    def __init__(self):
        pygame.display.set_caption("Multigame")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0]-100,pygame.display.get_desktop_sizes()[0][1]-100),pygame.RESIZABLE)
        self.screen_size = self.screen.get_size()
        self.running = 1
        self.events = []