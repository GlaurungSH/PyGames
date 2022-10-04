import pygame
import sys


def events(gun):
    """Event handling"""
    for event in pygame.event.get():  # Collecting all user events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # right key
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:  # right key
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

