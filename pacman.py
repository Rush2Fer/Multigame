import pygame, sys
pygame.init()
clock = pygame.time.Clock()
from math import dist

SPAWN_FANTOME_ROSE = pygame.event.custom_type()
SPAWN_FANTOME_BLEU = pygame.event.custom_type()
SPAWN_FANTOME_ORANGE = pygame.event.custom_type()
RESPAWN_FANTOME_ROUGE = pygame.event.custom_type()
RESPAWN_FANTOME_ROSE = pygame.event.custom_type()
RESPAWN_FANTOME_BLEU = pygame.event.custom_type()
RESPAWN_FANTOME_ORANGE = pygame.event.custom_type()
FIN_BONUS = pygame.event.custom_type()
BLINK_FANTOME = pygame.event.custom_type()

NB_COLONNES = 21
NB_LIGNES = 23
MURS = [[1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
       ]
PASTILLES = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
             [0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
             [0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
             [0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
             [0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0],
             [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
             [0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             ]
DROITE = [1,0]
BAS = [0,1]
GAUCHE = [-1,0]
HAUT = [0,-1]
DIRECTIONS2INDEX = [[None,1,3],
              [0,None,None],
              [2,None,None]
              ]
#IMAGES_PACMAN[direction][animation]
IMAGES_PACMAN = [[pygame.image.load("images/Pacman/pacman_00.png"),pygame.image.load("images/Pacman/pacman_10.png")],
                 [pygame.image.load("images/Pacman/pacman_01.png"),pygame.image.load("images/Pacman/pacman_11.png")],
                 [pygame.image.load("images/Pacman/pacman_02.png"),pygame.image.load("images/Pacman/pacman_12.png")],
                 [pygame.image.load("images/Pacman/pacman_03.png"),pygame.image.load("images/Pacman/pacman_13.png")]
                 ]
DICT_COULEUR2INDEX = dict(Rouge = 0, Bleu = 1, Rose = 2, Orange = 3)
#IMAGES_FANTOMES[DICT_COULEUR2INDEX[couleur]][direction][animation]
IMAGES_FANTOMES = [[[pygame.image.load("images/Pacman/rouge_00.png"),pygame.image.load("images/Pacman/rouge_10.png")],
                  [pygame.image.load("images/Pacman/rouge_01.png"),pygame.image.load("images/Pacman/rouge_11.png")],
                  [pygame.image.load("images/Pacman/rouge_02.png"),pygame.image.load("images/Pacman/rouge_12.png")],
                  [pygame.image.load("images/Pacman/rouge_03.png"),pygame.image.load("images/Pacman/rouge_13.png")]],
                 [[pygame.image.load("images/Pacman/bleu_00.png"),pygame.image.load("images/Pacman/bleu_10.png")],
                  [pygame.image.load("images/Pacman/bleu_01.png"),pygame.image.load("images/Pacman/bleu_11.png")],
                  [pygame.image.load("images/Pacman/bleu_02.png"),pygame.image.load("images/Pacman/bleu_12.png")],
                  [pygame.image.load("images/Pacman/bleu_03.png"),pygame.image.load("images/Pacman/bleu_13.png")]],
                 [[pygame.image.load("images/Pacman/rose_00.png"),pygame.image.load("images/Pacman/rose_10.png")],
                  [pygame.image.load("images/Pacman/rose_01.png"),pygame.image.load("images/Pacman/rose_11.png")],
                  [pygame.image.load("images/Pacman/rose_02.png"),pygame.image.load("images/Pacman/rose_12.png")],
                  [pygame.image.load("images/Pacman/rose_03.png"),pygame.image.load("images/Pacman/rose_13.png")]],
                 [[pygame.image.load("images/Pacman/orange_00.png"),pygame.image.load("images/Pacman/orange_10.png")],
                  [pygame.image.load("images/Pacman/orange_01.png"),pygame.image.load("images/Pacman/orange_11.png")],
                  [pygame.image.load("images/Pacman/orange_02.png"),pygame.image.load("images/Pacman/orange_12.png")],
                  [pygame.image.load("images/Pacman/orange_03.png"),pygame.image.load("images/Pacman/orange_13.png")]],
                 ]
IMAGES_FANTOMES_APPEURE = [[pygame.image.load("images/Pacman/fantome_00.png"),pygame.image.load("images/Pacman/fantome_01.png")],
                           [pygame.image.load("images/Pacman/fantome_10.png"),pygame.image.load("images/Pacman/fantome_11.png")]
                           ]

class PacmanJeu:
    
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Multigame")
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0]-100,pygame.display.get_desktop_sizes()[0][1]-100),pygame.RESIZABLE)
        self.running = 1
        self.events = []
        self.taille_case = int(self.screen.get_height()/(NB_LIGNES+2))
        self.decalage_x_map = int(self.screen.get_width()/2 - self.taille_case*9.5)
        self.decalage_y_map = self.taille_case
        self.time_last_animation = 0
        self.score = 0
        self.murs = pygame.sprite.Group()
        self.init_murs()
        self.pastilles = pygame.sprite.Group()
        self.pac = Pacman(self)
        self.fantomes = pygame.sprite.Group()
        self.font = pygame.font.SysFont(None, int(self.taille_case*1.5))
        self.nouveau_niveau()
    
    def main(self):
        while(self.pac.vies!=0):
            while(self.running):
                
                self.resolution_events()
                
                self.affiche()
                
                self.update_animations()
                
                self.avance()
                
                self.check_win()
                
                clock.tick(60)
                pygame.display.flip()
            if(len(self.pastilles.sprites())==0):
                self.animation_win()
                self.nouveau_niveau()
            elif(self.pac.vies!=0):
                self.suite_manche()
                
        self.game_over()
        pygame.time.delay(3000)
            
    
    def nouveau_niveau(self):
        self.init_pastilles()
        self.suite_manche()
    
    def suite_manche(self):
        self.running = 1
        self.fantomes.empty()
        self.init_fantomes()
        self.pac.reset()
        self.affiche()
        img = self.font.render('Ready !', True, pygame.Color('yellow'))
        self.screen.blit(img, (self.decalage_x_map+int(8.7*self.taille_case), 14*self.taille_case))
        pygame.display.flip()
        pygame.time.delay(1000)
    
    def init_murs(self):
        for x in range(NB_COLONNES):
            for y in range(NB_LIGNES):
                if(MURS[x][y]):
                    self.murs.add(Mur(x, y, self))
    
    def init_pastilles(self):
        for x in range(1,round(NB_COLONNES*3/2-2)):
            for y in range(1,round(NB_LIGNES*3/2-2)):
                if(PASTILLES[round((x+0.5)*2/3)][round((y+0.5)*2/3)]):
                    self.pastilles.add(Pastille((x+0.5)*2/3, (y+0.5)*2/3, self))
        self.pastilles.add(Bonus(1, 3, self))
        self.pastilles.add(Bonus(19, 3, self))
        self.pastilles.add(Bonus(1, 17, self))
        self.pastilles.add(Bonus(19, 17, self))
    
    def init_fantomes(self):
        self.rouge = Fantome(self, "Rouge")
        self.fantomes.add(self.rouge)
        self.rose = Fantome(self, "Rose")
        self.fantomes.add(self.rose)
        self.bleu = Fantome(self, "Bleu")
        self.fantomes.add(self.bleu)
        self.orange = Fantome(self, "Orange")
        self.fantomes.add(self.orange)
        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ROSE), 0)
        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ROSE), 5000,1)
        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_BLEU), 0)
        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ORANGE), 0)
    
    def affiche(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.screen.blit(self.pac.image,self.pac.rect)
        self.murs.draw(self.screen)
        self.pastilles.draw(self.screen)
        self.fantomes.draw(self.screen)
        self.affiche_score()
        self.affiche_vies()
        
    def affiche_score(self):
        img = self.font.render('score : {}'.format(self.score), True, pygame.Color('white'))
        self.screen.blit(img, (self.decalage_x_map, 1))
        
    def affiche_vies(self):
        for vie in range(self.pac.vies):
            self.screen.blit(pygame.transform.scale(IMAGES_PACMAN[2][1],(self.taille_case,self.taille_case)),(self.decalage_x_map+vie*self.taille_case,self.decalage_y_map+NB_LIGNES*self.taille_case+1))
        
            
    def resolution_events(self):
        self.events += pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if (event.key == pygame.K_DOWN):
                    self.pac.direction_voulue = BAS
                if (event.key == pygame.K_UP):
                    self.pac.direction_voulue = HAUT
                if (event.key == pygame.K_RIGHT):
                    self.pac.direction_voulue = DROITE
                if (event.key == pygame.K_LEFT):
                    self.pac.direction_voulue = GAUCHE
            if (event.type == SPAWN_FANTOME_ROSE):
                if(self.rose.y == 9):
                    self.rose.actif = 1
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_BLEU), 5000,1)
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ROSE), 0)
                elif(self.rose.y == 11):
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ROSE), 40)
                    self.rose.y = round(self.rose.y - 0.1,1)
                    self.rose.update_rect()
                else:
                    self.rose.y = round(self.rose.y - 0.1,1)
                    self.rose.update_rect()
            if (event.type == SPAWN_FANTOME_BLEU):
                if(self.bleu.y == 9):
                    self.bleu.actif = 1
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ORANGE), 5000,1)
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_BLEU), 0)
                elif(self.bleu.y == 11):
                    if(self.bleu.x == 10):
                        self.bleu.y = round(self.bleu.y - 0.1,1)
                    else:
                        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_BLEU), 40)
                        self.bleu.x = round(self.bleu.x + 0.1,1)
                        self.bleu.update_rect()
                else:
                    self.bleu.y = round(self.bleu.y - 0.1,1)
                    self.bleu.update_rect()
            if (event.type == SPAWN_FANTOME_ORANGE):
                if(self.orange.y == 9):
                    self.orange.actif = 1
                    pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ORANGE), 0)
                elif(self.orange.y == 11):
                    if(self.orange.x == 10):
                        self.orange.y = round(self.orange.y - 0.1,1)
                    else:
                        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ORANGE), 40)
                        self.orange.x = round(self.orange.x - 0.1,1)
                        self.orange.update_rect()
                else:
                    self.orange.y = round(self.orange.y - 0.1,1)
                    self.orange.update_rect()
            if (event.type == RESPAWN_FANTOME_ROUGE):
                if(self.rouge.y == 9):
                    self.rouge.actif = 1
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ROUGE), 0)
                elif(self.rouge.y == 11):
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ROUGE), 40)
                    self.fantomes.add(self.rouge)
                    self.rouge.y = round(self.rouge.y - 0.1,1)
                    self.rouge.update_rect()
                else:
                    self.rouge.y = round(self.rouge.y - 0.1,1)
                    self.rouge.update_rect()
                    self.rouge.update_image()
            if (event.type == RESPAWN_FANTOME_ROSE):
                if(self.rose.y == 9):
                    self.rose.actif = 1
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ROSE), 0)
                elif(self.rose.y == 11):
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ROSE), 40)
                    self.fantomes.add(self.rose)
                    self.rose.y = round(self.rose.y - 0.1,1)
                    self.rose.update_rect()
                else:
                    self.rose.y = round(self.rose.y - 0.1,1)
                    self.rose.update_rect()
                    self.rose.update_image()
            if (event.type == RESPAWN_FANTOME_BLEU):
                if(self.bleu.y == 9):
                    self.bleu.actif = 1
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_BLEU), 0)
                elif(self.bleu.y == 11):
                    if(self.bleu.x == 10):
                        self.bleu.y = round(self.bleu.y - 0.1,1)
                    else:
                        pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_BLEU), 40)
                        self.fantomes.add(self.bleu)
                        self.bleu.x = round(self.bleu.x + 0.1,1)
                        self.bleu.update_rect()
                else:
                    self.bleu.y = round(self.bleu.y - 0.1,1)
                    self.bleu.update_rect()
                    self.bleu.update_image()
            if (event.type == RESPAWN_FANTOME_ORANGE):
                if(self.orange.y == 9):
                    self.orange.actif = 1
                    pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ORANGE), 0)
                elif(self.orange.y == 11):
                    if(self.orange.x == 10):
                        self.orange.y = round(self.orange.y - 0.1,1)
                    else:
                        pygame.time.set_timer(pygame.event.Event(RESPAWN_FANTOME_ORANGE), 40)
                        self.fantomes.add(self.orange)
                        self.orange.x = round(self.orange.x - 0.1,1)
                        self.orange.update_rect()
                        self.orange.update_image()
                else:
                    self.orange.y = round(self.orange.y - 0.1,1)
                    self.orange.update_rect()
            if(event.type == FIN_BONUS):
                for fantome in self.fantomes.sprites():
                    fantome.appeure = 0
                    fantome.animation_appeure = 0
                pygame.time.set_timer(BLINK_FANTOME, 0)
                pygame.time.set_timer(FIN_BONUS, 0)
            if(event.type == BLINK_FANTOME):
                pygame.time.set_timer(BLINK_FANTOME, 500)
                for fantome in self.fantomes.sprites():
                    fantome.animation_appeure = 1 - fantome.animation_appeure
        self.events = []
    
    def avance(self):
        time = pygame.time.get_ticks()
        self.pac.avance()
        if(time%4!=0):
            for fantome in self.fantomes:
                fantome.avance()
            
    def update_animations(self):
        time = pygame.time.get_ticks()
        if (time-self.time_last_animation>250):
            self.time_last_animation=time
            self.pac.animation = 1 - self.pac.animation
            for fantome in self.fantomes.sprites():
                fantome.animation = 1 - fantome.animation
                
    def update_score(self,collisions):
        self.score += 10*len(collisions)
        
    def check_win(self):
        if(len(self.pastilles.sprites())==0):
            self.running = 0
    
    def animation_win(self):
        for i in range(3):
            self.screen.fill(pygame.Color(0,0,0))
            self.pastilles.draw(self.screen)
            self.affiche_score()
            self.affiche_vies()
            self.murs.draw(self.screen)
            pygame.display.flip()
            pygame.time.delay(500)
            self.screen.fill(pygame.Color(0,0,0))
            self.pastilles.draw(self.screen)
            self.affiche_score()
            self.affiche_vies()
            for mur in self.murs.sprites():
                self.screen.blit(mur.get_image(True), mur.rect)
            pygame.display.flip()
            pygame.time.delay(500)
            
    
    def game_over(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.murs.draw(self.screen)
        self.pastilles.draw(self.screen)
        self.affiche_score()
        img = self.font.render('game over', True, pygame.Color('red'))
        self.screen.blit(img, (self.decalage_x_map+8*self.taille_case, 14*self.taille_case))
        pygame.display.flip()

class Mur(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.update_rect()
        
    def get_image(self, image_blanche = False):
        x=self.x
        y=self.y
        base_nom_image = "images/Pacman/mur_"
        if(image_blanche):
            base_nom_image += "blanc_"
        if(x==10 and y==10):
            return pygame.transform.scale(pygame.image.load("images/Pacman/porte0.png"),(self.jeu.taille_case,self.jeu.taille_case))
        elif(x!=0 and x!=NB_COLONNES-1 and y!=0 and y!=NB_LIGNES-1):
            return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+str(MURS[x][y+1])+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
        else:
            if(x==0):
                if(y==0):
                    return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+str(MURS[x][y+1])+"00.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+"00"+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+str(MURS[x][y+1])+"0"+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(x==NB_COLONNES-1):
                if(y==0):
                    return pygame.transform.scale(pygame.image.load(base_nom_image+"0"+str(MURS[x][y+1])+str(MURS[x-1][y])+"0.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    return pygame.transform.scale(pygame.image.load(base_nom_image+"00"+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    return pygame.transform.scale(pygame.image.load(base_nom_image+"0"+str(MURS[x][y+1])+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==0):
                return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+str(MURS[x][y+1])+str(MURS[x-1][y])+str(0)+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==NB_LIGNES-1):
                return pygame.transform.scale(pygame.image.load(base_nom_image+str(MURS[x+1][y])+str(0)+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.decalage_y_map + self.jeu.taille_case*self.y
    
class Pacman(pygame.sprite.Sprite):
    
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.vies = 3
        self.reset()
    
    def reset(self):
        self.x = 10
        self.y = 17
        self.direction = BAS
        self.direction_voulue = BAS
        self.animation = 1
        self.image = pygame.transform.scale(pygame.image.load("images/Pacman/pacman_00.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.decalage_y_map + self.jeu.taille_case*self.y
    
    def avance(self):
        if(self.direction==DROITE and self.x==20):
            self.x=0
        elif(self.direction==GAUCHE and self.x==0):
            self.x=20
        elif (self.direction != self.direction_voulue and not self.colision_prochain(self.direction_voulue)):
            self.direction = self.direction_voulue
        elif (self.colision_prochain(self.direction)):
            return
        self.x = round(self.x + self.direction[0]*0.1,1)
        self.y = round(self.y + self.direction[1]*0.1,1)
        self.update_rect()
        self.update_image()
        collisions = pygame.sprite.spritecollide(self, self.jeu.pastilles,True,pygame.sprite.collide_mask)
        self.check_bonus(collisions)
        self.jeu.update_score(collisions)
    
    def colision_prochain(self,direction):
        test = pygame.sprite.Sprite()
        test.rect = self.image.get_rect()
        test.rect.x, test.rect.y = self.rect.x, self.rect.y
        test.rect.x += direction[0]
        test.rect.y += direction[1]
        return pygame.sprite.spritecollideany(test, self.jeu.murs)
    
    def check_bonus(self,collisions):
        for i in range(len(collisions)):
            if(type(collisions[i])==Bonus):
                self.jeu.score += 50
                for fantome in self.jeu.fantomes.sprites():
                    fantome.appeure = 1
                    fantome.animation_appeure = 0
                pygame.time.set_timer(FIN_BONUS, 7000)
                pygame.time.set_timer(BLINK_FANTOME, 5000)
                
    def update_image(self):
        self.image = pygame.transform.scale(IMAGES_PACMAN[DIRECTIONS2INDEX[self.direction[0]][self.direction[1]]][self.animation],(self.jeu.taille_case,self.jeu.taille_case))

    def animation_mort(self):
        self.jeu.screen.fill(pygame.Color(0,0,0))
        self.jeu.murs.draw(self.jeu.screen)
        self.jeu.pastilles.draw(self.jeu.screen)
        self.jeu.affiche_score()
        self.jeu.affiche_vies()
        for i in range(19):
            pygame.draw.rect(self.jeu.screen, pygame.Color('black'), self.rect)
            self.jeu.screen.blit(pygame.transform.scale(pygame.image.load("images/Pacman/pacman_mort_"+str(i)+".png"),(self.jeu.taille_case,self.jeu.taille_case)), self.rect)
            pygame.display.flip()
            pygame.time.delay(100)

class Fantome(pygame.sprite.Sprite):
    
    def __init__(self,jeu,nom):
        super().__init__()
        self.jeu = jeu
        self.nom = nom
        if(nom=="Rouge"):
            self.x = 10
            self.y = 9
            self.actif = 1
        if(nom=="Bleu"):
            self.x = 9
            self.y = 11
            self.actif = 0
        if(nom=="Rose"):
            self.x = 10
            self.y = 11
            self.actif = 0
        if(nom=="Orange"):
            self.x = 11
            self.y = 11
            self.actif = 0
        self.direction = BAS
        self.but = (9,8)
        self.animation = 1
        self.animation_appeure = 0
        self.appeure = 0
        self.image = pygame.transform.scale(pygame.image.load("images/Pacman/"+self.nom+"_00.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.decalage_y_map + self.jeu.taille_case*self.y
        
    def avance(self):
        if(self.actif):
            if(self.direction==DROITE and self.x==20):
                self.x=0
            elif(self.direction==GAUCHE and self.x==0):
                self.x=20
            elif(self.colision_prochain(self.direction) or self.on_intersection()):
                self.direction = self.update_direction()
            self.x = round(self.x + self.direction[0]*0.1,1)
            self.y = round(self.y + self.direction[1]*0.1,1)
            self.update_rect()
            self.update_image()
            self.check_collision()
        
        
    def colision_prochain(self,direction):
        test = pygame.sprite.Sprite()
        test.rect = self.image.get_rect()
        test.rect.x, test.rect.y = self.rect.x, self.rect.y
        test.rect.x += direction[0]
        test.rect.y += direction[1]
        return pygame.sprite.spritecollideany(test, self.jeu.murs)
    
    def on_intersection(self):
        if((10*self.x)%10==0 and (10*self.y)%10==0):
            x=int(self.x)
            y=int(self.y)
            chemins = 4-(MURS[x+1][y]+MURS[x][y+1]+MURS[x-1][y]+MURS[x][y-1])
            if(chemins>2):
                return True
        return False
    
    def update_direction(self):
        directions=self.directions_possibles()
        if(len(directions)==1):
            return directions[0]
        vect_objectif = self.objectif()
        for direc in self.ordre_pref_dir(vect_objectif):
            if (direc in directions):
                return direc
    
    def directions_possibles(self):
        directions = list()
        for direc in [DROITE,BAS,GAUCHE,HAUT]:
            if(not MURS[round(self.x) + direc[0]][round(self.y) + direc[1]]):
                oppose = self.direction[0]*(-1), self.direction[1]*(-1)
                if(not(direc[0]==oppose[0] and direc[1]==oppose[1])):
                    directions.append(direc)
        return directions
    
    def objectif(self):
        if(not self.appeure):
            if(self.nom=="Rouge"):
                return self.jeu.pac.x - self.x, self.jeu.pac.y - self.y
            if(self.nom=="Bleu"):
                return (self.jeu.pac.x - self.jeu.rouge.x)*2, (self.jeu.pac.y - self.jeu.rouge.y)*2
            if(self.nom=="Rose"):
                return self.jeu.pac.x + self.jeu.pac.direction[0]*2 - self.x, self.jeu.pac.y + self.jeu.pac.direction[1]*2 - self.y
            if(self.nom=="Orange"):
                if(dist((self.x,self.y),(self.jeu.pac.x,self.jeu.pac.y))<=6):
                    if(self.x<=9 and self.y<=10):
                        return NB_COLONNES-1,NB_LIGNES-1
                    elif(self.x>9 and self.y<=10):
                        return 1,NB_LIGNES-1
                    elif(self.x<=9 and self.y>10):
                        return NB_COLONNES-1,1
                    elif(self.x>9 and self.y>10):
                        return 1,1
                else:
                    return self.jeu.pac.x + self.jeu.pac.direction[0]*2 - self.x, self.jeu.pac.y + self.jeu.pac.direction[1]*2 - self.y
        else:
            if(self.x<=9 and self.y<=10):
                return self.x - self.jeu.pac.x + 1,self.y - self.jeu.pac.y + 1
            elif(self.x>9 and self.y<=10):
                return self.x - self.jeu.pac.x - 1,self.y - self.jeu.pac.y + 1
            elif(self.x<=9 and self.y>10):
                return self.x - self.jeu.pac.x + 1,self.y - self.jeu.pac.y - 1
            elif(self.x>9 and self.y>10):
                return self.x - self.jeu.pac.x - 1,self.y - self.jeu.pac.y - 1
    
    def ordre_pref_dir(self,vect_objectif):
        if(abs(vect_objectif[0])>abs(vect_objectif[1])):
            if(vect_objectif[0]>0):
                if(vect_objectif[1]>0):
                    return (DROITE,HAUT,BAS,GAUCHE)
                else:
                    return (DROITE,BAS,HAUT,GAUCHE)
            else:
                if(vect_objectif[1]<0):
                    return (GAUCHE,HAUT,BAS,DROITE)
                else:
                    return (GAUCHE,BAS,HAUT,DROITE)
        else:
            if(vect_objectif[0]>0):
                if(vect_objectif[1]<0):
                    return (HAUT,DROITE,GAUCHE,BAS)
                else:
                    return (BAS,DROITE,GAUCHE,HAUT)
            else:
                if(vect_objectif[1]<0):
                    return (HAUT,GAUCHE,DROITE,BAS)
                else:
                    return (BAS,GAUCHE,DROITE,HAUT)
                
    def update_image(self):
        if(not self.appeure):
            self.image = pygame.transform.scale(IMAGES_FANTOMES[DICT_COULEUR2INDEX[self.nom]][DIRECTIONS2INDEX[self.direction[0]][self.direction[1]]][self.animation],(self.jeu.taille_case,self.jeu.taille_case))
        else:
            self.image = pygame.transform.scale(IMAGES_FANTOMES_APPEURE[self.animation_appeure][self.animation],(self.jeu.taille_case,self.jeu.taille_case))
    
    def check_collision(self):
        if(not self.appeure):
            if(pygame.sprite.collide_mask(self, self.jeu.pac)!=None):
                self.jeu.running = 0
                self.jeu.pac.vies -= 1
                self.jeu.pac.animation_mort()
        else:
            if(pygame.sprite.collide_mask(self, self.jeu.pac)!=None):
                self.kill()
                self.actif = 0
                self.appeure = 0
                self.animation_appeure = 0
                score = 200
                for fantome in self.jeu.fantomes.sprites():
                    if(fantome.appeure==0):
                        score *= 2
                self.jeu.score += score
                if(self == self.jeu.rouge):
                    self.x = 10
                    self.y = 11
                    pygame.time.set_timer(RESPAWN_FANTOME_ROUGE, 1000)
                if(self == self.jeu.rose):
                    self.x = 10
                    self.y = 11
                    pygame.time.set_timer(RESPAWN_FANTOME_ROSE, 1000)
                if(self == self.jeu.bleu):
                    self.x = 9
                    self.y = 11
                    pygame.time.set_timer(RESPAWN_FANTOME_BLEU, 1000)
                if(self == self.jeu.orange):
                    self.x = 11
                    self.y = 11
                    pygame.time.set_timer(RESPAWN_FANTOME_ORANGE, 1000)
    
class Pastille(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/Pacman/pastille.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.decalage_y_map + self.jeu.taille_case*self.y
    
class Bonus(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/Pacman/bonus.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.decalage_y_map + self.jeu.taille_case*self.y
    