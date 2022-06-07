import pygame

#pygame.display.init()
#screen_width = pygame.display.get_desktop_sizes()[0][0] - 100
#screen_height = pygame.display.get_desktop_sizes()[0][1] - 100
screen_width = 600
screen_height = 600

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = 'images/SpaceInvaders/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width * 0.075, screen_width * 0.075))
        self.rect = self.image.get_rect(topleft=(x, y))

        if color == 'blue': self.value = 100
        if color == 'green': self.value = 200
        if color == 'yellow': self.value = 300
    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side):
        super().__init__()
        self.image = pygame.image.load('images/SpaceInvaders/extra.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width * 0.1, screen_width * 0.05))

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 60))

    def update(self):
        self.rect.x += self.speed
