import pygame
#from Bullet import bullet
import math

screen = pygame.display.set_mode((800, 600))


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/User_icon.png')
        self.X = 400
        self.Y = 300
        self.changeX = 0
        self.changeY = 0
        self.velocity = 10
        self.rect = self.image.get_rect(midbottom = (400,300))

    def draw_character(self):
        #print(self.rect)

        # Gets mouse position
        mx, my = pygame.mouse.get_pos() # Gets the mouse postion

        x = (self.X + self.rect[2] // 2) # Gets the position of the X and Y
        y = (self.Y + self.rect[3] // 2)

        difX = mx - x # Calculates the distance between the mouse and the player icon
        difY = my - y
        # angle = 0

        angle = math.atan2(difX, difY) * (180 / math.pi) - 5 # Calculates the angle of the player and the mouse
        print(angle)
        rotated_image = pygame.transform.rotate(self.image, angle) # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.X, self.Y)) # Draws the player and the rotation of the player

        #pygame.draw.circle(screen, [255, 66, 99], (x, y), 5)

    # def draw_bullet(self,mouse_X,mouse_Y):
    #     return bullet(mouse_X,mouse_Y)

    def boundaries(self):
        if self.X <= 0:
            self.X = 0
        elif self.X >= 750:
            self.X = 750

        if self.Y <= 0:
            self.Y = 0
        elif self.Y >= 555:
            self.Y = 555

    def update(self):
        self.boundaries()
        self.draw_character()








'''
  def Test(self):
        print("hello")
'''
