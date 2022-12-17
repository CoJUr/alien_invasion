import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the ships fired bullets"""

    def __init__(self, ai_game):
        """Create bullet object at ships current location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at 0, 0 and then set position
        self.rect = pygame.Rect(0, 0,  # init placeholder position values
                                self.settings.bullet_width, self.settings.bullet_height)
        # set correct position now (bullet position depends on ship position)
        # makes bullets fire from top of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position as a decimal so can make fine bullet speed adjustments
        self.y = float(self.rect.y)

    def update(self):
        """Function for moving the bullet up the screen"""
        # update decimal position of bullet
        self.y -= self.settings.bullet_speed
        # update rect position:
        self.rect.y = self.y

    def draw_bullet(self):
        """Function to draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
