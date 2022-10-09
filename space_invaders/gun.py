import pygame


class Gun():

    def __init__(self, screen):
        """Initialize a gun"""
        self.screen = screen  # Getting our screen
        self.image = pygame.image.load('images/laser_gun.png')
        self.rect = self.image.get_rect()  # We get the image of the gun as a rectangle
        self.screen_rect = screen.get_rect()  # Getting our screen object
        self.rect.centerx = self.screen_rect.centerx  # Cannon on X coordinate exactly in the center of the screen
        self.center = float(self.rect.centerx)  # The ability of the rect attribute to accept float numbers
        self.rect.bottom = self.screen_rect.bottom  # Cannon in Y coordinate at the bottom of the screen
        self.mright = False  # Movement of the gun to the right only when the key is pressed
        self.mleft = False  # Movement of the gun to the left

    def output_gun(self):
        """Drawing a gun on the screen"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Gun position update"""
        if self.mright and self.rect.right < self.screen_rect.right:  # if self.mright == True and ->
            # -> The x-coordinate of the right edge of the gun must be less than ->
            # -> the x-coordinate of the right edge of the display
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:  # to move left
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """Places the cannon at the bottom center of the screen"""
        self.center = self.screen_rect.centerx
