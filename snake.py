from jeu import Jeu
import pygame
import random

TETE = [pygame.image.load("images/Snake/s_nord.png"), pygame.image.load("images/Snake/s_est.png"),
        pygame.image.load("images/Snake/s_sud.png"), pygame.image.load("images/Snake/s_ouest.png")]

CORPS = [pygame.image.load("images/Snake/corps_vertical.png"), pygame.image.load("images/Snake/corps_horizontal.png"),
         pygame.image.load("images/Snake/corps_vertical.png"), pygame.image.load("images/Snake/corps_horizontal.png"),
         pygame.image.load("images/Snake/angle_nord_est.png"), pygame.image.load("images/Snake/angle_nord_ouest.png"),
         pygame.image.load("images/Snake/angle_sud_est.png"), pygame.image.load("images/Snake/angle_sud_ouest.png")]
# 0                                                                    1
# 2                                           3                                                      4
# 5                                                                6                                              7
QUEUE = [pygame.image.load("images/Snake/q_nord.png"), pygame.image.load("images/Snake/q_est.png"),
         pygame.image.load("images/Snake/q_sud.png"), pygame.image.load("images/Snake/q_ouest.png")]

POMME = pygame.image.load("images/Snake/pomme.png")


class SnakeGenerate(pygame.sprite.Group):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.tete = [6 * 64, 8 * 64]
        self.taille = 5
        self.corps = [[2 * 64, 8 * 64], [3 * 64, 8 * 64], [4 * 64, 8 * 64], [5 * 64, 8 * 64], self.tete]
        self.mouv = [1, 1, 1, 1, 1]
        self.angles = [0, 0, 0, 0, 0]

    def afficher(self):
        return

    def agrandir(self):
        return

    def en_collision(self):
        return True


def update_move():
    global apple_loc
    global jeu
    global move
    SnakeG.tete = pos_x, pos_y
    if grid_coordinates(SnakeG.tete) != PREV_HEAD:
        if grid_coordinates(SnakeG.tete) in SnakeG.corps:
            print("OUPSS LE SNAKE A EU UN ACCIDENT")
            jeu.running = False
        elif grid_coordinates(SnakeG.tete) == (tuple([64 * x for x in apple_loc])):
            apple_loc = None
            SnakeG.taille += 1
        if apple_loc != None:
            SnakeG.corps.pop(0)
            SnakeG.mouv.pop(0)
            SnakeG.angles.pop(0)
        SnakeG.corps.append(PREV_HEAD)
        SnakeG.mouv.append((dir_to_int(change_to)))
        SnakeG.angles.append(move)
        move = 0


def init_game():
    global apple_loc
    global PREV_HEAD
    global pos_x, pos_y
    global change_to
    global move
    global offset
    global clock
    global EAT
    global screen
    global jeu
    global SnakeG
    pygame.init()
    pygame.display.set_caption('SNAKE MULTIGAME')
    screen = pygame.display.set_mode(
        (pygame.display.get_desktop_sizes()[0][0] - 100, pygame.display.get_desktop_sizes()[0][1] - 100),
        pygame.RESIZABLE)
    offset = 64
    clock = pygame.time.Clock()
    jeu = Jeu()
    EAT = True
    SnakeG = SnakeGenerate(jeu)
    jeu.running = True
    pygame.display.init()
    pygame.display.flip()
    pos_x, pos_y = SnakeG.tete
    apple_loc = generate_apple(0)
    change_to = ''
    PREV_HEAD = grid_coordinates(SnakeG.tete)
    move = 0


def event_update():
    global change_to
    global move
    global PREV_HEAD
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu.running = False
            pygame.display.flip()
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and change_to != 'DOWN':
                if change_to == 'LEFT':
                    move = 4
                elif change_to == 'RIGHT':
                    move = 5
                change_to = 'UP'

            if event.key == pygame.K_DOWN and change_to != 'UP':
                if change_to == 'LEFT':
                    move = 6
                elif change_to == 'RIGHT':
                    move = 7
                change_to = 'DOWN'

            if event.key == pygame.K_LEFT and change_to != 'RIGHT':
                if change_to == 'UP':
                    move = 7
                elif change_to == 'DOWN':
                    move = 5
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and change_to != 'LEFT':
                if change_to == 'UP':
                    move = 6
                elif change_to == 'DOWN':
                    move = 4
                change_to = 'RIGHT'

            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    PREV_HEAD = grid_coordinates(SnakeG.tete)


def set_difficulty(a):
    global DIFFICULTY
    DIFFICULTY = a


def display_apple():
    screen.blit(POMME, (tuple([64 * x for x in apple_loc])))


def real_pos_snake():
    global pos_y
    global pos_x
    if change_to != '':
        if change_to == 'UP':
            pos_y -= 10
        elif change_to == 'DOWN':
            pos_y += 10
        elif change_to == 'LEFT':
            pos_x -= 10
        else:
            pos_x += 10


def show_snake():
    screen.blit(TETE[(SnakeG.mouv[-2])], grid_coordinates(SnakeG.corps[-1]))
    for position, mouvement, angle in zip(SnakeG.corps[1:SnakeG.taille - 1], SnakeG.mouv[1:SnakeG.taille - 1],
                                          SnakeG.angles[1:SnakeG.taille - 1]):
        if angle == 0:
            screen.blit(CORPS[mouvement], position)
        else:
            screen.blit(CORPS[angle], position)
    screen.blit(QUEUE[SnakeG.mouv[0]], SnakeG.corps[0])


def generate_map():
    screen.fill((0, 0, 0, 1))
    for i in range(16):
        for j in range(16):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (44, 140, 82), [64 * i, 64 * j, 64, 64])
            else:
                pygame.draw.rect(screen, (37, 116, 69), [64 * i, 64 * j, 64, 64])


def generate_apple(a):
    global SnakeG
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    if a == 0:
        return (8, 6)
    while (x, y) in SnakeG.corps or (x, y) == apple_loc:
        x = random.randint(1, 16)
        y = random.randint(1, 16)
    return (x, y)


def grid_coordinates(coords):
    x = (coords[0] // 64) * 64
    y = (coords[1] // 64) * 64
    return (x, y)


def dir_to_int(s):
    if change_to == 'UP':
        return 0
    elif change_to == 'DOWN':
        return 2
    elif change_to == 'LEFT':
        return 3
    else:
        return 1


def affiche_grille():
    for (x, y) in SnakeG.corps:
        print("DEBUG: \n\tX: {} \n\t Y: {} ".format(x / 64, y / 64))


init_game()
set_difficulty(40)
while jeu.running:
    if pos_x < 0 or pos_x > 64 * 16 or pos_y < 0 or pos_y > 64 * 16:
        print("Perdu ! sortie de terrain")
        jeu.running = False
    # MAP GENERATION
    generate_map()
    # END MAP GEN
    if apple_loc == None:
        apple_loc = generate_apple(1)
    display_apple()
    update_move()
    show_snake()
    event_update()
    real_pos_snake()
    clock.tick(DIFFICULTY)
    pygame.display.flip()
