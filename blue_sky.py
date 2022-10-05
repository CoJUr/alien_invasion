"""A pygame window with a blue background"""
import sys
import pygame
from settings import Settings
from ship import Ship


class BlueSky:
    """A class to manage the blue sky game"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                                            (self.settings.screen_width,
                                             self.settings.screen_height))

        pygame.display.set_caption("Blue Sky")

        # set the background color to blue
        self.bg_color = (0, 50, 135)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Listen for key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Refactor to re-home the code for updating the screen"""
        self.screen.fill(self.bg_color)

        # make the most recently drawn screen visible, illusory movement
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    bs = BlueSky()
    bs.run_game()