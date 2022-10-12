import pygame


class Ship:
    """A class for managing the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        # need a settings attribute to access in update()
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's x position (rect expects ints)
        self.x = float(self.rect.x)

        # Movement flags to be initially set to False
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Update ship's position based on movement flag."""
        # instead of its rect, update ship's x value based on movement flags
        if self.moving_right:
            self.x += self.settings.ship_speed
        #     updating self.x by the value of settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # two separate if statements allow stand-still when both pressed

        # update ship's self.rect.x after updating self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location using its rect and blit()"""
        self.screen.blit(self.image, self.rect)


