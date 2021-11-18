import pygame
import math

screen = pygame.display.set_mode((800, 600))


class bullet(pygame.sprite.Sprite):
    def __init__(self,Image_path, pos_X, pos_Y, angle):
        super().__init__()
        self.Image_path = Image_path
        self.image = pygame.image.load(Image_path)
        self.posX  = pos_X
        self.posY = pos_Y
        self.angle = angle
        self.x_direction = 1
        self.y_direction = 1
        self.start_x = pos_X
        self.start_y = pos_Y
        self.hyp = 1
        self.velocity = 0.0005


    # Velocity
    def set_vel(self):
        temp_angle = abs(self.angle)


        if temp_angle == 90:
            X = 10000000000000 # sets a point that is far away from the screen
            Y = self.start_y

        elif temp_angle == 180 or temp_angle == 0:
            Y = 10000000000000
            X = self.start_x

        else:
            X = 10000000000000
            rad_angle = (self.angle*math.pi)/180 # Converts the angle from degrees to radians
            Y = X*math.tan((math.pi/2) - rad_angle) # Gets the y direction by multiplying the x and the and the tan angl

        # Calculates the from the character and the x and y point
        dif_X = abs(self.posX - X)
        dif_Y = abs(self.posY - Y)

        # Calculates the hypotenuse
        hyp = ((dif_X**2) + (dif_Y**2)) ** 0.5

        # Three point to make the triangle put into a tuple
        self.ratio = (dif_Y/hyp ,dif_X/hyp ,1)

        # Changes the direction of the bullet
        if abs(self.angle) > 90:
             self.y_direction = -1 # Bullet above 90, bullet shoots up

        if self.angle < 0:
            self.x_direction = -1 # Bullet shoots left, bullet shoots left

    # Calculates the amount X an Y should increase relative to the hyp
    def calc_x(self):
        return (self.hyp / self.ratio[2]) * self.ratio[1]

    def calc_y(self):
        return (self.hyp / self.ratio[2]) * self.ratio[0]

    # Makes the bullet move
    def move(self,screen):
        #self.hyp += self.velocity

        self.posX += self.calc_x() * self.x_direction
        self.posY += self.calc_y() * self.y_direction

        rotated_image = pygame.transform.rotate(self.image, self.angle) # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.posX, self.posY))


    def destroy(self,bullet_array):
        bullet_array.remove(self)
        del self


    def update(self):
        self.set_vel()
        self.move(screen)
        self.destroy()














