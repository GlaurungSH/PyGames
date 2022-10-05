import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Create a bullet in the position of the gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)  # Create a bullet - initial position coordinates and size in pixels
        self.color = 30, 230, 86  # Bullet color
        self.speed = 1.5  # Bullet speed. The rate of change of position along the Y coordinate
        self.rect.centerx = gun.rect.centerx  # The appearance of a bullet at the top of the gun
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)  # The ability of the rect attribute to accept float numbers

    def update(self):
        """Moving the bullet up"""
        self.y -= self.speed  # The Y coordinate will decrease by the speed of the bullet
        self.rect.y = self.y  # Update bullet position

    def draw_bullet(self):
        """Draw a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
