import pygame, sys
pygame.init()
clock = pygame.time.Clock()
from pacman import PacmanJeu as Pacman
from pacman import PacmanJeu as Snake
from pacman import PacmanJeu as SpaceInvader
from pacman import PacmanJeu as Puissance4
from pacman import PacmanJeu as Morpion

class Menu:
    
    def __init__(self):
        pygame.display.set_caption("Multigame")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((900,600))
        self.font = pygame.font.SysFont(None, int(self.screen.get_height()/5))
        self.events = []
        self.running = 1
        self.jeux = pygame.sprite.Group()
        self.init_jeux()
        
    def init_jeux(self):
        self.jeux.add(Jeu(Pacman,3*int(self.screen.get_width()*0.09),2*int(self.screen.get_width()*0.09),pygame.transform.scale(pygame.image.load("images/icon_pacman.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09)))))
        self.jeux.add(Jeu(Pacman,5*int(self.screen.get_width()*0.09),2*int(self.screen.get_width()*0.09),pygame.transform.scale(pygame.image.load("images/icon_space_invader.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09)))))
        self.jeux.add(Jeu(Pacman,7*int(self.screen.get_width()*0.09),2*int(self.screen.get_width()*0.09),pygame.transform.scale(pygame.image.load("images/icon_snake.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09)))))
        self.jeux.add(Jeu(Pacman,3*int(self.screen.get_width()*0.09),4*int(self.screen.get_width()*0.09),pygame.transform.scale(pygame.image.load("images/icon_puissance4.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09)))))
        self.jeux.add(Jeu(Pacman,5*int(self.screen.get_width()*0.09),4*int(self.screen.get_width()*0.09),pygame.transform.scale(pygame.image.load("images/icon_morpion.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09)))))
    
    def resolution_events(self):
        self.events += pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                self.running = 0
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.running = 0
        self.event = []
    
    def affiche(self):
        self.screen.fill(pygame.Color(50,150,200))
        titre = self.font.render('Multigames', True, pygame.Color('white'))
        self.screen.blit(titre, (2*int(self.screen.get_width()*0.09),0.5*int(self.screen.get_width()*0.09)))
        self.jeux.draw(self.screen)
        self.screen.blit(pygame.transform.scale(pygame.image.load("images/icon_coming_soon.png"), (int(self.screen.get_width()*0.09),int(self.screen.get_width()*0.09))), (7*int(self.screen.get_width()*0.09),4*int(self.screen.get_width()*0.09)))
    
    def choix_jeu(self):
        for jeu in self.jeux.sprites():
            if (jeu.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
                return jeu.jeu()
        return None
    
    def main_menu(self):
        jeu = None
        while(self.running):
            
            self.resolution_events()
            
            self.affiche()
            
            jeu = self.choix_jeu()
            if(jeu!=None):
                jeu.main()
                jeu = None
            
            clock.tick(60)
            pygame.display.flip()
        
class Jeu(pygame.sprite.Sprite):
    
    def __init__(self, jeu, x, y, image):
        super().__init__()
        self.jeu = jeu
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        