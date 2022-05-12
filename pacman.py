import pygame

clock = pygame.time.Clock()

images_map=[None,pygame.image.load("images/bonus.png"),pygame.image.load("images/pastille.png"),pygame.image.load("images/mur_vertical.png"),pygame.image.load("images/mur_horizontal.png"),pygame.image.load("images/coin_haut_droit.png"),pygame.image.load("images/coin_haut_gauche.png"),pygame.image.load("images/coin_bas_gauche.png"),pygame.image.load("images/coin_bas_droit.png"),pygame.image.load("images/porte.png")]
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

class Pacman:
    def __init__(self):
        pygame.display.set_caption("Multigame")
        self.screen = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0][0]-100,pygame.display.get_desktop_sizes()[0][1]-100),pygame.RESIZABLE)
        self.screen_size = self.screen.get_size()
        self.running = 1
        self.doors_state = 0
        self.map = pygame.sprite.Group()
        self.init_map()
        self.portes = self.portes()
        self.pac = pygame.sprite.Sprite()
        self.init_pac()
        self.events = []
        
        
    def init_map(self):
        for i in range(31):
            for j in range(28):
                if(contenu_map[i][j]!=0):
                    self.map.add(Case(j,i,self))

    def init_pac(self):
        self.pac.image = pygame.image.load("images/pacman.png")
        self.pac.rect = self.pac.image.get_rect()
        self.pac.rect.x = int(self.screen.get_width()/2) - int(self.pac.rect.w/2)
        self.pac.rect.y = int(3*self.screen.get_height()/4) - 12
        self.pac.direction = bas

    def portes(self):
        doors = list()
        for e in self.map.sprites():
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
                    self.pac.direction = haut
                if (event.key == pygame.K_UP):
                    self.pac.direction = bas
                if (event.key == pygame.K_RIGHT):
                    self.pac.direction = droite
                if (event.key == pygame.K_LEFT):
                    self.pac.direction = gauche
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
    
    def affiche_pacman(self):
        self.screen.fill(pygame.Color(0,0,0))
        for sprite in self.map:
            if(sprite.visible==1):
                self.screen.blit(sprite.image,sprite.rect)
        self.screen.blit(self.pac.image,self.pac.rect)
        
    def avance_pacman(self):
        previous_rect_x = self.pac.rect.x
        previous_rect_y = self.pac.rect.y
        if (self.pac.direction == bas):
            self.pac.rect.y -= 1
        elif (self.pac.direction == droite):
            self.pac.rect.x += 1
        elif (self.pac.direction == haut):
            self.pac.rect.y += 1
        elif (self.pac.direction == gauche):
            self.pac.rect.x -= 1
        if (pygame.sprite.spritecollideany(self.pac,self.map)!=None):
            self.pac.rect.x = previous_rect_x
            self.pac.rect.y = previous_rect_y
    
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
        res = ""
        i=0
        for sprite in self.map:
            res += str(sprite) + ";"
            i+=1
        return res+str(i)
    

class Case(pygame.sprite.Sprite):
    
    def __init__(self,x,y,pac):
        super().__init__()
        self.pac = pac
        self.contenu = contenu_map[y][x]
        self.visible = 1
        self.image = images_map[self.contenu]
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
