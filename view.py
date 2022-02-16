import pygame

from events import InitializeEvent, QuitEvent, TickEvent, EventListener, Event, EventManager
from model import SnakeGameEngine


class GraphicalView(EventListener):
    def __init__(self, event_manager: EventManager, model: SnakeGameEngine):

        self.event_manager = event_manager
        event_manager.add_listener(self)
        self.model = model
        self.is_initialized = False
        self.screen = None
        self.clock = None
        self.fps = model.fps
        self.width, self.height = model.width, model.height

    def _on_event(self, event):

        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            self.is_initialized = False
            pygame.quit()
        elif isinstance(event, TickEvent):
            self.render_all()
            self.clock.tick(self.fps)

    def render_all(self):
        """
        Draw the current game state on screen.
        Does nothing if is_initialized == False (pygame.init failed)
        """
        if not self.is_initialized:
            return

        self.screen.fill((0, 0, 0))
        self.render_snake()
        pygame.display.flip()

    def render_snake(self):
        snake_surface = pygame.Surface((self.model.scale, self.model.scale))
        snake_surface.fill((255, 255, 255))
        for pos in self.model.snake.body:
            self.screen.blit(snake_surface, pos)

    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """

        pygame.init()
        pygame.display.set_caption(self.model.title)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.is_initialized = True
