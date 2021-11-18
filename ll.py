import pygame
from character_class_v2 import Character

player = pygame.sprite.GroupSingle() # Adding player to a group on its own
player.add(Character())

#character = Character()
print(Character().velocity)

#player.vel_change()