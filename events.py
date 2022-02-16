from abc import ABCMeta, abstractmethod

from data import Direction


class Event(object):
    name = "Generic Event"

    def __str__(self):
        return self.name


class EventListener(metaclass=ABCMeta):

    def post_event(self, event: Event):
        self._on_event(event)

    @abstractmethod
    def _on_event(self, event: Event):
        pass


class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners: WeakKeyDictionary[EventListener] = WeakKeyDictionary()

    def add_listener(self, listener: EventListener):
        self.listeners[listener] = 1

    def remove_listener(self, listener: EventListener):
        if listener in self.listeners:
            del self.listeners[listener]

    def post_event(self, event: Event):
        for listener in self.listeners:
            listener.post_event(event)


class TickEvent(Event):
    name = "Tick Event"


class QuitEvent(Event):
    name = "Quit Event"


class InitializeEvent(Event):
    name = "Initialize Event"


class MovementEvent(Event):
    name = "Movement Event"

    def __init__(self, direction: Direction):
        self.direction = direction


class DeathEvent(Event):
    name = "Death Event"


class PickupAppleEvent(Event):
    name = "Pickup Apple Event"


class GenerateAppleEvent(Event):
    name = "Generate Apple Event"


class RestartEvent(Event):
    name = "Restart Event"
