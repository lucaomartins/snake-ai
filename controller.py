import pygame.event

from data import Direction
from events import Event, TickEvent, QuitEvent, EventManager, EventListener, MovementEvent
from model import SnakeGameEngine


class EventController(EventListener):
    """
    Handles pygame input.
    """

    def __init__(self, event_manager: EventManager, model: SnakeGameEngine):
        """
        Initialize the event controller.
        """

        self.event_manager = event_manager
        self.model = model
        event_manager.add_listener(self)

    def _on_event(self, event: Event):
        """
        Receive events posted to the message queue.
        """

        movement_map = {
            pygame.K_UP: Direction.UP,
            pygame.K_DOWN: Direction.DOWN,
            pygame.K_LEFT: Direction.LEFT,
            pygame.K_RIGHT: Direction.RIGHT
        }

        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.event_manager.post_event(QuitEvent())
                if event.type == pygame.KEYDOWN:
                    if movement_map.get(event.key) is not None:
                        self.event_manager.post_event(MovementEvent(movement_map.get(event.key)))


