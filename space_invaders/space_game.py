import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((550, 700))  # Creating a Display Game
    pygame.display.set_caption('Space Invaders')  # Title for the graphics window
    bg_color = (0, 0, 0)  # Window background color -> Black
    gun = Gun(screen)  # Draw the gun object on the graphics screen
    bullets = Group()  # Create a bullet container
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()  # Create an instance of the Stats class
    player_score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()  # Gun position update
            controls.update_screen(bg_color, screen, stats, player_score, gun, aliens, bullets)  # Screen update
            controls.update_bullets(screen, stats, player_score, aliens, bullets)  # Bullet position update
            controls.update_aliens(stats, screen, player_score, gun, aliens, bullets)  # Aliens position update


run()
