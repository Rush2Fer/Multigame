import pygame
pygame.init()
clock = pygame.time.Clock()
from jeu import Jeu
import math

SPAWN_FANTOME_ROSE = pygame.event.custom_type()
SPAWN_FANTOME_BLEU = pygame.event.custom_type()
SPAWN_FANTOME_ORANGE = pygame.event.custom_type()
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
IMAGES_PACMAN = [[pygame.image.load("images/pacman_00.png"),pygame.image.load("images/pacman_10.png")],
                 [pygame.image.load("images/pacman_01.png"),pygame.image.load("images/pacman_11.png")],
                 [pygame.image.load("images/pacman_02.png"),pygame.image.load("images/pacman_12.png")],
                 [pygame.image.load("images/pacman_03.png"),pygame.image.load("images/pacman_13.png")]
                 ]
DICT_COULEUR2INDEX = dict(Rouge = 0, Bleu = 1, Rose = 2, Orange = 3)
#IMAGES_FANTOMES[couleur][direction][animation]
IMAGES_FANTOMES = [[[pygame.image.load("images/rouge_00.png"),pygame.image.load("images/rouge_10.png")],
                  [pygame.image.load("images/rouge_01.png"),pygame.image.load("images/rouge_11.png")],
                  [pygame.image.load("images/rouge_02.png"),pygame.image.load("images/rouge_12.png")],
                  [pygame.image.load("images/rouge_03.png"),pygame.image.load("images/rouge_13.png")]],
                 [[pygame.image.load("images/bleu_00.png"),pygame.image.load("images/bleu_10.png")],
                  [pygame.image.load("images/bleu_01.png"),pygame.image.load("images/bleu_11.png")],
                  [pygame.image.load("images/bleu_02.png"),pygame.image.load("images/bleu_12.png")],
                  [pygame.image.load("images/bleu_03.png"),pygame.image.load("images/bleu_13.png")]],
                 [[pygame.image.load("images/rose_00.png"),pygame.image.load("images/rose_10.png")],
                  [pygame.image.load("images/rose_01.png"),pygame.image.load("images/rose_11.png")],
                  [pygame.image.load("images/rose_02.png"),pygame.image.load("images/rose_12.png")],
                  [pygame.image.load("images/rose_03.png"),pygame.image.load("images/rose_13.png")]],
                 [[pygame.image.load("images/orange_00.png"),pygame.image.load("images/orange_10.png")],
                  [pygame.image.load("images/orange_01.png"),pygame.image.load("images/orange_11.png")],
                  [pygame.image.load("images/orange_02.png"),pygame.image.load("images/orange_12.png")],
                  [pygame.image.load("images/orange_03.png"),pygame.image.load("images/orange_13.png")]],
                 ]
IMAGES_FANTOMES_APPEURE = [[pygame.image.load("images/fantome_00.png"),pygame.image.load("images/fantome_01.png")],
                           [pygame.image.load("images/fantome_10.png"),pygame.image.load("images/fantome_11.png")]
                           ]

class PacmanJeu(Jeu):
    
    def __init__(self):
        super().__init__()
        self.taille_case = int(self.screen.get_height()/NB_LIGNES)
        self.decalage_x_map = int(self.screen.get_width()/2 - self.taille_case*9.5)
        self.bonus = 0
        self.time_last_animation = 0
        self.score = 0
        self.murs = pygame.sprite.Group()
        self.init_murs()
        self.pastilles = pygame.sprite.Group()
        self.init_pastilles()
        self.pac = Pacman(self)
        self.fantomes = pygame.sprite.Group()
        self.init_fantomes()
    
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
        pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ROSE), 2000,1)
    
    def affiche(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.screen.blit(self.pac.image,self.pac.rect)
        self.murs.draw(self.screen)
        self.pastilles.draw(self.screen)
        self.fantomes.draw(self.screen)
            
            
    def resolution_events(self):
        self.events += pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                self.running = False
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.running = False
                if (event.key == pygame.K_DOWN):
                    self.pac.direction_voulue = BAS
                if (event.key == pygame.K_UP):
                    self.pac.direction_voulue = HAUT
                if (event.key == pygame.K_RIGHT):
                    self.pac.direction_voulue = DROITE
                if (event.key == pygame.K_LEFT):
                    self.pac.direction_voulue = GAUCHE
            if (event.type == SPAWN_FANTOME_ROSE):
                self.rose.actif = 1
                pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_BLEU), 2000,1)
            if (event.type == SPAWN_FANTOME_BLEU):
                self.bleu.actif = 1
                pygame.time.set_timer(pygame.event.Event(SPAWN_FANTOME_ORANGE), 2000,1)
            if (event.type == SPAWN_FANTOME_ORANGE):
                self.orange.actif = 1
            if(event.type == FIN_BONUS):
                self.bonus = 0
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

class Mur(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        if(x==10 and y==10):
            self.image = pygame.transform.scale(pygame.image.load("images/porte0.png"),(self.jeu.taille_case,self.jeu.taille_case))
        elif(x!=0 and x!=NB_COLONNES-1 and y!=0 and y!=NB_LIGNES-1):
            self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+str(MURS[x][y+1])+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
        else:
            if(x==0):
                if(y==0):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+str(MURS[x][y+1])+"00.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+"00"+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+str(MURS[x][y+1])+"0"+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(x==NB_COLONNES-1):
                if(y==0):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_0"+str(MURS[x][y+1])+str(MURS[x-1][y])+"0.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_00"+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_0"+str(MURS[x][y+1])+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==0):
                self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+str(MURS[x][y+1])+str(MURS[x-1][y])+str(0)+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==NB_LIGNES-1):
                self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MURS[x+1][y])+str(0)+str(MURS[x-1][y])+str(MURS[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
    
class Pacman(pygame.sprite.Sprite):
    
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = 10
        self.y = 17
        self.direction = BAS
        self.direction_voulue = BAS
        self.animation = 1
        self.image = pygame.transform.scale(pygame.image.load("images/pacman_00.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
    
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
                self.jeu.bonus = 1
                pygame.time.set_timer(FIN_BONUS, 7000)
                pygame.time.set_timer(BLINK_FANTOME, 5000)
                
    def update_image(self):
        self.image = pygame.transform.scale(IMAGES_PACMAN[DIRECTIONS2INDEX[self.direction[0]][self.direction[1]]][self.animation],(self.jeu.taille_case,self.jeu.taille_case))
    
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
            self.x = 10
            self.y = 9
            self.actif = 0
        if(nom=="Rose"):
            self.x = 10
            self.y = 9
            self.actif = 0
        if(nom=="Orange"):
            self.x = 10
            self.y = 9
            self.actif = 0
        self.direction = BAS
        self.but = (9,8)
        self.animation = 1
        self.animation_appeure = 0
        self.image = pygame.transform.scale(pygame.image.load("images/"+self.nom+"_00.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
        
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
        if(not self.jeu.bonus):
            if(self.nom=="Rouge"):
                return self.jeu.pac.x - self.x, self.jeu.pac.y - self.y
            if(self.nom=="Bleu"):
                return (self.jeu.pac.x - self.jeu.rouge.x)*2, (self.jeu.pac.y - self.jeu.rouge.y)*2
            if(self.nom=="Rose"):
                return self.jeu.pac.x + self.jeu.pac.direction[0]*2 - self.x, self.jeu.pac.y + self.jeu.pac.direction[1]*2 - self.y
            if(self.nom=="Orange"):
                if(math.dist((self.x,self.y),(self.jeu.pac.x,self.jeu.pac.y))<=6):
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
        if(not self.jeu.bonus):
            self.image = pygame.transform.scale(IMAGES_FANTOMES[DICT_COULEUR2INDEX[self.nom]][DIRECTIONS2INDEX[self.direction[0]][self.direction[1]]][self.animation],(self.jeu.taille_case,self.jeu.taille_case))
        else:
            self.image = pygame.transform.scale(IMAGES_FANTOMES_APPEURE[self.animation_appeure][self.animation],(self.jeu.taille_case,self.jeu.taille_case))
    
    def check_collision(self):
        if(not self.jeu.bonus):
            if(pygame.sprite.collide_mask(self, self.jeu.pac)!=None):
                self.jeu.running = 0
        else:
            if(pygame.sprite.collide_mask(self, self.jeu.pac)!=None):
                self.kill()
    
class Pastille(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/pastille.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
    
class Bonus(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/bonus.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
        
    
jeu = PacmanJeu()

while(jeu.running):
    
    jeu.resolution_events()
    
    jeu.affiche()
    
    jeu.update_animations()
    
    jeu.avance()
    
    jeu.check_win()
    
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
    