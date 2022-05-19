import pygame
pygame.init()
clock = pygame.time.Clock()
from jeu import Jeu
import math

NB_COLONNES = 19
NB_LIGNES = 22
MAP = [[1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
       [1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1],
       [1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
       [1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
       [1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
       [1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
       [1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
       [1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
       [1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
       [1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
       [1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
       [1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
       [1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
       [1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1],
       [1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
       [1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1],
       ]
DROITE = [1,0]
BAS = [0,1]
GAUCHE = [-1,0]
HAUT = [0,-1]

class PacmanJeu(Jeu):
    
    def __init__(self):
        super().__init__()
        self.taille_case = int(self.screen.get_height()/NB_LIGNES)
        self.decalage_x_map = int(self.screen.get_width()/2 - self.taille_case*9.5)
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
                if(MAP[x][y]):
                    self.murs.add(Mur(x, y, self))
    
    def init_pastilles(self):
        for x in range(NB_COLONNES):
            for y in range(NB_LIGNES):
                if(not MAP[x][y]):
                    self.pastilles.add(Pastille(x, y, self))
    
    def init_fantomes(self):
        self.fantomes.add(Fantome(self, "Rouge"))
        self.fantomes.add(Fantome(self, "Bleu"))
        self.fantomes.add(Fantome(self, "Rose"))
        self.fantomes.add(Fantome(self, "Orange"))
    
    def affiche(self):
        self.screen.fill(pygame.Color(0,0,0))
        self.screen.blit(self.pac.image,self.pac.rect)
        for mur in self.murs:
            self.screen.blit(mur.image,mur.rect)
        for fantome in self.fantomes:
            self.screen.blit(fantome.image,fantome.rect)
            
            
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
        self.events = []
    
    def avance(self):
        self.pac.avance()
        for fantome in self.fantomes:
            fantome.avance()

class Mur(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
        if(x==9 and y==9):
            self.image = pygame.transform.scale(pygame.image.load("images/porte0.png"),(self.jeu.taille_case,self.jeu.taille_case))
        elif(x!=0 and x!=NB_COLONNES-1 and y!=0 and y!=NB_LIGNES-1):
            self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+str(MAP[x][y+1])+str(MAP[x-1][y])+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
        else:
            if(x==0):
                if(y==0):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+str(MAP[x][y+1])+"00.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+"00"+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+str(MAP[x][y+1])+"0"+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(x==NB_COLONNES-1):
                if(y==0):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_0"+str(MAP[x][y+1])+str(MAP[x-1][y])+"0.png"),(self.jeu.taille_case,self.jeu.taille_case))
                elif(y==NB_LIGNES-1):
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_00"+str(MAP[x-1][y])+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
                else:
                    self.image = pygame.transform.scale(pygame.image.load("images/mur_0"+str(MAP[x][y+1])+str(MAP[x-1][y])+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==0):
                self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+str(MAP[x][y+1])+str(MAP[x-1][y])+str(0)+".png"),(self.jeu.taille_case,self.jeu.taille_case))
            elif(y==NB_LIGNES-1):
                self.image = pygame.transform.scale(pygame.image.load("images/mur_"+str(MAP[x+1][y])+str(0)+str(MAP[x-1][y])+str(MAP[x][y-1])+".png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
    
class Pacman(pygame.sprite.Sprite):
    
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = 9
        self.y = 16
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
        if(self.direction==DROITE and self.x==18):
            self.x=0
        elif(self.direction==GAUCHE and self.x==0):
            self.x=18
        elif (self.direction != self.direction_voulue and not self.colision_prochain(self.direction_voulue)):
            self.direction = self.direction_voulue
        elif (self.colision_prochain(self.direction)):
            return
        self.x = round(self.x + self.direction[0]*0.1,1)
        self.y = round(self.y + self.direction[1]*0.1,1)
        self.update_rect()
    
    def colision_prochain(self,direction):
        test = pygame.sprite.Sprite()
        test.rect = self.image.get_rect()
        test.rect.x, test.rect.y = self.rect.x, self.rect.y
        test.rect.x += direction[0]
        test.rect.y += direction[1]
        return pygame.sprite.spritecollideany(test, self.jeu.murs)
    
class Fantome(pygame.sprite.Sprite):
    
    def __init__(self,jeu,nom):
        super().__init__()
        self.jeu = jeu
        self.nom = nom
        if(nom=="Rouge"):
            self.x = 9
            self.y = 8
        if(nom=="Bleu"):
            self.x = 1
            self.y = 1
        if(nom=="Rose"):
            self.x = 17
            self.y = 1
        if(nom=="Orange"):
            self.x = 9
            self.y = 4
        self.direction = BAS
        self.but = (9,8)
        self.animation = 1
        self.image = pygame.transform.scale(pygame.image.load("images/"+self.nom+"_00.png"),(self.jeu.taille_case,self.jeu.taille_case))
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.jeu.decalage_x_map + self.jeu.taille_case*self.x
        self.rect.y = self.jeu.taille_case*self.y
        
    def avance(self):
        if(self.direction==DROITE and self.x==18):
            self.x=0
        elif(self.direction==GAUCHE and self.x==0):
            self.x=18
        elif(self.colision_prochain(self.direction) or self.on_intersection()):
            self.direction = self.update_direction()
        self.x = round(self.x + self.direction[0]*0.1,1)
        self.y = round(self.y + self.direction[1]*0.1,1)
        self.update_rect()
        
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
            chemins = 4-(MAP[x+1][y]+MAP[x][y+1]+MAP[x-1][y]+MAP[x][y-1])
            if(chemins>2):
                return True
        return False
    
    def update_direction(self):
        directions=self.directions_possibles()
        if(len(directions)==1):
            return directions[0]
        case_objectif = self.objectif()
        vect_objectif_x = case_objectif[0] - self.x
        vect_objectif_y = case_objectif[1] - self.y
        vect_objectif = (vect_objectif_x, vect_objectif_y) 
        for direc in self.ordre_pref_dir(vect_objectif):
            if (direc in directions):
                return direc
    
    def directions_possibles(self):
        directions = list()
        for direc in [DROITE,BAS,GAUCHE,HAUT]:
            if(not MAP[round(self.x) + direc[0]][round(self.y) + direc[1]]):
                oppose = self.direction[0]*(-1), self.direction[1]*(-1)
                if(not(direc[0]==oppose[0] and direc[1]==oppose[1])):
                    directions.append(direc)
        return directions
    
    def objectif(self):
        if(self.nom=="Rouge"):
            return self.jeu.pac.x, self.jeu.pac.y
        if(self.nom=="Bleu"):
            for fantome in self.jeu.fantomes.sprites():
                if (fantome.nom == "Rose"):
                    rose = fantome
            return rose.x + (self.jeu.pac.x - rose.x)*2, rose.y + (self.jeu.pac.y - rose.y)*2
        if(self.nom=="Rose"):
            return self.jeu.pac.x + self.jeu.pac.direction[0]*2, self.jeu.pac.y + self.jeu.pac.direction[1]*2
        if(self.nom=="Orange"):
            if(math.dist((self.x,self.y),(self.jeu.pac.x,self.jeu.pac.y))<=4):
                if(self.x<=9 and self.y<=10):
                    return 17,20
                elif(self.x>9 and self.y<=10):
                    return 1,20
                elif(self.x<=9 and self.y>10):
                    return 17,1
                elif(self.x>9 and self.y>10):
                    return 1,1
            else:
                return self.jeu.pac.x + self.jeu.pac.direction[0]*2, self.jeu.pac.y + self.jeu.pac.direction[1]*2
    
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
    
class Pastille(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.x = x
        self.y = y
    
jeu = PacmanJeu()

while(jeu.running):
    
    jeu.resolution_events()
    
    jeu.affiche()
    
    jeu.avance()
    
    clock.tick(60)
    pygame.display.flip()
    
pygame.quit()
    