import pygame, sys
from operator import attrgetter
from random import randint, random
import math

#contantes couleurs
BLANC = pygame.Color(255, 255, 255)
NOIR = pygame.Color(0, 0, 0)
ROUGE = pygame.Color(198, 44, 42)
CYAN = pygame.Color(90, 165, 158)
VERT = pygame.Color(94, 186, 87)
GRIS = pygame.Color(129, 129, 129)
VIOLET = pygame.Color(149, 64, 149)
MARRON = pygame.Color(161, 122, 81)
JAUNE = pygame.Color(230, 230, 0)

class Jeu:
    
    def __init__(self):
        pygame.display.set_caption("Achtung")
        self.screen = pygame.display.set_mode((1455, 780))
        self.bg_menu = pygame.image.load("images/bg_menu.jpg")
        self.joueurs = pygame.sprite.Group()
        self.charger_joueurs()
        self.joueurs_in_game = []
        self.joueurs_vivants = []
        self.classement = []
        self.events = []
        self.key_pressed = {}
        self.font = pygame.font.SysFont("freesansbold.ttf", 32)
        self.pret = False
        self.bonus = pygame.sprite.Group()
        self.boundless_actif = False
        self.compteur = 0
        self.proba_bonus = 0.00425
        
    def charger_joueurs(self):
        self.joueurs.add(Joueur(self, "Fred", pygame.image.load("images/Fred.jpg"), 388, 200, ROUGE))
        self.joueurs.add(Joueur(self, "Greenlee", pygame.image.load("images/Greenlee.jpg"), 385, 257, VERT))
        self.joueurs.add(Joueur(self, "Pinkney", pygame.image.load("images/Pinkney.jpg"), 389, 321, VIOLET))
        self.joueurs.add(Joueur(self, "Bluebell", pygame.image.load("images/Bluebell.jpg"), 389, 380, CYAN))
        self.joueurs.add(Joueur(self, "Willem", pygame.image.load("images/Willem.jpg"), 390, 439, MARRON))
        self.joueurs.add(Joueur(self, "Greydon", pygame.image.load("images/Greydon.jpg"), 390, 499, GRIS))
                
    def update_events(self):
        self.events += pygame.event.get()
        
    def resolution_events_menu(self):
        for event in self.events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                if len(self.joueurs_in_game) >= 2:
                    self.pret = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for joueur in self.joueurs:
                    if joueur.rect.collidepoint(pygame.mouse.get_pos()):
                        if joueur in self.joueurs_in_game:
                            self.joueurs_in_game.remove(joueur)
                        else:
                            self.joueurs_in_game += [joueur]
                        if joueur in self.joueurs_in_game:
                            self.get_touches(joueur)
                        break
        self.events = []
        
    def get_touches(self, joueur):
        self.screen.blit(pygame.image.load("images/touche_g.jpg"), (546, joueur.rect.y)) # affiche la demande de touche
        pygame.display.flip() # actualise le screen
        
        # bloque et attend la touche
        event = pygame.event.wait()
        while event.type != pygame.KEYDOWN:
            event = pygame.event.wait()
            
        joueur.touche_g = event.unicode # enregistre la touche
        joueur.touche_g_key_code = event.key# enregistre la touche
        pygame.draw.rect(self.screen, (0, 0, 0), (546, joueur.rect.y, 146, 32)) # efface la demande de touche
        self.affiche_commandes()
        
        self.screen.blit(pygame.image.load("images/touche_d.jpg"), (685, joueur.rect.y)) # affiche la demande de touche
        pygame.display.flip() # actualise le screen
        
        # bloque et attend la touche
        event = pygame.event.wait()
        while event.type != pygame.KEYDOWN:
            event = pygame.event.wait()
            
        joueur.touche_d = event.unicode# enregistre la touche
        joueur.touche_d_key_code = event.key# enregistre la touche
        pygame.draw.rect(self.screen, (0, 0, 0), (685, joueur.rect.y, 139, 32)) # efface la demande de touche
        self.affiche_commandes()
        pygame.display.flip()
        pygame.event.clear(pump = False)
        
    def affichage_menu(self):
        self.screen.blit(self.bg_menu, (0,0)) #affiche le background du menu
        self.affiche_commandes()
        self.surbrille_joueur_in_game()
        self.passage_sur_nom()
                
    def affiche_commandes(self):
        for joueur in self.joueurs_in_game:
            touche_droite = self.font.render(joueur.touche_g.upper(), True, BLANC, NOIR)
            self.screen.blit(touche_droite, (610, joueur.rect.y))
            touche_gauche = self.font.render(joueur.touche_d.upper(), True, BLANC, NOIR)
            self.screen.blit(touche_gauche, (755, joueur.rect.y))
                
    def surbrille_joueur_in_game(self):
        for joueur in self.joueurs_in_game:
            joueur.surbriller()
            
    def passage_sur_nom(self):
        for joueur in self.joueurs:
            if joueur.rect.collidepoint(pygame.mouse.get_pos()):
                joueur.surbriller()
                
    def fin_partie(self):
        max_points = 0
        second_points = 0
        for joueur in self.joueurs_in_game:
            if joueur.points > max_points:
                second_points = max_points
                max_points = joueur.points
        if max_points >= 10 * len(self.joueurs_in_game) - 10 and max_points - second_points >= 2:
            return True
        else:
            return False
                
    def prepare_manche(self):
        for bonus in self.bonus:
            if bonus.actif:
                bonus.arret_effet()
            del bonus
        self.bonus.empty()
        self.key_pressed = {}
        self.joueurs_vivants = []
        for joueur in self.joueurs_in_game:
            self.joueurs_vivants += [joueur]
            joueur.angle_direction = randint(1, 360)
            joueur.corps = [[randint(160, 830), randint(51, 728)]]
        for i in range(10):
            self.avancer_joueurs()
            
    def affiche_jeu(self):
        self.affiche_cadre()
        self.affiche_score_goal()
        self.affiche_score()
        self.affiche_bonus()
        self.affiche_joueurs()
                
    def affiche_cadre(self):
        if not self.boundless_actif:
            pygame.draw.rect(self.screen, JAUNE, (100, 1, 780, 778), 3)
        else:
            pygame.draw.rect(self.screen, pygame.Color(round(230*abs((math.cos(5*self.compteur*math.pi/180)+1)/2)),round(230*abs((math.cos(5*self.compteur*math.pi/180)+1)/2)),0), (100, 1, 780, 778), 3)
    
    def affiche_score_goal(self):
        text_goal = self.font.render("goal", True, BLANC, NOIR)
        self.screen.blit(text_goal, (980, 50))
        special_font = pygame.font.SysFont("freesansbold.ttf", 100)
        text_points = special_font.render("{}".format(len(self.joueurs_in_game) * 10 - 10), True, BLANC, NOIR)
        self.screen.blit(text_points, (965, 85))
        text_diff = self.font.render("2 points d'écart", True, BLANC, NOIR)
        self.screen.blit(text_diff, (925, 160))
        
    def affiche_score(self):
        pygame.draw.rect(self.screen, NOIR, (899, 249, 140, 200))
        self.update_classement_joueurs()
        for i, joueur in enumerate(self.classement):
            text_joueur = self.font.render("{}".format(joueur.nom), True, joueur.couleur, NOIR)
            self.screen.blit(text_joueur, (900, 250 + 35*i))
            score = self.font.render("{}".format(joueur.points), True, joueur.couleur, NOIR)
            self.screen.blit(score, (1000, 250 + 35*i))
            
    def update_classement_joueurs(self):
        self.classement = sorted(self.joueurs_in_game, key=attrgetter("points"), reverse = True)

    def affiche_bonus(self):
        for bonus in self.bonus:
            if not bonus.actif:
                self.screen.blit(bonus.image,(bonus.rect.x,bonus.rect.y))
        
    def affiche_joueurs(self):
        for joueur in self.joueurs_in_game:
            for section in joueur.corps[:-1]:
                point = [int(section[0]), int(section[1])]
                pygame.draw.circle(self.screen, joueur.couleur, point, 2)
            pygame.draw.circle(self.screen, JAUNE, (int(joueur.corps[-1][0]), int(joueur.corps[-1][1])), 2)
                
    def attendre_espace(self):
        wait = True
        while wait:
            event = pygame.event.wait()
            try:
                if event.type != pygame.KEYUP and event.key == pygame.K_SPACE:
                    wait = False
            except:
                pass
            self.events += [event]
            
    def fin_manche(self):
        return (len(self.joueurs_vivants) <= 1)
    
    def resolution_events_jeu(self):
        for event in self.events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                self.key_pressed[event.key] = True
            if event.type == pygame.KEYUP:
                self.key_pressed[event.key] = False
                
    def update_direction_joueurs(self):
        for joueur in self.joueurs_in_game:
            if self.key_pressed.get(joueur.touche_g_key_code, False):
                joueur.angle_direction += 2
            elif self.key_pressed.get(joueur.touche_d_key_code, False):
                joueur.angle_direction -= 2
                
    def avancer_joueurs(self):
        for joueur in self.joueurs_vivants:
            joueur.corps += [[joueur.corps[-1][0] + (joueur.vitesse * math.sin(math.radians(joueur.angle_direction))), joueur.corps[-1][1] + (joueur.vitesse * math.cos(math.radians(joueur.angle_direction)))]]
            if joueur.hors_cadre():
                if self.boundless_actif:
                    joueur.recadrer()
                else:
                    joueur.mort()
            if joueur.trou():
                del joueur.corps[-2]
                
    def check_collisions_j2j(self):
        for joueur in self.joueurs_vivants:
            tete = joueur.corps[-1]
            for joueur_autre in self.joueurs_in_game:
                if joueur is joueur_autre:
                    for point_joueur in joueur.corps[:-10]:
                        if math.sqrt((tete[0] - point_joueur[0])**2 + (tete[1] - point_joueur[1])**2) <= 3:
                            joueur.mort()
                            break
                else:
                    for point_autre in joueur_autre.corps:
                        if math.sqrt((tete[0] - point_autre[0])**2 + (tete[1] - point_autre[1])**2) <= 3:
                            joueur.mort()
                            break
                        
    def check_collisions_j2b(self):
        for joueur in self.joueurs_vivants:
            tete = joueur.corps[-1]
            for bonus in self.bonus:
                if not bonus.actif:
                    if bonus.rect.collidepoint(tete):
                        bonus.actif = True
                        bonus.effet(joueur)
                        
    def update_bonus(self):
        if random() <= self.proba_bonus:
            num_bonus = randint(0,10)
            if num_bonus in [0,1]:
                bonus_cree = Boundless(self, pygame.image.load("images/bonus_boundless.jpg"))
            if num_bonus in [2]:
                bonus_cree = Wipe(self, pygame.image.load("images/bonus_wipe.jpg"))
            if num_bonus in [3,4,5]:
                bonus_cree = SpeedMe(self, pygame.image.load("images/bonus_speed.jpg"))
            if num_bonus in [6,7]:
                bonus_cree = SlowMe(self, pygame.image.load("images/bonus_slow.jpg"))
            if num_bonus in [8,9]:
                bonus_cree = SpeedThem(self, pygame.image.load("images/malus_speed.jpg"))
            if num_bonus in [9,10]:
                bonus_cree = SlowThem(self, pygame.image.load("images/malus_slow.jpg"))
            self.bonus.add(bonus_cree)
        for bonus in self.bonus:
            if bonus.actif:
                bonus.actif_depuis += 1
            if bonus.actif_depuis >= bonus.duree:
                bonus.arret_effet()
                self.bonus.remove(bonus)
                del bonus
                

    def affiche_gagnant(self):
        max_points = 0
        joueur_gagnant = ""
        for joueur in self.joueurs_in_game:
            if joueur.points > max_points:
                max_points = joueur.points
                joueur_gagnant = joueur
        couleur_attenuee = joueur_gagnant.couleur//pygame.Color(3, 3, 3)
        pygame.draw.rect(self.screen, couleur_attenuee, (170, 215, 640, 300))
        pygame.draw.rect(self.screen, joueur_gagnant.couleur, (170, 215, 640, 300), 3)
        special_font = pygame.font.Font("freesansbold.ttf", 60)
        gagnant = special_font.render("WINNER {}".format(joueur_gagnant.nom.upper()), True, joueur_gagnant.couleur, None)
        self.screen.blit(gagnant, (490 - (pygame.font.Font.size(special_font, "WINNER {}".format(joueur_gagnant.nom.upper()))[0] / 2), 390 - 2*(pygame.font.Font.size(special_font, "WINNER {}".format(joueur_gagnant.nom.upper()))[1] / 3)))        
        
class Joueur(pygame.sprite.Sprite):
    
    def __init__(self, jeu, nom, image, pos_x, pos_y, couleur):
        super().__init__()
        self.jeu = jeu
        self.nom = nom
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.couleur = couleur
        self.touche_g = ""
        self.touche_d = ""
        self.touche_g_key_code = 0
        self.touche_d_key_code = 0
        self.points = 0
        self.corps = []
        self.angle_direction = 0
        self.vitesse = 1.2
        self.proba_trou = 0
        self.est_trou = False
        self.est_trou_depuis = 0
        
    def surbriller(self):
        self.jeu.screen.blit(self.image, self.rect)
        
    def mort(self):
        self.jeu.joueurs_vivants.remove(self)
        for joueur in self.jeu.joueurs_vivants:
            joueur.points += 1
            
    def trou(self):
        if self.est_trou:
            self.est_trou_depuis += 1
            if self.est_trou_depuis >= 10:
                self.est_trou = False
                self.est_trou_depuis = 0
                self.proba_trou = 0
        else:
            self.proba_trou += 0.0001
            proba = random()
            if proba < self.proba_trou:
                self.est_trou = True
        return self.est_trou
    
    def hors_cadre(self):
        return (self.corps[-1][0] < 100 or self.corps[-1][0] > 880 or self.corps[-1][1] < 1 or self.corps[-1][1] > 779)
        
    def recadrer(self):
        if self.corps[-1][0] < 100:
            self.corps[-1] = [878,self.corps[-1][1]]
        if self.corps[-1][0] > 880:
            self.corps[-1] = [102,self.corps[-1][1]]
        if self.corps[-1][1] < 1:
            self.corps[-1] = [self.corps[-1][0],777]
        if self.corps[-1][1] > 779:
            self.corps[-1] = [self.corps[-1][0],3]
        
        
    def __repr__(self):
        return "{}".format(self.nom)
    
class Bonus(pygame.sprite.Sprite):
    
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.duree = 300 # 5 secondes = 300 frames (60 frames par secondes)
        
class Boundless(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.actif = False
        self.actif_depuis = 0
        self.duree = 420 # 7 secondes
    
    def effet(self, joueur):
        self.jeu.boundless_actif = True
        
    def arret_effet(self):
        self.jeu.boundless_actif = False
        
class Wipe(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.actif = False
        self.actif_depuis = 0
        
    def effet(self, joueur):
        for joueur in self.jeu.joueurs_in_game:
            tete = joueur.corps[-1]
            joueur.corps = []
            joueur.corps = [[round(tete[0]),round(tete[1])]]
            
    def arret_effet(self):
        pass
        
class SpeedMe(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.actif = False
        self.actif_depuis = 0
        self.joueurs_affectes = []
        
    def effet(self, joueur):
        self.joueurs_affectes += [joueur]
        joueur.vitesse *= 1.5
        
    def arret_effet(self):
        for joueur in self.joueurs_affectes:
            joueur.vitesse /= 1.5
        
class SlowMe(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.actif = False
        self.actif_depuis = 0
        self.joueurs_affectes = []
        
    def effet(self, joueur):
        self.joueurs_affectes += [joueur]
        joueur.vitesse /= 1.5
        
    def arret_effet(self):
        for joueur in self.joueurs_affectes:
            joueur.vitesse *= 1.5
        
class SpeedThem(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.numeros = [5]
        self.actif = False
        self.actif_depuis = 0
        self.joueurs_affectes = []
    
    def effet(self, joueur):
        for autre_joueur in self.jeu.joueurs_in_game:
            if not joueur == autre_joueur:
                self.joueurs_affectes += [autre_joueur]
                autre_joueur.vitesse *= 1.5
                
    def arret_effet(self):
        for joueur in self.joueurs_affectes:
            joueur.vitesse /= 1.5
        
class SlowThem(Bonus):
    
    def __init__(self, jeu, image):
        Bonus.__init__(self, jeu)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(110,870)
        self.rect.y = randint(11,769)
        self.numeros = [6]
        self.actif = False
        self.actif_depuis = 0
        self.joueurs_affectes = []
        
    def effet(self, joueur):
        for autre_joueur in self.jeu.joueurs_in_game:
            if not joueur == autre_joueur:
                self.joueurs_affectes += [autre_joueur]
                autre_joueur.vitesse /= 1.5
                
    def arret_effet(self):
        for joueur in self.joueurs_affectes:
            joueur.vitesse *= 1.5
        

        
        
        
        
        