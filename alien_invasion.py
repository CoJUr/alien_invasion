"""Create an empty Pygame window for the Alien Invasion game."""
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))  # surface
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # listen for key and mouse events (event loop)
            self._check_events()  # helper method (event loop)
            self.ship.update() # now the ships update() should be called

            # redraw the screen during each pass through the loop
            self._update_screen()  # helper method run_game refactor part 2

    def _check_events(self):
        """Listen for key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # set moving_right flag to False when key is released
                    self.ship.moving_right = False

    def _update_screen(self):
        """Refactor to re-home the code for updating the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # draw the ship on the background

        # make the most recently drawn screen visible, illusory movement
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
