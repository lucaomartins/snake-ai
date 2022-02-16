from controller import EventController
from events import EventManager
from model import SnakeGameEngine
from view import GraphicalView


def main():
    event_manager = EventManager()
    game_model = SnakeGameEngine(event_manager)
    graphics = GraphicalView(event_manager, game_model)
    controller = EventController(event_manager, game_model)
    game_model.run()


if __name__ == '__main__':
    main()
