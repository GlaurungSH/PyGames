import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """Output of game information"""
    def __init__(self, screen, stats):
        """Scoring initialization"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (30, 230, 86)
        self.font = pygame.font.SysFont(None, 36)  # Font type and font size
        self.image_score()  # Drawing the font on the screen
        self.image_high_score()  # Displaying the record
        self.image_lives()  # Get the number of lives

    def image_score(self):
        """Converts invoice text to a graphic"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()  # Getting a rect object from our image
        self.score_rect.right = self.screen_rect.right - 40  # We place the account at the top right
        self.score_rect.top = 20  # Top indent

    def image_high_score(self):
        """Converts a record to a graphic image"""
        self.high_score_img = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_lives(self):
        """Number of lives"""
        self.guns = Group()
        for lives_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + lives_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """Displaying an invoice on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.guns.draw(self.screen)