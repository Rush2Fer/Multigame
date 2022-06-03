import pygame

pygame.init()

screen_size_x = 600
screen_size_y = screen_size_x * (1498 / 1730)
score_size = 100
screen = pygame.display.set_mode([screen_size_x, screen_size_y + score_size])

bord_size_x = screen_size_x / 40
colonne_size = (screen_size_x - (0.91 * bord_size_x)) / 7
bord_size_y = screen_size_y / 50
line_size = (screen_size_y - (1.5 * bord_size_y)) / 6

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

text_size = 40
text_menu = 70
text_gagnant = 90
Nom_J1 = 'Joueur 1'
Nom_J2 = 'Joueur 2'
font = pygame.font.SysFont(None, text_size)


jeton_size = screen_size_x / 8.5

p4_grille = pygame.image.load('images/P4/Board.png')
p4_grille = pygame.transform.scale(p4_grille, (screen_size_x, screen_size_y))
jeton_j1 = pygame.image.load('images/P4/Red.png')
jeton_j1 = pygame.transform.scale(jeton_j1, (jeton_size, jeton_size))
jeton_j2 = pygame.image.load('images/P4/Yellow.png')
jeton_j2 = pygame.transform.scale(jeton_j2, (jeton_size, jeton_size))

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 100, 200)
pink_fade = (170, 50, 100)
score_color = blue


class P4Jeu:

    def main(self):
        self.init_screen()

        # loop
        while 1:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            global i, cpt
            self.affiche_joueur(i)
            colonne = self.detect_colon()
            if colonne != 0:
                self.placer_pion(i, colonne)
                self.trouver_gagnant(i)
                i = i * -1
                cpt += 1
            pygame.display.flip()
            if cpt == 42:
                self.afficher_gagnant(0)


    def init_screen(self):
        global font, i, z, cl, cpt

        cpt = 0
        i = 1
        z = 5
        cl = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]

        # Fill the background
        screen.fill(black)
        font = pygame.font.SysFont(None, text_size)
        pygame.draw.rect(screen, score_color, (0, screen_size_y, screen_size_x, score_size))
        screen.blit(p4_grille, (0, 0))
        pygame.display.flip()


    def detect_colon(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()[0]
            for c in range(1, 8):
                if (pos > ((c - 1) * screen_size_x / 7)) and (pos < (c * screen_size_x / 7)):
                    pygame.time.delay(300)
                    if cl[0][c - 1] != 1 and cl[0][c - 1] != -1:
                        return c
        return 0


    def affiche_joueur(self, joueur):
        global text
        pygame.draw.rect(screen, score_color, (0, screen_size_y, screen_size_x, score_size))
        if joueur == 1:
            text = font.render('Tour de : {}'.format(Nom_J1), True, white)
        elif joueur == -1:
            text = font.render('Tour de : {}'.format(Nom_J2), True, white)
        screen.blit(text, text.get_rect(center=(screen_size_x / 2, screen_size_y + (score_size / 2))))


    def placer_pion(self, joueur, colonne):
        global z, jeton
        if joueur == 1:
            # print('pion J1 - colonne {}'.format(colonne))
            jeton = jeton_j1
            for z in range(5, -1, -1):
                if cl[z][colonne - 1] == 0:
                    cl[z][colonne - 1] = joueur
                    break
        elif joueur == -1:
            # print('pion J2 - colonne {}'.format(colonne))
            jeton = jeton_j2
            for z in range(5, -1, -1):
                if cl[z][colonne - 1] == 0:
                    cl[z][colonne - 1] = joueur
                    break

        pos_jeton_y = (bord_size_y + z * line_size)
        pos_jeton_x = bord_size_x + (colonne - 1) * colonne_size
        screen.blit(jeton, (pos_jeton_x, pos_jeton_y))


    def test_suite(self, px, py, joueur):
        global nb
        if cl[px][py] == joueur:
            nb += 1
            if nb == 4:
                self.afficher_gagnant(joueur)
                return
        else:
            nb = 0


    def trouver_gagnant(self, joueur):
        global nb
        nb = 0

        # recherche colonne
        for C in range(0, 7):
            for L in range(0, 6):
                self.test_suite(L, C, joueur)
            nb = 0

        # recherche ligne
        for L in range(0, 6):
            for C in range(0, 7):
                self.test_suite(L, C, joueur)
            nb = 0

        # recherche diagonale
        # diagonale SUD-EST
        for L in range(1, 3):
            for C in range(0, 6-L):
                x = C+L
                y = C
                self.test_suite(x, y, joueur)
            nb = 0
        for D in range(0, 6):
            self.test_suite(D, D, joueur)
        nb = 0
        for L in range(1, 4):
            for C in range(0, 7-L):
                x = C
                y = C+L
                self.test_suite(x, y, joueur)
            nb = 0

        # diagonale SUD-OUEST
        for L in range(1, 3):
            for C in range(0, 6-L):
                x = C+L
                y = 6-C
                self.test_suite(x, y, joueur)
            nb = 0
        for D in range(0, 6):
            self.test_suite(D, 6-D, joueur)
        nb = 0
        for L in range(1, 4):
            for C in range(0, 7-L):
                x = C
                y = 6-(C+L)
                self.test_suite(x, y, joueur)
            nb = 0


    def afficher_gagnant(self, joueur):
        global font, text

        font = pygame.font.SysFont(None, text_gagnant)
        pygame.draw.rect(screen, score_color, (0, screen_size_y, screen_size_x, score_size))

        if joueur == 1:
            text = font.render('Gagnant : {}'.format(Nom_J1), True, white)
        elif joueur == -1:
            text = font.render('Gagnant : {}'.format(Nom_J2), True, white)
        elif joueur == 0:
            text = font.render('Pas de gagnant', True, white)

        screen.blit(text, text.get_rect(center=(screen_size_x / 2, screen_size_y / 2)))

        pygame.draw.rect(screen, pink_fade, (buton_rejouer_xi, buton_rejouer_yi, buton_rejouer_xl, buton_rejouer_yl))
        pygame.draw.rect(screen, pink, (buton_rejouer_xi, buton_rejouer_yi, buton_rejouer_xl, buton_rejouer_yl), 5)
        title = font.render('REJOUER', True, pink)
        screen.blit(title, title.get_rect(center=(buton_rejouer_xi + buton_rejouer_xl / 2, buton_rejouer_yi + buton_rejouer_yl / 2)))

        pygame.draw.rect(screen, pink_fade, (buton_menu_xi, buton_menu_yi, buton_menu_xl, buton_menu_yl))
        pygame.draw.rect(screen, pink, (buton_menu_xi, buton_menu_yi, buton_menu_xl, buton_menu_yl), 5)
        title = font.render('MENU', True, pink)
        screen.blit(title, title.get_rect(center=(buton_menu_xi + buton_menu_xl / 2, buton_menu_yi + buton_menu_yl / 2)))

        pygame.display.flip()
        self.fin_partie()


    def fin_partie(self):

        # loop
        while 1:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos_x = pygame.mouse.get_pos()[0]
                pos_y = pygame.mouse.get_pos()[1]
                if (pos_x > buton_rejouer_xi) and (pos_x < (buton_rejouer_xi + buton_rejouer_xl)) and (pos_y > buton_rejouer_yi) and (pos_y < (buton_rejouer_yi + buton_rejouer_yl)):
                    pygame.time.delay(100)
                    self.main()
                elif (pos_x > buton_menu_xi) and (pos_x < (buton_menu_xi + buton_menu_xl)) and (pos_y > buton_menu_yi) and (pos_y < (buton_menu_yi + buton_menu_yl)):
                    pygame.time.delay(100)
                    # menu general

# a retirer
jeu = P4Jeu()
jeu.main()