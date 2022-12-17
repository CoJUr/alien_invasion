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
        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position as a decimal
        self.y = float(self.rect.y)
