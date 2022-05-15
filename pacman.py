import pygame
from jeu import Jeu

clock = pygame.time.Clock()

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
        self.doors_state = 0
        self.pastilles = pygame.sprite.Group()
        self.murs = pygame.sprite.Group()
        self.init_map()
        self.portes = self.portes()
        self.pac = Pacman(self)
        
        
    def init_map(self):
        for i in range(31):
            for j in range(28):
                if(contenu_map[i][j]!=0):
                    case = Case(j,i,self)
                    if(not (contenu_map[i][j]==1 or contenu_map[i][j]==2)):
                        self.murs.add(case)
                    else:
                        self.pastilles.add(case)

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
            # if event.type == pygame.VIDEORESIZE:
            #     scale_w = event.w/self.screen_size[0]
            #     scale_h = event.h/self.screen_size[1]        
            #     for e in self.map.sprites():
            #         size = e.image.get_size()
            #         size = (size[0] * scale_w, size[1] * scale_h)
            #         e.image = pygame.transform.scale(e.image, size)
            #         e.rect.x *= scale_w
            #         e.rect.y *= scale_h
            #         e.rect.size = e.image.get_size()
            #     self.screen_size=self.screen.get_size()
        self.events = []
    
    def affiche_jeu(self):
        self.screen.fill(pygame.Color(0,0,0))
        for sprite in self.murs:
            if(sprite.visible==1):
                self.screen.blit(sprite.image,sprite.rect)
        for sprite in self.pastilles:
            if(sprite.visible==1):
                self.screen.blit(sprite.image,sprite.rect)
        self.screen.blit(images_pacman[self.pac.animation][self.pac.direction],self.pac.rect)
    
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

    def __repr__(self):
        return "Objet PamanJeu"


class Pacman(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.direction = bas
        self.direction_voulue = bas
        self.animation = 0
        self.image = images_pacman[self.animation][self.direction]
        self.mask = pygame.mask.from_threshold(self.image,(255,201,14,255),(246,192,5,255))
        self.rect = self.image.get_rect()
        self.rect.x = int(self.jeu.screen.get_width()/2) - int(self.rect.w/2)
        self.rect.y = int(3*self.jeu.screen.get_height()/4) - 13
        self.time_last_animation = 0
        
    def avance(self):
        if (self.direction != self.direction_voulue and not self.collide_tourne(self.direction_voulue)):
            self.direction = self.direction_voulue
            if (self.direction == bas):
                self.rect.y -= 1
            elif (self.direction == droite):
                self.rect.x += 1
            elif (self.direction == haut):
                self.rect.y += 1
            elif (self.direction == gauche):
                self.rect.x -= 1
        else:
            if (not self.collide_droit()):
                if (self.direction == bas):
                    self.rect.y -= 1
                elif (self.direction == droite):
                    self.rect.x += 1
                elif (self.direction == haut):
                    self.rect.y += 1
                elif (self.direction == gauche):
                    self.rect.x -= 1
        pygame.sprite.spritecollide(self, self.jeu.pastilles, True)
        
    def collide_droit(self):
        return self.collide_distance(self.direction,1)
    
    def collide_tourne(self,direction):
        return self.collide_distance(direction,3)
    
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
        testeur_sprite = pygame.sprite.Sprite()
        testeur_sprite.image = self.image
        testeur_sprite.mask = self.mask
        testeur_sprite.rect = pygame.Rect(rect_x, rect_y, self.rect.w, self.rect.h)
        return pygame.sprite.spritecollideany(testeur_sprite, self.jeu.murs,pygame.sprite.collide_mask)
            
    def update_animation(self):
        time = pygame.time.get_ticks()
        if (time-self.time_last_animation>500):
            self.time_last_animation=time
            self.animation = 1 - self.animation
        

class Fantome(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.jeu = jeu
        self.direction = bas
        self.image = images_fantome[self.direction]
        self.rect = self.pac.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1
        self.animation = 0
        
    def avance(self):#IA pour bouger fantomes vers pacman
        pass # TO DO

class Case(pygame.sprite.Sprite):
    
    def __init__(self,x,y,pac):
        super().__init__()
        self.pac = pac
        self.contenu = contenu_map[y][x]
        self.visible = 1
        self.image = images_map[self.contenu]
        self.mask = pygame.mask.from_threshold(self.image,(63,72,204,255),(62,71,203,255))
        w = pac.screen.get_width()
        h = pac.screen.get_height()
        taille = int((h)/31)
        offset_x = int(w/2)-int(h/2)+int(1.5*taille)
        self.rect = self.image.get_rect()
        self.rect.x = x*taille+offset_x+image_offset_x[self.contenu]
        self.rect.y = y*taille+image_offset_y[self.contenu]
    
    def __repr__(self):
        return "({},{}):{}".format(self.rect.x,self.rect.y,self.contenu)

    def update(self, value):
        self.visible = value
