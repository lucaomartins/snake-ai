import typing

from pygame.math import Vector2

from data import Direction
from events import EventListener, MovementEvent, InitializeEvent, TickEvent, QuitEvent, EventManager


class SnakeGameEngine(EventListener):
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager
        event_manager.add_listener(self)

        self.width, self.height = 600, 600
        self.scale = 20
        self.fps = 15
        self.title = "Snake"
        self.running = False
        self.snake = Snake(event_manager, self)

    def _on_event(self, event):
        if isinstance(event, QuitEvent):
            self.running = False

    def run(self):
        """
        Starts the game engine loop.

        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify().
        """
        self.running = True
        self.event_manager.post_event(InitializeEvent())
        while self.running:
            newTick = TickEvent()
            self.event_manager.post_event(newTick)


class Snake(EventListener):
    def __init__(self, event_manager: EventManager, model: SnakeGameEngine, length=3):
        self.event_manager = event_manager
        self.event_manager.add_listener(self)
        initial_position = Vector2(model.width / 2, model.height / 2)
        self.body = []
        self.scale = model.scale
        for i in range(length):
            self.body.append(initial_position + Vector2(i * model.scale, 0))
        self.direction = Direction.RIGHT

    def _on_event(self, event):
        if isinstance(event, MovementEvent):
            self.direction = event.direction
            return

        if isinstance(event, TickEvent):
            self.move()

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]
        direction_vector_map = {
            Direction.UP: Vector2(0, -1),
            Direction.DOWN: Vector2(0, 1),
            Direction.LEFT: Vector2(-1, 0),
            Direction.RIGHT: Vector2(1, 0)
        }
        self.body[0] = self.body[0] + (direction_vector_map[self.direction] * self.scale)

