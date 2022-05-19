import pygame
from jeu import Jeu

clock = pygame.time.Clock()

images_map_base=[None,pygame.image.load("images/bonus.png"),pygame.image.load("images/pastille.png"),pygame.image.load("images/mur_vertical.png"),pygame.image.load("images/mur_horizontal.png"),pygame.image.load("images/coin_haut_droit.png"),pygame.image.load("images/coin_haut_gauche.png"),pygame.image.load("images/coin_bas_gauche.png"),pygame.image.load("images/coin_bas_droit.png"),pygame.image.load("images/porte.png")]
images_pacman_base=[[pygame.image.load("images/pacman_0.png"),pygame.image.load("images/pacman_1.png"),pygame.image.load("images/pacman_2.png"),pygame.image.load("images/pacman_3.png")],
               [pygame.image.load("images/pacman_4.png"),pygame.image.load("images/pacman_5.png"),pygame.image.load("images/pacman_6.png"),pygame.image.load("images/pacman_7.png")]
               ]
images_fantome_base=[[pygame.image.load("images/fantome_0.png"),pygame.image.load("images/fantome_1.png"),pygame.image.load("images/fantome_2.png"),pygame.image.load("images/fantome_3.png")],
               [pygame.image.load("images/fantome_4.png"),pygame.image.load("images/fantome_5.png"),pygame.image.load("images/fantome_6.png"),pygame.image.load("images/fantome_7.png")]
               ]
images_map=[None,pygame.image.load("images/bonus.png"),pygame.image.load("images/pastille.png"),pygame.image.load("images/mur_vertical.png"),pygame.image.load("images/mur_horizontal.png"),pygame.image.load("images/coin_haut_droit.png"),pygame.image.load("images/coin_haut_gauche.png"),pygame.image.load("images/coin_bas_gauche.png"),pygame.image.load("images/coin_bas_droit.png"),pygame.image.load("images/porte.png")]
images_pacman=[[pygame.image.load("images/pacman_0.png"),pygame.image.load("images/pacman_1.png"),pygame.image.load("images/pacman_2.png"),pygame.image.load("images/pacman_3.png")],
               [pygame.image.load("images/pacman_4.png"),pygame.image.load("images/pacman_5.png"),pygame.image.load("images/pacman_6.png"),pygame.image.load("images/pacman_7.png")]
               ]
images_fantome=[[pygame.image.load("images/fantome_0.png"),pygame.image.load("images/fantome_1.png"),pygame.image.load("images/fantome_2.png"),pygame.image.load("images/fantome_3.png")],
               [pygame.image.load("images/fantome_4.png"),pygame.image.load("images/fantome_5.png"),pygame.image.load("images/fantome_6.png"),pygame.image.load("images/fantome_7.png")]
               ]
vide = bas = 0
bonus = droite = 1
pastille = haut = 2
mur_vert = gauche = 3
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
image_offset_x = [0,4,8,8,0,0,8,8,0,0]
image_offset_y = [0,4,8,0,8,8,8,0,0,8]

class PacmanJeu(Jeu):
    def __init__(self):
        super().__init__()
        self.screeen_size = (self.screen.get_width(), self.screen.get_height())
        self.scale_images()
        self.doors_state = 0
        self.pastilles = pygame.sprite.Group()
        self.murs = pygame.sprite.Group()
        self.init_map()
        self.portes = self.portes()
        self.pac = Pacman(self)
        self.fantomes = pygame.sprite.Group()
        self.init_fantomes()
        self.time_last_animation = 0
        self.score = 0
        
        
    def init_map(self):
        for i in range(31):
            for j in range(28):
                if(contenu_map[i][j]!=0):
                    case = Case(j,i,self)
                    if(not (contenu_map[i][j]==1 or contenu_map[i][j]==2)):
                        self.murs.add(case)
                    else:
                        self.pastilles.add(case)
    
    def init_fantomes(self):
        for i in range(1):
            self.fantomes.add(Fantome(self,i))
    
    def scale_images(self):
        h = self.screen.get_height()
        taille_case = int(h/31)
        taille_pac = int(1.8*h/31)
        for i in range(1,len(images_map)):
            images_map[i] = pygame.transform.scale(images_map_base[i], (taille_case,taille_case))
        for i in range(len(images_pacman)):
            for j in range(len(images_pacman[i])):
                images_pacman[i][j] = pygame.transform.scale(images_pacman_base[i][j], (taille_pac,taille_pac))
        for i in range(len(images_fantome)):
            for j in range(len(images_fantome[i])):
                images_fantome[i][j] = pygame.transform.scale(images_fantome_base[i][j], (taille_pac,taille_pac))

    def portes(self):
        doors = list()
        for e in self.murs.sprites():
            if (e.contenu==9):
                doors.append(e)
        return doors
    
    def resolution_events(self):
        self.events += pygame.event.get()
        for event in self.events:
            if (event.type == pygame.QUIT):
                self.running = False
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    self.running = False
                if (event.key == pygame.K_DOWN):
                    self.pac.direction_voulue = haut
                if (event.key == pygame.K_UP):
                    self.pac.direction_voulue = bas
                if (event.key == pygame.K_RIGHT):
                    self.pac.direction_voulue = droite
                if (event.key == pygame.K_LEFT):
                    self.pac.direction_voulue = gauche
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                continue
            if event.type == pygame.VIDEORESIZE:
                previous_size = self.screen_size
                self.screen_size = event.size
                self.scale_images()
                self.update_affichage(previous_size)
        self.events = []
    
    def affiche_jeu(self):
        self.screen.fill(pygame.Color(0,0,0))
        for sprite in self.murs:
            if(sprite.visible==1):
                self.screen.blit(sprite.image,sprite.rect)
        for sprite in self.pastilles:
            if(sprite.visible==1):
                self.screen.blit(sprite.image,sprite.rect)
        self.screen.blit(self.pac.image,self.pac.rect)
        for sprite in self.fantomes.sprites():
            self.screen.blit(sprite.image,sprite.rect)
    
    def animation_ouverture_porte(self):
        time = pygame.time.get_ticks()
        if (self.doors_state == 0) and time >=4000:
            for e in self.portes:
                e.update(0)
            self.doors_state = 1

        elif (self.doors_state == 1) and time >= 4500:
            self.doors_state = 2
            for e in self.portes:
                e.update(1)
        elif (self.doors_state==2) and time >= 5000:
            self.doors_state = 3
            for e in self.portes:
                e.update(0)
    
    def update_affichage(self,previous_size):
        #met les bonnes images
        self.pac.image = images_pacman[self.pac.animation][self.pac.direction]
        for sprite in self.murs.sprites():
            sprite.image = images_map[sprite.contenu]
        for sprite in self.pastilles.sprites():
            sprite.image = images_map[sprite.contenu]
        
        #au bon endroit
        w ,h = self.screen_size
        taille_case = int(h/31)
        taille_pac = int(1.8*h/31)
        offset_x = int(w/2)-int(12.5*taille_case)
        ancienne_taille_case = int(previous_size[1]/31)
        ancienne_taille_pac = int(1.8*previous_size[1]/31)
        ancien_offset_x = int(previous_size[0]/2)-int(12.5*ancienne_taille_case)
        
        #pacman
        x, y = (self.pac.rect.x-ancien_offset_x+ancienne_taille_pac/2)/ancienne_taille_case, ((self.pac.rect.y/ancienne_taille_case)*3+1)/3
        self.pac.rect = self.pac.image.get_rect()
        self.pac.rect.x = offset_x+taille_case*x-taille_pac/2
        self.pac.rect.y = taille_case*((y*3-1)/3)
        
        #map
        for sprite in self.murs.sprites():
            x, y = (sprite.rect.x-ancien_offset_x)/ancienne_taille_case, sprite.rect.y/ancienne_taille_case
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = x*taille_case+offset_x
            sprite.rect.y = y*taille_case
        for sprite in self.pastilles.sprites():
            x, y = (sprite.rect.x-ancien_offset_x)/ancienne_taille_case, sprite.rect.y/ancienne_taille_case
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = x*taille_case+offset_x
            sprite.rect.y = y*taille_case
            
    def update_animations(self):
        time = pygame.time.get_ticks()
        if (time-self.time_last_animation>500):
            self.time_last_animation=time
            self.pac.animation = 1 - self.pac.animation
            for sprite in self.fantomes.sprites():
                sprite.animation = 1 - sprite.animation
            
    def avance(self):
        self.pac.avance()
        for sprite in self.fantomes.sprites():
            sprite.deplace()

    def __repr__(self):
        return "Objet PacmanJeu"


class Pacman(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.direction = bas
        self.direction_voulue = bas
        self.animation = 1
        w ,h = self.jeu.screen_size
        taille_case = int(h/31)
        taille_pac = int(1.8*h/31)
        self.image = images_pacman[self.animation][self.direction]
        self.image = pygame.transform.scale(self.image, (taille_pac,taille_pac))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        offset_x = int(w/2)-int(h/2)+int(1.5*taille_case)
        self.rect.x = offset_x+taille_case*14-taille_pac/2
        self.rect.y = taille_case*((23*3-1)/3)
        
    def avance(self):
        if (self.direction != self.direction_voulue and not self.collide_tourne(self.direction_voulue)):
            self.direction = self.direction_voulue
            if (self.direction == bas):
                self.rect.y -= 2
            elif (self.direction == droite):
                self.rect.x += 2
            elif (self.direction == haut):
                self.rect.y += 2
            elif (self.direction == gauche):
                self.rect.x -= 2
        else:
            if (not self.collide_droit()):
                if (self.direction == bas):
                    self.rect.y -= 2
                elif (self.direction == droite):
                    self.rect.x += 2
                elif (self.direction == haut):
                    self.rect.y += 2
                elif (self.direction == gauche):
                    self.rect.x -= 2
        self.image = images_pacman[self.animation][self.direction]
        pygame.sprite.spritecollide(self, self.jeu.pastilles,True,pygame.sprite.collide_mask)
        
    def collide_droit(self):
        return self.collide_distance(self.direction,self.epaisseur_bord_mask()+2)
    
    def collide_tourne(self,direction):
        return self.collide_distance(direction,self.rect.w/2)
    
    def collide_distance(self,direction,distance):
        rect_x = self.rect.x
        rect_y = self.rect.y
        if (direction == bas):
            rect_y -= distance
        elif (direction == droite):
            rect_x += distance
        elif (direction == haut):
            rect_y += distance
        elif (direction == gauche):
            rect_x -= distance
        bord = self.epaisseur_bord_mask()
        if (self.direction == bas):
            rect_y += bord
        elif (self.direction == droite):
            rect_x -= bord
        elif (self.direction == haut):
            rect_y -= bord
        elif (self.direction == gauche):
            rect_x += bord
        testeur_sprite = pygame.sprite.Sprite()
        testeur_sprite.image = self.image
        testeur_sprite.mask = self.mask
        testeur_sprite.rect = pygame.Rect(rect_x, rect_y, self.rect.w, self.rect.h)
        return pygame.sprite.spritecollideany(testeur_sprite, self.jeu.murs,pygame.sprite.collide_mask)
    
    def epaisseur_bord_mask(self):
        i = 0
        while not self.mask.get_at((i,self.mask.get_size()[1]/2)):
            i += 1
        return i
        

class Fantome(pygame.sprite.Sprite):
    def __init__(self,jeu,num):
        super().__init__()
        self.jeu = jeu
        self.numero = num
        self.but = (11,13)
        
        self.direction = bas
        self.animation = 0
        w ,h = self.jeu.screen_size
        taille_case = int(h/31)
        taille_fant = int(1.8*h/31)
        self.image = images_fantome[self.animation][self.direction]
        self.image = pygame.transform.scale(self.image, (taille_fant,taille_fant))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        offset_x = int(w/2)-int(h/2)+int(1.5*taille_case)
        self.rect.x = offset_x+taille_case*14-taille_fant/2
        self.rect.y = taille_case*((11*3-1)/3)
        self.appeure = 0
        
    def deplace(self):
        """Si le fantom est à une intersection,
        recalcule la case but et détermine la direction du chemin le plus court.
        Modifie le rect du fantome pour qu'il se déplace"""
        if(self.in_intersection()):
            self.calcul_but()
            self.calcul_direction()
        if (self.direction == bas):
            self.rect.y -= 2
        elif (self.direction == droite):
            self.rect.x += 2
        elif (self.direction == haut):
            self.rect.y += 2
        elif (self.direction == gauche):
            self.rect.x -= 2
        
        self.image = images_fantome[self.animation][self.direction]
        
    def in_intersection(self):
        return False
    
    def collide_droit(self):
        return self.collide_distance(self.direction,self.epaisseur_bord_mask()+2)
    
    def collide_tourne(self,direction):
        return self.collide_distance(direction,self.rect.w/2)
    
    def collide_distance(self,direction,distance):
        rect_x = self.rect.x
        rect_y = self.rect.y
        if (direction == bas):
            rect_y -= distance
        elif (direction == droite):
            rect_x += distance
        elif (direction == haut):
            rect_y += distance
        elif (direction == gauche):
            rect_x -= distance
        bord = self.epaisseur_bord_mask()
        if (self.direction == bas):
            rect_y += bord
        elif (self.direction == droite):
            rect_x -= bord
        elif (self.direction == haut):
            rect_y -= bord
        elif (self.direction == gauche):
            rect_x += bord
        testeur_sprite = pygame.sprite.Sprite()
        testeur_sprite.image = self.image
        testeur_sprite.mask = self.mask
        testeur_sprite.rect = pygame.Rect(rect_x, rect_y, self.rect.w, self.rect.h)
        return pygame.sprite.spritecollideany(testeur_sprite, self.jeu.murs,pygame.sprite.collide_mask)
    
    def epaisseur_bord_mask(self):
        i = 0
        while not self.mask.get_at((i,self.mask.get_size()[1]/2)):
            i += 1
        return i

class Case(pygame.sprite.Sprite):
    
    def __init__(self,x,y,jeu):
        super().__init__()
        self.jeu = jeu
        self.contenu = contenu_map[y][x]
        self.visible = 1
        w ,h = self.jeu.screen_size
        taille = int((h)/31)
        self.image = images_map[self.contenu]
        self.image = pygame.transform.scale(self.image, (taille,taille))
        self.mask = pygame.mask.from_surface(self.image)
        offset_x = int(w/2)-int(h/2)+int(1.5*taille)
        self.rect = self.image.get_rect()
        self.rect.x = x*taille+offset_x
        self.rect.y = y*taille

    def __repr__(self):
        return "({},{}):{}".format(self.rect.x,self.rect.y,self.contenu)

    def update(self, value):
        self.visible = value


def affiche_mask(mask : pygame.mask.Mask):
    ligne=""
    for i in range(mask.get_size()[0]):
        for j in range(mask.get_size()[0]):
            ligne += "{} ".format(mask.get_at((j,i)))
        print(ligne)
        ligne = ""