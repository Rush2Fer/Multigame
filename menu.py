import pygame, sys
pygame.init()
clock = pygame.time.Clock()
from pacman import PacmanJeu as Pacman
from pacman import PacmanJeu as Snake
from space_invader import Game as SpaceInvader
from p4 import P4Jeu as Puissance4
from morpion import MorpionJeu as Morpion

class Menu:
    
    def __init__(self):
        pygame.display.set_caption("Multigame")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((900,600))
        self.font_titre = pygame.font.Font("neo_latina.ttf", 100)
        self.font = pygame.font.Font("neo_latina.ttf", 30)
        self.events = []
        self.running = 1
        self.jeux = pygame.sprite.Group()
        self.init_jeux()
        
    def init_jeux(self):
        self.jeux.add(Jeu(Pacman,"Pacman",int(self.screen.get_width()*0.143),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_pacman.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(SpaceInvader,"Space Invader",int(self.screen.get_width()*0.428),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_space_invader.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Pacman,"Snake",int(self.screen.get_width()*0.714),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_snake.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Puissance4,"Puissance 4",int(self.screen.get_width()*0.143),int(self.screen.get_height()*0.65),pygame.transform.scale(pygame.image.load("images/icon_puissance4.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Morpion,"Morpion",int(self.screen.get_width()*0.428),int(self.screen.get_height()*0.65),pygame.transform.scale(pygame.image.load("images/icon_morpion.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
    
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
        titre = self.font_titre.render('Multigames', True, pygame.Color('white'))
        self.screen.blit(titre, (int(self.screen.get_width()/2 - titre.get_width()/2),int(self.screen.get_width()*0.01)))
        self.jeux.draw(self.screen)
        for jeu in self.jeux.sprites():
            img_txt = self.font.render(jeu.titre, True, pygame.Color('white'))
            self.screen.blit(img_txt,(jeu.rect.bottomleft[0]+jeu.rect.w/2-img_txt.get_width()/2,jeu.rect.bottomleft[1]))
        self.screen.blit(pygame.transform.scale(pygame.image.load("images/icon_coming_soon.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15))), (int(self.screen.get_width()*0.714),int(self.screen.get_height()*0.65)))
    
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
    
    def __init__(self, jeu, titre, x, y, image):
        super().__init__()
        self.jeu = jeu
        self.titre = titre
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        