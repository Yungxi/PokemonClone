from enum import Enum

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2
    ENCOUNTER = 3

    SCALE = 60