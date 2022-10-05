import pygame
import sys
from bullet import Bullet


def events(screen, gun, bullets):
    """Event handling"""
    for event in pygame.event.get():  # Collecting all user events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # right key
                gun.mright = True
            elif event.key == pygame.K_a:  # left key
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)  # Create a bullet when pressing the space bar
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:  # right key
                gun.mright = False
            elif event.key == pygame.K_a:  # left key
                gun.mleft = False

def update_screen(bg_color, screen, gun, bullets):
    """Screen update"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():  # Draw the bullets in front of the cannon ->
        # -> so that the bullets are not on top of the cannon on the screen
        bullet.draw_bullet()
    gun.output_gun()
    pygame.display.flip()  # We draw the last screen so that after the loop ends there is no empty window

def update_bullets(bullets):
    """Bullet position update"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Remove the bullet after reaching the end of the screen.
            # Since the bullet continues to move along the Y coordinate after the end of the screen (occupies memory)

    # print(len(bullets))  -> Checking if bullets are being removed