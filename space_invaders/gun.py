import pygame


class Gun():

    def __init__(self, screen):
        """Initialize a gun"""
        self.screen = screen  # Getting our screen
        self.image = pygame.image.load('images/laser_gun.png')
        self.rect = self.image.get_rect()  # We get the image of the gun as a rectangle
        self.screen_rect = screen.get_rect()  # Getting our screen object
        self.rect.centerx = self.screen_rect.centerx  # Cannon on X coordinate exactly in the center of the screen
        self.rect.bottom = self.screen_rect.bottom  # Cannon in Y coordinate at the bottom of the screen

    def output_gun(self):
        """Drawing a gun on the screen"""
        self.screen.blit(self.image, self.rect)
