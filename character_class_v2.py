import pygame
from Bullet import bullet
import math

screen = pygame.display.set_mode((800, 600))

class Character(pygame.sprite.Sprite):
    def __init__(self,X,Y,changeX,changeY):
        super().__init__()
        self.image = pygame.image.load('Assets/User_icon.png')
        self.X = X
        self.Y = Y
        self.changeX = changeX
        self.changeY = changeY
        self.velocity = 1
        self.bullets = []
        self.angle = 0
        self.rect = self.image.get_rect(center = (400,300))



    def player_input(self):
        key = pygame.key.get_pressed()
        p = pygame
        self.changeX = 0
        self.changeY = 0
        if key[p.K_DOWN] or key[p.K_UP] or key[p.K_w] or key[p.K_s]:
            self.changeY = self.velocity * - (int(key[p.K_UP] or key[p.K_w]) * 2 - 1)

        if key[p.K_LEFT] or key[p.K_RIGHT] or key[p.K_a] or key[p.K_d]:
            self.changeX = self.velocity * - (int(key[p.K_LEFT] or key[p.K_a]) * 2 - 1)

        self.X += self.changeX
        self.Y += self.changeY

    def draw_character(self):
        # Gets mouse position
        mx, my = pygame.mouse.get_pos()

        # Gets the position of the X and Y
        x = (self.X + self.rect[2] // 2)
        y = (self.Y + self.rect[3] // 2)

        # Calculates the distance between the mouse and the player icon
        difX = mx - x
        difY = my - y
        # angle = 0

        # Calculates the angle of the player and the mouse
        angle = math.atan2(difX, difY) * (180 / math.pi)

        self.angle = angle
        #print ('playerangle', angle)
        rotated_image = pygame.transform.rotate(self.image, angle) # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.X - 25 ,self.Y-32)) # Draws the player and the rotation of the player


        # pygame.draw.line(screen, pygame.Color("red"), (self.X,self.Y), (mx,my), 2)
        # pygame.draw.line(screen, pygame.Color("red"), (self.X,self.Y), (self.X,10000), 2)



    def boundaries(self):
        if self.X <= 0:
            self.X = 0
        elif self.X >= 750:
            self.X = 750

        if self.Y <= 0:
            self.Y = 0
        elif self.Y >= 555:
            self.Y = 555

    def fire(self):

        new_bullet = bullet('Assets/Bullet.png',self.X,self.Y,self.angle)
        new_bullet.set_vel()
        self.bullets.append(new_bullet)
        pass


    def update(self):
        self.player_input()
        self.boundaries()
        self.draw_character()


