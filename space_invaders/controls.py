import pygame
import sys
import time
from bullet import Bullet
from aliens import Alien


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


def update_screen(bg_color, screen, gun, aliens, bullets):
    """Screen update"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():  # Draw the bullets in front of the cannon ->
        # -> so that the bullets are not on top of the cannon on the screen
        bullet.draw_bullet()
    gun.output_gun()
    aliens.draw(screen)  # Draw an aliens on the screen
    pygame.display.flip()  # We draw the last screen so that after the loop ends there is no empty window


def update_bullets(screen, aliens, bullets):
    """Bullet position update"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Remove the bullet after reaching the end of the screen.
            # Since the bullet continues to move along the Y coordinate after the end of the screen (occupies memory)
    # print(len(bullets))  -> Checking if bullets are being removed

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # Checking collisions ->
    # (bullets hitting aliens or aliens hitting a cannon)
    # True, True -> We remove the bullet and the alien.
    # False, True -> We remove only alien.
    if len(aliens) == 0:  # Create a new alien army if the player destroyed the previous one
        bullets.empty()
        create_army(screen, aliens)


def gun_kill(stats, screen, gun, aliens, bullets):
    """Clash of guns and aliens"""
    stats.guns_left -= 1  # Removing one life on collision
    aliens.empty()  # Reset the aliens on the screen
    bullets.empty()  # Reset the bullets on the screen
    create_army(screen, aliens)  # Re-create the aliens on the screen
    gun.create_gun()  # Re-create the gun on the screen
    time.sleep(1)  # Reboot after 1 seconds


def update_aliens(stats, screen, gun, aliens, bullets):
    """Alien position update"""
    aliens.update()

    if pygame.sprite.spritecollideany(gun, aliens):  # Checking if the alien object overlaps the cannon object
        gun_kill(stats, screen, gun, aliens, bullets)

    aliens_check(stats, screen, gun, aliens, bullets)


def aliens_check(stats, screen, gun, aliens, bullets):
    """Checking if the alien army has reached the edge of the screen"""
    screen_rect = screen.get_rect()  # Get the screen rectangle

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break  # If at least one alien has reached the edge of the screen, ->
            # we stop the loop, since we do not need to go through other aliens


def create_army(screen, aliens):
    """Creation of an alien army"""
    alien = Alien(screen)  # Create one alien
    alien_width = alien.rect.width  # Single alien width
    number_alien_x = int((550 - 2 * alien_width) / alien_width)  # Possible number of aliens in one row
    alien_height = alien.rect.height  # Single alien height
    number_alien_y = int((700 - 100 - 2 * alien_height) / alien_height)  # Number of possible rows of aliens

    for raw_number in range(number_alien_y - 2):
        for alien_number in range(number_alien_x):  # Create and fill one row of aliens
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * raw_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * raw_number)
            aliens.add(alien)  # Adding created aliens to the group
