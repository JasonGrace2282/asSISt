from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


@dataclass
class House:
    length: int
    width: int
    coordinate: tuple[int, int]
    direction: Direction


@dataclass
class Plot:
    houses: list[House]
    length: int
    width: int
    roads: list[tuple[int, int, int]]
