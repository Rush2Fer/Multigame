import pygame


images_map=[pygame.image.load("images/vide.png"),pygame.image.load("images/bonus.png"),pygame.image.load("images/pastille.png"),pygame.image.load("images/mur_vertical.png"),pygame.image.load("images/mur_horizontal.png"),pygame.image.load("images/coin_haut_droit.png"),pygame.image.load("images/coin_haut_gauche.png"),pygame.image.load("images/coin_bas_gauche.png"),pygame.image.load("images/coin_bas_droit.png"),pygame.image.load("images/porte.png")]
vide = 0
bonus = 1
pastille = 2
mur_vert = 3
mur_horiz = 4
coin_haut_droit = 5
coin_haut_gauche = 6
coin_bas_gauche = 7
coin_bas_droit = 8
porte = 9
contenu_map = [[6,4,4,4,4,4,4,4,4,4,4,4,4,5,6,4,4,4,4,4,4,4,4,4,4,4,4,5],
               [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
               [3,2,6,4,4,5,2,6,4,4,4,5,2,3,3,2,6,4,4,4,5,2,6,4,4,5,2,3],
               [3,1,3,0,0,3,2,3,0,0,0,3,2,3,3,2,3,0,0,0,3,2,3,0,0,3,1,3],
               [3,2,7,4,4,8,2,7,4,4,4,8,2,7,8,2,7,4,4,4,8,2,7,4,4,8,2,3],
               [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
               [3,2,6,4,4,5,2,6,5,2,6,4,4,4,4,4,4,5,2,6,5,2,6,4,4,5,2,3],
               [3,2,7,4,4,8,2,3,3,2,7,4,4,5,6,4,4,8,2,3,3,2,7,4,4,8,2,3],
               [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
               [7,4,4,4,4,5,2,3,7,4,4,5,0,3,3,0,6,4,4,8,3,2,6,4,4,4,4,8],
               [0,0,0,0,0,3,2,3,6,4,4,8,0,7,8,0,7,4,4,5,3,2,3,0,0,0,0,0],
               [0,0,0,0,0,3,2,3,3,0,0,0,0,0,0,0,0,0,0,3,3,2,3,0,0,0,0,0],
               [0,0,0,0,0,3,2,3,3,0,6,4,4,9,9,4,4,5,0,3,3,2,3,0,0,0,0,0],
               [4,4,4,4,4,8,2,7,8,0,3,0,0,0,0,0,0,3,0,7,8,2,7,4,4,4,4,4],
               [0,0,0,0,0,0,2,0,0,0,3,0,0,0,0,0,0,3,0,0,0,2,0,0,0,0,0,0],
               [4,4,4,4,4,5,2,6,5,0,3,0,0,0,0,0,0,3,0,6,5,2,6,4,4,4,4,4],
               [0,0,0,0,0,3,2,3,3,0,7,4,4,4,4,4,4,8,0,3,3,2,3,0,0,0,0,0],
               [0,0,0,0,0,3,2,3,3,0,0,0,0,0,0,0,0,0,0,3,3,2,3,0,0,0,0,0],
               [0,0,0,0,0,3,2,3,3,0,6,4,4,4,4,4,4,5,0,3,3,2,3,0,0,0,0,0],
               [6,4,4,4,4,8,2,7,8,0,7,4,4,5,6,4,4,8,0,7,8,2,7,4,4,4,4,5],
               [3,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,3],
               [3,2,6,4,4,5,2,6,4,4,4,5,2,3,3,2,6,4,4,4,5,2,6,4,4,5,2,3],
               [3,2,7,4,5,3,2,7,4,4,4,8,2,7,8,2,7,4,4,4,8,2,3,6,4,8,2,3],
               [3,1,2,2,3,3,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,3,3,2,2,1,3],
               [7,4,5,2,3,3,2,6,5,2,6,4,4,4,4,4,4,5,2,6,5,2,3,3,2,6,4,8],
               [6,4,8,2,7,8,2,3,3,2,7,4,4,5,6,4,4,8,2,3,3,2,7,8,2,7,4,5],
               [3,2,2,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,3,3,2,2,2,2,2,2,3],
               [3,2,6,4,4,4,4,8,7,4,4,5,2,3,3,2,6,4,4,8,7,4,4,4,4,5,2,3],
               [3,2,7,4,4,4,4,4,4,4,4,8,2,7,8,2,7,4,4,4,4,4,4,4,4,8,2,3],
               [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
               [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8]
               ]

class Pacman:
    def __init__(self,screen):
        self.map = pygame.sprite.Group()
        self.init_map(screen)
        
    def init_map(self,screen):
        taille = int((screen.get_height())/31)
        for i in range(31):
            for j in range(28):
                self.map.add(Case(j,i,))

    def portes(self):
        doors = list()
        for e in self.map.sprites():
            if (e.rect.x, e.rect.y) == (13, 12) or (e.rect.x, e.rect.y) == (14, 12):
                doors.append(e)
        return doors
        
    def affiche_pacman(self,screen):
        w = screen.get_width()
        h = screen.get_height()
        taille = int((h)/31)
        offset_x = int(w/2)-int(h/2)+int(1.5*taille)
        for sprite in self.map:
            screen.blit(sprite.image,(offset_x+sprite.rect.x*taille,sprite.rect.y*taille))

    def __repr__(self):
        res = ""
        i=0
        for sprite in self.map:
            res += str(sprite) + ";"
            i+=1
        return res+str(i)
    

class Case(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.contenu = contenu_map[y][x]
        self.image = images_map[self.contenu]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def __repr__(self):
        return "({},{}):{}".format(self.rect.x,self.rect.y,self.contenu)

    def update(self, value):
        self.contenu = value
        self.image = images_map[self.contenu]
