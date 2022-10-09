import pygame


class Alien(pygame.sprite.Sprite):  # Based on one alien, we create a whole group of identical aliens
    """One alien class"""

    def __init__(self, screen):
        """IInitialize and create initial position"""
        super(Alien, self).__init__()  # Since the Alien class is a child
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()  # Converting the alien image to a rectangle
        self.rect.x = self.rect.width  # Tracking the width of the rectangle along the X coordinate
        self.rect.y = self.rect.height  # Tracking the height of the rectangle along the Y coordinate
        self.x = float(self.rect.x)  # For a smoother movement of the alien, ->
        # we convert the coordinates to the float type
        self.y = float(self.rect.y)

    def draw(self):
        """Alien display on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moving aliens on the screen"""
        self.y += 0.1
        self.rect.y = self.y
