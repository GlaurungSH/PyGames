import pygame
import sys


def events(gun):
    """Event handling"""
    for event in pygame.event.get():  # Collecting all user events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # right key
                gun.mright = True
            elif event.key == pygame.K_a:  # left key
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:  # right key
                gun.mright = False
            elif event.key == pygame.K_a:  # left key
                gun.mleft = False

