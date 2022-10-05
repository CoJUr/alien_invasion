import pygame


class Pikachu:
    """A class for setting up Pikachu"""

    def __init__(self, bs_game):
        """Initialize Pikachu at the center of the screen"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # load the Pikachu image and get its rect
        self.image = pygame.image.load('images/pikachu.bmp')
        self.rect = self.image.get_rect()

        # start each new Pikachu at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Pikachu at its current location using its rect and blit()"""
        self.screen.blit(self.image, self.rect)