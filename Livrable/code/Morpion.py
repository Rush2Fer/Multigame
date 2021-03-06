import pygame

pygame.init()

screen_size_x = 600
screen_size_y = screen_size_x
score_size = 100


colonne_size = screen_size_x / 3
line_size = screen_size_x / 3

text_size = 40
text_menu = 70
text_gagnant = 90
Nom_J1 = 'Joueur 1'
Nom_J2 = 'Joueur 2'
font = pygame.font.SysFont(None, text_size)

jeton_j1 = pygame.image.load('images/Morpion/croix.png')
jeton_j1 = pygame.transform.scale(jeton_j1, ((screen_size_x / 2), (screen_size_x / 2.5)))
jeton_j2 = pygame.image.load('images/Morpion/rond.png')
jeton_j2 = pygame.transform.scale(jeton_j2, ((screen_size_x / 3.5), (screen_size_x / 3.5)))

buton_multi_xi = screen_size_x / 4
buton_multi_yi = screen_size_y * 0.5
buton_multi_xl = screen_size_x / 2
buton_multi_yl = screen_size_y * 0.15

buton_rejouer_xi = screen_size_x / 2
buton_rejouer_yi = screen_size_y
buton_rejouer_xl = screen_size_x / 2
buton_rejouer_yl = score_size

buton_menu_xi = 0
buton_menu_yi = screen_size_y
buton_menu_xl = screen_size_x / 2
buton_menu_yl = score_size

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 100, 200)
pink_fade = (170, 50, 100)
score_color = blue


class MorpionJeu:
    
    def __init__(self):
        self.screen = pygame.display.set_mode([screen_size_x, screen_size_y + score_size])
        self.running = 1
        

    def main(self):
        self.init_screen()
        pygame.event.clear()

        # loop
        while self.running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0

            global i, cpt
            self.affiche_joueur(i)
            colonne, ligne = self.detect_pos()
            if (colonne != 0) & (ligne != 0):
                self.placer_pion(i, colonne, ligne)
                self.trouver_gagnant(i)
                i = i * -1
                cpt += 1
            pygame.display.flip()
            if cpt == 9:
                self.afficher_gagnant(0)
        

    def init_screen(self):
        global font, i, z, cl, cpt

        cpt = 0
        i = 1
        z = 5
        cl = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

        # Fill the background
        font = pygame.font.SysFont(None, text_size)
        self.screen.fill(white)
        pygame.draw.rect(self.screen, score_color, (0, screen_size_y, screen_size_x, score_size))
        for z in range(1, 3):
            pygame.draw.line(self.screen, black, (0, z * (screen_size_y / 3)), (screen_size_x, z * (screen_size_y / 3)), 5)
            pygame.draw.line(self.screen, black, (z * (screen_size_x / 3), 0), (z * (screen_size_x / 3), screen_size_y), 5)
        pygame.display.flip()


    def detect_pos(self):
        if pygame.mouse.get_pressed()[0]:
            pos_c = pygame.mouse.get_pos()[0]
            pos_l = pygame.mouse.get_pos()[1]
            for c in range(1, 4):
                if (pos_c > ((c - 1) * screen_size_x / 3)) and (pos_c < (c * screen_size_x / 3)):
                    for l in range(1, 4):
                        if (pos_l > ((l - 1) * screen_size_x / 3)) and (pos_l < (l * screen_size_x / 3)):
                            if cl[l - 1][c - 1] != 1 and cl[l - 1][c - 1] != -1:
                                return c, l
        return 0, 0


    def affiche_joueur(self, joueur):
        global text
        pygame.draw.rect(self.screen, score_color, (0, screen_size_y, screen_size_x, score_size))
        if joueur == 1:
            text = font.render('Tour de : {}'.format(Nom_J1), True, white)
        elif joueur == -1:
            text = font.render('Tour de : {}'.format(Nom_J2), True, white)
        self.screen.blit(text, text.get_rect(center=(screen_size_x / 2, screen_size_y + (score_size / 2))))


    def placer_pion(self, joueur, colonne, ligne):
        global z, jeton
        bord_size_x = -screen_size_x / 12
        bord_size_y = -screen_size_y / 20
        if joueur == 1:
            # print('pion J1 - colonne {} - ligne {}'.format(colonne, ligne))
            jeton = jeton_j1
            if cl[ligne - 1][colonne - 1] == 0:
                cl[ligne - 1][colonne - 1] = joueur
        elif joueur == -1:
            # print('pion J2 - colonne {} - ligne {}'.format(colonne, ligne))
            jeton = jeton_j2
            bord_size_x = screen_size_x / 40
            bord_size_y = screen_size_y / 40
            if cl[ligne - 1][colonne - 1] == 0:
                cl[ligne - 1][colonne - 1] = joueur

        pos_jeton_x = (bord_size_x + (colonne - 1) * colonne_size)
        pos_jeton_y = (bord_size_y + (ligne - 1) * line_size)
        self.screen.blit(jeton, (pos_jeton_x, pos_jeton_y))


    def test_suite(self, px, py, joueur):
        global nb
        if cl[px][py] == joueur:
            nb += 1
            if nb == 3:
                self.afficher_gagnant(joueur)
                return
        else:
            nb = 0


    def trouver_gagnant(self, joueur):
        global nb
        nb = 0

        # recherche colonne
        for C in range(0, 3):
            for L in range(0, 3):
                self.test_suite(L, C, joueur)
            nb = 0

        # recherche ligne
        for L in range(0, 3):
            for C in range(0, 3):
                self.test_suite(L, C, joueur)
            nb = 0

        # recherche diagonale
        # diagonale SUD-EST
        for D in range(0, 3):
            self.test_suite(D, D, joueur)
        nb = 0

        # diagonale SUD-OUEST
        for D in range(0, 3):
            self.test_suite(D, 2 - D, joueur)
        nb = 0


    def afficher_gagnant(self, joueur):
        global font, text

        font = pygame.font.SysFont(None, text_gagnant)
        pygame.draw.rect(self.screen, score_color, (0, screen_size_y, screen_size_x, score_size))

        if joueur == 1:
            text = font.render('Gagnant : {}'.format(Nom_J1), True, black)
        elif joueur == -1:
            text = font.render('Gagnant : {}'.format(Nom_J2), True, black)
        elif joueur == 0:
            text = font.render('Pas de gagnant', True, black)

        self.screen.blit(text, text.get_rect(center=(screen_size_x / 2, screen_size_y / 2)))

        pygame.draw.rect(self.screen, pink_fade, (buton_rejouer_xi, buton_rejouer_yi, buton_rejouer_xl, buton_rejouer_yl))
        pygame.draw.rect(self.screen, pink, (buton_rejouer_xi, buton_rejouer_yi, buton_rejouer_xl, buton_rejouer_yl), 5)
        title = font.render('REJOUER', True, pink)
        self.screen.blit(title, title.get_rect(
            center=(buton_rejouer_xi + buton_rejouer_xl / 2, buton_rejouer_yi + buton_rejouer_yl / 2)))

        pygame.draw.rect(self.screen, pink_fade, (buton_menu_xi, buton_menu_yi, buton_menu_xl, buton_menu_yl))
        pygame.draw.rect(self.screen, pink, (buton_menu_xi, buton_menu_yi, buton_menu_xl, buton_menu_yl), 5)
        title = font.render('MENU', True, pink)
        self.screen.blit(title, title.get_rect(center=(buton_menu_xi + buton_menu_xl / 2, buton_menu_yi + buton_menu_yl / 2)))

        pygame.display.flip()
        self.fin_partie()


    def fin_partie(self):
        # loop
        while self.running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0

            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos_x = pygame.mouse.get_pos()[0]
                pos_y = pygame.mouse.get_pos()[1]
                if (pos_x > buton_rejouer_xi) and (pos_x < (buton_rejouer_xi + buton_rejouer_xl)) and (
                        pos_y > buton_rejouer_yi) and (pos_y < (buton_rejouer_yi + buton_rejouer_yl)):
                    pygame.time.delay(100)
                    self.main()
                elif (pos_x > buton_menu_xi) and (pos_x < (buton_menu_xi + buton_menu_xl)) and (pos_y > buton_menu_yi) and (
                        pos_y < (buton_menu_yi + buton_menu_yl)):
                    pygame.time.delay(100)
                    # menu general
                    self.running = 0