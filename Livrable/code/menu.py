import pygame, webbrowser
pygame.init()
clock = pygame.time.Clock()
from pacman import PacmanJeu as Pacman
from snake import SnakeJeu as Snake
from space_invader import Game as SpaceInvader
from P4 import P4Jeu as Puissance4
from Morpion import MorpionJeu as Morpion

class Menu:
    
    def __init__(self):
        pygame.display.set_caption("Multigame")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((900,600))
        self.font_titre = pygame.font.Font("fonts/SparTakus.ttf", 75)
        self.font = pygame.font.Font("fonts/SparTakus.ttf", 20)
        self.events = []
        self.running = 1
        self.jeux = pygame.sprite.Group()
        self.jeu = None
        self.init_jeux()
        
    def init_jeux(self):
        self.jeux.add(Jeu(Pacman,"Pacman",int(self.screen.get_width()*0.143),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_pacman.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(SpaceInvader,"Space Invader",int(self.screen.get_width()*0.428),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_space_invader.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Snake,"Snake",int(self.screen.get_width()*0.714),int(self.screen.get_height()*0.28),pygame.transform.scale(pygame.image.load("images/icon_snake.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Puissance4,"Puissance 4",int(self.screen.get_width()*0.143),int(self.screen.get_height()*0.65),pygame.transform.scale(pygame.image.load("images/icon_puissance4.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(Morpion,"Morpion",int(self.screen.get_width()*0.428),int(self.screen.get_height()*0.65),pygame.transform.scale(pygame.image.load("images/icon_morpion.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
        self.jeux.add(Jeu(GTA,"GTA V",int(self.screen.get_width()*0.714),int(self.screen.get_height()*0.65),pygame.transform.scale(pygame.image.load("images/icon_gtav.png"), (int(self.screen.get_width()*0.15),int(self.screen.get_width()*0.15)))))
    
    def resolution_events(self):
        self.events += pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                self.running = 0
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.running = 0
            if (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                for jeu in self.jeux.sprites():
                    if (jeu.rect.collidepoint(pygame.mouse.get_pos())):
                        self.jeu = jeu.jeu()
        self.events = []
    
    def affiche(self):
        self.screen.fill(pygame.Color(50,150,200))
        titre = self.font_titre.render('Multigames', True, pygame.Color('white'))
        self.screen.blit(titre, (int(self.screen.get_width()/2 - titre.get_width()/2),int(self.screen.get_width()*0.05)))
        self.jeux.draw(self.screen)
        for jeu in self.jeux.sprites():
            img_txt = self.font.render(jeu.titre, True, pygame.Color('white'))
            self.screen.blit(img_txt,(jeu.rect.bottomleft[0]+jeu.rect.w/2-img_txt.get_width()/2,jeu.rect.bottomleft[1]+int(self.screen.get_width()*0.02)))
    
    def main_menu(self):
        while(self.running):
            
            self.resolution_events()
            
            self.affiche()
            
            if(self.jeu!=None):
                self.jeu.main()
                self.jeu = None
                self.screen = pygame.display.set_mode((900,600))
            
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
        
class GTA:
    
    def main(self):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=DLzxrzFCyOs")
        pygame.time.delay(1000)
        
if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
    pygame.quit()
    