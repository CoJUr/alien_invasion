"""Create an empty Pygame window for the Alien Invasion game."""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width,
        #      self.settings.screen_height))  # assigning surface to screen
        # pygame.display.set_caption("Alien Invasion")
        # refactor to use fullscreen mode:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)

        # set the background color
        self.bg_color = (230, 230, 230)

        #     create a group to store live bullets
        self.bullets = pygame.sprite.Group()

    #     update pos of bullets on each pass thru our while True loop

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # listen for key and mouse events (event loop)
            self._check_events()  # helper method (event loop)
            self.ship.update()  # now the ships update() should be called
            self.bullets.update()  # updating each bullet's sprite position

            # redraw the screen during each pass through the loop:
            self._update_screen()  # helper method run_game refactor part 2

    def _check_events(self):
        """Listen for key presses and mouse events"""

        # refactor _check_events() into 2 methods: for keydown and keyup events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses. -- refactor of _check_events()"""
        if event.key == pygame.K_RIGHT:
            # move the ship by reassigning the flag to True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        #         ^keyboard shortcut to close the game if pressed q
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  # firing bullets on spacebar down event

    def _check_keyup_events(self, event):
        """Respond to key releases. -- refactor of _check_events()"""
        if event.key == pygame.K_RIGHT:
            # reset moving_right/left flag to False on keyrelease
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        new_bullet = Bullet(self)  # creating new instance of a bullet
        self.bullets.add(new_bullet)  # add() = append() analog 4 Pygame groups

    def _update_screen(self):
        """Update imgs on screen, and flip to the new screen.
        Refactor to re-home the code for updating the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # drawing the ship on the background
        for bullet in self.bullets.sprites():
            # draw each bullet onto the screen
            bullet.draw_bullet()

        # make the most recently drawn screen visible -- illusory movement
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
