import pygame, sys
from player import Player
import obstacle
from aliens import Alien, Extra
from random import choice, randint
from laser import Laser

pygame.init()

class Game:
    def __init__(self):
        #général setup
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),pygame.RESIZABLE)
        # Player setup
        player_sprite = Player((self.screen_width / 2, self.screen_height), self.screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #health et score
        self.lives = 3
        self.live_surf =pygame.image.load('images/SpaceInvaders/player2.png').convert_alpha()
        self.live_surf = pygame.transform.scale(self.live_surf, (self.screen_width*0.075, self.screen_height*0.06))
        self.live_x_start_pos = self.screen_width-(self.live_surf.get_size()[0] * 2 +20)
        self.score = 0
        self.font = pygame.font.Font('./Pixeled.ttf',18)

        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (self.screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacle(*self.obstacle_x_positions, x_start=self.screen_width / 15,
                                      y_start=self.screen_height - 145)

        # alien setup
        self.aliens = pygame.sprite.Group()
        self.aliens_lasers = pygame.sprite.Group()
        self.aliens_setup(rows=6, cols=8)
        self.aliens_direction = 1

        #ectra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        #boutton setup
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        #smallfont = pygame.font.SysFont('Corbel', 35)
        self.text = self.font.render('QUIT', True, (255,255,255))
        
        self.running = True

    def main(self):

        # screen_width = pygame.display.get_desktop_sizes()[0][0] - 100
        # screen_height = pygame.display.get_desktop_sizes()[0][1] - 100
        clock = pygame.time.Clock()

        ALIENLASER = pygame.USEREVENT + 1
        pygame.time.set_timer(ALIENLASER, 600)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == ALIENLASER:
                    self.alien_shoot()

            self.screen.fill((0, 0, 0))
            self.run()

            pygame.display.flip()
            clock.tick(60)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacle(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def aliens_setup(self, rows, cols, x_distance=50, y_distance=50, x_offset=40, y_offset=60):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:
                    alien_sprite = Alien('blue', x, y)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right > self.screen_width:
                self.aliens_direction *= -1
                # self.aliens_direction += -0.5
                # print(self.aliens_direction)
                self.alien_move_down(7)
                break
            elif alien.rect.left <= 0:
                self.aliens_direction *= -1
                # self.aliens_direction += 0.5
                # print(self.aliens_direction)
                self.alien_move_down(7)
                break

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, self.screen_height)
            self.aliens_lasers.add(laser_sprite)

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left'])))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):

        #laser du joueur
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                #obstacle
                if pygame.sprite.spritecollide(laser,self.blocks,True):
                    laser.kill()

                #alien
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()

                #extra
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()
                    self.score +=  500
        #alien lasers
        if self.aliens_lasers:
            for laser in self.aliens_lasers:
                # obstacle
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                #joueur
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -=1


        #aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.lives=0

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * self.live_surf.get_size()[0])
            self.screen.blit(self.live_surf,(x,8))

    def display_score(self):
        score_surf = self.font.render(f'score : {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (10,-10))
        self.screen.blit(score_surf,score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won', False, 'white')
            victory_rect = victory_surf.get_rect(center = (self.screen_width/2, self.screen_height/2))
            self.screen.blit(victory_surf, victory_rect)

            while self.running:
                mouse = pygame.mouse.get_pos()
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        self.running=False
                        break
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if self.screen_width / 2-80 <= mouse[0] <= self.screen_width / 2+60  and self.screen_height / 2+30 <= mouse[1] <= self.screen_height / 2+85 :
                            self.running=False
                            break

                if self.screen_width / 2-80 <= mouse[0] <= self.screen_width / 2+60  and self.screen_height / 2 +30<= mouse[1] <= self.screen_height / 2+85 :
                    pygame.draw.rect(self.screen, self.color_light, [self.screen_width / 2-80, self.screen_height / 2+50, 140, 40])

                else:
                    pygame.draw.rect(self.screen, self.color_dark, [self.screen_width / 2-80, self.screen_height / 2+50, 140, 40])

                self.screen.blit(self.text, (self.screen_width / 2 -45, self.screen_height / 2+37))


                pygame.display.update()



    def death_message(self):
        if self.lives<=0:
            death_surf = self.font.render('Game Over', False, 'white')
            death_rect = death_surf.get_rect(center = (self.screen_width/2, self.screen_height/2))
            self.screen.blit(death_surf, death_rect)

            while self.running:
                mouse = pygame.mouse.get_pos()
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        self.running=False
                        break
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if self.screen_width / 2-80 <= mouse[0] <= self.screen_width / 2+60  and self.screen_height / 2+30 <= mouse[1] <= self.screen_height / 2+85 :
                            self.running=False
                            break

                if self.screen_width / 2-80 <= mouse[0] <= self.screen_width / 2+60  and self.screen_height / 2 +30<= mouse[1] <= self.screen_height / 2+85 :
                    pygame.draw.rect(self.screen, self.color_light, [self.screen_width / 2-80, self.screen_height / 2+50, 140, 40])

                else:
                    pygame.draw.rect(self.screen, self.color_dark, [self.screen_width / 2-80, self.screen_height / 2+50, 140, 40])

                self.screen.blit(self.text, (self.screen_width / 2 -45, self.screen_height / 2+37))


                pygame.display.update()





    def run(self):
        self.player.update()
        self.aliens.update(self.aliens_direction)
        self.extra.update()
        self.aliens_lasers.update()
        self.extra_alien_timer()

        self.alien_position_checker()
        self.collision_checks()


        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.blocks.draw(self.screen)
        self.aliens.draw(self.screen)
        self.aliens_lasers.draw(self.screen)
        self.extra.draw(self.screen)

        self.display_lives()
        self.display_score()
        self.victory_message()
        self.death_message()