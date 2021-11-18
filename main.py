'''
you will need to install:
pygame
math
random
'''

import pygame
from pygame.locals import *
import random
from character_class_v2 import Character
from Enemy import enemy

# Intialize pygame
pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))

########################################################################################
# Players data
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0



# Enemies data
enemy_image_path = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Player object
character = Character(playerX,playerY,playerX_change,playerY_change)

# Enemy object
zombie = enemy(enemy_image_path, enemyX, enemyY, enemyX_change, enemyY_change)
zombie.adding_multiple_enemies()
#print(zombie)



player = pygame.sprite.GroupSingle() # Adding player to a group on its own
player.add(Character(playerX,playerY,playerX_change,playerY_change))

running = True
# -------- Main Program Loop -----------
def main():
    while running:
        # Background colour
        screen.fill(WHITE)

        # Adding the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Fire button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                   character.fire()

        # Enemy loop
        for i in range(num_of_enemies): # Loops throw enemies and draws them
            zombie.draw(i, enemyX[i], enemyY[i])
            zombie.move_to_player(character.X, character.Y)


        # Bullet list
        for bullet in character.bullets:
            screen_width, screen_height = screen.get_size()

            if bullet.posX >= screen_width or bullet.posX <= 0:
                bullet.destroy(character.bullets)

            elif bullet.posY >= screen_height or bullet.posY <= 0:
                bullet.destroy(character.bullets)
            else:
                bullet.move(screen)



        character.update()
        pygame.display.update()

# Calling main program
main()
