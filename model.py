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
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    DIRECTION_MAP = {
        Direction.UP: UP,
        Direction.DOWN: DOWN,
        Direction.LEFT: LEFT,
        Direction.RIGHT: RIGHT
    }

    def __init__(self, event_manager: EventManager, model: SnakeGameEngine, length=3):
        self.event_manager = event_manager
        self.event_manager.add_listener(self)

        self.direction = Snake.RIGHT

        self.scale = model.scale
        initial_position = Vector2(model.width / 2, model.height / 2)
        self.body = [initial_position + (Vector2(i, 0) * model.scale) for i in range(length)]

    def _on_event(self, event):
        if isinstance(event, MovementEvent):
            self.change_direction(Snake.DIRECTION_MAP[event.direction])
            return

        if isinstance(event, TickEvent):
            self.move()
            return

    def change_direction(self, direction):
        if direction != self.direction.rotate(180):
            self.direction = direction

    def move(self):
        self.body.pop(-1)
        self.body.insert(0, self.body[0] + (self.direction * self.scale))
