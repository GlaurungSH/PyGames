import pygame
import controls
from gun import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((550, 700))  # Creating a Display Game
    pygame.display.set_caption('Space Invaders')  # Title for the graphics window
    bg_color = (0, 0, 0)  # Window background color -> Black
    gun = Gun(screen)  # Draw the gun object on the graphics screen
    bullets = Group()  # Create a bullet container

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()  # Gun position update
        controls.update_screen(bg_color, screen, gun, bullets)  # Screen update
        controls.update_bullets(bullets)  # Bullet position update


run()
