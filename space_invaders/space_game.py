import pygame
import sys
from gun import Gun


def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 650))  # Creating a Display Game
    pygame.display.set_caption('Space Invaders')  # Title for the graphics window
    bg_color = (0, 0, 0) # Window background color -> Black
    gun = Gun(screen)  # Draw the gun object on the graphics screen

    while True:
        for event in pygame.event.get():  # Collecting all user events
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        gun.output_gun()
        pygame.display.flip()  # We draw the last screen so that after the loop ends there is no empty window

run()