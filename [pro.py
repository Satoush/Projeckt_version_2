import pygame
from character_class_v2 import Character
WHITE = (255, 255, 255)

character = Character(400,300,0,0)

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        pygame.display.update()

